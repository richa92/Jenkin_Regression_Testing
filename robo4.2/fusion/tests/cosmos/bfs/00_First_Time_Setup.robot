*** Settings ***
Documentation    First Time Setup
Resource         resource.txt

*** Test Cases ***
First Time Setup
    [Tags]    FTS
    [Documentation]    Configure First time setup for OneView Appliance
    Assign Administrator Password    ${admin_password}
    Configure Oneview Interface