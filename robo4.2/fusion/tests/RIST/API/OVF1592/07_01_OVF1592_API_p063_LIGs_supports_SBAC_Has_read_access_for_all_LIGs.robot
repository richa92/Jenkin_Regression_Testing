*** Settings ***
Documentation        LIG supports SBAC Has read access for all LIGs
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
LIG supports SBAC Has read access for all LIGs
    [Documentation]  OVF1592 API p063 LIG supports SBAC Has read access for all LIGs

    ${lig_uris}=   Create List
    :FOR   ${name}    IN    @{LIG}
    \    ${lig_uri}=    Get LIG URI    ${name}
    \    Append To List    ${lig_uris}  ${lig_uri}
    ${resps}=   Fusion Api Get Lig

    :FOR   ${lig_name_members}   IN   @{resps["members"]}
    \   Should Contain  '${LIG}'  '${lig_name_members["name"]}'

    :FOR   ${lig_uri_members}   IN   @{resps["members"]}
    \   Should Contain  '${lig_uris}'  '${lig_uri_members["uri"]}'