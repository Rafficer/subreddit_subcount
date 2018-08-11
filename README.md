# Subreddit subcount
Small, bad python script to pull subreddit subcounts

Usage:

* `python tracker.py subredditname1 subredditname2` 

The script now works with a database. It needs a Table called "Subcounts" in a Database.

It also needs the following columns:

![x](https://i.imgur.com/98uKSgm.png)

If CSV files from previous Versions exist, they can be automatically thrown in a Database with the *transferCSVtoDB.py* Script.

You can add as many subreddits as you want.

**Add your DB credentials to DBCredentials.py and the subreddits to track to subredditlist.txt.**

It's meant to be called via cron multiple times a day to ensure that it's not failing. It will only add a new entry once a day.

I use `5 */2 * * * /path/to/tracker.py`

**Python modules required:**

* json
* urllib2
* datetime
* os
* MySQLdb