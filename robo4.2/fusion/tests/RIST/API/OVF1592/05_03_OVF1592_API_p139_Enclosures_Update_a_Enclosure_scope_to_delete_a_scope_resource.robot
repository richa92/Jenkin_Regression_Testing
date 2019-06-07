*** Settings ***
Documentation        Enclosures supports SBAC_Update a Enclosure scope which is the active scope to delete a scope resource
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
Enclosures supports SBAC_Update a Enclosure scope which is the active scope to remove a scope resource
    [Documentation]  OVF1592_API_p139 Enclosures supports SBAC_Update a Enclosure scope which is the active scope to delete a scope resource
    Log    Set the patch body based on the location of scope1    console=True
    ${scopes}=    Get Assigned Scope URIs By Resource Name    ENC:${new_enc_name}
    ${scope}=    Get Scope URI By Name    ${Scope_List[3]}

    ${body}=    Set Variable If  '${scopes[0]}'=='${scope}'  ${Patch_remove_Scope0}  ${Patch_remove_Scope1}

    Log    deleting scope1    console=True
    Active Permission Session  ${edit_users_permission}    ${credentials['sa_credentials']}
    ${resp} =    Patch Resources Scopes  ENC:${new_enc_name}   ${body}
    Wait For Task2    ${resp}
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  ENC:${new_enc_name}  ${TRUE}
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[3]}  ENC:${new_enc_name}  ${FALSE}
    log    Successfully! Test Case : OVF1592_API_p139 Enclosures supports SBAC_Update a Enclosure scope which is the active scope to delete a scope resource    console=true
