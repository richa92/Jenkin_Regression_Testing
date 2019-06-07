*** Settings ***
Documentation        OVF1504 - APIp015_IA_Can_Assign_Existing_User_With_SPA_Role

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
Test Setup           Fusion Api Login Appliance      ${APPLIANCE_IP}    ${admin_credentials}
Test Teardown        Clear Environment

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
OVF1504_APIp015_IA_Can_Assign_Existing_User_With_SPA_Role
    [Documentation]    OVF1504_APIp015_IA_Can_Assign_Existing_User_With_SPA_Role
    Log     \n- Test Case: OVF1504_APIp015_IA_Can_Assign_Existing_User_With_SPA_Role    console=True
    Add Users from variable    ${p015_new_users_wo_spa_role}
    Edit Existing User Role    ${p015_assign_users_spa_role}     ${p015_new_users_wo_spa_role}
    Log     \n- Test Case: Successfully: OVF1504_APIp015_IA_Can_Assign_Existing_User_With_SPA_Role    console=True
