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
OVF945APIp005 Refresh ML Gen9 server in monitored statusRefresh ML Gen9 server in monitored status

   Log to console and logfile  	Refresh servers
   :FOR	${servername}	IN	@{servernames}
   \   power on server    ${servername}
   \   Log to console and logfile  	Refresh server '${servername}'
   \   Refresh Server Hardware    ${servername}
   \   ${server_status} =   Get Server Hardware State  ${servername}
   \   ${power_status} =    Get Server Power  ${servername}
   \   should be equal  ${server_status}   Monitored  msg =Server status is not as expected as Monitored
   \   should be equal  ${power_status}   On       msg =Power status is not as expected after refresh



