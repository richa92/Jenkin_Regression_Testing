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
F221APIp013p014 Delete Profile And Validate

    Should Not Be Equal     ${APPLIANCE_IP}  ${None}  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.218.154'

    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}

    ${ret} =    Delete Server Profile And Validate The Deletion    ${createProfileP11P12P61}    ${True}

    Should Match    ${ret}    PASS
