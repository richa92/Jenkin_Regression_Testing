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
OVF550APIp004 Discover TBird enclosure and check Gen10 server driver inventory
    Power On Server    ${Gen10SYName}
    Wait Until Keyword Succeeds    600    10    Run cpqlocfg and Verify Server POST State  ${Gen10SYIP}  FINISHED_POST
    Sleep    60s
    Refresh Server Hardware   ${Gen10SYName}
    Validate Hardware Firmware Version   ${GEN10SYServer}   ${GEN10SYInventory}
