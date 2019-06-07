*** Settings ***
Documentation        OVF1504    APIn022_SPA_role_is_not_allowed_to_modify_interconnect_in_its_scope

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
OVF1504_APIn022_SPA_role_is_not_allowed_to_modify_interconnect_in_its_scope
    [Documentation]    OVF1504_APIn022_SPA_role_is_not_allowed_to_modify_interconnect_in_its_scope
    Log    \n- Test Case: OVF1504_APIn022_SPA_role_is_not_allowed_to_modify_interconnect_in_its_scope    console=True
    Fusion Api Login Appliance      ${APPLIANCE_IP}    ${admin_credentials}
    ${resources_list} =    Create List    IC:${INTERCONNECT1}
    Update Scope With Resources    scope_name=OVF1504Scope    resources_list=${resources_list}
    credential Login     ${credentials_list}
    :FOR     ${credential}     IN     @{credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        Can Not Modify Resources   interconnect_dto=${interconnect_dto}    errorCode=ACTION_FORBIDDEN_BY_ROLE
    Log    \n- Test Case: Successfully: OVF1504_APIn022_SPA_role_is_not_allowed_to_modify_interconnect_in_its_scope    console=True
