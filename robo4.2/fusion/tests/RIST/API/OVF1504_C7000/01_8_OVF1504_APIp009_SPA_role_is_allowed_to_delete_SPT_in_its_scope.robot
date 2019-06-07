*** Settings ***
Documentation        OVF1504    APIp009_SPA_role_is_allowed_to_delete_SPT_in_its_scope

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
OVF1504_APIp009_SPA_role_is_allowed_to_delete_SPT_in_its_scope
    [Documentation]    OVF1504_APIp009_SPA_role_is_allowed_to_delete_SPT_in_its_scope
    Log    \n- Test Case: OVF1504_APIp009_SPA_role_is_allowed_to_delete_SPT_in_its_scope    console=True
    ${resources_list} =    Create List    SVOL:${VOL3}    FC:${FC1}
    Fusion Api Login Appliance      ${APPLIANCE_IP}    ${admin_credentials}
    Update Scope With Resources    scope_name=OVF1504Scope    resources_list=${resources_list}
    ${index} =    Set Variable    ${0}
    credential Login     ${credentials_list}
    :FOR     ${credential}     IN     @{credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        Can Delete SPT    ${p001_server_profile_template_profiles[${index}]}
    \        ${index} =    Set Variable    ${index+1}
    Log    \n- Test Case: Successfully: OVF1504_APIp009_SPA_role_is_allowed_to_delete_SPT_in_its_scope    console=True
