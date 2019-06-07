*** Settings ***
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

Suite Setup     Precondition Setup
Suite Teardown  Clear Environment After Test

*** Variables ***
${APPLIANCE_IP}    ${None}

*** Keywords ***
Precondition Setup
    [Documentation]  The precondition Setup
    Set Log Level           TRACE
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    Switch Security Mode To    LEGACY
    Check If Current Security Mode Meets Target Mode    LEGACY
    Wait For ALL Enclosures Complete Refresh
    Run Keyword And Ignore Error    Remove All Enclosures

Clear Environment After Test
    [Documentation]  Clear Environment After Test
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    Switch Security Mode To    LEGACY
    Check If Current Security Mode Meets Target Mode    LEGACY
    Wait For ALL Enclosures Complete Refresh
    Run Keyword And Ignore Error    Remove All Enclosures
    Fusion Api Logout Appliance