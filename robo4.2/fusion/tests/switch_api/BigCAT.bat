REM ++
REM  Batch file to execute Comet PreCAT tag-based testing.
REM  Logs are sent to \\eml.usa.hp.com\eMgmt\Hydrogen\Jenkins\CFEDVT\log
REM --
set FUSION_IP=10.0.12.18
set SWITCH_IP=16.119.98.156
set MY_LIBRARY=C:\Users\Administrator\git\robogalaxy

REM Generate time and date stamp
set TIMESTAMP=%date:~10,4%-%date:~4,2%-%date:~7,2%@%time:~0,2%h%time:~3,2%m%time:~6,2%s
set TIMESTAMP=%TIMESTAMP: =%

REM Update you GIT repository
cd %MY_LIBRARY%
git pull
git status

REM  Execute the PreCAT testing
cd %MY_LIBRARY%\tests\efusion\functional\switch 
pybot --variable FUSION_IP:%FUSION_IP% ^
      --variable SWITCH_IP:%SWITCH_IP% ^
      --include PreCAT ^
      --exclude deferred ^
      --log  \\eml.usa.hp.com\eMgmt\Hydrogen\Jenkins\CFEDVT\log\BigCAT%TIMESTAMP%.html ^
      . 
