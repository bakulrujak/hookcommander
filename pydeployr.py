#!/usr/bin/env python3

import sys
from repo import aws

# print("This is arguments:", sys.argv[1])

commit = sys.argv[1]

if not len(commit) < 5:
	try:
		response = aws.do_deploy(commit)
		print(response)
	except ValueError:
		print("Uh-oh, something is not running like it use to be :(", commit)
else:
	print("Oops, it seems your commit ID is not the valid one", commit)
