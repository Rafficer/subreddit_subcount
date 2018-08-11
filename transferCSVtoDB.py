import MySQLdb
from DBCredentials import DBName, DBPassword, DBServerHostname, DBUsername

filename = "subcounts.subredditname.csv"
subredditname = "subredditname"

conn = MySQLdb.connect(host=DBServerHostname,
        user=DBUsername,
        passwd=DBPassword,
        db=DBName)

dbc = conn.cursor()


with open(filename, 'r') as myfile:
  data = myfile.readlines()

filelength = len(data)
i=0
for x in data:
    if(len(x) != 1):
            if(i != 0):
                delimited = x.split(",")
                date = delimited[0]
                subcount = delimited[1]
                dbc.execute("INSERT INTO Subcounts (Date, Subreddit, Subcount) VALUES (%s,%s,%s)",(date,subredditname,subcount))
                conn.commit()
                conn.close()
            i=i+1
