*** Settings ***
Documentation        SA-Associated with Drive Enclosure_Create a new server profile, validate user has "use" rights on drive-enclosures category
Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              copy
Library              Collections
Library              String
Library              json
Library              XML
Library              SSHLibrary
Library              Dialogs
Variables            ${DATA_FILE}
Resource             ./../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt

Test Setup           Run Keywords  Login Appliance  ${APPLIANCE_IP}    ${credentials["admin_credentials"]}
...                  AND           Prepare Environment For Test
Test Teardown        Clear Environment After Test   ${create_server_profile_de1}  Remove

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Server Profiles Associated with Drive Enclosure Create a new active sp validate user has use rights on drive enclosures
    Log   Create new server profiles sp5 with inactive drive enclosure storage    console=True
    Active Permission Session  ${edit_sa_users_permission}    ${credentials['sa_credentials']}
    ${resp}=  Add Server Profile  ${create_server_profile_de1}
    Wait For Task2   ${resp}  timeout=20m  interval=10
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  SP:${new_sp_name}   ${True}
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  DE:${drive_enc}   ${False}
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[2]}  DE:${drive_enc}   ${True}

*** Keywords ***
Prepare Environment For Test
    [Documentation]  Prepare Environment For Test
    Log    Change the scope from "Test" to "Stage"    console=True
    ${resp}=  Patch Resources Scopes   DE:${drive_enc}   ${Patch_remove_Scope0}
    Wait For Task2   ${resp}  timeout=60
    ${resp}=  Patch Resources Scopes   DE:${drive_enc}   ${Patch_add_Scope2}
    Wait For Task2   ${resp}  timeout=60
