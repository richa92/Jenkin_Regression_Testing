*** Settings ***
Documentation        OVF167 - n006_SA_Role_Group_CanNot_Modify_Other_Resources

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
Test Setup           Pre Condition    directoryProfiles=${directory}   groupProfiles=${n003_sa_role_only_group}
Test Teardown        Clear Test Environment   directoryFlag=${true}

*** Variables ***
${APPLIANCE_IP}      unknown

*** Test Cases ***
OVF167_n006_SA_Role_Group_CanNot_Modify_Other_Resources
    [Documentation]   n006_SA_Role_Group_CanNot_Modify_Other_Resources
    Log To Console    \n- Test Case: n006_SA_Role_Group_CanNot_Modify_Other_Resources
    credential Login     ${group_credentials_list}
    ${index} =    Set Variable    ${0}
    :FOR     ${credential}     IN     @{group_credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        Should Failed To Modify Server Hardware Type    body=${sh_modify_body}
    \        ${index} =    Set Variable    ${index+1}
    Log To Console    \n- Test Case: Successfully: n006_SA_Role_Group_CanNot_Modify_Other_Resources
