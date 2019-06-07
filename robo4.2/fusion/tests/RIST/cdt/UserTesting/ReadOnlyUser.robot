*** Settings ***
#Library             RoboGalaxyLibrary
Library             pabot.PabotLib
Resource            ../resource.txt

*** Variables ***
${USERNAME}           rheid
${PASSWORD}           readonly
${SERVER_HARDWARE}    0000A66101, bay 4

*** Test Cases ***
Login
    Login As ${username} who is a ${password}

Power On Server
    ${servers} =    Fusion Api Get Server Hardware
    Power off Server    ${SERVER_HARDWARE}

