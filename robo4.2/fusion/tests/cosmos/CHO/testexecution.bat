@echo off
set /p Range=Enter Number Of Iterations:
echo %Range%
set /p filepath=Enter the path of test suit file:
echo %filepath%

REM FOR /L %%G IN (1,1,%Range%) DO pabot --processes 3 -l log%%G.html -r report%%G.html -o output%%G.xml -d C:\results --exitonfailure %filepath%

FOR /L %%G IN (1,1,%Range%) DO pabot --processes 3 -d C:\results\iteration%%G --exitonfailure %filepath%
