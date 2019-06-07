@ECHO OFF
REM ECHO %ScriptDirectory%

SET ScriptDirectory=%~dp0

SET PowerShellScriptPath=%ScriptDirectory%TbirdRunner.ps1 


PowerShell -NoProfile -ExecutionPolicy Bypass -Command "%PowerShellScriptPath%"


Rem  *******************************************************************************
@Echo Off & Echo. 
Echo. &  Echo The evironment variables used: &  Echo. 
Echo JOB_NAME =========== %JOB_NAME%
Echo BUILD_NUMBER ======= %BUILD_NUMBER%
Echo BUILD_ID =========== %BUILD_ID%
Echo BUILD_TAG ========== %BUILD_TAG%
Echo BUILD_URL ========== %BUILD_URL%
ECHO ScriptDirectory ==== %ScriptDirectory%
ECHO PowerShellScriptPath %PowerShellScriptPath%
Echo. &  Echo.