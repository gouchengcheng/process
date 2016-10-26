############
#
# stat the frequency of retweet number from 20160510.txt
#
# coding=UTF-8
#!/usr/bin/python
import re
from collections import defaultdict
import operator
uids = set()

pfile = open("savefile")
count = 0
for line in pfile:
    m=re.findall('uid":"(\d+)',line)
    for uid in m:
        uids.add(uid)
    count += 1
    if count%100 ==0:
        print count

pfile.close()

pfile = open('uid_list','w')

for x in uids:
    pfile.write(str(x) + '\n')

pfile.close()
