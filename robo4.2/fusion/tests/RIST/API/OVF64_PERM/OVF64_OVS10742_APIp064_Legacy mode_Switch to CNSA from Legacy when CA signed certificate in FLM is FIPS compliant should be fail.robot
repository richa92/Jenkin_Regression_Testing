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
Legacy mode_Switch to CNSA from Legacy when CA signed certificate in FLM is FIPS compliant should be fail
    Switch Security Mode To    LEGACY
    Check If Current Security Mode Meets Target Mode    LEGACY
    Wait For ALL Enclosures Complete Refresh
    All Enclosures Status Should Be OK or Warning
    TBird Enclosures are configured    ${Ring}
    Install CA Signed Certificate on FLM    ${IssuerIP}    ${ssh_credentials}    ${signature_algorithm_sha256}
    Verify CA Signed Certificate on FLM    FIPS
    Wait For ALL Enclosures Complete Refresh
    All Enclosures Status Should Be OK or Warning
    ${resp} =   Get Security Compatibility Report    CNSA
    Check Non-compliant Item In Compatibility Report    ${Ring}    ${resp}    ${tbirdenclosureName_info}
    Switch Security Mode To    CNSA
    Check If Current Security Mode Meets Target Mode    CNSA
    Wait For ALL Enclosures Complete Refresh
    Enclosures Status Should Be Critical
