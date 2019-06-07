*** Settings ***
Documentation        Server Profiles Associated with FC Update a server profile and edit the existing connection which related FC is in the inactive scope, modify the bandwidth only
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

Test Setup           Run Keywords    Login Appliance  ${APPLIANCE_IP}    ${credentials["admin_credentials"]}
...                  AND    Prepare Environment for Test
Test Teardown        Logout Appliance
*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
[SPA] - Server Profiles Associated with FC Update a server profile and edit the existing connection which related FC is in the inactive scope, modify the bandwidth only
    [Documentation]  OVF1592 API p182 [Server Profile Administrator] Server Profiles Associated with FC Update a server profile and edit the existing connection which related FC is in the inactive scope modify the bandwidth only

    Log     Edit server profiles sp2 change port     console=True
    Active Permission Session  ${edit_spa_users_permission}    ${credentials['spa_credentials']}
    ${resp}=  Edit Server Profile  ${Edit_sp_fc_port2}
    Wait For Task2   ${resp}   timeout=600

*** Keywords ***
Prepare Environment for Test
    [Documentation]  Prepare Environment for Test
    Log     Edit server profiles sp2 with add fc4      console=True
    ${resp}=  Edit Server Profile  ${Edit_sp_fc3}
    Wait For Task2   ${resp}   timeout=600
