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
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url

*** Test Cases ***
OVF945APIp001 Add ML series Gen9 server as monitored
    Run Keyword And Ignore Error    Add Server Hardware Async   ${GEN9MLServerMonitored}   ${TRUE}
    Log to console and logfile  	Check server is monitored
	:FOR	${servername}	IN	@{servernames}
    \   Wait Until Keyword Succeeds    60s    5s    Verify Search Server Hardware Status Till Complete    ${servername}  Monitored


