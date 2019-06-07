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
Test Setup           Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

*** Variables ***
${APPLIANCE_IP}       ${None}


*** Test Cases ***
F1408APIn26 Edit SP To Remove Boot Volume All Storage Paths

    ${resps} =    Edit Server Profiles from variable    ${editProfileN26}

    Validate Server Profile Creation Or Edit Failed As Expected    ${resps}    edit    StoragePathDisabledBootVolume
