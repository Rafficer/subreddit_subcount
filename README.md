# Subreddit subcount
Small, bad python script to pull subreddit subcounts

Usage:

* `python tracker.py subredditname1 subredditname2` 

The script will automatically create a file called subcounts.*subredditname*.csv for each specified subreddit.

You can add as many subreddits as you want.

It's meant to be called via cron multiple times a day to ensure that it's not failing. It will only add a new entry once a day.

I use `5 */2 * * * /path/to/file subredditname1 subredditname2`

**Python modules required:**

* json
* urllib2
* datetime
* os
* sys