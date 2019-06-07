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

Resource                        ./../../../../Resources/api/fusion_api_resource.txt
Resource            ../global_variables.robot

Suite Setup                     Setup
Suite Teardown                  Teardown

Variables 		                ${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}                 APPLIANCE_IP

${powerState_timeout}           40

${wordy}                        ${True}

${DATA_FILE}                    ./Big Bird discovery DCS.py

&{IPv6}                         ipAddressType=Ipv6LinkLocal    ipAddress=REGEX:([0-9a-fA-F]{4}:){3}[0-9a-fA-F]{4}
@{ipAddressList}                ${IPv6}

*** Test Cases ***
Power Off Graphite
    Power Off Interconnects from list    ${graphite_ICs_On}

Verify Graphite Off
    Wait Until Keyword Succeeds    2m    10s    Verify Interconnects from list  ${graphite_ICs_Off}

Power On Graphite
    Power On Interconnects from list    ${graphite_ICs_Off}

Verify Graphite On
    Wait Until Keyword Succeeds    2m    10s    Verify Interconnects from list  ${graphite_ICs_On}

*** Keywords ***
Setup
    Set Log Level	DEBUG
#    Log Variables    level=INFO
#    Fail    because
    Should Not Be Equal As Strings    ${APPLIANCE_IP}    APPLIANCE_IP

    ${admin_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}

Teardown
    Fusion Api Logout Appliance