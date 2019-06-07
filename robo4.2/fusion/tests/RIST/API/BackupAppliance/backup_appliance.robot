*** Settings ***
Documentation        BackupAppliance
Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              copy
Library              Collections
Library              String
Resource             ../../../../Resources/api/fusion_api_resource.txt

Variables            ./Regression_Data.py

Test Setup           Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}
Test Teardown        Fusion Api Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown

*** Test Cases ***
Backup Appliance Before 3_1 feature test
    [Documentation]    Backup Appliance
    Log    \n-- Backup the appliance    console=true
    Create Backup

    Log    -- Download the backup to local disk    console=true
    ${uri}=     Get Backup URI
    ${resp}=    Download Backup   ${uri}  ${backup_file}
    Should Be Equal As Strings    ${resp["status_code"]}  200
    OperatingSystem.File Should Exist    ${EXECDIR}\\${backup_file}
    ...               msg=Backup file ${backup_file} is not existing in folder ${EXECDIR}