*** Settings ***
Documentation        Logical Interconnects support SBAC_Try to "update from group" for LI which in the inactive scope
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

Test Setup           Login Appliance    ${APPLIANCE_IP}    ${credentials["admin_credentials"]}
Test Teardown        Clear Test Environment
*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Logical Interconnects support SBAC_Try to "update from group" for LI which in the inactive scope
    [Documentation]  OVF1592_API_n054 Logical Interconnects support SBAC_Try to "update from group" for LI which in the inactive scope
    Prepare Test Environment

    Log    Logical Interconnects support SBAC_Try to "update from group" for LI which in the inactive scope    console=true
    ${resp} =  Update Logical Interconnect Internal Network  ${LI1}    ${li_internal_network_add_active1}
    Wait For Task2   ${resp}   600    10

    Active Permission Session  ${edit_ia_users_permission}    ${credentials['ia_credentials']}
    ${resp} =  Update Logical Interconnect from Group    ${li_update_dto}
    Should Match Regexp        ${resp['message']}    ${errorMessages['NOT_AUTHORIZED_ERROR']}
    Should Be Equal            '${resp['status_code']}'    '403'
    Log    Successfully! Test Case : OVF1592_API_n054 Logical Interconnects support SBAC_Try to "update from group" for LI which in the inactive scope    console=true

*** Keywords ***
Prepare Test Environment
    [Documentation]    Prepare environment for this test
    Patch Resources Scopes  LI:${LI1}    ${Patch_remove_Scope0}
    ${LI_list} =    Create List    LI:${LI1}
    Update Scope With Resources    scope_name=${Scope_List[2]}    resources_list=${LI_list}    add_flag=${TRUE}

    Patch Resources Scopes  LIG:${LIG[4]}    ${Patch_remove_Scope0}
    ${LIG_list} =    Create List    LIG:${LIG[4]}
    Update Scope With Resources    scope_name=${Scope_List[1]}    resources_list=${LIG_list}    add_flag=${TRUE}

Clear Test Environment
    [Documentation]    Clear test environment after LI test completed
    Login Appliance    ${APPLIANCE_IP}    ${credentials["admin_credentials"]}
    ${resp} =  Update Logical Interconnect from Group    ${li_update_dto}