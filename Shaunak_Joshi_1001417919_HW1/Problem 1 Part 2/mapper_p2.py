#!/usr/bin/python

import sys
import os
from os.path import basename 
import string


file_path = os.getenv('map_input_file')
filename = os.path.basename(file_path)

for line in sys.stdin:
	line = line.strip().split()
	for w in line:
		for c in string.punctuation:
			w = w.replace(c,"")
		if len(w) > 0:
			sys.stdout.write("{0}\t{1}\n".format(w,filename))
