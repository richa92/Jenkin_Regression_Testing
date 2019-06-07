*** Settings ***
Documentation        OVF1504    APIp008_SPA_role_is_allowed_to_edit_SPT_with_new_vol_with_VMTURI_is_userVT_but_related_sp_is_not_in_its_scope

Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              copy
Library              Collections
Library              String
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./OVF1504.txt


Variables            ${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}      unknown

*** Test Cases ***
OVF1504_APIp008_SPA_role_is_allowed_to_edit_SPT_with_new_vol_with_VMTURI_is_userVT_but_related_sp_is_not_in_its_scope
    [Documentation]    OVF1504_APIp008_SPA_role_is_allowed_to_edit_SPT_with_new_vol_with_VMTURI_is_userVT_but_related_sp_is_not_in_its_scope
    Log    \n- Test Case: OVF1504_APIp008_SPA_role_is_allowed_to_edit_SPT_with_new_vol_with_VMTURI_is_userVT_but_related_sp_is_not_in_its_scope    console=True
    Fusion Api Login Appliance      ${APPLIANCE_IP}    ${admin_credentials}
    ${resources_list} =    Create List    SPOOL:${SP1}
    Update Scope With Resources    scope_name=OVF1504Scope    resources_list=${resources_list}    add_flag=${false}
    ${index} =    Set Variable    ${0}
    credential Login     ${credentials_list}
    :FOR     ${credential}     IN     @{credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        Log to console   \nJanedebu_current_user_is_${credential['userName']}
    \        Can Update SPT    ${p008_server_profile_template_profiles[${index}]}
    \        ${index} =    Set Variable    ${index+1}
    Log    \n- Test Case: Successfully: OVF1504_APIp008_SPA_role_is_allowed_to_edit_SPT_with_new_vol_with_VMTURI_is_userVT_but_related_sp_is_not_in_its_scope    console=True
