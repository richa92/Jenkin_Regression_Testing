*** Settings ***
Documentation        Enclosure Groups Support Scope Remove EG resources scopes via EG Interface
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

Test Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["admin_credentials"]}
Test Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Server Profiles Support Scope_Remove SP resources scopes via SP Interface
    [Documentation]  OVF1592_API_p152 Server Profiles Support Scope_Remove SP resources scopes via SP Interface
    Log    Remove scope "Production" via SP interface    console=True
    ${scopes}=    Get Assigned Scope URIs By Resource Name    SP:${new_sp_name}
    ${scope}=    Get Scope URI By Name    ${Scope_List[0]}

    ${body}=    Set Variable If  '${scopes[0]}'=='${scope}'  ${Patch_remove_Scope0}  ${Patch_remove_Scope1}

    Log   Remove EG5 scope of production     console=True
    ${resp}=  Patch Resources Scopes   SP:${new_sp_name}  ${body}
    Wait For Task2   ${resp}  timeout=60
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[0]}  SP:${new_sp_name}   ${False}
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  SP:${new_sp_name}   ${True}