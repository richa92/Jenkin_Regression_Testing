@echo off
for /F "tokens=2-4 delims=/ " %%i in ('date /t') do set cdate=%%k%%i%%j
For /f "tokens=1,2,3 delims=: " %%f in ('time /t') do set ctime=%%f%%g%%h

IF "%1"=="" goto ARG_NOT_EXIST
IF NOT EXIST "%1" goto NOTEXIST
IF "%2"=="" goto ARG_NOT_EXIST

python -c "import re;import sys;sys.exit(-1) if not re.search(r'https?://([^/]*)/?', '%2') else sys.exit(0)"
IF NOT ERRORLEVEL 0 goto WRONG_URL
set orig=%1
set applianceurl=%2
set folder=_%orig:.txt=%__%cdate%_%ctime%
echo ApplianceUrl: %applianceurl%
echo Test Case Folder: %1
echo Output folder: %folder%
pybot -v PauseWhenFailed:True -v DataFile:OVAQual_data.xml -v ApplianceUrl:%applianceurl% -v Browser:firefox --logtitle OVAQual_120_RC8Binary_Firefox_Test_Log --reporttitle OVAQual_120_RC8Binary_Firefox_Test_Report --reportbackground green:yellow:red --outputdir %folder% %1
goto END

:ARG_NOT_EXIST
echo Please specify arguments
echo Usage: 
echo      runtest.bat FOLDER APPLIANCEURL
echo Example: 
echo      runtest.bat OVAQual https://127.0.0.1
goto END

:NOTEXIST
echo folder "%1" not exist
goto END

:WRONG_URL
echo Argument APPLIANCEURL "%applianceurl%" is not well-formed URL.
goto END

:END
