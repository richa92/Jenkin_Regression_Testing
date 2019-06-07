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
F221APIn15 Edit SP To Remove Primary Connection

    ${resps} =    Edit Server Profiles from variable    ${editProfileN15}

    Validate Server Profile Creation Or Edit Failed As Expected    ${resps}    edit    MISSING_STORAGE_PATHS

