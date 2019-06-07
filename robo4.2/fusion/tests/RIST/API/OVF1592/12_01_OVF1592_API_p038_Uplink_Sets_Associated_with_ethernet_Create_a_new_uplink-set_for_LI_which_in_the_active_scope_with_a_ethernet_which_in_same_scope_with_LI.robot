*** Settings ***
Documentation        Uplink Sets Associated with ethernet Create a new uplink set for LI which in the active scope with a ethernet which in same scope with LI
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
Test Teardown        Logout Appliance
*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Uplink Sets Associated with ethernet Create a new uplink set for LI which in the active scope with a ethernet which in same scope with LI
    Prepare Test Environment
    Active Permission Session  ${edit_ia_users_permission}    ${credentials['ia_credentials']}
    Log  Create uplinksets for LI
    ${resps}=   Add Uplinkset from variable Async    ${add_Uplinksets1}
    Wait For Task2  ${resps}    timeout=240

*** Keywords ***
Prepare Test Environment
    [Documentation]  Prepare Test Environment
    Patch Resources Scopes  LI:${LI1}    ${Patch_remove_Scope0}
    ${LI_list} =    Create List    LI:${LI1}
    Update Scope With Resources    scope_name=${Scope_List[1]}    resources_list=${LI_list}    add_flag=${TRUE}

    Patch Resources Scopes  LIG:${LIG[4]}    ${Patch_remove_Scope0}
    ${LIG_list} =    Create List    LIG:${LIG[4]}
    Update Scope With Resources    scope_name=${Scope_List[1]}    resources_list=${LIG_list}    add_flag=${TRUE}
