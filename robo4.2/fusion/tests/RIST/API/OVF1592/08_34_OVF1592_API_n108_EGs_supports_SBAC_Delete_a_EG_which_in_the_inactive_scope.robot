*** Settings ***
Documentation        supports SBAC Delete an EG which in the inactive scope
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
FCoE supports SBAC Delete an EG which in the inactive scope
    [Documentation]  OVF1592 API n022 FCoE supports SBAC Delete an EG which in the inactive scope
    Log    Delete EG4     console=True
    ${resp}=  Fusion Api Delete Enclosure Group    name=${EG_list[3]}
    Wait For Task2   ${resp}   timeout=60   PASS=Error  errorMessage=${NOT_AUTHORIZED_ERROR}    VERBOSE=True

    ${EG_Uri_Result}=    Get Enclosure Group URI   ${EG_list[3]}
    Should Not Be Equal  '${EG_uri_result}'   '/rest/EnclosureGroup_${EG_list[3]}_not_found'
