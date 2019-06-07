*** Settings ***
Documentation        OVF2     APIp003_IA can edit user with one or more permissions restricted by scope

Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              copy
Library              Collections
Library              String
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./OVF2_C7000.txt


Variables            ${DATA_FILE}
Test Setup           Fusion Api Login Appliance      ${APPLIANCE_IP}    ${admin_credentials}


*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
OVF2_APIp007 Can edit existing group with permission restricted by scope
    [Documentation]    p003_can edit user with one or more permissions restricted by scope
    Log To Console    \n- Test Case: OVF2APIp003_IA can edit user with one or more permissions restricted by scope
    Edit Existing Group Role    ${p005_new_group}
    Log To Console    \n- Test Case: Successfully: p003_IA can edit user with one or more permissions restricted by scope
