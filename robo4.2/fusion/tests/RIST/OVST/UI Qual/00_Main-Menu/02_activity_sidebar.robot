*** Settings ***
Documentation    Activity Sidebar functionality
Resource         ../resource.txt
Suite Setup      Suite Setup
Suite Teardown   Logout and Close Browser
Force Tags       smoke  mainmenu  tbird  c7000
Test Timeout     ${TEST_TIMEOUT}

*** Test Cases ***
Pressing the Activity Icon Should Toggle Display of the Activity Sidebar
    [Documentation]  Pressing the Activity Icon Should Toggle Display of the Activity Sidebar
    ...     \n Click on Activity Icon
    ...     \n Acitivty Sidebar should be visible
    ...     \n Acitivty Sidebar label name should be Activity
    ...     \n Click on Activity Icon again
    ...     \n Activity sidebar should not be visible

    Open Activity Side Bar
    Close Activity Side Bar