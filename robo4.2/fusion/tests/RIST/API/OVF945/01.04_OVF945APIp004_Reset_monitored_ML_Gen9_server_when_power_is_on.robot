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
OVF945APIp004 Reset monitored ML Gen9 server when power is on

   Log to console and logfile  	reset all servers
   :FOR	${servername}	IN	@{servernames}
   \   Log to console and logfile  	Power on server '${servername}' before reset
   \   power on server   ${servername}
   \   Reset Server    ${servername}    Reset
   \   ${power_status} =     Get Server Power   ${servername}
   \   should be equal  ${power_status}  On  msg =Power status is not as expected to reset


