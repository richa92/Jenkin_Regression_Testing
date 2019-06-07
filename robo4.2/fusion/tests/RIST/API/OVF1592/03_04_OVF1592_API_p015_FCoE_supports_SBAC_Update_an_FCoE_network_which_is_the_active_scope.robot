*** Settings ***
Documentation        FCoE supports SBAC Update an FCoE network which is the active scope
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
FCoE supports SBAC Update an FCoE network which is the active scope
  [Documentation]  OVF1592 API p015 FCoE supports SBAC Update an FCoE network which is the active scope

   Log   Set "fcoe1" name to "fcoe5"    console=True
   ${resp}=   update fcoe network    ${fcoe_networks[0]["name"]}  ${update_fcoe_network}
   Wait For Task2    ${resp}

   Log   Restore Network reset name to "fcoe1"    console=True
   ${resps}=   Update FCOE Network   ${update_fcoe_network[0]["name"]}     ${update_fcoe_network2}
   Wait For Task2    ${resps}
