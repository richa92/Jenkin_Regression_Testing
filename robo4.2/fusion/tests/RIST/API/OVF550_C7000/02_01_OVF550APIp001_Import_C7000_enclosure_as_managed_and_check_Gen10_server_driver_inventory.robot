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
OVF550APIp001 Import C7000 enclosure as managed and check Gen10 server driver inventory
    Set To Dictionary    ${ilo_credentials}    password    ${bl_password}
    Run cpqlocfg and Power On Server    ${Gen10WinBLIP}
    Wait Until Keyword Succeeds    600    10    Run cpqlocfg and Verify Server POST State  ${Gen10WinBLIP}  FINISHED_POST
    Sleep    60s
    Clear Multi OA VC Mode  ${WPST32Encls}
    Run Keyword And Ignore Error    Add Enclosures from variable      ${Managed32}  20min
    Validate Hardware Firmware Version   ${GEN10BLServer}   ${GEN10BLInventory}
