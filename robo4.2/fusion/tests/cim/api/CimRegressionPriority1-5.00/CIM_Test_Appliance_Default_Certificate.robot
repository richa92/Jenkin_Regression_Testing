*** Settings ***
Documentation    Test case to verify appliance default certificate
...                Verify Default validity and Alternate name fields in certificate
...                To be tested without creating any Self-signed/CA signed certificate
...    Generic Usage:
...                pybot -v Appliance_IP:<IP_ADDRESS> CIM_Test_Appliance_Default_Certificate.robot
...    Variables:
...                CERTIFICATE_VALIDITY - Certificate Validity period is passed in global variables
...    TestData:
...                APPLIANCE_IP - Appliance IP address is passed from pybot command
...                ADMIN_CREDENTIALS - Administrator credential are used from TestData420 data file
...                DownloadPath - Download path is set in CIM_Settings_Keywords.txt resource file

Library           RoboGalaxyLibrary
Library           FusionLibrary

Resource          ../resources.txt

*** Test Cases ***
Test Default Appliance Certificate
    [Documentation]    Check the Default Appliance Validity and Alternate Name fields
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${ADMIN_CREDENTIALS}
    Verify Certificate Validity    ${CERTIFICATE_VALIDITY}
    Verify Certificate Alternate Name
