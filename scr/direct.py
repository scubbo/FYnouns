import sys
import os
import FYnouns

import cgitb
cgitb.enable()

sys.stdout.write("Content-type: image/jpg\r\n\r\n")
#sys.stdout.write("Content-type: text/plain\r\n\r\n")
query = os.environ['QUERY_STRING']
arg = {}
for pair in query.split('&'):
	arg[pair.split('=')[0]] = pair.split('=')[1]
if arg.has_key('query'):
	with open(FYnouns.getURLToImage(arg['query']), 'rb') as imageFile:
		sys.stdout.write(imageFile.read())
	
