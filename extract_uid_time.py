############
#
# extract uid, **, retweet_time(sorted) from savefile
#
# coding=UTF-8
#!/usr/bin/python
import re
from collections import defaultdict
import operator

uid_rtime = []

pfile = open("savefile.txt")
ufile = open('uid_rt.txt','w')
count = 1
for line in pfile:
    uids = re.findall('uid":"(\d+)',line)
    #uids = set(list(uids) + list(m))
    rtimes = re.findall('pt":(\d+)',line)

    number = len(uids)
    for i in xrange(number):
        uid_rtime.append((uids[i],int(rtimes[i])))

    new_list = sorted(uid_rtime, key= lambda rt:rt[1])

    for x in new_list:
        ufile.write(x[0]+' '+ str(count)+' '+ str(x[1]) + '\n')

    count += 1
    #print m.group(0)
    #n=re.search('\d+',m.group(0))
    #print n.group(0)
    #print type(n.group(0))
    #uids.add(n.group(0))
    #pass

ufile.close()
pfile.close()

