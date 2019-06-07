*** Settings ***
Documentation                   Big Bird Discovery and Management (Monitored Enclosure)
...                             Verifies
...                               -  Drive Enclosure count is correct
...                               -  One Physical Enclosure contains correct DE data
...                               -  One Physical Drive Enclosure contains correct data
...                               -  Toggle the uidState and powerState of all the Drive Enclosures
...                               -  Reset and Refresh a random Drive Enclosure

Library                         FusionLibrary
Library                         RoboGalaxyLibrary
Library                         OperatingSystem
Library                         BuiltIn
Library                         Collections
Library                         XML
Library                         String
Library                         json

Resource                       ./../../../../Resources/api/fusion_api_resource.txt
Resource                       ../global_variables.robot


Variables 		                ${DATA_FILE}

Suite Teardown                  Clean Up

*** Variables ***
${APPLIANCE_IP}                 APPLIANCE_IP

${powerState_timeout}           40

${wordy}                        ${True}

${DATA_FILE}                    ./Big Bird discovery DCS.py

*** Test Cases ***
Verify Enclosure Count
    Set Log Level	DEBUG

    Should Not Be Equal As Strings    ${APPLIANCE_IP}    APPLIANCE_IP

    ${admin_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}

    ${de} =    Verify Drive Enclosure Count    ${expected_number_of_DE}

    Set Suite Variable    ${ALL_DE}    ${de}

Toggle Verify UUID and Power States of the DE
    Log to console and logfile    ${AlL_DE}
    Toggle Verify uidState and powerState Drive Enclosures    ${ALL_DE}

Reset DE
    [Tags]    Performance    drive_enclosures-condition-reset
    Reset Random Drive Enclosure
    Sleep    20 seconds    reason=Drive Enclosure Drive Bays take a while to fully populate data after Refresh.

Refresh DE
    [Tags]    Performance    drive_enclosures-condition-refresh
    Refresh Random Drive Enclosure

Verify Enclosures
    Verify Enclosures from list  ${enclosures}

Verify Drive Enclosures
    Verify Drive Enclosures from list    ${drive_enclosures}

*** Keywords ***
Clean Up
    Fusion Api Logout Appliance