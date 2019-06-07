*** Settings ***
Documentation        OVF564 Delete SP with unassigned network forcibly when server is power on

Library              FusionLibrary
Library              BuiltIn
Library              Collections
Library              json
Library              Dialogs
Library              String
Resource             ./../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ./Regression_Data.py

Test Setup           Login And Clear Test Environtment    ${APPLIANCE_IP}    ${admin_credentials}

*** Variables ***
${APPLIANCE_IP}       ${None}


*** Test Cases ***
Delete SP with unassigned network forcibly when server is power on
    ${resps} =  Add Server Profiles from Variable    ${createProfileP011}
    Validate Server Profile Applied Successfully     ${resps}
    ${rc} =  Validate Server Profiles Connections Network Applied  ${createProfileP011}
    Should be true    ${rc}    msg=Failed to apply server profile connections

    Power on server    ${createProfileP010[0]["serverHardwareUri"]}

    ${rc} =  Delete Server Profile And Validate The Deletion  ${createProfileP011}    ${True}
    Should Match     ${rc}    PASS