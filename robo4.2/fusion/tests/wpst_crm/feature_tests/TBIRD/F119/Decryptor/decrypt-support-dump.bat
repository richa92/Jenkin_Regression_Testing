@echo off
echo *********************************
echo Utility to decrypt support dump
echo *********************************
echo.

if "%1" NEQ "-f" (
    echo Invalid option. Valid command: decrypt-support-dump -f absolute-path-of-support-dump-file -k absolute-path-of-private-key-file
    exit /B
)
if not exist ""%2"" (
    echo Support dump file was not found.
    exit /B
)
if "%3" NEQ "-k" (
    echo Invalid option. Valid command: decrypt-support-dump -f absolute-path-of-support-dump-file -k absolute-path-of-private-key-file
    exit /B
)
if not exist "%4" (
    echo Private key file was not found.
    exit /B
)

rem Set the jar in the classpath
echo *********************************
echo Setting classpath
echo *********************************
echo.
echo %~dp0
set classpath=%~dp0\Decryption-Util.jar;%CLASSPATH%
echo %classpath%
echo.

echo Support dump file: %2
echo Private Key file: %4
rem Decrypting support dump
java com.hp.ci.mgmt.supportdump.util.EncryptionUtil %2 %4

