*** Settings ***
Documentation     Backup and Restore on different Appliance

Library           RoboGalaxyLibrary
Library           FusionLibrary
Library           SSHLibrary
Library           OperatingSystem
Library           String
Library           Collections
Library           XML
Resource          ../Resource/CIM_Backup_Restore_Keyword.txt
Resource          ../Resource/CIM_Common_Resource.txt

***Variables***
${filename}      backup.bkp

***Test Case***

Create Backup and upload on different appliance
    [Documentation]     Create backup one one appliance and upload on a different appliance
    Validate that Both appliance has same version
    Login         ${admin_credentials}
    Create Backup
    Download Backup for OneView
    Login         ${admin_credentials}    ${APPLIANCE_IP_NEW}
    Restore Appliance    ${file}
    Remove File    ${file}

***Keyword***

Validate that Both appliance has same version
    [Documentation]     Check the version for both appliance
    Login         ${admin_credentials}
    ${ver} =    Fusion Api Get Appliance Version
    Log    ${ver}
    ${version1} =    Get From Dictionary    ${ver}    softwareVersion
    Login         ${admin_credentials}    ${APPLIANCE_IP_NEW}
    ${vers} =    Fusion Api Get Appliance Version
    ${version2} =    Get From Dictionary    ${vers}    softwareVersion
    Should Be Equal    ${version1}    ${version2}    msg="The version of the appliance are not same so restore is not possible"
    Log to Console and Logfile    The appliance versions are same so Restore on different appliance is possible.