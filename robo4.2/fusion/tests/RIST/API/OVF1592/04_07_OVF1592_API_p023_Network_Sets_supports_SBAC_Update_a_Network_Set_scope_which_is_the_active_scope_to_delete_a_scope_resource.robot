*** Settings ***
Documentation        Network Sets supports SBAC Update a Network Set scope which is the active scope to delete a scope resource
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

Test Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["na_credentials"]}
Test Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Network Sets supports SBAC Update a Network Set scope which is the active scope to delete a scope resource
    [Documentation]  OVF1592 API p023 Network Sets supports SBAC Update a Network Set scope which is the active scope to delete a scope resource
    Log    Set the patch body based on the location of scope1    console=True
    ${scopes}=    Get Assigned Scope URIs By Resource Name    NS:${network_set_list[1]}
    ${scope}=    Get Scope URI By Name    ${Scope_List[3]}

    ${body}=    Set Variable If  '${scopes[0]}'=='${scope}'  ${Patch_remove_Scope0}  ${Patch_remove_Scope1}

    Log    deleting scope1 from net-set2    console=True
    ${resp}=   Patch Resources Scopes   NS:${network_set_list[1]}   ${body}
    Wait For Task2  ${resp}
    Validate Resource Assigned/Unassigned To Scope    ${Scope_List[3]}  network-setV\\d*:${network_set_list[1]}  ${False}
    Validate Resource Assigned/Unassigned To Scope    ${Scope_List[1]}  network-setV\\d*:${network_set_list[1]}  ${TRUE}
