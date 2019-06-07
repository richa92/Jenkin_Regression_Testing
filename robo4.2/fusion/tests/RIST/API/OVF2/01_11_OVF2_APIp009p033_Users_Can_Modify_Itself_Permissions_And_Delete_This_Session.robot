*** Settings ***
Documentation        OVF2     APIp009p015p033_User can modify retrive and delete user permission with one or more permissions disable and delete it

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
OVF2_API_p009p015p033_User can modify retrive and delete permission with one or more permissions disable
    [Documentation]    p009p015p033_User can modify retrive and delete permission with one or more permissions disable
    credential Login     ${p001_credentials_list}
    ${index} =    Set Variable    ${0}
    :FOR     ${credential}     IN     @{p001_credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        Log To Console     \n- Test Case: OVF2APIp009_User can modify permission with one or more permissions disable
    \        ${session_list} =  Edit User Active Permission    ${p009_edit_users_permission[${index}]}    ${credential['userName']}
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
