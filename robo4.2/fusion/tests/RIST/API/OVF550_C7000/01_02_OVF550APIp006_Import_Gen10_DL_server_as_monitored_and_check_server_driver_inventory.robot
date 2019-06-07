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
OVF550APIp007 Import Gen10 DL server as monitored and check server driver inventory
    Run Keyword And Ignore Error    Add Server Hardware Async   ${GEN10DLServerMonitored}   ${TRUE}
    Validate Hardware Firmware Version   ${GEN10DLServerMonitored}   ${GEN10DLInventory}
    Power off ALL servers   PressAndHold
