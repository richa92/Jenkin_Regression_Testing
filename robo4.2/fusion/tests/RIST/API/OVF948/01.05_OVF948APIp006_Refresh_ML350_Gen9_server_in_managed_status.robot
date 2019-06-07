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
OVF948APIp006 Refresh ML350 Gen9 server in managed status

   Log to console and logfile  	Refresh ML servers
   power on server    ${servername}
   Log to console and logfile  	Refresh server '${servername}'
   ${resps} =   Refresh Server Hardware    ${servername}
   wait for task2   ${resps}  timeout=5m  interval=10
   ${server_status} =   Get Server Hardware State  ${servername}
   ${power_status} =    Get Server Power  ${servername}
   should be equal  ${server_status}   NoProfileApplied   msg =Server status is not as expected as Managed
   should be equal  ${power_status}   On       msg =Power status is not as expected after refresh



