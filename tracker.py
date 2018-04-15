import json
import urllib2
import datetime
import os
import sys

subreddits = sys.argv
del subreddits[0]
date = datetime.datetime.now().strftime("%Y-%m-%d")

def get_lastdate(file):
        lastline = get_lastline(file)
        array = lastline.split(",", 1)
        date = array[0]
        return date

def get_lastline(file):
    with open(file, "r") as f1:
        lastline = f1.readlines()[-1]
        return lastline

def process(subreddit):
    filename = "subcounts.{}.csv".format(subreddit)
    lastdate = get_lastdate(filename)

    if date in lastdate:
        exit(0)
    else:
        get_subcount(subreddit, filename)


def get_subcount(subreddit, filename):
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

    if os.path.isfile(filename) == False:
        with open(filename,"w+") as csvfile:
            with open(filename, "a") as csvfile:
                csvfile.write("Date, Subcount\n")

    with open(filename, "a") as csvfile:
        csvfile.write("\n{},{}".format(date, subscribers))

for sub in subreddits:
    process(sub)