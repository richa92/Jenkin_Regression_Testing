*** Settings ***
Documentation        OVF2     APIp004_IA can delete user with one or more permissions restricted by scope

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
Test Teardown        Clear Test Environment     userFlag=${true}    scopeFlag=${true}

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
OVF2_API_p004_IA can delete user with one or more permissions restricted by scope
    [Documentation]    p004_IA can delete user with one or more permissions restricted by scope
    Log To Console    \n- Test Case: OVF2APIp004_IA can delete user with one or more permissions restricted by scope
    ${ret} =    Remove All Users
    Log To Console    \n- Test Case: Successfully: p004_IA can delete user with one or more permissions restricted by scope
