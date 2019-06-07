*** Settings ***
Documentation        Enclosure Groups supports SBAC_Update a EG which is the active scope
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

Suite Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["sa_credentials"]}
Suite Teardown        Remove Enclosure Group By Name  ${new_EG_name}

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Enclosure Groups supports SBAC_Update a EG which is the active scope
  [Documentation]  OVF1592 API p111 Enclosure Groups supports SBAC_Update a EG which is the active scope

  Log   Create new Enclosure Groups EG5 with inactive scope    console=True
  ${resp}=  Add Enclosure Group From Variable  ${create_EG1}
  Wait For Task2   ${resp}   timeout=60
  ${resps}=  Edit Enclosure Group    ${Edit_EG}
  Wait For Task2   ${resps}   timeout=60
