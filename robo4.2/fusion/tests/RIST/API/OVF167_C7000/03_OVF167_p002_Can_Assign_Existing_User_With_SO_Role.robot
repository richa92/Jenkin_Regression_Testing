*** Settings ***
Documentation        OVF167 - p002_IA_Can_Assign_Existing_User_With_SO_Role

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
Test Setup           Pre Condition    userProfiles=${p002_new_users_wo_so_role}
Test Teardown        Clear Test Environment   userFlag=${true}

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
OVF167_p002_IA_Can_Assign_Existing_User_With_SO_Role
    [Documentation]    p002_IA_Can_Assign_Existing_User_With_SO_Role
    Log To Console     \n- Test Case: p002_IA_Can_Assign_Existing_User_With_SO_Role
    Edit Existing User Role    ${p002_assign_users_so_role}     ${p002_new_users_wo_so_role}
    Log To Console     \n- Test Case: Successfully: p002_IA_Can_Assign_Existing_User_With_SO_Role
