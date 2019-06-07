*** Settings ***
Documentation        Interconnects supports SBAC Update a Interconnect which is the active scope
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

Test Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["ia_credentials"]}
Test Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Interconnects supports SBAC Update a Interconnect which is the active scope
    [Documentation]  OVF1592 API p033 Interconnects supports SBAC Update a Interconnect which is the active scope

    Log    read access for all Network Sets
    ${resps}=   Fusion Api Get Interconnect
    ${names}=   Create List
    ${uris}=   Create List
    :FOR   ${resp}   IN   @{resps["members"]}
    \      Append To List    ${names}    ${resp["name"]}
    \      Append To List    ${uris}    ${resp["uri"]}

    ${IC_uris}=    Create List
    :FOR    ${IC}  IN    @{interconects_list}
    \       ${uri}=   Get IC URI    ${IC}
    \       Should Contain    ${names}    ${IC}
    \       Should Contain    ${uris}    ${uri}
