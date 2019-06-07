This will generate Libdoc (High Level Resource documentation) for all the resources file in a given repository
If all your resource files are in one folder then you should set the FLAT variable to Yes. All the libdoc html files are copied into the libdoc folder and an index.html file is created. 
If your resource files are located in various folders underneath one common folder, such as fusion\resources, set the FLAT variable to Yes and the libdoc html files will be created in each folder, as well as under libdoc,
with an index.html file. 

Arguments

GIT_REPO_ROOT - path on local system where your repos are located

RESOURCES_ROOT_FOLDER - path to resource folder

FLAT - set to No if all resource files are located in one flat folder, yes if resource files are stored in subfolders

FILETYPE - normally this would be set to html, which then generates html doc files, otherwise if set to xml, will generate xml files
if xml is specified the xml files are only written to the libdoc folder, files are not created in subfolders



Example arguments using RIDE and with a GIT respository root of c:\robogalaxy, this example which will generate html doc files
--variable GIT_REPO_ROOT:c:robogalaxy --variable RESOURCES_ROOT_FOLDER:c:\robogalaxy\fusion\resources --variable FLAT:No --variable FILETYPE:html

This will generate xml file
--variable GIT_REPO_ROOT:c:robogalaxy --variable RESOURCES_ROOT_FOLDER:c:\robogalaxy\fusion\resources --variable FLAT:No --variable FILETYPE:xml

To execute from command line using Pybot, this example which will generate html doc files

pybot --variable GIT_REPO_ROOT:c:/robogalaxy --variable RESOURCES_ROOT_FOLDER:c:/robogalaxy/fusion/resources --variable FLAT:No --variable FILETYPE:html Generate_Resource_Doc.txt

This example which will generate xml doc files
pybot --variable GIT_REPO_ROOT:c:/robogalaxy --variable RESOURCES_ROOT_FOLDER:c:/robogalaxy/fusion/resources --variable FLAT:No --variable FILETYPE:xml Generate_Resource_Doc.txt