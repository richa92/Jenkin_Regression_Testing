*** Settings ***
Documentation        OVF1504    APIn021_SPA_role_is_not_allowed_to_modify_li_not_in_its_scope

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
OVF1504_APIn021_SPA_role_is_not_allowed_to_modify_li_not_in_its_scope
    [Documentation]    OVF1504_APIn021_SPA_role_is_not_allowed_to_modify_li_not_in_its_scope
    Log    \n- Test Case: OVF1504_APIn021_SPA_role_is_not_allowed_to_modify_li_not_in_its_scope    console=True
    credential Login     ${credentials_list}
    :FOR     ${credential}     IN     @{credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        Can Not Modify Resources   li_profile=${li_profile}    errorCode=ACTION_FORBIDDEN_BY_ROLE
    Log    \n- Test Case: Successfully: OVF1504_APIn021_SPA_role_is_not_allowed_to_modify_li_not_in_its_scope    console=True
