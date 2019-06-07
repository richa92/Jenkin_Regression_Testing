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
F444p005 - Check whether the connection with virtual ports(5-8) in SPT can be listed correctly via REST API with resource server-profile-templates
    Log    Logging in OneView appliance    console=true
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.220.131'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    F444p005 - Check whether the connection with virtual ports(5-8) in SPT can be listed correctly via REST API with resource server-profile-templates    console=true
    Should Not Be Equal     ${F444_SPT}    'unknown'    msg=Please specify a valid server profile template
    ${resp} =               Fusion Api Get Server Profile templates
    ${sptlist} =            Get From Dictionary        ${resp}     members
    should not be empty     ${sptlist}    F444p005 - API - There is no server profile template created at all.
    :FOR    ${spt}    IN    @{sptlist}
    \       ${name} =       Get From dictionary     ${spt}    name
    \       Run Keyword If  '${name}' == '${F444_SPT}'        Verify connections in server profile template    ${spt}
    run keyword if          '${F444p005_verified}' != 'True'        FAIL   F444p005 - API - There is no server profile template ${F444_SPT} available for testing. set case to failure.

    Log    Logging out OneView appliance    console=true
    Fusion Api Logout Appliance