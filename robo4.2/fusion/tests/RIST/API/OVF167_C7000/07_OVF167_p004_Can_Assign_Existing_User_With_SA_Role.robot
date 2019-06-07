*** Settings ***
Documentation        OVF167 - p004_IA_Can_Assign_Existing_User_With_SA_Role

Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              copy
Library              Collections
Library              String
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./OVF167_C7000.txt

Variables            ${DATA_FILE}
Test Setup           Pre Condition    userProfiles=${p004_new_users_wo_sa_role}
Test Teardown        Clear Test Environment   userFlag=${true}

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
OVF167_p004_IA_Can_Assign_Existing_User_With_SA_Role
    [Documentation]   p004_IA_Can_Assign_Existing_User_With_SA_Role
    Log To Console    \n- Test Case: p004_IA_Can_Assign_Existing_User_With_SA_Role
    Edit Existing User Role    ${p004_assign_users_sa_role}     ${p004_new_users_wo_sa_role}
    Log To Console    \n- Test Case: Successfully p004_IA_Can_Assign_Existing_User_With_SA_Role
