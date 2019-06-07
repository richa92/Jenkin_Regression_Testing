*** Settings ***
Documentation        OVF167 - n003_SA_Role_User_CanNot_Delete_Other_Resources

Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              copy
Library              Collections
Library              String
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./OVF167.txt


Variables            ${DATA_FILE}
Test Setup           Pre Condition    userProfiles=${n003_sa_role_only_user}
Test Teardown        Clear Test Environment   userFlag=${true}

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
OVF167_n003_SA_Role_User_CanNot_Delete_Other_Resources
    [Documentation]   n003_SA_Role_User_CanNot_Delete_Other_Resources
    Log To Console    \n- Test Case: n003_SA_Role_User_CanNot_Delete_Other_Resources
    credential Login     ${p003_user_credentials_list}
    ${index} =    Set Variable    ${0}
    :FOR     ${credential}     IN     @{p003_user_credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        Should Failed To Delete Server Hardware Type
    \        ${index} =    Set Variable    ${index+1}
    Log To Console    \n- Test Case: Successfully: n003_SA_Role_User_CanNot_Delete_Other_Resources
