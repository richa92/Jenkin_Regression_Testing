*** Settings ***
Documentation        Restore appliance, and check the resources can be restored.
Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              copy
Library              Collections
Library              String
Resource             ./../../../../../Resources/api/fusion_api_resource.txt
Variables            ./Restore_Regression_Data.py

Test Setup           Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}
Test Teardown        Fusion Api Logout Appliance
**Suite Teardown       Remove Backup Bin File**

*** Variables ***
${APPLIANCE_IP}      ${fusion_ip}

*** Test Cases ***
Restore Appliance
    Set log level  TRACE
    Log    \n-- Upload the backup file to local disk    console=True
    ${resp}=    Upload Backup   ${EXECDIR}\\${backup_file}
    Should Be Equal As Strings    ${resp["status_code"]}  200
    Log    \n-- Upload and Restore OneView from backup ${backup_file}    console=True
    Restore Appliance      ${EXECDIR}\\${backup_file}

Validate Resource Status After Restore
    Set log level  TRACE
    Log    \nCheck resources status By Name   console=True
    :FOR   ${resource}  IN    @{resources_names}
    \    Check Resource Attribute    ${resource}  status  (?i)OK|Warning

*** Keywords ***
Remove Backup Bin File
    [Documentation]  Remove Backup Bin File
    Run Keyword And Ignore Error    Remove File    ${EXECDIR}\${backup_file}
