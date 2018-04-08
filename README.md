# Subreddit subcount
Small, bad python script to pull subreddit subcounts

Usage:

* python tracker.py *subredditname*

The script will automatically create a file called subcounts.*subredditname*.csv

It's meant to be called via cron each day. I use `0 3 * * * python /path/to/file subredditname`

**Python modules required:**

* json
* urllib2
* datetime
* os
* sys