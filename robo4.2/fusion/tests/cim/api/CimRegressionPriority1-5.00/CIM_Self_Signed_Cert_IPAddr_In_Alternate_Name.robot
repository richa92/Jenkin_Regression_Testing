*** Settings ***
Documentation    Create appliance self signed certificate with IPAddress Only in Alternate Name
...    It covers:
...        Create Self Signed Certificate with IPAddress in Alternate name
...        Verify IP Address in Alternate Name fields
...        Verify Task Details for 'Task Name', 'Owner' and 'State'
...        Verify Entry in Audit log file
...    Generic Usage:
...        pybot -v Appliance_IP:<IP_ADDRESS> CIM_Self_Signed_Cert_IPAddr_In_Alternate_Name.robot
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
    ${alternateName} =   Set Certificate Alternate Name    IPAddress
    Create Self Signed Certificate    ${alternateName}
    Verify Self Signed Certificate    ${alternateName}
    Download and verify entry in Audit log file    ${DownloadPath}    ${searchText}
