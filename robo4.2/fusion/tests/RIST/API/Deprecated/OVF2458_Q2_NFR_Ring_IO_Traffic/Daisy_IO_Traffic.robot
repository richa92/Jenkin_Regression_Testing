*** Settings ***
Documentation                   Perform Backup Restore Operations
...                             For Daisy, can't add profile as all are already assigned.  Will work on new test
...                             strategy for Daisy.
...                             6/22/17  Will delete a profile post backup.  Then verify profile once backup is restored.

Library                         FusionLibrary
Library                         RoboGalaxyLibrary
Library                         OperatingSystem
Library                         BuiltIn
Library                         Collections
Library                         XML
Library                         String
Library                         json

Resource                        ./../../../../Resources/api/fusion_api_resource.txt
Resource                        ../global_variables.robot

Variables 		                ${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}                 APPLIANCE_IP

${wordy}                        ${True}

${DATA_FILE}                    ./Daisy_Data.py

*** Test Cases ***
Ping Blade From Testhead
    ${admin_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
    Power On Server    ${SERVER1}

    Set Suite Variable    ${FUSION_SSH_USERNAME}    root
    Set Suite Variable    ${FUSION_SSH_PASSWORD}    hpvse123
    Set Suite Variable    ${FUSION_IP}    16.114.218.178

    Log    Ping: ${PING_COUNT} packets and expecting: ${PING_EXPECT}
    ${output} =    Execute SSH Command    ping -c ${PING_COUNT} ${SERVER1_IP1}
    Should Contain    ${output}    ${PING_EXPECT}

    ${output} =    Execute SSH Command    ping -c ${PING_COUNT} ${SERVER1_IP2}
    Should Contain    ${output}    ${PING_EXPECT}

    ${output} =    Execute SSH Command    ping -c ${PING_COUNT} ${SERVER1_IP3}
    Should Contain    ${output}    ${PING_EXPECT}

    Fusion Api Logout Appliance
