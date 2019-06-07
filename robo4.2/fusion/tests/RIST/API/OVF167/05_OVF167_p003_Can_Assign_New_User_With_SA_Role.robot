*** Settings ***
Documentation        OVF167 - p003_IA_Can_Assign_New_User_With_SA_Role

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
OVF167_p003_IA_Can_Assign_New_User_With_SA_Role
    [Documentation]    p003_IA_Can_Assign_New_User_With_SA_Role
    Log To Console     \n- Test Case: Create New different role use and at same time assign sa role to them
    Add Users From Variable Async    ${p003_new_users_with_sa_role}
    Log To Console     \n- Test Case: Successfully p003_IA_Can_Assign_New_User_With_SA_Role
