*** Settings ***
Documentation         Server Profiles Associated with Server hardware_Create a server profile which in active scope using a empty bay which in the inactive scope
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

Suite Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["spo_credentials"]}
Test Teardown         Clean Scopes After Test
Suite Teardown        Revert SP Environment After Test    ${Edit_server_profile_base}

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
[SPO] - Server Profiles Associated with Server hardware_Create a server profile which in active scope using a empty bay which in the inactive scope
    [Documentation]  OVF1592 API n165 [SPA] Server Profiles Associated with Server hardware_Create a server profile which in active scope using a empty bay which in the inactive scope

    Log   Edit server profiles sp2     console=True
    ${resp}=  Edit Server Profile  ${Edit_server_profile_EG3}
    Wait For Task2   ${resp}   timeout=600    PASS=Error  errorMessage=${ASSOCIATION_FORBIDDEN_BY_SCOPE}    VERBOSE=True

*** Keywords ***
Clean Scopes After Test
    [Documentation]  Clean Scopes After Test
    Login Appliance  ${APPLIANCE_IP}    ${credentials["admin_credentials"]}
    ${resp}=  Patch Resources Scopes   ENC:${enc_name_list[1]}   ${Patch_remove_Scope0}
    Wait For Task2   ${resp}   timeout=120
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[0]}  ENC:${enc_name_list[1]}   ${False}
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  ENC:${enc_name_list[1]}   ${False}
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[2]}  ENC:${enc_name_list[1]}   ${False}

    ${resp}=  Patch Resources Scopes   EG:${EG_list[4]}   ${Patch_remove_Scope0}
    Wait For Task2   ${resp}   timeout=120
    ${resp}=  Patch Resources Scopes   EG:${EG_list[4]}   ${Patch_add_Scope1}
    Wait For Task2   ${resp}   timeout=120
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  EG:${EG_list[4]}   ${True}
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[2]}  EG:${EG_list[4]}   ${False}
