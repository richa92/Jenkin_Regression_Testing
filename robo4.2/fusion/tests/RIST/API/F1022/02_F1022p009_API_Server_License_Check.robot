*** Settings ***
Documentation        F1022 - Support 8G FC Upgrade Licensing

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
Validate Server License Informaton
    [Documentation]    F1022p009_API_Server_License_Check.
    ...                Validate the auto-discovered FC license can not be applied to serve hardware after Re-image Tbird OV

    Log    \n- Logging in OneView appliance    console=true
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.209.231'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    \nChecking the server hardware info    console=true
    Validate FC Licenses Didn't Impact Server Hardware

    Log    \n- Logging out OneView appliance    console=true
    Fusion Api Logout Appliance
