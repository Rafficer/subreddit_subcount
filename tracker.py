import json
import urllib2
import datetime
import os
import sys
import MySQLdb

from DBCredentials import DBName, DBPassword, DBServerHostname, DBUsername

conn = MySQLdb.connect(host=DBServerHostname,
			user=DBUsername,
			passwd=DBPassword,
			db=DBName)

c = conn.cursor()
c.execute("SELECT tracked_subs FROM tracked_subs")

fetch = c.fetchall()

subreddits = []

for subreddit_from_DB in fetch:
    subreddits.append(subreddit_from_DB[0])

print subreddits


date = datetime.datetime.now().strftime("%Y-%m-%d")

def process(subreddit):
    conn = MySQLdb.connect(host=DBServerHostname,
			user=DBUsername,
			passwd=DBPassword,
			db=DBName)

    dbc = conn.cursor()

    dbc.execute("SELECT * FROM Subcounts Where Date=%s AND Subreddit=%s",(date,subreddit))
    cond = dbc.fetchone()
    conn.close()

    print "Checked " + subreddit
    if(cond != None):
        print "exiting"
        return
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

    req = urllib2.Request("https://api.reddit.com/r/{}/about".format(subreddit), headers=request_headers)
    res = urllib2.urlopen(req)

    jdata = json.loads(res.read())

    subscribers = jdata['data']['subscribers']

    conn = MySQLdb.connect(host=DBServerHostname,
			user=DBUsername,
			passwd=DBPassword,
            db=DBName)

    dbc = conn.cursor()

    print "Processing " + subreddit

    dbc.execute("""INSERT INTO Subcounts (Date, Subreddit, Subcount) VALUES (%s,%s,%s)""",(date,subreddit,subscribers))
    conn.commit()
    conn.close()


for sub in subreddits:
    process(sub)
