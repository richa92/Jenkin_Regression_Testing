*** Settings ***
Documentation        OVF2     APIp0010p032_Group can modify user permission with one or more permissions disable and delete it

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
OVF2APIp010p032_Grou[ can modify permission with one or more permissions disable and delete it
    [Documentation]    p010_Group can modify permission with one or more permissions disable
    credential Login     ${p005_credentials_list}
    ${index} =    Set Variable    ${0}
    :FOR     ${credential}     IN     @{p005_credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        Log To Console     \n- Test Case: OVF2APIp009_User can modify permission with one or more permissions disable
    \        ${session_list} =  Edit User Active Permission    ${p010_edit_groups_permission[${index}]}    ${credential['userName']}
    \        Log To Console     \n- Test Case: Successfully: p009_User can modify permission with one or more permissions disable
    \        Log To Console     \n- Test Case: OVF2APIp015_Retrieves user session
    \        ${ret} =  Retrieve Sessions    ${session_list}
    \        Should Be True    ${true}
    \        Log To Console     \n- Test Case: Successfully: p015_Retrive user session
    \        Log To Console     \n- Test Case: OVF2APIp033_Remove user session
    \        ${ret} =  Delete Sessions    ${session_list}
    \        Should Be True    ${true}
    \        Log To Console     \n- Test Case: Successfully: p033_Remove user session
    \        ${index} =    Set Variable    ${index+1}
