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
${APPLIANCE_IP}      unknown

*** Test Cases ***
OVF948APIp003 Power on ML350 Gen9 server in managed status

   Log to console and logfile  	Power off server '${servername}' before power on
   power off server   ${servername}    PressAndHold
   Log to console and logfile  	Power on ML servers
   power on server    ${servername}
   ${power_status} =     Get Server Power   ${servername}
   should be equal  ${power_status}  On   msg =Power status is not as expected to powen on

