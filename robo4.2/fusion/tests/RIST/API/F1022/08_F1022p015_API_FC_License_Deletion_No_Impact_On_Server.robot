*** Settings ***
Documentation        F1022p015_API_FC_License_Deletion_No_Impact_On_Server

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
Validate Deleted FC Upgrade License Status And No Impact On Server License
    [Documentation]   F1022p015_API_FC_License_Deletion_No_Impact_On_Server
    ...               Delete FC upgrade license, check its status and check no impact on server license

    Log    \n- Logging in OneView appliance    console=true
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.209.231'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    \nRemoving all FC licenses from license pool    console=true
    Remove All FC Licenses

    Log    Checking all FC licenses are deleted from license pool    console=true
    Validate Not Exist FC Licenses In License Pool    ${newLicenses}

    Log    Checking FC license did not be applied to serve hardware    console=true
    Validate FC Licenses Didn't Impact Server Hardware

    Log    \n- Logging out OneView appliance    console=true
    Fusion Api Logout Appliance
