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

*** Variables ***
${APPLIANCE_IP}                 ${None}

*** Test Cases ***
OVF550APIp009Check Gen10 SY server driver inventory after power on and refresh
    Power off ALL servers
    Power on ALL servers
    Refresh Server Hardware   ${Gen10SYName}
    Validate Hardware Firmware Version   ${GEN10SYServer}   ${GEN10SYInventory}
