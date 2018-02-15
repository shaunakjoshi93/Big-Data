#!/usr/bin/python

import sys
import os
from os.path import basename 

for line in sys.stdin:
	line = line.strip().split()
	for w in line:
		filename = os.getenv('map_input_file') 
		sys.stdout.write("{0}\t{1}\n".format(w, os.path.basename(filename)))
