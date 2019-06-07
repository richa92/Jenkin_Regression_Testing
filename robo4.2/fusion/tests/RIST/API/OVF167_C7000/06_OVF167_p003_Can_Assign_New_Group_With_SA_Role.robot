*** Settings ***
Documentation        OVF167 - p003_IA_Can_Assign_New_Group_With_SA_Role

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
Test Setup           Pre Condition     ${directory}
Test Teardown        Clear Test Environment   directoryFlag=${true}

*** Variables ***
${APPLIANCE_IP}      unknown

*** Test Cases ***
OVF167_p003_IA_Can_Assign_New_Group_With_SA_Role
    [Documentation]    p003_Can_Assign_New_Group_With_SA_Role
    Log To Console     \n- Test Case: p003_Can_Assign_New_Group_With_SA_Role
    Create Groups      ${p003_new_group_with_sa_role}
    Log To Console     \n- Test Case: Successfully p003_Can_Assign_New_Group_With_SA_Role
