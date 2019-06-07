*** Settings ***
Library              FusionLibrary
Library              BuiltIn
Library              Collections
Library              json
Library              Dialogs
Library              String
Resource             ./../../../../Resources/api/fusion_api_resource.txt
Resource             ./keyword.txt
Variables           ./Regression_Data.py

Test Setup      Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}

*** Variables ***
${APPLIANCE_IP}      unknown

*** Test Cases ***
OVF948APIp005 Reset managed ML350 Gen9 server when power is on

   Log to console and logfile  	reset ML server
   Log to console and logfile  	Power on server '${servername}' before reset
   power on server   ${servername}
   Reset Server    ${servername}    Reset
   ${power_status} =     Get Server Power   ${servername}
   should be equal  ${power_status}  On  msg =Power status is not as expected to reset
