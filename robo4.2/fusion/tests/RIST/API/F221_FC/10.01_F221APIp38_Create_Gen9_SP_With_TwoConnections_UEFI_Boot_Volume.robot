*** Settings ***
Documentation                   F221 SP with Connection and Volume

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
F221APIp038 Create SP with Primary And Secondary Connections with Private Volume As UEFI Boot

    ${resps} =    Add Server Profiles from variable    ${createGen9ProfileP38}

    Validate Server Profile Applied Successfully    ${resps}

    Validate Server Profile Primary Connection And Volume Boot Status    ${createGen9ProfileP38}    priority    Primary




