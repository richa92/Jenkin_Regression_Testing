*** Settings ***
Documentation        Server Profiles Associated with FCOE Create a new server profile and add a new connection using an FCOE, the FCOE is in different scope with SP
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

Test Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["spa_credentials"]}
Test Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
[SPA] - Server Profiles Associated with FCOE Create a new server profile and add a new connection using an FCOE, the FCOE is in different scope with SP
    [Documentation]  OVF1592 API n166 [Server Profile Administrator] Server Profiles Associated with FCOE Create a new server profile and add a new connection using an FCOE, the FCOE is in different scope with SP

    Log     Can Not Create new server profiles sp5 of Test with add fcoe3      console=True
    ${resp}=  Add Server Profile  ${create_sp_fcoe2}
    Wait For Task2   ${resp}   timeout=600   PASS=Error  errorMessage=${ASSOCIATION_FORBIDDEN_BY_SCOPE}    VERBOSE=True
