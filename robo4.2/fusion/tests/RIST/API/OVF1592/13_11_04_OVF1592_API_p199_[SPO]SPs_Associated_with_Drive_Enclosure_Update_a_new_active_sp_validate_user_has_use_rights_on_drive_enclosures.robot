*** Settings ***
Documentation        Associated with Drive Enclosure_Update a new server profile, validate user has "use" rights on drive-enclosures category
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

Test Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["spo_credentials"]}
Test Teardown        Run Keywords    Revert SP Environment After Test    ${Edit_sp_network_base}
...                  AND             Revert Drive Enclosure Scope After Test
*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
[SPO] - Server Profiles Associated with Drive Enclosure Update a new active sp validate user has use rights on drive enclosures
    Log   Update server profiles sp2 with inactive drive enclosure storage    console=True
    ${resp}=  Edit Server Profile  ${Edit_server_profile_de1}
    Wait For Task2   ${resp}  timeout=20m  interval=10

*** Keywords ***
Revert Drive Enclosure Scope After Test
    [Documentation]  Revert Drive Enclosure Scope After Test
    Log    Change the scope from "Stage" to "Test"    console=True
    Login Appliance  ${APPLIANCE_IP}    ${credentials["admin_credentials"]}
    ${resp}=  Patch Resources Scopes   DE:${drive_enc}   ${Patch_remove_Scope0}
    Wait For Task2   ${resp}  timeout=60
    ${resp}=  Patch Resources Scopes   DE:${drive_enc}   ${Patch_add_Scope1}
    Wait For Task2   ${resp}  timeout=60
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  DE:${drive_enc}   ${True}
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[2]}  DE:${drive_enc}   ${False}
