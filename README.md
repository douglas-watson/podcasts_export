# Export downloaded episodes from Apple Podcasts

Douglas Watson, 2020, MIT License.

This script finds all downloaded episodes in Apple Podcasts on macOS Catalina and copies them to a folder, setting ID3 tags in the process. It is only meant to be executed within an Automator workflow, but if you want to run it from the shell:

```
pip install mp3_tagger
python podcasts_export.py DESTINATION_FOLDER
```

You can also install the workflow directly, by unzipping then opening [Export Downloaded Podcasts.zip](Export%20Downloaded%20Podcasts.zip). This should create a new Service within the Podcasts app:

![Export Downloaded Podcasts service](export_podcast_service.png)

The workflow first prompts you for a destination folder, then executes the script.

Written in the already-deprecated Python 2.7, which is still the default version in Automator. It may break in future OS updates.