*** Settings ***
Documentation                   Big Bird Discovery and Management
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

Resource                        ./../../../../Resources/api/fusion_api_resource.txt
Resource            ../global_variables.robot


Variables 		                ${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}                 16.114.213.16

${powerState_timeout}           30
${refresh_reset_timeout}        10
${interval}                     1

${wordy}                        ${True}

${DATA_FILE}                    ./F172-BB-NegativeTests_DCS.py

*** Test Cases ***
F172 Big Bird Negative Tests
    Set Log Level	DEBUG

    ${admin_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}

    Patch Drive Enclosure Negative Test

    Patch Drive Enclosure Uid flashing And On

    Fusion Api Logout Appliance


*** Keywords ***
Patch Drive Enclosure Negative Test
    [DOCUMENTATION]    Try to change partNumber of a Drive Enclosure
    # PATCH [{op: "replace", path: "/partNumber", value: "abcd"}]
    ${all_DE} =    Fusion Api Get Drive Enclosure

    ${this_DE} =    Get From List    ${all_DE['members']}    0
    ${name} =    Get From Dictionary    ${this_DE}   name
    ${uri} =    Get From Dictionary    ${this_DE}    uri
    ${partNumber} =    Get From Dictionary    ${this_DE}    partNumber

    Log To Console and Log File    DE to change PartNumber: ${name} ${uri} ${partNumber}

    @{patchPayload} =    Create List
    ${resetpartNumber} =    Create Dictionary    op=replace    path=/partNumber    value=abcd
    Append To List    ${patchPayload}    ${resetpartNumber}
    ${response} =    Fusion API Patch Drive Enclosure    ${patchPayload}    ${uri}

    Wait For Task2    ${response}    timeout=60	interval=5    errorMessage=Unsupported_DE_patch

Patch Drive Enclosure Uid flashing And On
    [DOCUMENTATION]    Try to set UID to flashing of a Drive Enclosure
    # PATCH [{op: "replace", path: "/uidState", value: "Flashing"}]
    ${all_DE} =    Fusion Api Get Drive Enclosure

    ${this_DE} =    Get From List    ${all_DE['members']}    0
    ${name} =    Get From Dictionary    ${this_DE}   name
    ${uri} =    Get From Dictionary    ${this_DE}    uri

    Log To Console and Log File    DE to set UID flashing: ${name} ${uri}

    @{patchPayload} =    Create List
    ${uidFlash} =    Create Dictionary    op=replace    path=/uidState    value=Flashing
    Append To List    ${patchPayload}    ${uidFlash}
    ${response} =    Fusion API Patch Drive Enclosure    ${patchPayload}    ${uri}
    Wait For Task2    ${response}    timeout=60	interval=5

    Log To Console and Log File    DE to set UID On: ${name} ${uri}

    @{patchPayload} =    Create List
    ${uidFlash} =    Create Dictionary    op=replace    path=/uidState    value=On
    Append To List    ${patchPayload}    ${uidFlash}
    ${response} =    Fusion API Patch Drive Enclosure    ${patchPayload}    ${uri}
    Wait For Task2    ${response}    timeout=60	interval=5