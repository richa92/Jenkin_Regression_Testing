*** Settings ***
Documentation    OVF550 Driver inventory test
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
Test Teardown   Remove All DL Server Hardware Async     ServerTypes=DL

*** Variables ***
${APPLIANCE_IP}                 ${None}

*** Test Cases ***
OVF550APIp008 - Check Gen10 DL server driver inventory after power on and refresh
    Run Keyword And Ignore Error    Add Server Hardware Async   ${GEN10DLServer}    ${TRUE}
    Power on ALL servers
    wait until keyword succeeds     15 min    1 min    Verify Firmware Version As Expected After Refresh    ${GEN10DLServer}   ${GEN10DLInventory}
