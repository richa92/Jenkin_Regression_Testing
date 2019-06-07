*** Settings ***
Documentation        OVF2     APIp002_IA can view user with one or more permissions restricted by scope

Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              copy
Library              Collections
Library              String
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./OVF2.txt

Variables            ${DATA_FILE}


*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
OVF2_API_p002_IA can view user with one or more permissions restricted by scope
    [Documentation]   p002_IA can view user with one or more permissions restricted by scope
    Log To Console    \n- Test Case: OVF2APIp002_IA can view user with one or more permissions restricted by scope
    ${ret} =    Validate User With Permissions
    Should Be True    ${ret}
    Log To Console    \n- Test Case: Successfully: p002_IA can view user with one or more permissions restricted by scope
