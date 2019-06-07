*** Settings ***
Documentation        OVF167 - n001_CanNot_Assign_NonExisting_User_With_SO_Role

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

Test Teardown        Clear Test Environment   userFlag=${true}

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
OVF167_n001_CanNot_Assign_NonExisting_User_With_SO_Role
    [Documentation]   n001_CanNot_Assign_NonExisting_User_With_SO_Role
    Log To Console    \n- Test Case: n001_CanNot_Assign_NonExisting_User_With_SO_Role
    Should Failed Assign Non Existing User Role    ${p002_assign_users_so_role}     ${p002_new_users_wo_so_role}
    Log To Console    \n- Test Case: Successfully: n001_CanNot_Assign_NonExisting_User_With_SO_Role
