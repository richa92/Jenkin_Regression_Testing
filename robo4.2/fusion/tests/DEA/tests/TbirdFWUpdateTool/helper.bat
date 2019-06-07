@ECHO OFF
REM Bypass executionPolicy check for all ps file
PowerShell.exe Set-ExecutionPolicy Bypass -File InputData.ps1
PowerShell.exe Set-ExecutionPolicy Bypass -File TbirdRunner.ps1
PowerShell.exe Set-ExecutionPolicy Bypass -File TbirdLib.psm1
PowerShell.exe Set-ExecutionPolicy Bypass -File Sshlib.psm1
PowerShell.exe Set-ExecutionPolicy Bypass -File TearDown.ps1
REM PowerShell.exe -ExecutionPolicy Bypass

REM unblock dll
powershell.exe Unblock-File .\Posh-SSH\poshssh.dll
powershell.exe Unblock-File .\Posh-SSH\Assembly\Renci.SshNet.dll
powershell.exe Unblock-File .\Posh-SSH\Assembly\Ionic.Zlib.dll
