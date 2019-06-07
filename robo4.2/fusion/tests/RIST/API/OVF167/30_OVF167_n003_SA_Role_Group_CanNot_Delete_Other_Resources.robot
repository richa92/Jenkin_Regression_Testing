*** Settings ***
Documentation        OVF167 - n003  Group Can Not Delete Other Resources with sa role

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
OVF167_n003 Group Can Not Delete Other Resources with sa role
    [Documentation]    User Can Not Delete Other Resources with sa role
    credential Login     ${group_credentials_list}
    ${index} =    Set Variable    ${0}
    :FOR     ${credential}     IN     @{group_credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        Should Failed To Delete Server Hardware Type
    \        ${index} =    Set Variable    ${index+1}
    Log To Console    \n- Test Case: Successfully User Can Not Delete Other Resources with sa role
