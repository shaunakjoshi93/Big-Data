#!/usr/bin/python

import sys
import os
import re
 
dict1 = {}
         
for line in sys.stdin:
        word, file1 = line.split('\t')
 	if word in dict1:
		if file1 in dict1[word]:
			dict1[word][file1] = dict1[word][file1] + 1
		else:			
			dict1[word][file1] = 1 

	else:
		dict1[word] = {}
		dict1[word][file1] = 1 

for word in dict1:
    sys.stdout.write("{0} {1}".format(word, dict1[word]))
	

