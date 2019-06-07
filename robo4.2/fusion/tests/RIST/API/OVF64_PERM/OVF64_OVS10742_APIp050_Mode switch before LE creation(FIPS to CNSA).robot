*** Settings ***
Documentation    Synergy enclosure related test cases for OVF64
Library              FusionLibrary
Library              BuiltIn
Library              Collections
Library              json
Library              Dialogs
Library              String
Library              robot.libraries.Process
Resource             ./../../../../Resources/api/security/login_domain.txt
Resource             ./keywords.txt
Resource             ../Fusion_Env_Setup/keywords.txt
Variables            ./Regression_Data.py


Test Setup                Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}
Test Teardown             Fusion Api Logout Appliance

*** Variables ***
#${Team_Name}                    SHQA
#${Ring}                         TBird13


*** Test Cases ***
Mode switch before LE creation(FIPS to CNSA)
    [Documentation]    Mode switch before LE creation(FIPS to CNSA)
    Switch Security Mode To    FIPS
    Check If Current Security Mode Meets Target Mode    FIPS
    Wait For ALL Enclosures Complete Refresh
    Delete Enclosure LE
    All Enclosures Status Should Be OK or Warning
    ${resp} =   Get Security Compatibility Report    CNSA
    Check Compliant Item In Compatibility Report    ${Ring}    ${resp}
    Switch Security Mode To    CNSA
    Check If Current Security Mode Meets Target Mode    CNSA
    Wait For ALL Enclosures Complete Refresh
    Setup Env For TBird    ${Ring}    Add_LE=true    Add_User=false
    All Enclosures Status Should Be OK or Warning