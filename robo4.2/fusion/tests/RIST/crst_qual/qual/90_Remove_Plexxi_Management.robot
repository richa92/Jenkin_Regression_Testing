*** Settings ***
Documentation     Remove Plexxi Management
Resource                ../resource.txt

Variables                       ../Common.py
Variables                       ../${DATA_FILE}

Suite Setup                     QUAL Suite Setup    ${admin_credentials}
Suite Teardown                  QUAL Suite Teardown

*** Test Cases ***
Plexxi Login
    [Documentation]    Ensure Logged Into Plexxi for the following [TAG] Test Cases
    [Tags]    90    CONFIRM_EMPTY_ACCESS_Ports    PLEXXI_ONEVIEW_CONFIG    RM_ONEVIEW_FABRICS

    Plexxi Login

Confirm Plexxi Access Ports Empty
    [Documentation]    With profiles removed, no vlans or native_port configured on access ports.
    [Tags]     90    CONFIRM_EMPTY_ACCESS_Ports

    Confirm Plexxi Access Ports    ${CONFIRM_PLEXXI_PORTS_EMPTY}

Remove OneView Configuration In Plexxi Connect
    [Documentation]    Remove OneView Configuration defined in data variable file from Plexxi Connect.
    [Tags]    90    PLEXXI_ONEVIEW_CONFIG
    Remove OneView Configuration From Composable Fabric Manager

Remove Fabrics
    [Documentation]   Remove fabrics in OneView
    [Tags]   90    RM_ONEVIEW_FABRICS
    ${fabrics} =   Fusion Api Get Fabric
    :FOR   ${fabric}   IN   @{fabrics['members']}
    \   ${resp} =   Fusion Api Delete Fabric   ${fabric['name']}
    \   Wait For Task2    ${resp}    timeout=60    interval=5
