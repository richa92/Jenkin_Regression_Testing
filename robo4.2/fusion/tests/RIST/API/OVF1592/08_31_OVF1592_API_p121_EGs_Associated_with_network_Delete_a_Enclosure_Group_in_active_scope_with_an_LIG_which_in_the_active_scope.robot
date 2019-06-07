*** Settings ***
Documentation        Enclosure Groups Associated with network_Delete a Enclosure Group in active scope with an LIG which in the active scope
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

Test Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["sa_credentials"]}
Test Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Enclosure Groups Associated with network_Delete a Enclosure Group in active scope with an LIG which in the active scope
    [Documentation]  OVF1592 API p121 Enclosure Groups Associated with network_Delete a Enclosure Group in active scope with an LIG which in the active scope
    Log   Create new Enclosure Groups EG5 with lig2    console=True
    ${resp}=   Add Enclosure Group from variable  ${create_EG4}
    Wait For Task2   ${resp}  timeout=60

    Log   Delete ${new_EG_name}     console=True
    Remove Enclosure Group By Name    ${new_EG_name}
    ${EG_uri_result}=    Get Enclosure Group URI     ${new_EG_name}
    Should Be Equal  '${EG_uri_result}'   '/rest/EnclosureGroup_${new_EG_name}_not_found'