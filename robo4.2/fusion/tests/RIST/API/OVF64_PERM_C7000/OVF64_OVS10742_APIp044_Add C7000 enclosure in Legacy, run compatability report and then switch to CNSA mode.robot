*** Settings ***
Documentation    Add C7000 enclosure in Legacy, run compatability report and then switch to FIPS mode
Library              FusionLibrary
Library              BuiltIn
Library              Collections
Library              json
Library              Dialogs
Library              String
Library              robot.libraries.Process
Resource             ./keywords.txt
Resource             ../Fusion_Env_Setup/keywords.txt
Variables            ./Regression_Data.py


Test Setup                Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}
Test Teardown             Run Keyword And Ignore Error    Remove All Enclosures

*** Variables ***


*** Test Cases ***
Add C7000 enclosure in Legacy, run compatability report and then switch to CNSA mode
    [Documentation]    Add C7000 enclosure in Legaccy, run compatability report and then switch to CNSA mode
    Switch Security Mode To    LEGACY
    Check If Current Security Mode Meets Target Mode    LEGACY
    Wait For ALL Enclosures Complete Refresh
    Run Keyword And Ignore Error    Remove All Enclosures
    Setup Env For C7000     ${Ring}    Add_Enclosure=true    Add_User=false
    Wait For ALL Enclosures Complete Refresh
    ${resp} =   Get Security Compatibility Report    CNSA
    Check Non-compliant Item In Compatibility Report    ${Ring}    ${resp}    ${c7000enclosureName_info}
    ${compliant} =  C7000 Enclosure Compliancevalidator    ${Ring}    FIPS
    Pass Execution If   '${compliant}' == 'True'   Run this case just for default Legacy compliant C7000 enclosure, skip if c7000 enclosure cert was changed to CNSA compliant
    Switch Security Mode To    CNSA
    Check If Current Security Mode Meets Target Mode    CNSA
    Enclosures Status Should Be Critical

