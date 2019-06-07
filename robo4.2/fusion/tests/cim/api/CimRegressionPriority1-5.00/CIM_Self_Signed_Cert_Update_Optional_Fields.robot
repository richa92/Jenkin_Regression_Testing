*** Settings ***
Documentation    Create appliance self signed certificate with FQDN Only in Alternate Name field
...    It covers:
...        Create Self Signed Certificate with FQDN in Alternate name
...        Verify Certificate Validity and Alternate Name fields
...        Verify Task Details for 'Task Name', 'Owner', 'Resource' and 'State'
...        Verify Entry in Audit log file
...    Generic Usage:
...        pybot -v Appliance_IP:<IP_ADDRESS> CIM_Create_Appliance_Certificate_Default.robot
...    Variables:
...        validity - Certificate Validity period
...        searchText - Text string to verify in audit log file
...    TestData:
...        APPLIANCE_IP - Appliance IP address is passed from pybot command
...        ADMIN_CREDENTIALS - Administrator credential are used from TestData420.py data file
...        DownloadPath - Download path is set in CIM_Settings_Keywords.txt resource file

Library           RoboGalaxyLibrary
Library           FusionLibrary
Resource          ../resources.txt
Variables         ../TestData/TestData500.py

*** Variables ***
${searchText}    A new self signed certificate for the appliance has been generated

*** Test Cases ***
Create Self Signed Certificate
    [Documentation]    Create Self Signed certificate for the appliance
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${ADMIN_CREDENTIALS}
    Create Self Signed Certificate    ${SELFSIGNEDCERTIFICATE['optionalFields'][0]}
    Verify Self Signed Certificate    ${SELFSIGNEDCERTIFICATE['optionalFields'][0]}
    Download and verify entry in Audit log file    ${DownloadPath}    ${searchText}
