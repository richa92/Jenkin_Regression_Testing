@echo off
rem (C) Copyright 2017-2018 Hewlett Packard Enterprise Development LP
echo ************************************
echo Utility to decrypt support dump 3.0
echo ************************************
echo.


IF "%1"=="" (
    echo %0: missing support dump file operand
    echo.
    echo.
    echo Valid command: %0 absolute-path-of-support-dump-file
    exit /B
)

if not exist ""%1"" (
    echo File with name %1 was not found. Please provide valid support dump file.
    exit /B
)

rem Set the jar in the classpath
rem echo *********************************
rem echo Setting classpath
rem echo *********************************
rem echo.
rem echo %~dp0
set classpath=%~dp0\Decryption-Util.jar;%CLASSPATH%
rem echo %classpath%
rem echo.

echo Please wait while we decrypt support dump file: %1
java com.hp.ci.mgmt.supportdump.util.DecryptionUtil %1