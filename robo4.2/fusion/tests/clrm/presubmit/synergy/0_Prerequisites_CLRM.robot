*** Settings ***
Documentation    Creates the Environment required for running CLRM Test Cases
Resource        ../resource.txt

Suite Setup      Login to the Appliance

Variables        test_data_dcs.py
*** Variables ***
${X-Api-Version}    1000

*** Test Cases ***
Add License to the appliance
    [Documentation]    Add license to the appliance
    Add License and Verify that License is added    ${newLicenses["license"]}    ${newLicenses["licenseType"]}