*** Settings ***
Documentation        add a valid SPP to external servers directory and auto-discovery of SPP from OV
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
${DataFile}         OVF547/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url

*** Test Cases ***
add a valid SPP to external servers directory and auto-discovery of SPP from OV
    Log    \n add a valid SPP to external servers directory and auto-discovery of SPP from OV    console=true
    Run Multi Cmd   ${SERVER_IP}    ${ssh_username}    ${ssh_password}    ${copy_hotfix_commands}
    ${uri} =    Wait Until Keyword Succeeds    500s    5s    Verify Firmware Exist    ${detect_version}
    ${firmware} =    Get Firmware Bundle   ${uri}
    Should Be Equal    ${firmware['status']}   ${ok_status}    msg=${firmware['name']} status verify failed