*** Settings ***
Documentation        OVF1504    APIn026_SPA_role_is_not_allowed_to_modify_SP_not_in_its_scope

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
OVF1504_APIn026_SPA_role_is_not_allowed_to_modify_SP_not_in_its_scope
    [Documentation]    OVF1504_APIn026_SPA_role_is_not_allowed_to_modify_SP_not_in_its_scope
    Log    \n- Test Case: OVF1504_APIn026_SPA_role_is_not_allowed_to_modify_SP_not_in_its_scope    console=True
    Fusion Api Login Appliance      ${APPLIANCE_IP}    ${admin_credentials}
    ${resp} =     Add Server Profile     ${sp_profile}    param=?force=true
    Wait For Task2    ${resp}    timeout=60    interval=5
    ${resources_list} =    Create List    SP:OVF1504_p010_sp
    Update Scope With Resources    scope_name=OVF1504Scope    resources_list=${resources_list}    add_flag=${false}
    credential Login     ${credentials_list}
    :FOR     ${credential}     IN     @{credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        Can Not Modify Resources   sp_profile=${sp1_profile}
    Log    \n- Test Case: Successfully: OVF1504_APIn026_SPA_role_is_not_allowed_to_modify_SP_not_in_its_scope    console=True
