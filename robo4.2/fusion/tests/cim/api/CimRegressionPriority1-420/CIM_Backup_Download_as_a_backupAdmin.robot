*** Settings ***
Documentation     Backup as a BackupAdminUser and Read-Only User


Library           RoboGalaxyLibrary
Library           FusionLibrary
Library           SSHLibrary
Library           OperatingSystem
Library           String
Library           Collections
Library           XML
Force Tags         Critical
Resource          ../Resource/CIM_User_Keywords.txt
Resource          ../Resource/CIM_Backup_Restore_Keyword.txt
Variables         ../TestData/TestData420.py

***Variables***
${login_user}    BackupAdminUser
${filename}      backup_by_backupadmin.bkp

***Test Case***

Create Backup As Backup Admin User
    [Documentation]     Create backup as a Backup Admin User
    Login    ${admin_credentials}
    Add Users from variable    ${users}
    Logout
    Login As Specific User    ${login_user}
    Create Backup
    Log To Console    Backup Created Succesfully using BackupAdmin User
    Download Backup for OneView   ${filename}
    Log To Console    Backup downloaded using the BackupAdmin User
    Remove File    ${file}
    Log to Console    Backup File ${filename} removed successfully
    Logout
