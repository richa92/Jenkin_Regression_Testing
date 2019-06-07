*** Settings ***
Documentation        Server Hardware support SBAC_Update an Server which is the active scope to delete an active scope
Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              copy
Library              Collections
Library              String
Library              json
Library              XML
Library              SSHLibrary
Library              Dialogs
Variables            ${DATA_FILE}
Resource             ./../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt


*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Server Hardware support SBAC_Update an Server which is the active scope to delete an active scope
    [Documentation]    erver Hardware support SBAC_Update an Server which is the active scope to delete an active scope
    Fusion Api Login Appliance      ${APPLIANCE_IP}    ${credentials['admin_credentials']}
    ${resources_list} =    Create List    SH:${sh_name}
    Update Scope With Resources    scope_name=${Scope_List[1]}    resources_list=${resources_list}

    Log    Set the patch body based on the location of Test    console=True
    ${scopes}=    Get Assigned Scope URIs By Resource Name    SH:${sh_name}
    ${scope}=    Get Scope URI By Name    ${Scope_List[1]}

    ${body}=    Set Variable If  '${scopes[0]}'=='${scope}'  ${Patch_remove_Scope0}  ${Patch_remove_Scope1}
    Fusion Api Logout Appliance

    log    Server Hardware support SBAC_Update an Server which is the active scope to delete an active scope    console=true
    Active Permission Session  ${edit_ia_users_permission}    ${credentials['ia_credentials']}
    ${resp} =    Patch Resources Scopes  SH:${sh_name}   ${body}
    Wait For Task2   ${resp}   timeout=200   PASS=Error  errorMessage=${ASSOCIATION_FORBIDDEN_BY_SCOPE}    VERBOSE=True

    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  SH:${sh_name}  ${TRUE}
    log    Successfully! Test Case : OVF1592_API_n138 Server Hardware support SBAC_Update an Server which is the active scope to delete an active scope    console=true
