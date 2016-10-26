############
#
# stat the frequency of retweet number from 20160510.txt
#
# coding=UTF-8
#!/usr/bin/python
import re
from collections import defaultdict
import operator

re_cnt_freq = defaultdict(int)

pfile = open("20161010.txt")
for line in pfile:
    m=re.search('mid_retweetnum":\d+',line)
    #print m.group(0)
    n=re.search('\d+',m.group(0))
    #print n.group(0)
    #print type(n.group(0))
    re_cnt_freq[int(n.group(0))] += 1
        
pfile.close()

pfile = open('re_cnt_freq','w')

sorted_x = sorted(re_cnt_freq.items(), key=operator.itemgetter(0), reverse=True)
for x in sorted_x:
    pfile.write(str(x[0]) + ' ' + str(x[1]) + '\n')

pfile.close()
