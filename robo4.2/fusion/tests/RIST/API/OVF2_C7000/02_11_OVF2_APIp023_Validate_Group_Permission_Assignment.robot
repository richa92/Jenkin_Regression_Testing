*** Settings ***
Documentation        OVF2     APIp023 Validate group permission assignment

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
OVF2_API_p023 Validate group permission assignment
    [Documentation]   p023 Validate group permission assignment
    Log To Console    \n- Test Case: OVF2APIp023 Validate group permission assignment
    ${ret} =    Validate Group Permission Assignment  ${p005_new_group}
    Should Be True    ${ret}
    Log To Console    \n- Test Case: Successfully: p023 Validate group permission assignment
