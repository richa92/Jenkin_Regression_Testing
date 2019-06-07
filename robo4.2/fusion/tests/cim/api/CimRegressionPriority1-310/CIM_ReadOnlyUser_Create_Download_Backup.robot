*** Settings ***
Documentation     Backup Restore as Read only User


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

***Variables***
${login_user}    ReadOnlyUser
${filename}      backup.bkp

***Test Case***

Create Backup As Read Only User
    [Documentation]     Create backup as a read Only user
    Login    ${admin_credentials}
    Remove User
    Create Backup
    Add Users from variable    ${users}
    Logout
    Login As Specific User    ${login_user}
    ${state} =    Run Keyword And Return Status    Create Backup
    Run Keyword If    '${state}' == 'True'    Fail    msg= The ReadOnly user should not be able to create backup
    Log To Console And Logfile    ReadOnlyUser cannot create backup

    #Download Backup as Readonly user
    ${state} =    Run Keyword And Return Status    Download Backup for OneView    ${filename}
    ${TextFileContent}=    OperatingSystem.Get File    ${file}
    Should Contain    '${TextFileContent}'    User not authorized for this operation.    msg=Back up downloaded
    Run Keyword If    '${state}' == 'True'     Fail    msg= The ReadOnly user should not be able to download backup
    Log To Console And Logfile    ReadOnly user is not Authorized to download backup.

    #Clean up
    Login    ${admin_credentials}
    Remove User
    Remove File    ${file}