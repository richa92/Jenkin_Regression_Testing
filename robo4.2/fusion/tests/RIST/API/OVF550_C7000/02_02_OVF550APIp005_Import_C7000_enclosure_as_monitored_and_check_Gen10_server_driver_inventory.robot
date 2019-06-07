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
Test Teardown   Remove All Enclosures

*** Variables ***
${APPLIANCE_IP}                 ${None}

*** Test Cases ***
OVF550APIp005_Import_C7000_enclosure_as_monitored_and_check_Gen10_server_driver_inventory
    Clear Multi OA VC Mode  ${WPST32Encls}
    Run Keyword And Ignore Error    Add Enclosures from variable      ${Monitored32}  20min
    Validate Hardware Firmware Version   ${GEN10BLServer}   ${GEN10BLInventory}
    Power off ALL servers   PressAndHold
