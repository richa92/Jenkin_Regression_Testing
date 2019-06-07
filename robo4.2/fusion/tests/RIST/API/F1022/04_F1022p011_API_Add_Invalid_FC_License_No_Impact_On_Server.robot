*** Settings ***
Documentation        F1022p011_API_Add_Invalid_FC_License_No_Impact_On_Server

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
Validate Invalid FC License No Impact On Server License
    [Documentation]   F1022p011_API_Add_Invalid_FC_License_No_Impact_On_Server.
    ...               Add invalid FC upgrade license, check its status and and check no impact on server license

    Log    \n- Logging in OneView appliance    console=true
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.209.231'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    \nChecking the invalid license is not existing in license pool    console=true
    Validate Invalid Licenses Is Not Existing In License Pool  ${newLicenses}

    Log    Try to add the new invalid licenses    console=true
    Run Keyword And Ignore Error    Add Licenses From Variable    ${newLicenses["invalidLicense"]}

    Log    Checking the license is not added into license pool    console=true
    Validate Invalid Licenses Is Not Existing In License Pool  ${newLicenses}

    Log    Checking FC license did not be applied to serve hardware    console=true
    Validate FC Licenses Didn't Impact Server Hardware

    Log    \n- Logging out OneView appliance    console=true
    Fusion Api Logout Appliance
