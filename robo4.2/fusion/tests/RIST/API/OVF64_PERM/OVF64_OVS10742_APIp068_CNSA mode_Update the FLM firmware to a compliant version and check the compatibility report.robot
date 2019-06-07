*** Settings ***
Documentation    Synergy enclosure related test cases for OVF64
Library              FusionLibrary
Library              BuiltIn
Library              Collections
Library              json
Library              Dialogs
Library              String
Library              robot.libraries.Process
Library              json
Library              Dialogs
Library              String
Resource             ./../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Resource             ../Fusion_Env_Setup/keywords.txt
Variables            ./Regression_Data.py


Test Setup                Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}
Test Teardown             Fusion Api Logout Appliance

*** Variables ***
#${Team_Name}                    SHQA
#${Ring}                         TBird13


*** Test Cases ***
CNSA mode_Update the FLM firmware to a compliant version and check the compatibility report
    Switch Security Mode To    CNSA
    Check If Current Security Mode Meets Target Mode    CNSA
    Wait For ALL Enclosures Complete Refresh
    All Enclosures Status Should Be OK or Warning
    TBird Enclosures are configured    ${Ring}
    Set and Check FLM firmware Version    ${Ring}    ${firmwareVersion_lower}
    Wait For ALL Enclosures Complete Refresh
    All Enclosures Status Should Be OK or Warning
    Set and Check FLM firmware Version    ${Ring}    ${firmwareVersion_higher}
    Wait For ALL Enclosures Complete Refresh
    All Enclosures Status Should Be OK or Warning
    ${resp} =   Get Security Compatibility Report    FIPS
    Check Compliant Item In Compatibility Report    ${Ring}    ${resp}

