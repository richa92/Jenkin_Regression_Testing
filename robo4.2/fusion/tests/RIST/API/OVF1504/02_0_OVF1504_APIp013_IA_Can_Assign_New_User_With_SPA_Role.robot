*** Settings ***
Documentation        OVF1504 - APIp013_IA_Can_Assign_New_User_With_SPA_Role

Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              copy
Library              Collections
Library              String
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./OVF1504.txt


Variables            ${DATA_FILE}
Test Setup           Clear Environment
Test Teardown        Clear Environment

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
OVF1504_APIp013_IA_Can_Assign_New_User_With_SPA_Role
    [Documentation]    OVF1504_APIp013_IA_Can_Assign_New_User_With_SPA_Role
    Log     \n- Test Case: OVF1504_APIp013_IA_Can_Assign_New_User_With_SPA_Role    console=True
    Add Users From Variable Async    ${p013_new_users_with_spa_role}
    Log     \n- Test Case: Successfully: OVF1504_APIp013_IA_Can_Assign_New_User_With_SPA_Role    console=True
