*** Settings ***
Library             RoboGalaxyLibrary
Library             FusionLibrary
Resource            ../resource/dcs_keywords.robot

*** Variables ***
${DCS_IP}         172.17.4.137:9990

*** Test Cases ***
Verify Virtual Hardware in Demo DCS
    #Verify Schematic
    ${devices}=    List All Devices of Type    Procurve    ${DCS_IP}
    ${device_count}=    Get Length    ${devices}
    Should Be Equal As Integers    ${device_count}    2
    ${devices}=    List All Devices of Type    DL360pGen8    ${DCS_IP}
    ${device_count}=    Get Length    ${devices}
    Should Be Equal    ${device_count}    ${1}
    ${devices}=    List All Devices of Type    DL360Gen9    ${DCS_IP}
    ${device_count}=    Get Length    ${devices}
    Should Be Equal    ${device_count}    ${1}
    ${devices}=    List All Devices of Type    DL380pGen8    ${DCS_IP}
    ${device_count}=    Get Length    ${devices}
    Should Be Equal    ${device_count}    ${2}

Verify Device Types
    ${types}=    List all Types of Devices    ${DCS_IP}

Find Actions for all Types
    ${types}=    List all Types of Devices    ${DCS_IP}
    :FOR    ${type}    IN    @{types}
    \    Print all Verbs in Device  ${type}    ${DCS_IP}

Find Attributes for all Types
    ${types}=    List all Types of Devices    ${DCS_IP}
    :FOR    ${type}    IN    @{types}
    \    Print all Attributes in Device  ${type}    ${DCS_IP}
