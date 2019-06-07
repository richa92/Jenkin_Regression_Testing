*** Settings ***
Documentation        Logical Interconnect supports SBAC_Update an Logical Interconnect which is the inactive scope
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
Logical Interconnect supports SBAC_Update an Logical Interconnect which is the inactive scope
  [Documentation]  OVF1592_API_n053 Logical Interconnect supports SBAC_Update an Logical Interconnect which is the inactive scope
  log    Logical Interconnect supports SBAC_Update an Logical Interconnect scope which is the inactive scope    console=true
  Active Permission Session  ${edit_ia_users_permission}    ${credentials['ia_credentials']}
  ${resp}=  Edit Telemetry Configurations for LI  ${li_profile}
  Wait For Task2   ${resp}   timeout=240   PASS=Error  errorMessage=${NOT_AUTHORIZED_ERROR}    VERBOSE=True
  Should Be Equal            '${resp['status_code']}'    '403'
  log    Successfully! Test Case : OVF1592_API_n053 Logical Interconnect supports SBAC_Update an Logical Interconnect which is the inactive scope    console=true
