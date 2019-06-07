*** Settings ***
Documentation        F1022p010_API_Add_FC_License_No_Impact_On_Server

Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              copy
Library              Collections
Library              String
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt

Variables            ${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Validate The FC license Addition No Impact On Server License
    [Documentation]    F1022p010_API_Add_FC_License_No_Impact_On_Server
    ...                Validate the FC license that manually added can not be applied to serve hardware

    Log    \n- Logging in OneView appliance    console=true
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.209.231'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    \nRemoving existing FC licenses before testing    console=true
    Remove All FC Licenses

    Log    Adding new licenses    console=true
    ${validLicenses}=     Get From Dictionary  ${newLicenses}  license
    Add Licenses From Variable    ${validLicenses}

    Log    Checking the new licenses are added into license pool    console=true
    Validate Exist Valid Licenses In License Pool But Unassigned To ICM    ${newLicenses}

    Log    Checking FC license did not be applied to serve hardware    console=true
    Validate FC Licenses Didn't Impact Server Hardware

    Log    \n- Logging out OneView appliance    console=true
    Fusion Api Logout Appliance
