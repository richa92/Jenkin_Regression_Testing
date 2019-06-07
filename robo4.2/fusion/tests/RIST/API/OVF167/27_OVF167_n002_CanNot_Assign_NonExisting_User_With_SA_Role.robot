*** Settings ***
Documentation        OVF167 - n002_CanNot_Assign_NonExisting_User_With_SA_Role

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
OVF167_n002_CanNot_Assign_NonExisting_User_With_SA_Role
    [Documentation]   n002_CanNot_Assign_NonExisting_User_With_SA_Role
    Log To Console    \n- Test Case: n002_CanNot_Assign_NonExisting_User_With_SA_Role
    Should Failed Assign Non Existing User Role    ${p004_assign_users_sa_role}     ${p004_new_users_wo_sa_role}
    Log To Console    \n- Test Case: Successfully: n002_CanNot_Assign_NonExisting_User_With_SA_Role
