"""
File name: json_style_formatter.py
Author: Jacob Muzzy
Date created: 8/3/2017
Date last modified: 8/24/2017
Python ver: 2.7

Purpose:
    To create a script that will allow
    multiple people to have the same json styled
    formatting to their RG data files

Other:
    More information including how to run
    this script properly can be found in the
    readme file associated to this script as
    well as the documentation below
"""

import sys
import os
bracket_count = 0


def check_for_open_bracket(char_in):
    """check for open bracket and increment global counter if true"""
    global bracket_count
    if char_in is "[" or char_in is "{":
        bracket_count += 1
        return True
    else:
        return False


def check_for_close_bracket(char_in):
    """check for closing bracket and decrement global counter if true"""
    global bracket_count
    if char_in is "]" or char_in is "}":
        bracket_count -= 1
        return True
    else:
        return False

# Open a new file for write and while there
# are lines to be read from the input file, take
# each line and read it char by char until certain
# cases are met. After a bracket or comma is encountered,
# it prints what part of the string it has and then continues.
# Special cases that this script checks for included comment
# lines, brackets and or commas located within a string,
# and also the case when a comma is located directly after
# a closing bracket in which case it wouldn't want to print
# a newline after the bracket.
os.system("autopep8 --in-place --ignore=E501 " + sys.argv[1])
write_file = open("newTempFile.py", "w+")
lineNumber = 0
with open(sys.argv[1]) as file_object:
    for full_line in file_object:
        lineNumber += 1
        quote = 0
        next_char = -1
        line = ""
        full_line = full_line[:-1].strip()
        if len(full_line) == 0:
            write_file.write("\n")
        if '%s' in full_line:
            write_file.write("%s\n" % full_line)
            line = ""
        # print full comment lines
        elif "#" in full_line:
            write_file.write("%s\n" % full_line)
            line = ""
        # check for the common case of a comma directly following an end bracket in lines that contain the pair
        elif "}," in full_line:
            for char in full_line:
                next_char += 1
                line += str(char)
                if char is '"' or char is "'":
                    quote += 1
                if quote % 2 == 0:
                    if char == ",":
                        if line[len(line) - 2] == "}":
                            line = line[:-2].strip()
                            write_file.write("%s\n" % line)
                            write_file.write("},\n")
                            line = ""
                        else:
                            write_file.write("%s\n" % line)
                            line = ""
                    if check_for_open_bracket(char):
                        write_file.write("%s\n" % line)
                        line = ""
        # all other lines will be dissected here
        else:
            for char in full_line:
                next_char += 1
                line += str(char)
                if char is '"' or char is "'":
                    quote += 1
                if quote % 2 == 0:
                    if char == ",":
                        write_file.write("%s\n" % line)
                        line = ""
                    if check_for_open_bracket(char):
                        write_file.write("%s\n" % line)
                        line = ""
                    if check_for_close_bracket(char):
                        write_file.write("%s\n" % line)
                        line = ""

        if line != "":
            write_file.write("%s\n" % line)

# Close all files, remove the original, and
# rename the temp file to the original file
# name. Then run autopep8 on the final file.
file_object.close()
write_file.close()

file_name = sys.argv[1]
os.remove(file_name)
os.rename("newTempFile.py", file_name)

status = os.system("autopep8 --in-place --ignore=E501 " + file_name)
print ("autopep8 finshed with exit code " + str(status))
