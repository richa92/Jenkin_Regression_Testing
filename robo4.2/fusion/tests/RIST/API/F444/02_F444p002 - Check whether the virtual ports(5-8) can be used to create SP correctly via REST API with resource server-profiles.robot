*** Settings ***
Documentation        F444_API_test cases automation.

Library              RoboGalaxyLibrary
Library              FusionLibrary
Library              OperatingSystem
Library              BuiltIn
Library              Collections
Library              XML
Library              SSHLibrary
Library              String
Library              json
Library  			 Dialogs

Resource             ./keywords.txt
Resource             ../../../../Resources/api/fusion_api_resource.txt

Variables            ${DATA_FILE}


*** Variables ***
${APPLIANCE_IP}             unknown
${F444_SP}                  F444_SP
${F444p003_verified}        unknown
${F444_SPT}                 F444_SPT
${F444p005_verified}        unknown


*** Test Cases ***
F444p002 - Check whether the virtual ports(5-8) can be used to create SP correctly via REST API with resource server-profiles
    Log    Logging in OneView appliance    console=true
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.220.131'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    Check whether the virtual ports(5-8) can be used to create SP correctly via REST API with resource server-profiles    console=true
    Power Off Servers in Profiles  ${F444_server_profile}
    ${list}=  Add Server Profiles from variable	 ${F444_server_profile}
    Wait For Task2  ${list}  timeout=1200  interval=20

    Log    Logging out OneView appliance    console=true
    Fusion Api Logout Appliance