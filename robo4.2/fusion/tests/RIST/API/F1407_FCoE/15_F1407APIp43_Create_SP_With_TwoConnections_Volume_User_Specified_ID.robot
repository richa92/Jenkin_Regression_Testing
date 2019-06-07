*** Settings ***
Documentation                   F1407 SP with Connection and Volume

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
F1407APIp043 Create SP with Primary And Secondary Connections with Private Volume with User Specified IDs

    ${resps} =    Add Server Profiles from variable    ${createProfileP43}

    Validate Server Profile Applied Successfully    ${resps}

    Validate Server Profile Primary Connection And Volume Boot Status    ${createProfileP43}    bootVolumeSource    ManagedVolume    ${False}

