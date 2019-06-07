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
Test Setup           Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

*** Variables ***
${APPLIANCE_IP}       ${None}


*** Test Cases ***
F221APIp32p33 Edit SP WIth XAPI 200 Version

    ${resps} =    Edit Server Profiles from variable    ${editProfileN33}    ${HeaderP31P33}

    log to console      respsis:@{resps}

    :FOR    ${resp}    IN    @{resps}
    \       ${errorCode} =    Get From Dictionary    ${resp}    errorCode
    \       Log To Console    The_actual_error_code_is:_${errorCode}
    \       Should Match    ${errorCode}    UNRECOGNIZED_JSON_FIELD


