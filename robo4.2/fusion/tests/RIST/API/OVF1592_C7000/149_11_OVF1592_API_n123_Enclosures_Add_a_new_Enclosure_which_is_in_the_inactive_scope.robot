*** Settings ***
Documentation        Enclosures supports SBAC_Add a new Enclosure which is in the inactive scope
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
Variables            ./Regression_Data.py
Resource             ./../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt


*** Variables ***
${APPLIANCE_IP}      unknown
${DataFile}         ./Regression_Data.py

*** Test Cases ***
Enclosures supports SBAC_Add a new Enclosure which is in the inactive scope
  [Documentation]  Enclosures supports SBAC_Add a new Enclosure which is in the inactive scope
  log    Add a new Enclosure which is in the active scope    console=true
  Fusion Api Login Appliance      ${APPLIANCE_IP}    ${credentials['admin_credentials']}
  ${resources_list} =    Create List    EG:${EG}
  Update Scope With Resources    scope_name=${Scope_List[1]}    resources_list=${resources_list}
  Active Permission Session  ${edit_users_permission}    ${credentials['sa_credentials']}
  ${resps} =    Add Enclosures from variable Async  ${Add_Encs2}
  Should Match Regexp         '${resps[0]['errorCode']}'    'CREATE_FORBIDDEN_ON_SCOPES'
  Should Be Equal            '${resps[0]['status_code']}'    '403'
  ${resp}=  Get Enclosure URI  ${new_ethernet_name}
  Should Contain  '${resp}'    '/bad_enclosure_uri'  msg=Add Enc which is in the inactive is faild
  log    Successfully! Test Case : OVF1592_API_n123 Enclosures supports SBAC_Add a new Enclosure which is in the inactive scope   console=true
