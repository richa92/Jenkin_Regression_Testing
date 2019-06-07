#!/usr/local/bin/python

''' Attempt to pretty print curl output by searching the input for
    the first occurrence of '{' and treating it as the start of a
    dictionary.  Accepts either standard input or a filename.'''

import sys

if len(sys.argv) == 2:
    if sys.argv[1] == "-h":
        import os
        basename = os.path.basename(sys.argv[0])
        print "Usage:  %s <file>" % basename
        print "Usage:  cat <file> | %s" % basename
        exit(0)
    else:
        myfile = sys.argv[1]
        f = open(myfile, 'r')
        mystr = f.read()
else:
    mystr = ""
    import fileinput
    for line in fileinput.input():
        mystr = mystr + line

import string
mystr = mystr[string.find(mystr, '{'):]

if mystr:
    import json

    # Try json first
    try:
        dict = json.loads(mystr)
    except ValueError:
        print "Attempting pprint on a non json string..."
        dict = eval(mystr)

    import pprint
    print pprint.PrettyPrinter().pformat(dict)
