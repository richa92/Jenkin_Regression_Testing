*** Settings ***
Documentation        OVF1504    APIn012_SPA_role_is_not_allowed_to_poweron_SH_not_in_its_scope

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
Test Setup           Pre Test


*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
OVF1504_APIn012_SPA_role_is_not_allowed_to_poweron_SH_not_in_its_scope
    [Documentation]    OVF1504_APIn012_SPA_role_is_not_allowed_to_poweron_SH_not_in_its_scope
    Log    \n- Test Case: OVF1504_APIn012_SPA_role_is_not_allowed_to_poweron_SH_not_in_its_scope    console=True
    Fusion Api Login Appliance      ${APPLIANCE_IP}    ${admin_credentials}
    ${state} =    Get Server Power    ${SH1}
    Run Keyword If    '${state}'=='On'    Power Off Server    ${SH1}
    credential Login     ${credentials_list}
    :FOR     ${credential}     IN     @{credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        Can Not Power SH    ${SH1}
    Log    \n- Test Case: Successfully: OVF1504_APIn012_SPA_role_is_not_allowed_to_poweron_SH_not_in_its_scope    console=True
