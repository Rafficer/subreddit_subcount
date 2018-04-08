import json
import urllib2
import datetime
import os
import sys

subreddit = str(sys.argv[1])
filename = "subcounts.{}.csv".format(subreddit)

request_headers = {
"Accept-Language": "en-US,en;q=0.5",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Referer": "https://reddit.com",
"Connection": "keep-alive" 
}

req = urllib2.Request("https://reddit.com/r/{}/.json".format(subreddit), headers=request_headers)
res = urllib2.urlopen(req)

jdata = json.loads(res.read())

subscribers = jdata['data']['children'][0]['data']['subreddit_subscribers']
date = datetime.datetime.now().strftime("%y-%m-%d")

if os.path.isfile(filename) == False:
    with open(filename,"w+") as csvfile:
        with open(filename, "a") as csvfile:
            csvfile.write("Date, Subcount\n")

with open(filename, "a") as csvfile:
    csvfile.write("{},{}\n".format(date, subscribers))