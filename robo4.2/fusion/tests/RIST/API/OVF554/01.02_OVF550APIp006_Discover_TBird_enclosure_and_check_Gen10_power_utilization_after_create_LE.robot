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
Resource             ../Fusion_Env_Setup/keywords.txt

Test Setup      Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.00
${DataFile}         OVF554/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url
${Team_Name}                    SHQA
${Ring}                         TBird13
${Add_LE}                       true
${Add_Storage}                  false

*** Test Cases ***
OVF550APIp003 Discover TBird enclosure and check Gen10 server driver inventory after create LE
    Setup Env For TBird     ${Ring}  ${Add_LE}      ${Add_Storage}          ${Team_Name}
    Validate Hardware Power Utilization   ${GEN10SYServer}
