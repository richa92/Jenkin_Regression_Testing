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
F1408APIn70 Edit SP To Add Second Connnection And Secondary Boot Without Boot Volume

    ${resps} =    Edit Server Profiles from variable    ${editProfileN70}

    Validate Server Profile Creation Or Edit Failed As Expected    ${resps}    edit    NoBootableVolumeAttachmentFoundForManagedVolumeConnection

