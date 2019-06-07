*** Settings ***
Documentation        Add networks to Network sets which in inactive scope
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

Test Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["admin_credentials"]}
Test Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Add networks to Network sets which in inactive scope
  [Documentation]  Add networks to Network sets which in inactive scope

   Log   Add networks to Network sets which in inactive scope
   ${resps}=   Update Network Set    ${update_network_set5}
   Wait For Task2   ${resps}   timeout=60
