set RB=C:\cygwin\home\jenkins\robogalaxy
set PY=%RB%\tools\Python27
set ROBOPATH=%PY%;%PY%\scripts;%PY%\lib\site-packages;%RB%\tools\exe
set PATH=c:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Program Files\TortoiseSVN\bin;c:\cosmos\robot-tests;C:\Program Files\Code Collaborator Client;c:\program files (x86)\notepad++;c:\Program Files (x86)\Microsoft SQL Server\100\Tools\Binn\;c:\Program Files\Microsoft SQL Server\100\Tools\Binn\;c:\Program Files\Microsoft SQL Server\100\DTS\Binn\;C:\Program Files (x86)\OpenSSH\bin;C:\Program Files (x86)\Java\jre7\bin;%ROBOPATH%
set PYTHONPATH=%RB%;

cd C:\cygwin\home\jenkins\robogalaxy\tests\fusion\qual

@echo off
for /F "tokens=2-4 delims=/ " %%i in ('date /t') do set cdate=%%k%%i%%j
For /f "tokens=1,2,3 delims=: " %%f in ('time /t') do set ctime=%%f%%g%%h

set orig=OVAQual.txt
set folder=_%orig:.txt=%__%cdate%_%ctime%
echo Output folder: %folder%
pybot --outputdir %folder% %orig%
