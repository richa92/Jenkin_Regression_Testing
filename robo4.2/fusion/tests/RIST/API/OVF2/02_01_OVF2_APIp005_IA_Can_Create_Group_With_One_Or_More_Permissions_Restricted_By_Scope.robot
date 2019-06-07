*** Settings ***
Documentation        OVF2     APIp005_IA can create group with one or more permissions restricted by scope

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
Test Setup           Clear Test Environment    directoryFlag=${true}    scopeFlag=${true}


*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
OVF2_API_p005_IA can create group with one or more permissions restricted by scope
    [Documentation]    p005_IA can create group with one or more permissions restricted by scope
    Log To Console    \n- Test Case: OVF2APIp005_IA can create group with one or more permissions restricted by scope
    Pre Condition    directoryProfiles=${directory}
    Create Scopes With Resources      ${p001_new_scope_with_resources}
    Create New Group With Scope Restricted     ${p005_new_group}
    Log To Console    \n- Test Case: Successfully: p005_IA can create group with one or more permissions restricted by scope
