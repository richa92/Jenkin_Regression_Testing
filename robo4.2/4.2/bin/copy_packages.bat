set SHARE=%1
set REPO=%2
set USERNAME=%3
set PASSWORD=%4
if NOT "%COMPUTERNAME%" == "ROBOGALAXY" (
    set SHARE=%1
    echo Mounting %SHARE%\%REPO%
    net use %SHARE%\%REPO% /user:"%USERNAME%" "%PASSWORD%"
    xcopy dist\* %SHARE%\%REPO% /sechrky
    net use %SHARE%\%REPO% /delete

) else (
    xcopy dist\* c:\www\repo\github\%REPO% /sechrky
)
