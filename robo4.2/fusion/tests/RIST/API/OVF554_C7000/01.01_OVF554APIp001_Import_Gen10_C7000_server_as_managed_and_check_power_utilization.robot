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
    Clear Multi OA VC Mode  ${WPST20Encls}
    Run Keyword And Ignore Error    Add Enclosures from variable      ${Managed20}  20min
    Validate Hardware Power Utilization   ${GEN10BLServer}
    Run Keyword And Ignore Error    Remove All Enclosures

