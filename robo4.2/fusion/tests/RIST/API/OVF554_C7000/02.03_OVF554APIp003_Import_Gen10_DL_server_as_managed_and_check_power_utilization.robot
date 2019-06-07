*** Settings ***
Library              FusionLibrary
Library              BuiltIn
Library              Collections
Library              json
Library              Dialogs
Library              String
Resource             ./../../../../Resources/api/fusion_api_resource.txt
Resource             ./keyword.txt
Variables            ./Regression_Data.py

Test Setup      Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.00
${DataFile}         OVF554/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url

*** Test Cases ***
OVF554APIp003 – Import Gen10 DL server as managed and check power Utilization
    Run Keyword And Ignore Error    Add Server Hardware Async   ${GEN10DLServer}    ${TRUE}
    Validate Hardware Power Utilization   ${GEN10DLServer}
    Run Keyword And Ignore Error    Remove All DL Server Hardware Async     ServerTypes=DL
