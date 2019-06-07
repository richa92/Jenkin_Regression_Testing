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
OVF948APIp017 Edit SP with legacy boot order enabled with managed ML350 Gen9 server

    Clear Test Environtment
    ${resps} =  Add Server Profiles from variable  ${emptyProfile}
    wait for task2  ${resps}  timeout=50m  interval=10
    ${resps} =  Edit Server Profiles from variable       ${APIp017editBootProfiles}
    wait for task2  ${resps}  timeout=50m  interval=10
