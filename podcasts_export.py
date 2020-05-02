#!/usr/bin/env python
#
#  Podcasts Export
#  ---------------
#  Douglas Watson, 2020
#
#  Receives the location of Apple Podcasts' database, finds episodes that have
#  been downloaded, then renames and copies those files into a new folder.
#

import os
import sys
import shutil
import urllib
import sqlite3

SQL = """
SELECT p.ZAUTHOR, p.ZTITLE, e.ZTITLE, e.ZASSETURL
from ZMTEPISODE e 
join ZMTPODCAST p
    on e.ZPODCASTUUID = p.ZUUID 
where ZASSETURL NOTNULL;
"""

def check_imports():
    try:
        import mp3_tagger
    except ImportError:
        os.system("""osascript -e 'do shell script "/usr/bin/easy_install mp3_tagger" with administrator privileges'""")

def get_downloaded_episodes(db_path):
    return sqlite3.connect(db_path).execute(SQL).fetchall()

def main(db_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for author, podcast, title, path in get_downloaded_episodes(db_path):
        dest_path = os.path.join(output_dir, "{}-{}-{}.mp3".format(author, podcast, title))
        shutil.copy(urllib.unquote(path[len('file://'):]), dest_path)

        mp3 = mp3_tagger.MP3File(dest_path)
        mp3.artist = author
        mp3.album = podcast
        mp3.song = title
        mp3.save()

if __name__ == "__main__":
    if len(sys.argv) <= 1:
            sys.stderr.write("No output folder specified\n")
            sys.exit(1)

    check_imports()
    import mp3_tagger
    output_dir = sys.argv[1]
    db_path = os.path.expanduser("~/Library/Group Containers/243LU875E5.groups.com.apple.podcasts/Documents/MTLibrary.sqlite")
    main(db_path, output_dir)