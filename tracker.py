import json
import urllib2
import datetime
import os
import sys
import MySQLdb

DBServerHostname=""
DBUser=""
DBPassword=""
DBName=""

subreddits = sys.argv
del subreddits[0]
date = datetime.datetime.now().strftime("%Y-%m-%d")

def process(subreddit):
    conn = MySQLdb.connect(host=DBServerHostname,
			user=DBUser,
			passwd=DBPassword,
			db=DBName)

    dbc = conn.cursor()

    dbc.execute("SELECT * FROM Subcounts Where Date=%s AND Subreddit=%s",(date,subreddit))
    cond = dbc.fetchone()
    conn.close()


    if(cond != None):
        exit(0)
    else:
        get_subcount(subreddit)


def get_subcount(subreddit):
    request_headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Referer": "https://reddit.com",
    "Connection": "keep-alive" 
    }

    req = urllib2.Request("https://reddit.com/r/{}/about/.json".format(subreddit), headers=request_headers)
    res = urllib2.urlopen(req)

    jdata = json.loads(res.read())

    subscribers = jdata['data']['subscribers']

    conn = MySQLdb.connect(host=DBServerHostname,
			user=DBUser,
			passwd=DBPassword,
			db=DBName)

    dbc = conn.cursor()

    dbc.execute("""INSERT INTO Subcounts (Date, Subreddit, Subcount) VALUES (%s,%s,%s)""",(date,subreddit,subscribers))
    conn.commit()
    conn.close()

for sub in subreddits:
    process(sub)