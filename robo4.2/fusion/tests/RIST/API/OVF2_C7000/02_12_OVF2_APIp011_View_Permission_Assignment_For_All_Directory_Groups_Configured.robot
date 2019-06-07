*** Settings ***
Documentation        OVF2     APIp011 View permission assignments for all directory groups configured for a particular directory

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
OVF2_API_p011 View permission assignments for all directory groups configured for a particular directory
    [Documentation]   p011 View permission assignments for all directory groups configured for a particular directory
    Log To Console    \n- Test Case: OVF2APIp011 View permission assignments for all directory groups configured for a particular directory
    ${ret} =    View All Directory Groups Permission Assignment
    Should Be True    ${ret}
    Log To Console    \n- Test Case: Successfully: p011 View permission assignments for all directory groups configured for a particular directory
