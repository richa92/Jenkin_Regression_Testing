*** Settings ***
Documentation        FCoE supports SBAC Update an FCoE network scope which is the active scope to delete an active scope
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
FCoE supports SBAC Update an FCoE network scope which is the active scope to delete an active scope
    [Documentation]  OVF1592 API n018 FCoE supports SBAC Update an FCoE network scope which is the active scope to delete an active scope
    Log    Set the patch body based on the location of Test    console=True
    ${scopes}=    Get Assigned Scope URIs By Resource Name    FCOE:${fcoe_networks[1]['name']}
    ${scope}=    Get Scope URI By Name    ${Scope_List[1]}

    ${body}=    Set Variable If  '${scopes[0]}'=='${scope}'  ${Patch_remove_Scope0}  ${Patch_remove_Scope1}

    Log    Deleting Test from fcoe2    console=True
    ${resp}=   Patch Resources Scopes  FCOE:${fcoe_networks[1]['name']}   ${body}
    Wait For Task2   ${resp}   timeout=200   PASS=Error  errorMessage=${ASSOCIATION_FORBIDDEN_BY_SCOPE}    VERBOSE=True
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}   FCOE:${fcoe_networks[1]["name"]}  ${True}