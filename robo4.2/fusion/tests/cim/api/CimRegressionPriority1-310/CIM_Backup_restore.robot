*** Settings ***
Documentation     Backup Restore


Library           RoboGalaxyLibrary
Library           FusionLibrary
Library           SSHLibrary
Library           OperatingSystem
Library           String
Library           Collections
Library           XML
Resource          ../Resource/CIM_Backup_Restore_Keyword.txt


***Test Case***

Create Backup and download to local
    [Documentation]     Create backup and download
    Login    ${admin_credentials}
    Create Backup
    Download Backup for OneView
    Logout

Upload backup and restore appliance
    [Documentation]     Upload backup and restore
    Login    ${admin_credentials}
    Restore Appliance    ${file}
    Remove File    ${file}
    Logout
