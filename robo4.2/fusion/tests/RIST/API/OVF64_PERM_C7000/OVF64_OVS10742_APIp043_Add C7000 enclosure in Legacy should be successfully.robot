*** Settings ***
Documentation    Add C7000 enclosure in Legacy, then remove it successfully
Library              FusionLibrary
Library              BuiltIn
Library              Collections
Library              json
Library              Dialogs
Library              robot.libraries.Process
Library              String
Resource             ./../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Resource             ../Fusion_Env_Setup/keywords.txt
Variables            ./Regression_Data.py


Test Setup                Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}
Test Teardown             Run Keyword And Ignore Error    Remove All Enclosures

*** Variables ***


*** Test Cases ***
Add C7000 enclosure in Legacy should be successfully
    [Documentation]    Add C7000 enclosure in Legacy, then remove it successfully
    Switch Security Mode To    LEGACY
    Check If Current Security Mode Meets Target Mode    LEGACY
    Wait For ALL Enclosures Complete Refresh
    Run Keyword And Ignore Error    Remove All Enclosures    param=?force=true
    Setup Env For C7000     ${Ring}    Add_Enclosure=true    Add_User=false
    All Enclosures Status Should Be OK or Warning
