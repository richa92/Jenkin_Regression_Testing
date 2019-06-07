*** Settings ***
Documentation        Enclosure Groups supports SBAC_Has read access for all Enclosure Groups
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

Suite Setup             Login Appliance  ${APPLIANCE_IP}    ${credentials["sa_credentials"]}
Suite Teardown          Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Enclosure Groups supports SBAC_Has read access for all Enclosure Groups
    [Documentation]  OVF1592 API p114 Enclosure Groups supports SBAC_Has read access for all Enclosure Groups
    ${eg_uris}=   Create List
    :FOR   ${name}    IN    @{EG_list}
    \    ${eg_uri}=    Get Enclosure Group URI    ${name}
    \    Append To List    ${eg_uris}  ${eg_uri}

   ${EnclosureGroup_uris}=   Get Enclosure Group Uris   ${EG_list}
   ${resps}=   Fusion Api Get Enclosure Groups
   :FOR   ${EG}   IN   @{resps["members"]}
   \   Should Contain  '${EG_list}'  '${EG["name"]}'
   :FOR   ${EG}   IN   @{resps["members"]}
   \   Should Contain  '${EnclosureGroup_uris}'  '${EG["uri"]}'
