*** Settings ***
Documentation        OVF1504    APIn010_SPA_role_is_not_allowed_to_edit_SPT_with_new_vol_with_VMTURI_is_userVT_but_it_is_not_in_its_scope

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
OVF1504_APIn010_SPA_role_is_not_allowed_to_edit_SPT_with_new_vol_with_VMTURI_is_userVT_but_it_is_not_in_its_scope
    [Documentation]    OVF1504_APIn010_SPA_role_is_not_allowed_to_edit_SPT_with_new_vol_with_VMTURI_is_userVT_but_it_is_not_in_its_scope
    Log    \n- Test Case: OVF1504_APIn010_SPA_role_is_not_allowed_to_edit_SPT_with_new_vol_with_VMTURI_is_userVT_but_it_is_not_in_its_scope    console=True
    ${index} =    Set Variable    ${0}
    credential Login     ${credentials_list}
    :FOR     ${credential}     IN     @{credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        Can Not Edit SPT    ${n010_server_profile_template_profiles[${index}]}
    \        ${index} =    Set Variable    ${index+1}
    Log    \n- Test Case: Successfully: OVF1504_APIn010_SPA_role_is_not_allowed_to_edit_SPT_with_new_vol_with_VMTURI_is_userVT_but_it_is_not_in_its_scope    console=True
