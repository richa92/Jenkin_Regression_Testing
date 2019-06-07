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

F444p001 - Check whether the virtual ports can be listed correctly via REST API with resource server-hardware
    Log    Logging in OneView appliance    console=true
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.220.131'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    API F444p001 - Check whether the virtual ports can be listed correctly via REST API with resource server-hardware    console=true
    ${shurilist}=    create list
    ${resp}=         Fusion Api Get Server Hardware
    ${shlist}=       Get From Dictionary     ${resp}   members
    :FOR    ${sh}    IN     @{shlist}
    \       ${uri}=  Get From dictionary  ${sh}  uri
    \       append to list  ${shurilist}  ${uri}
    :FOR    ${shuri}  IN    @{shurilist}
    \       ${resp}=        Fusion Api Get Server Hardware  ${shuri}
    \       ${name}=        Get From Dictionary      ${resp}  name
    \       ${model}=       Get From Dictionary      ${resp}  model
    \       ${state}=       Get From Dictionary      ${resp}  state
    \       Run Keyword If  '${state}' == 'Unmanaged'         Continue For Loop
    \       ${deviceslots}=    Get From Dictionary   ${resp["portMap"]}      deviceSlots
    \       Log    Checking the server hardware model: ${model}, name: ${name}...Skip SH not Gen9...    console=true
    \       ${ret}     ${value}=     Run Keyword and Ignore Error    should match regexp  ${model}  Gen9
    \       Log    value is: ${value}...    console=true
    \       Run Keyword If  '${ret}' == 'FAIL'
    \       ...             Continue For Loop
    \       ...             ELSE    Verify Virtual Port of deviceSlots      ${deviceslots}  ${name}

    Log    Logging out OneView appliance    console=true
    Fusion Api Logout Appliance
