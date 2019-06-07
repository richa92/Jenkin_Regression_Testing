*** Settings ***
Documentation        Enclosure Groups supports SBAC_Update a EG scope which is the active scope to add a scope resource
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
Server Profiles supports SBAC Update a SP scope which is the active scope to add a scope resoure
  [Documentation]  OVF1592 API p158 Server Profiles supports SBAC Update a SP scope which is the active scope to add a scope resoure

  Log   Add scope scope1 for SP2    console=True
  ${resp}=  Patch Resources Scopes   SP:${sp_list[1]}   ${Patch_add_Scope3}
  Wait For Task2   ${resp}  timeout=60
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[3]}  SP:${sp_list[1]}   ${True}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  SP:${sp_list[1]}   ${True}
