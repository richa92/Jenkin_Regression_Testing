*** Settings ***
Documentation    Test case to create appliance self signed certificate with default values
...    It covers:
...        Create Self Signed Certificate with Default Values
...        Verify Certificate data
...        Verify Entry in entry in Audit log file
...    Generic Usage:
...        pybot -v Appliance_IP:<IP_ADDRESS> CIM_Create_Self_Signed_Certificate_Default.robot
...    Variables:
...        searchText - Text string to verify in audit log file
...    TestData:
...        APPLIANCE_IP - Appliance IP address is passed from pybot command
...        ADMIN_CREDENTIALS - Administrator credential are used from TestData420.py data file
...        DownloadPath - Download path is set in CIM_Settings_Keywords.txt resource file

Library           RoboGalaxyLibrary
Library           FusionLibrary

Resource          ../resources.txt

*** Variables ***
${searchText}    A new self signed certificate for the appliance has been generated

*** Test Cases ***
Create Self Signed Certificate
    [Documentation]    Create Self Signed certificate for the appliance
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${ADMIN_CREDENTIALS}
    ${cert} =   Fusion Api Get Appliance Certificate
    Create Appliance Selfsigned Cert
    Verify Self Signed Certificate    ${cert}
    Download and verify entry in Audit log file    ${DownloadPath}    ${searchText}
