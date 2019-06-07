*** Settings ***
Documentation        Server Profiles Associated with Server hardware_Create a server profile which in active scope using a server hardware which in the inactive scope
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
[SPA] - Server Profiles Associated with Server hardware_Create a server profile which in active scope using a server hardware which in the inactive scope
    [Documentation]  OVF1592 API n159 [Server Profile Administrator] Server Profiles Associated with Server hardware_Create a server profile which in active scope using a server hardware which in the inactive scope
    Log   Create new server profiles sp5 sh with inactive   console=True
    ${resp}=  Add Server Profile  ${create_server_profile_SH2}
    Wait For Task2   ${resp}   timeout=600    PASS=Error  errorMessage=${ASSOCIATION_FORBIDDEN_BY_SCOPE}    VERBOSE=True
