*** Settings ***
Documentation                   Enable feature toggles
...                             Used to enable feature toggles for features to be tested

Library        FusionLibrary
Library        BuiltIn
Library        Collections
Library        json
Library        Dialogs
Resource        ./keywords.txt
Variables       ./Regression_Data.py
Variables       ./Feature_Toggles.py

*** Variables ***


*** Test Cases ***
Enable feature toggles by given features
    ${resp} =  Fusion Cli Enable Feature Toggles    ${APPLIANCE_IP}    ${features}     ${featureTogglesMapping}    ${ssh_credentials}
    Run Keyword If  ${resp}      Reboot appliance via API    ${APPLIANCE_IP}    ${admin_credentials}

# For OVF167 and OVF2, need to populate the role and reboot
    ${resp} =  Populate Role Flag    ${features}     ${PopulateFeatures}
    Run Keyword If      ${resp}       Populate the role and reboot    ${APPLIANCE_IP}     ${admin_credentials}        ${ssh_credentials}      ${populateCMDs}

