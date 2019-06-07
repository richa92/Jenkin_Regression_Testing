#!/usr/local/bin/python

import json
import re
import string
import pprint


# Format REST text class
# Define the class
class FormatRestText(object):

    def __init__(self, text):
        self.text = text

    def formatText(self):
        mytext = self.text
        mytext = mytext[string.find(mytext, '{'):]

        if mytext:
            try:
                dict = json.loads(mytext)
            except ValueError:
                print "Attempting to pretty up non json string..."
                dict = eval(mytext)

            # JRT print pprint.PrettyPrinter().pformat(dict)
            newtext = pprint.PrettyPrinter().pformat(dict)
        return newtext
