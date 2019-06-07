*** Settings ***
Documentation        Server Profiles Support Scope Add SP resources to scopes via scope Interface
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

Suite Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["admin_credentials"]}
Suite Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Server Profiles Support Scope Add SP resources to scopes via scope Interface
  [Documentation]  OVF1592 API p153 Server Profiles Support Scope Add SP resources to scopes via scope Interface

  Log    Adding scope of Production to sp5   console=True
  ${SP_list1} =  Create List    SP:${new_sp_name}
  ${resp}=  Update Scope With Resources   ${Scope_List[0]}  resources_list=${SP_list1}  add_flag=${true}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[0]}  SP:${new_sp_name}   ${True}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  SP:${new_sp_name}   ${True}

