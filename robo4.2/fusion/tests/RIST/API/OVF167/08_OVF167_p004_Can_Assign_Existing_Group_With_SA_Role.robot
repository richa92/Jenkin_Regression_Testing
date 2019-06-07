*** Settings ***
Documentation        OVF167 - p004_IA_Can_Assign_Existing_Group_With_SA_Role

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
Test Setup           Pre Condition    directoryProfiles=${directory}   groupProfiles=${p004_new_group_wo_sa_role}
Test Teardown        Clear Test Environment   directoryFlag=${true}

*** Variables ***
${APPLIANCE_IP}      unknown

*** Test Cases ***
OVF167_p004_IA_Can_Assign_Existing_Group_With_SA_Role
    [Documentation]   p004_IA_Can_Assign_Existing_Group_With_SA_Role
    Log To Console    \n- Test Case: p004_IA_Can_Assign_Existing_Group_With_SA_Role
    Edit Group Role Assignment    ${p004_assign_group_with_sa_role}
    Log To Console    \n- Test Case: Successfully p004_IA_Can_Assign_Existing_Group_With_SA_Role
