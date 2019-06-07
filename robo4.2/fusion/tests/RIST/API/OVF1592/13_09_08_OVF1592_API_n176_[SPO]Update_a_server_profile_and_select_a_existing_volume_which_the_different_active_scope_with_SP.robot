*** Settings ***
Documentation        Update a server profile and select a existing volume which is in the different active scope with SP
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

Test Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["spo_credentials"]}
Test Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
[SPO] - Update a server profile and select a existing volume which is in the different active scope with SP
    [Documentation]  OVF1592 API n176 [Server Profile Operator] Update a server profile and select a existing volume which is in the different active scope with SP

    log     Edit new server profiles sp5   console=True
    ${resp}=  Edit Server Profile  ${Edit_server_profile_volume2}    param=?force=ignoreServerHealth,ignoreSANWarnings
    Wait For Task2   ${resp}   timeout=600    PASS=Error  errorMessage=${ASSOCIATION_FORBIDDEN_BY_SCOPE}     VERBOSE=True
