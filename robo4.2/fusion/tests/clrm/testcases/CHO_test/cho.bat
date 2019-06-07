echo off
set /p Range=Enter Number Of Iterations:
echo %Range%
set /p filepath=Enter the path of test suit file:
echo %filepath%

REM FOR /L %%G IN (1,1,%Range%) DO pabot --processes 2 -l log%%G.html -r report%%G.html -o output1%%G.xml -d E:\results %filepath%

FOR /L %%G IN (1,1,%Range%) DO pabot --processes 2 -d F:\results\passbuildOV_4_1_jul14_ssh1_%%G %filepath%