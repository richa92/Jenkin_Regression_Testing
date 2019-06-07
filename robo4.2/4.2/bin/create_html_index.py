"""
create_html_index.py is used to create an index file for the files in a folder

"""

import os
import sys
from string import Template


def buildFileIndex(files):
    values = {'fileList': files}

    s = Template("""
    <h1>Resource Files Keywords</h1></br>
    <html>
        <div>
            $fileList
        </div>
    </html>
    """)

    htmlOutput = s.substitute(values)
    return htmlOutput

dir = sys.argv[1]
files = os.listdir(dir)

outputFilename = dir + '\\index.html'
outputFile = open(outputFilename, 'w')

listOfFiles = ['<a href="' + file + '">'
               + file
               + '</a><br />' for file in files]

listOfFilesStr = '\n'.join(listOfFiles)
outputFile.write(buildFileIndex(listOfFilesStr))

print('Index written to', outputFilename)

outputFile.close()
