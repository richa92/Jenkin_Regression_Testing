*** Settings ***
Documentation        OVF2     APIp008_IA can delete group with one or more permissions restricted by scope

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
Test Setup           Fusion Api Login Appliance      ${APPLIANCE_IP}    ${admin_credentials}
Test Teardown        Clear Test Environment    directoryFlag=${true}    scopeFlag=${true}

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
OVF2APIp008_IA can delete group with one or more permissions restricted by scope
    [Documentation]    p008_IA can delete group with one or more permissions restricted by scope
    Log To Console    \n- Test Case: OVF2APIp008_IA can delete group with one or more permissions restricted by scope
    ${ret} =    Remove Groups
    Should Be True    ${ret}
    Log To Console    \n- Test Case: Successfully: p008_IA can delete group with one or more permissions restricted by scope
