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
F444p006 - Check whether the connections with virtual ports(5-8) can be listed correctly
    Log    Logging in OneView appliance    console=true
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.220.131'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    F444p006 - Check whether the connections with virtual ports(5-8) can be listed correctly    console=true
    ${resp} =         Fusion Api Get connections
    ${connlist} =     Get From Dictionary        ${resp}       members
    should not be empty      ${connlist}    F444p006 - API - There is no connection created at all.
    ${count} =        get length   ${connlist}
    Log    total virtual port number of physical port is ${count}    console=true
    :FOR    ${conn}    IN    @{connlist}
    \       ${name} =        Get From dictionary     ${conn}   name
    \       ${connuri} =     Get From dictionary     ${conn}   uri
    \       ${resp} =        Fusion Api Get connections        ${connuri}

    Log    Logging out OneView appliance    console=true
    Fusion Api Logout Appliance