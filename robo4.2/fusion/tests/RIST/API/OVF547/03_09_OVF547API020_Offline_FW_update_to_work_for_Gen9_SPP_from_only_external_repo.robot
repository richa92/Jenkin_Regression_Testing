*** Settings ***
Documentation        Offline FW update to work for Gen9 SPP from only external repo
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
Test Teardown    Remove Repository

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.00
${DataFile}         OVF547/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url

*** Test Cases ***
Offline FW update to work for Gen9 SPP from only external repo
    Log    \n Starting update firmware    console=true
    Run Keyword And Ignore Error    Power off ALL servers   PressAndHold
    Update server firmware when create profile   ${createBLProfilesWithGen9}
    Remove All Server Profiles     ${TRUE}