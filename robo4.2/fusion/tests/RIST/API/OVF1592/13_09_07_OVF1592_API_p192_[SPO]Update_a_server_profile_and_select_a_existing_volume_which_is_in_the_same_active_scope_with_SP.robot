*** Settings ***
Documentation        Update a server profile and select a existing volume which is in the same active scope with SP
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
Test Teardown        Revert SP Environment After Test    ${Edit_sp_network_base}

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
[SPO] - Update a server profile and select a existing volume which is in the same active scope with SP
    [Documentation]  OVF1592 API p192 [Server Profile Operator] Update a server profile and select a existing volume which is in the same active scope with SP

    Log   Editing new server profiles sp2   console=True
    ${resp}=  Edit Server Profile  ${Edit_server_profile_volume1}    param=?force=ignoreServerHealth,ignoreSANWarnings
    Wait For Task2   ${resp}   timeout=600
    Validate Volume Assigned/Unassigned To Server Profile  ${vol_list[1]}  ${sp_list[1]}  ${True}
