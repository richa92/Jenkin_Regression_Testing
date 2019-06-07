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
OVF550APIp002 Import Gen10 DL server as managed and check server driver inventory
    Set To Dictionary    ${ilo_credentials}    password    ${dl_password}
    Run cpqlocfg and Power On Server    ${Gen10RHDLIP}
    Wait Until Keyword Succeeds    600    10    Run cpqlocfg and Verify Server POST State  ${Gen10RHDLIP}  FINISHED_POST
    Sleep    60s
    Run Keyword And Ignore Error    Add Server Hardware Async   ${GEN10DLServer}    ${TRUE}
    Validate Hardware Firmware Version   ${GEN10DLServer}    ${GEN10DLInventory}
