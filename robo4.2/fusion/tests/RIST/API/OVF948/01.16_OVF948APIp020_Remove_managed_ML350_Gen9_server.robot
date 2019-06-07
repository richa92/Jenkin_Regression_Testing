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
OVF948APIp020 Remove managed ML350Gen9 server

   Clear Test Environtment
   Log to console and logfile      removing ML server
   Remove All DL Server Hardware Async  ${TRUE}  404  ML

