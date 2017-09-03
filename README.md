**Next episode** plays video files and keeps track of what is already played.

Installation
------------

```
pip install --upgrade --user https://github.com/alcm-b/nextepisode/archive/master.zip
```

Usage
-----

`nextepisode ~/Videos/TvSeriesDirectory` starts media player and enqueues the next
unseen file from the directory `~/Videos/TvSeriesDirectory`.

A next file to play is determined by sorting file names in alphabetical order
and picking up the first file that is not yet seen.
