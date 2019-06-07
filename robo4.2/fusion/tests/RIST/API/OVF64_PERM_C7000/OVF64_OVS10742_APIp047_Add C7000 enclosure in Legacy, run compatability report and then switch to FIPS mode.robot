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
Add C7000 enclosure in Legacy, run compatability report and then switch to FIPS mode
    [Documentation]    Add C7000 enclosure in Legaccy, run compatability report and then switch to FIPS mode
    ${compliant} =  C7000 Enclosure Compliancevalidator    ${Ring}    FIPS
    Check If Current Security Mode Meets Target Mode    LEGACY
    Wait For ALL Enclosures Complete Refresh
    Run Keyword And Ignore Error    Remove All Enclosures
    Setup Env For C7000     ${Ring}    Add_Enclosure=true    Add_User=false
    Wait For ALL Enclosures Complete Refresh
    ${resp} =   Get Security Compatibility Report    FIPS
    Check Non-compliant Item In Compatibility Report    ${Ring}    ${resp}    ${c7000enclosureName_info}
    Pass Execution If   '${compliant}' == 'True'   Run this case just for default Legacy compliant C7000 enclosure, skip if c7000 enclosure cert was changed to FIPS compliant
    Switch Security Mode To    FIPS
    Check If Current Security Mode Meets Target Mode    FIPS
    Enclosures Status Should Be Critical

