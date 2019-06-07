*** Settings ***
Documentation        OVF2     APIp001_IA can create user with one or more permissions restricted by scope

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
Test Setup           Clear Test Environment   userFlag=${true}   directoryFlag=${true}    scopeFlag=${true}


*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
OVF2_API_p001_IA can create user with one or more permissions restricted by scope
    [Documentation]    p001_IA can create user with one or more permissions restricted by scope
    Log To Console    \n- Test Case: OVF2APIp001_IA can create user with one or more permissions restricted by scope
    Create Scopes With Resources      ${p001_new_scope_with_resources}
    Create New User With Scope Restricted     ${p001_new_user}
    Log To Console    \n- Test Case: Successfully: p001_IA can create user with one or more permissions restricted by scope
