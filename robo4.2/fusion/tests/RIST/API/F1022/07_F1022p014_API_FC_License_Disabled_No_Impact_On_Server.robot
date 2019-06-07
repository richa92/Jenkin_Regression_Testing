*** Settings ***
Documentation        F1022p014_API_FC_License_Disabled_No_Impact_On_Server

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
Validate Disabled FC Upgrade License Status And No Impact On Server License
    [Documentation]   F1022p014_API_FC_License_Disabled_No_Impact_On_Server
    ...               Disable FC upgrade license, check its status and check no impact on server license

    Log    \n- Logging in OneView appliance    console=true
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.209.231'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    \nRemoving fc uplinkset from LI.    console=true
    ${us_uri}=    Get Uplinkset URI    ${US_name}
    Should Not Be Equal As Strings  ${us_uri}  '/bad_uplinkset_uri'  msg=The fc uplinkset has been removed previously.
    ${resp}=    Remove Uplinkset By Uri  ${us_uri}
    Wait For Task2   ${resp}    10min    5

    Log    \nChecking the new licenses are existing in license pool    console=true
    Validate Exist Valid Licenses In License Pool But Unassigned To ICM  ${newLicenses}

    Log    Checking licenses has been released from interconnect.    console=true
    Validate Logical Interconnect FC License Consumption  ${LI_name}  ${0}  No

    Log    Checking FC license did not impact serve hardware    console=true
    Validate FC Licenses Didn't Impact Server Hardware

    Log    \n- Logging out OneView appliance    console=true
    Fusion Api Logout Appliance
