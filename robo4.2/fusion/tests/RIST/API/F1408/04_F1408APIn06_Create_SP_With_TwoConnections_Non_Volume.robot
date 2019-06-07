*** Settings ***
Documentation                   F1408 SP with Connection and Volume

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
F1408APIn006 Create SP with Two Connections Non Volume

    ${resps} =    Add Server Profiles from variable    ${createProfileN06}

    Validate Server Profile Creation Or Edit Failed As Expected    ${resps}    create    NoBootableVolumeAttachmentFoundForManagedVolumeConnection


