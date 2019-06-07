Author: Jacob Muzzy
Contact: jacob.muzzy@hpe.com

WHY
    This script was written because of its perceived usefulness in the FVT Team.
    We were looking for a way that all our RG data files could be formatted uniformly because many of
    our robo data files were built with different styles.
    This was made specifically for data files built with json blobs, as it formats the file
    based on commas and brackets to allow all properties of the same level to appear on the same tab
    level instead of in one line like in some cases

WHAT IS DOES
    The script associated to this readme file (json_style_formatter.py) is
    reading the file line by line, then character by character,
    looking for commas and brackets while watching out for special
    cases like brackets or commas inside quotes, and then printing
    the lines to a temporary file, then it removes the original file and
    renames the temporary file to the original. This script also preserves newlines and comments.

INSTALLING / RUNNING THE SCRIPT
    This script can be ran with the command line using the python interpreter like
        python {filePathToScript} {filePathToTargetFile}

    The other option is to add this script as an external tool for pycharm
        1) Open PyCharm
        2) File
        3) Settings...
        4) select the "Tools" drop down menu on the content bar (left side)
        5) select "External Tools"
        6) add an external tool with the green plus sign at the top of the window
        7) Fill in fields
            Name: jsonFormatter
                # or whatever name you would like
            Description: *add the "what it does" section from above
                # or a condensed version you would like to see
            Program: python
            Parameters: \RoboGalaxy\Fusion_4.00\Tools\JSONFormatting\json_style_formatter.py $FilePath$
                # your full path may be different than the one listed
                # here due to being able to name your local fusion repo
            Working Directory: $ProjectFileDir$
        8) select "OK"
        9) press "Apply"

        It can now be accessed by right clicking on the file of your choice, select
        "External Tools", and then the script name. It is also available from the toolbar at the top
        of pyCharm in "Tools", and then "External Tools".

THINGS TO NOTE
    Edits to the script are welcome as this was developed for and tested on certain files.

    Like other tools, like autopep8, if this tool is run on a file with no local edits prior
    to the script being run, the undo function (ctrl + z) will not be available. This being said, the file
    can still be reverted to the last repository version with ctrl + alt + z.

