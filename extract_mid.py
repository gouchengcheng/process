############
#
# get the mid from 20161010.txt and remove the very high 
# frequency rwtweeted messages > 50000
#
# coding=UTF-8
#!/usr/bin/python
import re
from collections import defaultdict
import operator
import json

re_cnt_freq = defaultdict(int)

pfile = open("20161010.txt")
mid =[]
for line in pfile:
	tree = json.loads(line)
	retweet_num = int(tree['mid_retweetnum'])
	if retweet_num < 50000:
		mid.append(tree['mid'])
        
pfile.close()

pfile = open('mid_list','w')

for x in mid:
    pfile.write(str(x) + '\n')

pfile.close()
