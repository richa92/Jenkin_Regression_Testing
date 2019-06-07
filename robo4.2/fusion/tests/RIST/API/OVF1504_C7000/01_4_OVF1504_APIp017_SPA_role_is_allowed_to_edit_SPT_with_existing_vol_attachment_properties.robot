*** Settings ***
Documentation        OVF1504    APIp017_SPA_role_is_allowed_to_edit_SPT_with_existing_vol_attachment_properties

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

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
OVF1504_APIp017_SPA_role_is_allowed_to_edit_SPT_with_existing_vol_attachment_properties
    [Documentation]    OVF1504_APIp017_SPA_role_is_allowed_to_edit_SPT_with_existing_vol_attachment_properties
    Log    \n- Test Case: OVF1504_APIp017_SPA_role_is_allowed_to_edit_SPT_with_existing_vol_attachment_properties    console=True
    ${index} =    Set Variable    ${0}
    credential Login     ${credentials_list}
    :FOR     ${credential}     IN     @{credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        Can Update SPT    ${p017_server_profile_template_profiles[${index}]}
    \        ${index} =    Set Variable    ${index+1}
    Log    \n- Test Case: Successfully: OVF1504_APIp017_SPA_role_is_allowed_to_edit_SPT_with_existing_vol_attachment_properties    console=True
