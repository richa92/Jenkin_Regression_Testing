*** Settings ***
Documentation                   OVF906 Firmware Update For Gen10 Servers
...                               -  Firmware Update For Gen10 Servers
Library              FusionLibrary
Library              BuiltIn
Library              Collections
Library              json
Library              Dialogs
Library              String
Resource             ./../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ./Regression_Data.py
Test Setup           Login And Upload Firmware Bundle   Gen10Snap1

*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one

*** Test Cases ***
OVF906APIp004 Edit profile and update firmware offline for Gen10 BL server when firmware baseline higher than installed
    [Tags]    Performance    server-profiles-condition-gen10_firmware
    Create empty server profile  ${editSYProfiles}
    Update server firmware when create profile   ${editSYProfiles}
    Validate Firmware Installed    ${editSYProfiles}    ${FirmwareVersion}
