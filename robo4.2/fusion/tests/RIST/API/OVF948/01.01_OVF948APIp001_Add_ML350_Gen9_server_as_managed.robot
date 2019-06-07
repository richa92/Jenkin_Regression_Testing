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
OVF948APIp001 Add ML350 Gen9 server as managed

    ${resps}=    Add Server hardware from variable    ${GEN9MLServerManaged}
    Wait For Task2    ${resps}  timeout=10m  interval=5
    Log to console and logfile  	Check server is managed
    Wait Until Keyword Succeeds    60s    5s    Verify Search Server Hardware Status Till Complete  ${servername}   NoProfileApplied


