*** Settings ***
Documentation                   F1184 Local Storage Configuration By HPSUT
...                               -  Local Storage Configuration By HPSUT
Library              FusionLibrary
Library              BuiltIn
Library              Collections
Library              json
Library              Dialogs
Library              String
Resource             ./../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ./Regression_Data.py
Test Setup           Get Run Specific Data File Variables Login the Users And Validate Firmware Bundle

*** Variables ***
# add your DCS appliance IP
${APPLIANCE_IP}        'DCS APPLIANCE IP'
${TARGET}            'C7000'
#C7000 or TBird
${DATA_FILE}         dcs_variables.py
*** Test Cases ***
F1184APIp004 Edit SP with no SPP and configure LocalStorage, and Gen 9 snap 6 in repo
    [Tags]    Performance    server profiles-condition-local_storage
    Create empty server profile  ${editProfiles}
    Update local storage when edit profile  ${False}
