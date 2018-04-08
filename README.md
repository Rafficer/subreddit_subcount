# Subreddit subcount
Small, bad python script to pull subreddit subcounts

Usage:

* `python tracker.py subredditname1 subredditname2` 

The script will automatically create a file called subcounts.*subredditname*.csv for each specified subreddit.

You can add as many subreddits as you want.

It's meant to be called via cron each day. I use `0 3 * * * python /path/to/file subredditname1 subredditname2`

**Python modules required:**

* json
* urllib2
* datetime
* os
* sys