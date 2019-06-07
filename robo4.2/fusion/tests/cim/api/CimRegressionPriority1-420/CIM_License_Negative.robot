*** Settings ***
Documentation     Adding License to One View

Library           RoboGalaxyLibrary
Library           FusionLibrary
Library           SSHLibrary
Library           OperatingSystem
Library           String
Library           Collections
Library           XML
Resource          ../Resource/CIM_Common_Resource.txt
Resource          ../Resource1-42/CIM_License_Keywords.txt
Resource             ../Resource1-42/CIM_Common_Resource.txt

Variables             ../Resource1-42/resourcetype.py
Variables     ../TestData/TestData420.py

*** Test Cases ***

Add Invalid License
    [Documentation]     Try to add invalid license to appliance
    Login    ${admin_credentials}
    Log To Console And Logfile    Adding invalid licenses
    Run Keyword and expect error    Invalid License Key    Add License and Verify that License is added     ${newLicenses["invalidLicense"]}    ${License_type}
    Log To COnsole and Logfile    License key is invalid so cannot add license
    Logout

Add Duplicate License
    [Documentation]     Add a Existing License to the appliance
    Login    ${admin_credentials}
    Log To Console And Logfile    Adding existing licenses
    Run keyword and Ignore Error    Add License and Verify that License is added     ${newLicenses["license"]}    ${License_type}
    Logout