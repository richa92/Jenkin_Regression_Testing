*** Settings ***
Documentation        Enclosure Groups supports SBAC_Create new EG which is in the inactive scope
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
Server Profiles supports SBAC_Create new SP which cross the scope between active and inactive
    [Documentation]  OVF1592_API_n144 Server Profiles supports SBAC_Create new SP which cross the scope between active and inactive

    Log   Create new Server profile SP6 with inactive scope    console=True
    ${resp}=  Add Server Profile  ${create_sp_neg_2}  status_code=403
    Wait For Task2   ${resp}   timeout=60   PASS=Error  errorMessage=${CREATION_NOT_AUTHORIZED_ERROR}    VERBOSE=True
