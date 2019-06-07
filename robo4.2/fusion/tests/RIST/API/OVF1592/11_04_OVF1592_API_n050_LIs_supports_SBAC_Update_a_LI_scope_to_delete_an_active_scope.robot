*** Settings ***
Documentation        Logical Interconnect supports SBAC_Update an Logical Interconnect scope which is the active scope to delete an active scope
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
Logical Interconnect supports SBAC_Update an Logical Interconnect scope which is the active scope to delete an active scope
    [Documentation]  OVF1592_API_n050 Logical Interconnect supports SBAC_Update an Logical Interconnect scope which is the active scope to delete an active scope
    log    Logical Interconnect supports SBAC_Update an Logical Interconnect scope which is the active scope to delete an active scope    console=true
    Active Permission Session  ${edit_ia_users_permission}    ${credentials['ia_credentials']}

    Log    Set the patch body based on the location of Test    console=True
    ${scopes}=    Get Assigned Scope URIs By Resource Name    LI:${LI1}
    ${scope}=    Get Scope URI By Name    ${Scope_List[1]}

    ${body}=    Set Variable If  '${scopes[0]}'=='${scope}'  ${Patch_remove_Scope0}  ${Patch_remove_Scope1}
    ${resp} =    Patch Resources Scopes  LI:${LI1}   ${body}
    Wait For Task2   ${resp}   timeout=240   PASS=Error  errorMessage=${ASSOCIATION_FORBIDDEN_BY_SCOPE}    VERBOSE=True
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  LI:${LI1}  ${TRUE}
    log    Successfully! Test Case : OVF1592_API_n050 Logical Interconnect supports SBAC_Update an Logical Interconnect scope which is the active scope to delete an active scope    console=true
