*** Settings ***
Documentation        Server Profiles Support Scope Add SP resources to scopes via SP Interface
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
Server Profiles Support Scope Add SP resources to scopes via SP Interface
  [Documentation]  OVF1592 API p151 Server Profiles Support Scope Add SP resources to scopes via SP Interface

  Log  Create sp5   console=True
  ${resp}=  Add Server Profile  ${create_server_profile}
  Wait For Task2   ${resp}  timeout=600
  Log    add scope of Production to sp5    console=True
  ${resp}=   Patch Resources Scopes  SP:${new_sp_name}   ${Patch_add_Scope0}
  Wait For Task2   ${resp}  timeout=600
  Validate Resource Assigned/Unassigned To Scope  ${Scope_List[1]}  SP:${new_sp_name}   ${TRUE}
  Validate Resource Assigned/Unassigned To Scope  ${Scope_List[0]}  SP:${new_sp_name}   ${TRUE}
