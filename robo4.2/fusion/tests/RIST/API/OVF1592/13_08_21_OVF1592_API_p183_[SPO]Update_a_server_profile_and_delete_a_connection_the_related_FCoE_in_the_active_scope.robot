*** Settings ***
Documentation        Server Profiles Associated with FCOE Update a server profile and delete a connection, the related FCOE in the active scope
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
[SPO] - Server Profiles Associated with FCOE Update a server profile and delete a connection, the related FCOE in the active scope
    [Documentation]  OVF1592 API p183 [Server Profile Administrator] Server Profiles Associated with FCOE Update a server profile and delete a connection, the related FCOE in the active scope

    Log     Edit server profiles sp2 remove eth1     console=True
    ${resp}=  Edit Server Profile  ${Edit_sp_fcoe_base}
    Wait For Task2   ${resp}   timeout=600
