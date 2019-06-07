*** Settings ***
Documentation        OVF1504    APIn018_SPA_role_is_not_allowed_to_modify_fcoe_network_in_its_scope

Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              copy
Library              Collections
Library              String
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./OVF1504_C7000.txt


Variables            ${DATA_FILE}
Test Setup           Pre Test


*** Variables ***
${APPLIANCE_IP}      unknown

*** Test Cases ***
OVF1504_APIn018_SPA_role_is_not_allowed_to_modify_fcoe_network_in_its_scope
    [Documentation]    OVF1504_APIn018_SPA_role_is_not_allowed_to_modify_fcoe_network_in_its_scope
    Log    \n- Test Case: OVF1504_APIn018_SPA_role_is_not_allowed_to_modify_fcoe_network_in_its_scope    console=True
    Fusion Api Login Appliance      ${APPLIANCE_IP}    ${admin_credentials}
    ${resources_list} =    Create List    FCOE:${FCOE1}
    Update Scope With Resources    scope_name=OVF1504Scope    resources_list=${resources_list}    add_flag=${false}
    credential Login     ${credentials_list}
    :FOR     ${credential}     IN     @{credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        Can Not Modify Resources   fcoe_profile=${fcoe_profile}    errorCode=ACTION_FORBIDDEN_BY_ROLE
    Log    \n- Test Case: Successfully: OVF1504_APIn018_SPA_role_is_not_allowed_to_modify_fcoe_network_in_its_scope    console=True
