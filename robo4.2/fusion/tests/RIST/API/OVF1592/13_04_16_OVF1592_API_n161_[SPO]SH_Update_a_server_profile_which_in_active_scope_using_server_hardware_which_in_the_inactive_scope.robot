*** Settings ***
Documentation        Server Profiles Associated with EG_Update a server profile which in active scope using server hardware which in the inactive scope
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
Test Teardown        Revert SP Environment After Test    ${Edit_server_profile_base}

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
[SPO] - Server Profiles Associated with EG_Update a server profile which in active scope using server hardware which in the inactive scope
    [Documentation]  OVF1592 API n161 [Server Profile Administrator] Server Profiles Associated with EG_Update a server profile which in active scope using server hardware which in the inactive scope

    Log   Edit server profile sp2 to SH4
    ${resp}=  Edit Server Profile  ${Edit_server_profile_SH2}
    Wait For Task2   ${resp}   timeout=600    PASS=Error  errorMessage=${ASSOCIATION_FORBIDDEN_BY_SCOPE}    VERBOSE=True
