*** Settings ***
Documentation    Main Menu Functionality
Resource         ../resource.txt
Suite Setup      Suite Setup
Suite Teardown   Logout and Close Browser
Force Tags       smoke  mainmenu  tbird  c7000
Test Timeout     ${TEST_TIMEOUT}


*** Test Cases ***
Main Menu Links Should Open Correct Pages
    [Documentation]  Make sure that the main menu opens and closes correctly and that links are visible
    Open Main Menu
    Wait Until Element is Visible  xpath=//div[@id='hp-main-menu']//a
    Close Main Menu

Click All Main Menu Links and Verify Page Titles
    [Documentation]  Click all of the links on the main menu page and verify that the landing page title is consistent
    [Tags]  links

    # Get the main menu links and build a dictionary
    Open Main Menu
    ${titles}=  Create List
    ${elements}=  Get Webelements  xpath=//ul[@class='hp-section hp-menu-header']/li[a]
    :FOR  ${link}  in  @{elements}
    \    ${link_text}=  Get Text  ${link}
    \    Append To List  ${titles}  ${link_text}
    Close Main Menu

    Log    ${titles}
    # Iterate over the main menu links, click them, and verify the landing page titile
    :FOR  ${title}  in  @{titles}
    \    Click Main Menu Item   ${title}
    \    Page Should Be    ${title}

