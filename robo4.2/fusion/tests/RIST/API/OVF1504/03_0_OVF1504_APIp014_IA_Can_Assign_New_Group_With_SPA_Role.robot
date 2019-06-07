*** Settings ***
Documentation        OVF1504- APIp014_IA_Can_Assign_New_Group_With_SPA_Role

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
OVF1504_APIp014_IA_Can_Assign_New_Group_With_SPA_Role
    [Documentation]    OVF1504_APIp014_IA_Can_Assign_New_Group_With_SPA_Role
    Log     \n- Test Case: OVF1504_APIp014_IA_Can_Assign_New_Group_With_SPA_Role    console=True
    Prepare Directories For Test   ${directory_profiles}
    Create Groups      ${p014_new_group_with_spa_role}
    Log     \n- Test Case: Successfully: OVF1504_APIp014_IA_Can_Assign_New_Group_With_SPA_Role    console=True
