RFDoc_Create.bat is used to invoke the creation of the library documentation for low level and high level Robot keywords. It is located in the utils folder within the RG repository.

Open a command window and enter cd\<yourGITRootrepositorypath>\rg\RobogGalaxylibrary\utils

Let's assume for this example that GIT repositories are cloned into a folder named c:\git

cd \git\rg\robogalaxylibrary\utils

Enter RFDoc_Creat.bat to run the utility

RFDoc_Create.bat

At the first prompt enter the full path to the directory where your Robot resource files are located, for a particular repository.
The utility will use the entered path to search for all resource files which contain high level keywords anywhere under the folder specified, including its subfolders
Usually this is a folder called resource under the tests folder. 

At the second prompt enter the path to the low level keywords. This will always be a keywords folder. 

At the third prompt enter the name you wish to give to the library doc files to be created

At the fourth prompt enter the version name for the library doc. This will be added into the file contents.

AT the fifth prompt you can indicate whether or not you want any subpath's that were entered to be excluded from being searched. This is typically 'No'.
If you answer "Yes" another prompt will appear

Here is an example of running the utility to create a doc library for the Fusion 3.00 repository

******* Execution Starts ********

Enter the Resource files path: c:\git\fusion\tests\resources

Enter the Python Resource files path: c:\git\fusion\fusionlibrary\keywords

Enter the RFDoc File name without extension: Fusion_3.00

Enter the Version of the RFDoc: 3.00

DO you want to exclude any path in base path provided? [Yes or No]: No


The script runs and creates three files in the directory. In this case Fusion_3.00.xml Fusion_3.00.html and Fusion_3.00.txt

The xml file can then be uploaded using the RFDoc utility, callable from the RoboGalaxyLibrary Keywords link on the RoboGalaxy Wiki, assuming you have access to do so.











