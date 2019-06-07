*** Settings ***
Documentation                   F1236 Server firmware updates to move to the newer model for virtual media mount (Online & Offline)
...                                -  Server firmware updates to move to the newer model for virtual media mount (Online & Offline)
Library              FusionLibrary
Library              BuiltIn
Library              Collections
Library              json
Library              Dialogs
Library              String
Resource             ./../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ./Regression_Data.py
Test Setup           Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}

*** Variables ***
# add your DCS appliance IP
${APPLIANCE_IP}        'DCS APPLIANCE IP'
${TARGET}            'C7000'
#C7000 or TBird
${DATA_FILE}         dcs_variables.py
*** Test Cases ***
F1236APIp001 Update Gen8 server firmware using Firmware only
    Update server firmware when create profile  ${createGen8Profiles}   ${SNAP6SPP}     ${True}
    Validate Profile Firmware Version   ${createGen8Profiles}   ${SNAP6SPP}
