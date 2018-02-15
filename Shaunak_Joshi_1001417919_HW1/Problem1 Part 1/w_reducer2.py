#!/usr/bin/python

import sys
import os
import re
 
dict1 = {}
         
for line in sys.stdin:
        word, file1 = line.split('\t')
 	if word in dict1:
		if file1 in word:
			pass
		else:
			#dict1.setdefault(word, [])			
			dict1[word].append(file1) 
	else:
		#dict1.setdefault(word, [])
		dict1[word] = []
		dict1[word].append(file1) 
		

for word in dict1:
    print("{0}\t{1}".format(word, dict1[word]))
	   
              
'''for i in file1:
		
                doc_id, count = i.split(':')
                count = int(count)
 
                index[word].setdefault(doc_id, 0)
                index[word][doc_id] += count
'''
