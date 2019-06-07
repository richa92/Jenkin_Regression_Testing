*** Settings ***
Documentation        Enclosure Groups supports SBAC_Update a EG scope which is the active scope to delete a scope resource
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

Test Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["sa_credentials"]}
Test Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Enclosure Groups supports SBAC_Update a EG scope which is the active scope to delete a scope resource
    [Documentation]  OVF1592 API p113 Enclosure Groups supports SBAC_Update a EG scope which is the active scope to delete a scope resource
    Log    Set the patch body based on the location of scope1    console=True
    ${scopes}=    Get Assigned Scope URIs By Resource Name    EG:${EG_list[1]}
    ${scope}=    Get Scope URI By Name    ${Scope_List[3]}

    ${body}=    Set Variable If  '${scopes[0]}'=='${scope}'  ${Patch_remove_Scope0}  ${Patch_remove_Scope1}

    Log   Remove EG2 scope of scope1     console=True
    ${resp}=  Patch Resources Scopes   EG:${EG_list[1]}   ${body}
    Wait For Task2   ${resp}  timeout=60
    Validate Resource Assigned/Unassigned To Scope     ${Scope_List[3]}     EG:${EG_list[1]}   ${False}
    Validate Resource Assigned/Unassigned To Scope     ${Scope_List[1]}     EG:${EG_list[1]}   ${True}
