*** Settings ***
Documentation      Settings Page test suite
Resource           ../resource.txt
Suite Setup        Suite Setup
Suite Teardown     Logout and Close Browser
Force Tags         smoke settings  c7000 tbird
Test Timeout       ${TEST_TIMEOUT}


*** Variables ***
#  Create a list of dictionaries for the default panels on the dashboard page
&{link1}   link=Appliance                   page=Appliance
&{link2}   link=Backup                      page=Backup
&{link3}   link=Networking                  page=Networking
&{link4}   link=Time and Locale             page=Time and Locale
&{link5}   link=Licenses                    page=Licenses
&{link6}   link=Security                    page=Security
&{link7}   link=Notifications               page=Notifications
#&{link8}   link=Scopes                      page=Scopes
#&{link9}   link=Activity                    page=Activity
&{link10}  link=SNMP                        page=SNMP
&{link11}  link=Addresses and Identifiers   page=Addresses and Identifiers
&{link12}  link=Storage                     page=Storage
#&{link13}  link=Repository                  page=Repository
@{links}   ${link1}  ${link2}  ${link3}  ${link4}  ${link5}  ${link6}  ${link7}  ${link10}  ${link11}  ${link12}

*** Test Cases ***
Settings Page Links Should Open to Correct Panel
    [Documentation]  Navigate to each panel link on the page and make sure the page title is correct
    ...   \n Navigate to Settings page
    ...   \n Traverse panels
    ...   \n Ensure each link navigates to correct page

    Open Sub Menu   Appliance   Settings
    Navigate to Page  Settings
    Settings Page Links Should Be Visible
    :FOR  ${title}  in  @{links}
    \    Run Keyword If  '${title["page"]}' != '${None}'  Link Should Navigate to Expected Page  xpath=//a[@class='hp-anchor-uri' and text()='${title["link"]}']    ${title["page"]}
    #\    Click Element   id=hp-main-menu-control
    #\    Click Element   xpath=//div[@id='hp-main-menu']//a[text()='Settings']
    \    Click Element   xpath=//a[@class='hp-anchor-uri']

*** Keywords ***
Settings Page Links Should Be Visible
    [Documentation]  Verifies all panes links are visible on the Settings page
    :FOR  ${title}  in  @{links}
    \   Element Should Be Visible  xpath=//a[@class='hp-anchor-uri' and text()='${title["link"]}']

Link Should Navigate to Expected Page
    [Arguments]      ${link}  ${pageTitle}
    [Documentation]  Ensure that a clicked link navigates to a page with the correc title
    Sleep    5       # Wait until page loads object
    Click Element    ${link}
    ${xpath} =  Set Variable If  '${pageTitle}'== 'Storage'
    ...    //h1[text()='Storage']
    ...    //h1[a[@class='hp-anchor-uri']/ following-sibling::span[text()='${pageTitle}']]
    Element Should be Visible  ${xpath}
