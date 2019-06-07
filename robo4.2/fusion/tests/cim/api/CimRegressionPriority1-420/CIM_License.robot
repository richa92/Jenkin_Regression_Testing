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

Add License to the appliance
    [Documentation]     Add a valid License to the appliance
    Login    ${admin_credentials}
    Delete All Fusion License
    Log To Console And Logfile    Adding new licenses
    Add License and Verify that License is added     ${newLicenses["license"]}    ${License_type}
    Logout

Apply To Nodes and verify count
    [Documentation]     Apply license to the nodes
    Login    ${admin_credentials}
    ${TotalCapacity} =    Get All License Capacity
    Apply Licenses to Node
    ${assignedlicense} =    Get Length    ${node_list}
    ${assignedcount} =    Get All License Capacity
    ${verifyCapacity}=    Evaluate    ${assignedcount}+${assignedlicense}
    Should be Equal    ${TotalCapacity}    ${verifyCapacity}

Unassign License from Node and verify count
    [Documentation]     Unassign applied license from the node
    ${TotalCapacity} =    Get All License Capacity
    Unassign License from Node and verify count
    ${unassignedlicense} =    Get Length    ${node_list[0]}
    ${unassignedcount} =    Get All License Capacity
    ${verifyCapacity}=    Evaluate    ${unassignedcount} - ${unassignedlicense}
    Should be Equal    ${TotalCapacity}    ${verifyCapacity}

