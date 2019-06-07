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


*** Variables ***
${APPLIANCE_IP}       ${None}


*** Test Cases ***
F221APIn29 Edit SP To Change Primary Boot To Non Bootable

    ${resps} =    Edit Server Profiles from variable    ${editProfileN29}

    Validate Server Profile Creation Or Edit Failed As Expected    ${resps}    edit    ConnectionNotManagedBootVolume

