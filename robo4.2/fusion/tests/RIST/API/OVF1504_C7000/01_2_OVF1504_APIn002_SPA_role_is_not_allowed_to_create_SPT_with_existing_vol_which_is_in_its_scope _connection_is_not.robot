*** Settings ***
Documentation        OVF1504    APIn002_SPA_role_is_not_allowed_to_create_SPT_with_existing_vol_which_is_in_its_scope _connection_is_not

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
OVF1504_APIn002_SPA_role_is_not_allowed_to_create_SPT_with_existing_vol_which_is_in_its_scope _connection_is_not
    [Documentation]    OVF1504_APIn002_SPA_role_is_not_allowed_to_create_SPT_with_existing_vol_which_is_in_its_scope _connection_is_not
    Log    \n- Test Case: APIn002_SPA_role_is_not_allowed_to_create_SPT_with_existing_vol_which_is_in_its_scope _connection_is_not    console=True
    ${index} =    Set Variable    ${0}
    credential Login     ${credentials_list}
    :FOR     ${credential}     IN     @{credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        Can Not Create SPT    ${n002_server_profile_template_profiles[${index}]}
    \        ${index} =    Set Variable    ${index+1}
    Log    \n- Test Case: Successfully: APIn002_SPA_role_is_not_allowed_to_create_SPT_with_existing_vol_which_is_in_its_scope _connection_is_not    console=True
