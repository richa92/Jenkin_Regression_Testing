** Settings ***
Documentation        Report Generation
Library              RoboGalaxyLibrary
Library              FusionLibrary
Library              SSHLibrary
Library              OperatingSystem
Library              String
Library              Collections
Library              XML
Resource             ../Resource/CIM_Common_Resource.txt
Resource             ../Resource1-42/CIM_Common_Resource.txt
Resource             ../Resource1-42/CIM_Report_Keyword.txt

*** Variables ***
${reportName}=    Local users

*** Test Cases ***

Local User Report Generation
    [Documentation]    Gets the Local User Report and saves it in csv and xlsx format
    Get Reports from Appliance
    Save Report    ${reportName}    csv
    Save Report    ${reportName}    xlsx
    Logout
