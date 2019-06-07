*** Settings ***
Documentation        OVF1504    APIp010_SPA_role_is_allowed_to_create_SP_with_all_resources_in_its_scope

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
OVF1504_APIp010_SPA_role_is_allowed_to_create_SP_with_all_resources_in_its_scope
    [Documentation]    OVF1504_APIp010_SPA_role_is_allowed_to_create_SP_with_all_resources_in_its_scope
    Fusion Api Login Appliance      ${APPLIANCE_IP}    ${admin_credentials}
    ${resources_list} =    Create List    SVOL:${VOL1}    FC:${FC1}
    Update Scope With Resources    scope_name=OVF1504Scope    resources_list=${resources_list}
    credential Login     ${credentials_list}
    :FOR     ${credential}     IN     @{credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        Can Create And Delet SP    ${sp_profile}
    \        Sleep    5s
    Log    \n- Test Case: Successfully: OVF1504_APIp010_SPA_role_is_allowed_to_create_SP_with_all_resources_in_its_scope    console=True
