*** Settings ***
Library             RoboGalaxyLibrary
Resource            ../resource.txt
Documentation       Initial LE dump run

# Setup\Teardown for ALL test cases
Test Setup      Test Setup
Test Teardown   Test Teardown


*** Variables ***

*** Test Cases ***
Create and Download LE Support dump
    [Documentation]  Test of LE dump
    [Tags]    LE_DUMP

    # Create LE dump body list
    @{leDump_list} =    Create List
    ${le_list} =    Fusion Api Get Logical Enclosure
    ${count} =  Get From Dictionary  ${le_list}  count
    Return from keyword if  ${count}==0  Logical Enclosure not found
    LOG    LE list ${le_list}  console=True
    :FOR  ${le}  IN  @{le_list['members']}
    \    LOG    LE ${le['name']}  console=True
    \    ${ledump} =    Create Dictionary    name=${le['name']}    errorCode=myDump    excludeApplianceDump=False
    \    Append To List    ${leDump_list}   ${leDump}
    Create And Download Logical Enclosure Support Dump    ${leDump_list}    logDir=${OUTPUTDIR}

*** Keywords ***
