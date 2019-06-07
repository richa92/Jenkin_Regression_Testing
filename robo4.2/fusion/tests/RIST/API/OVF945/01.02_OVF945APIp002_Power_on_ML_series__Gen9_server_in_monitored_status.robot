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
OVF945APIp002 Power on ML series Gen9 server in monitored status

   Log to console and logfile  	Power on all servers
   :FOR	${servername}	IN	@{servernames}
   \   Log to console and logfile  	Power off server '${servername}' before power on
   \   power off server   ${servername}    PressAndHold
   \   power on server    ${servername}
   \   ${power_status} =     Get Server Power   ${servername}
   \   should be equal  ${power_status}  On   msg =Power status is not as expected to powen on


