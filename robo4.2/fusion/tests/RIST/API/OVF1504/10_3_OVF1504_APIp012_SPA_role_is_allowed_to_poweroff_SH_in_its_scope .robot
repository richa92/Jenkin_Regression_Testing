*** Settings ***
Documentation        OVF1504    APIp012_SPA_role_is_allowed_to_poweroff_SH_in_its_scope

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
OVF1504_APIp012_SPA_role_is_allowed_to_poweroff_SH_in_its_scope
    [Documentation]    OVF1504_APIp012_SPA_role_is_allowed_to_poweroff_SH_in_its_scope
    Log    \n- Test Case: OVF1504_APIp012_SPA_role_is_allowed_to_poweroff_SH_in_its_scope    console=True
    Fusion Api Login Appliance      ${APPLIANCE_IP}    ${admin_credentials}
    ${state} =    Get Server Power    ${SH1}
    Run Keyword If    '${state}'=='Off'    Power On Server    ${SH1}
    ${resources_list} =    Create List    SH:${SH1}
    Update Scope With Resources    scope_name=OVF1504Scope    resources_list=${resources_list}
    credential Login     ${credentials_list}
    :FOR     ${credential}     IN     @{credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        Can Power SH    ${SH1}    poweron_flag=${false}
    Log   \n- Test Case: Successfully: OVF1504_APIp012_SPA_role_is_allowed_to_poweroff_SH_in_its_scope    console=True
