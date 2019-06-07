*** Settings ***
Documentation         Server Profiles Associated with Server hardware_Create a server profile which in active scope using a empty bay which in the inactive scope
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

Suite Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["spa_credentials"]}
Suite Teardown        Revert SP Environment After Test    ${Edit_server_profile_base}

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
[SPA] - Server Profiles Associated with Server hardware_Create a server profile which in active scope using a empty bay which in the inactive scope
    [Documentation]  OVF1592 API n165 [SPA] Server Profiles Associated with Server hardware_Create a server profile which in active scope using a empty bay which in the inactive scope

    Log   Edit server profiles sp2     console=True
    ${resp}=  Edit Server Profile  ${Edit_server_profile_EG3}
    Wait For Task2   ${resp}   timeout=600    PASS=Error  errorMessage=${ASSOCIATION_FORBIDDEN_BY_SCOPE}    VERBOSE=True
