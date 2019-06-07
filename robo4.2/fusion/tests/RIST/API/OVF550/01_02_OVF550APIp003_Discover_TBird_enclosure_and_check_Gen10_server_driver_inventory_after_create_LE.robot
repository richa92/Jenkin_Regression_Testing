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
Resource             ../Fusion_Env_Setup/keywords.txt
Variables            ./Regression_Data.py

Test Setup      Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}

*** Variables ***
${APPLIANCE_IP}                 ${None}
${Team_Name}                    SHQA
${Ring}                         TBird13
${Add_LE}                       true
${Add_Storage}                  false

*** Test Cases ***
OVF550APIp003 Discover TBird enclosure and check Gen10 server driver inventory after create LE
    Setup Env For TBird     ${Ring}  ${Add_LE}      ${Add_Storage}          ${Team_Name}
    Validate Hardware Firmware Version   ${GEN10SYServer}   ${GEN10SYInventory}
