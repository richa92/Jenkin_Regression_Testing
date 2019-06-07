*** Settings ***
Documentation        Logical Interconnect supports SBAC_Update an Logical Interconnect scope which is the inactive scope
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

Test Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["admin_credentials"]}
Test Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Logical Interconnect supports SBAC_Update an Logical Interconnect scope which is the inactive scope
    [Documentation]  Logical Interconnect supports SBAC_Update an Logical Interconnect scope which is the inactive scope
    Log    Logical Interconnect supports SBAC_Update an Logical Interconnect scope which is the inactive scope    console=true
    Patch Resources Scopes  LI:${LI1}    ${Patch_remove_Scope0}
    Patch Resources Scopes  LI:${LI1}    ${Patch_add_Scope2}

    Active Permission Session  ${edit_ia_users_permission}    ${credentials['ia_credentials']}
    ${resp}=   Patch Resources Scopes  LI:${LI1}    ${Patch_add_Scope5}
    Wait For Task2   ${resp}   timeout=240   PASS=Error  errorMessage=${NOT_AUTHORIZED_ERROR}    VERBOSE=True
    Should Be Equal            '${resp['status_code']}'    '403'

    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[2]}  LI:${LI1}   ${TRUE}
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[5]}  LI:${LI1}   ${FALSE}
    Log    Successfully! Test Case : OVF1592_API_n052 Logical Interconnect supports SBAC_Update an Logical Interconnect scope which is the inactive scope    console=true
