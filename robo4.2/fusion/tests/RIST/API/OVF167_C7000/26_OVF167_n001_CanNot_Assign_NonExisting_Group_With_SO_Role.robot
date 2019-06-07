*** Settings ***
Documentation        OVF167 - n001_CanNot_Assign_NonExisting_Group_With_SO_Role

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
Test Setup           Pre Condition    directoryProfiles=${directory}
Test Teardown        Clear Test Environment   directoryFlag=${true}

*** Variables ***
${APPLIANCE_IP}      unknown

*** Test Cases ***
OVF167_n001_CanNot_Assign_NonExisting_Group_With_SO_Role
    [Documentation]   n001_CanNot_Assign_NonExisting_Group_With_SO_Role
    Log To Console    \n- Test Case: n001_CanNot_Assign_NonExisting_Group_With_SO_Role
    Log To Console    \n- Start to create different role and permission group and assign them SO role
    Should Failed Assign Non Existing Group Role    ${p002_assign_group_with_so_role}
    Log To Console    \n- Test Case: Successfully: n001_CanNot_Assign_NonExisting_Group_With_SO_Role
