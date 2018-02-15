#!/usr/bin/python

import sys
import os
import re
 
dict1 = {}
         
for line in sys.stdin:
        author, title = line.split('\t')
	author = author.strip()
	title = title.strip()

	if author in dict1:
		if title in dict1[author]:
			dict1[author][title] = dict1[author][title] + 1
		else:			
			dict1[author][title] = 1 

	else:
		dict1[author] = {}
		dict1[author][title] = 1 

for word in dict1:
    sys.stdout.write("{0}\t{1}".format(author, dict1[author]))
	

