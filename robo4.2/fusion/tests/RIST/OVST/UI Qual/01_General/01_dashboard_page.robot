*** Settings ***
Documentation    Dashboard page test suite
Resource         ../resource.txt
Suite Setup      Suite Setup
Suite Teardown   Logout and Close Browser
Force Tags       smoke  dashboard  c7000  tbird
Test Timeout     ${TEST_TIMEOUT}

*** Variables ***
#  Create a list of dictionaries for the default panels on the dashboard page
&{link1}  link=Server Profiles          page=Server Profiles
&{link2}  link=Server Hardware          page=Server Hardware
&{link3}  link=Servers with profiles    page=Server Hardware
&{link4}  link=Blade bays               page=${None}
&{link5}  link=Storage Pools            page=Storage Pools
&{link6}  link=Volumes                  page=Volumes
&{link7}  link=Logical Enclosures       page=Logical Enclosures
&{link8}  link=Enclosures               page=Enclosures
&{link9}  link=Logical Interconnects    page=Logical Interconnects
&{link10}  link=Interconnects           page=Interconnects
&{link11}  link=Appliance Alerts        page=Activity
@{links}   ${link1}  ${link2}  ${link3}  ${link4}  ${link5}  ${link6}  ${link7}  ${link8}  ${link9}  ${link10}  ${link11}

*** Test Cases ***
Reset Dashboard View
    [Documentation]  Dialog  Box 'Reset Dashboard Configuration' Should Display Elements As Expected
    [Tags]  reset
    Navigate to Page    Dashboard
    Select Item From Action or Panel Drop Menu  hp-dashboard-actions  Reset
    Dialog Should Be Visible   Reset Dashboard Configuration
    Element Should Be Visible  css=.hp-dialog > footer > .hp-controls > button.hp-ok
    Element Should Be Visible  css=.hp-dialog > footer > .hp-controls > button.hp-cancel
    Click Element              css=.hp-dialog > footer > .hp-controls > button.hp-ok
    Dialog Should Not Be Visible  Reset Dashboard Configuration

Default Dashboard Page Panel Links Should Open Correct Pages
    [Documentation]  Navigate to each panel link on the page and make sure the page title is correct
    [Tags]    panels
    :FOR  ${title}  in  @{links}
    \    Navigate to Page    Dashboard
    \    All Pane Links Should Be Visible
    \    Run Keyword If  '${title["page"]}' != '${None}'  Link Should Navigate to Correct Page  xpath=//span[@class='hp-name' and text()='${title["link"]}']/parent::a  ${title["page"]}

*** Keywords ***
All Pane Links Should Be Visible
    [Documentation]  Verifies that all panes are visible on the dashboard page
    :FOR  ${title}  in  @{links}
    \   Element Should Be Visible  xpath=//span[@class='hp-name' and text()='${title["link"]}']/parent::a
