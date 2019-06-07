*** Settings ***
Documentation    This test suite will verify that the new menu defined in OVF6447_Men_Restyle
...              correctly opens and navigates to all pages.
Library             RoboGalaxyLibrary
Library             FusionLibrary
Suite Setup         Load Test Data, Open Browser, and Login
Suite Teardown      Logout and Close Browser

*** Variables ***
${APPLIANCE_URL}     https://15.245.132.162
${DATAFILE}         data.xml
${BROWSER}          chrome


*** Test Cases ***
Guided Setup Show/Hide
    [Documentation]    Make sure guided setup works correctly
    Fusion UI Open Guided Setup
    Fusion UI Guided Setup Should Be Opened
    Fusion UI Close Guided Setup
    Fusion UI Guided Setup Should Be Closed

All Menu Links Should Open Their Corresponding Pages
    [Documentation]   Walk the links on the menu and check the page titles
    Fusion UI Navigate to Activity Page
    Fusion UI Navigate to Firmware Bundles Page
    Fusion UI Navigate to Reports Page
    # Servers
    Fusion UI Navigate to Server Profiles Page
    Fusion UI Navigate to Server Profile Template Page
    Fusion UI Navigate to Enclosure Groups Page
    Fusion UI Navigate to Logical Enclosures Page
    Fusion UI Navigate to Enclosures Page
    Fusion UI Navigate to Server Hardware Page
    Fusion UI Navigate to Server Hardware Types Page
    # Networking
    Fusion UI Navigate to Networks Page
    Fusion UI Navigate to Network Sets Page
    Fusion UI Navigate to Logical Interconnect Groups Page
    Fusion UI Navigate to Logical Interconnects Page
    Fusion UI Navigate to Interconnects Page
    Fusion UI Navigate to Logical Switch Groups Page
    Fusion UI Navigate to Switch Page
    # Storage
    Fusion UI Navigate to Storage Volumes Page
    Fusion UI Navigate to Storage Volume Templates Page
    Fusion UI Navigate to Storage Pools Page
    Fusion UI Navigate to Storage Systems Page
    Fusion UI Navigate to SAN Page
    Fusion UI Navigate to SAN Managers Page
    # Facilities
    Fusion UI Navigate to Data Centers Page
    Fusion UI Navigate to Racks Page
    Fusion UI Navigate to Power Delivery Devices Page
    Fusion UI Navigate to Unmanaged Devices Page
    # Appliance
    Fusion UI Navigate to Settings Page
    Fusion UI Navigate to Users and Groups Page


*** Keywords ***
Load Test Data, Open Browser, and Login
    [Documentation]    Do some stuff, then more stuff
    Load Test Data      ${DATAFILE}
    Open Browser    ${APPLIANCE_URL}     ${BROWSER}
    Sleep  5s
    Fusion UI Login To Appliance    Administrator

Logout and Close Browser
    [Documentation]    Clean up and close out
    Fusion UI Logout of Appliance
    Close Browser

