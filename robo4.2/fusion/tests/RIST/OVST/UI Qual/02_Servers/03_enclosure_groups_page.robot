*** Settings ***
Documentation    Enclosure Group Page Test Suite
Resource         ../resource.txt
Suite Setup      Suite Setup
Suite Teardown   Logout and Close Browser
Force Tags       smoke  enclosuregroup
Test Timeout     ${TEST_TIMEOUT}

*** Variables ***
@{ipv4_radio_btns}    Use address pool    Use DHCP    Manage externally

*** Test Cases ***
Tbird Applaince "Create Enclosure Group" Dialog Elements Should Appear As Expected
    [Tags]   tbird
    [Documentation]  Tbird Enclosure Group Page "Create Enclosure Group" Dialog Elements Should Appear As Expected
    ...    \n Navigate to Enclosure Groups Page
    ...    \n Click "Create Enclosure Group" button
    ...    \n "Create Enclosure Group" dialog should be visible
    ...    \n Enter text into Name field (use random characters) and Verify that name entered equals what was entered
    ...    \n Click the "Enclosure Count" menu item
    ...    \n Ensure that a menu is displayed with some number of enclosures.
    ...    \n Click each of the IPv4 radio buttons to ensure they work
    ...    \n Select "OS Deployment Settings" from the panel navigation menu
    ...    \n For each deployment network type
    ...    \n Click the "Deployment Network type" menu
    ...    \n Internal and External items should be visible
    ...    \n Select "Power" from the panel navigation menu
    ...    \n Ensure that "Redundant power feed" and "Redundant power supply" can both be selected as power mode.

    Open Sub Menu   Servers   Enclosure Groups
    Navigate to Page  Enclosure Groups
    Click Link  link=Create enclosure group
    Dialog Should Be Visible  Create Enclosure Group

    ${enclr_counts}=  Create List From Drop Down Menu  cic-enclosure-group-create-enclosure-count
    Remove values From List  ${enclr_counts}  1    # Removing default value from list
    :For  ${enclr_count}  In  @{enclr_counts}
    \    Select Item From Drop Down Menu  enclosuregroups.create_and_edit.count  ${enclr_count}
    \    Message Should Be Displayed To Confirm Element Selection  ${enclr_count}

    ${radio_count}=  Get Length  ${ipv4_radio_btns}
    :For  ${index}  In Range  1  ${radio_count}+1
    \    Click Element  xpath=//div[@id='cic-encgroups-ipv4-addresses-radio']/Input[${index}]
    \    Message Should Be Displayed To Confirm Element Selection  ${ipv4_radio_btns[${index}-1]}

    Select Item From Action or Panel Drop Menu  cic-enclosuregroups-panel-selector  OS Deployment Settings
    Panel Should Be Visible  OS Deployment Settings
    ${network_types}=  Create List From Drop Down Menu  cic-encgroups-imagestreamerconfiguration  # Id of select tag
    Remove values From List  ${network_types}    None  # Removing default value from list
    :For  ${network_type}  In  @{network_types}
    \    Select Item From Drop Down Menu  enclosuregroups.create_and_edit.deployment_network_type  ${network_type}
    \    Message Should Be Displayed To Confirm Element Selection  ${network_type}

    Select Item From Action or Panel Drop Menu  cic-enclosuregroups-panel-selector  Power
    Panel Should Be Visible  Power

    ${power_modes}=   Create List  Redundant power feed  Redundant power supply
    :For  ${power_mode}  In  @{power_modes}
    \    Click Element  xpath=//li[@id='cic-enclosuregroups-panel-add-power']//div[attribute::data-id]/ancestor::div[@class='hp-select-form']
    \    Click Element  xpath=//li[@id='cic-enclosuregroups-panel-add-power']//ol/li/span[text()='${power_mode}']
    \    Element Should Be Visible  xpath=//div[attribute::data-id and text()='${power_mode}']

    ${enclr_grp_name}=  Generate Random String  8  chars=[LETTERS][NUMBERS]
    Input Text  id=cic-encgroups-name  ${enclr_grp_name}
    Click Button  id=cic-encgroups-cancel
    Dialog Should Not Be Visible  Create Enclosure Group

C7000 Applaince "Create Enclosure Group" Dialog Elements Should Appear As Expected
    [Tags]  c7000
    [Documentation]  C7000 Applaince Enclosure Group Page Dialog "Create Enclosure Group" Should Display As Per Expected
    ...   \n Navigate to Enclosure Groups Page
    ...   \n Click "Create Enclosure Group" button
    ...   \n "Create Enclosure Group" dialog should be visible
    ...   \n Enter text into Name field (use random characters)
    ...   \n Iterate through items in panel selection menu
    ...   \n Create button should be visible and primary in "Create enclosure group" Dialog box
    ...   \n Create+ button should be visible in "Create enclosure group" Dialog box
    ...   \n Click Cancel button in "Create enclosure group" Dialog box
    ...   \n "Create enclosure group" Dialog box should not be visible

    Open Sub Menu   Servers   Enclosure Groups
    Navigate to Page  Enclosure Groups
    Click Link  link=Create enclosure group
    Dialog Should Be Visible  Create Enclosure Group
    ${enclosuregroup_name}=  Generate Random String  8  chars=[LETTERS][NUMBERS]
    Input Text  id=cic-encgroups-name  ${enclosuregroup_name}
    ${panels}=  Create List From Action or Panel Drop Menu  cic-enclosuregroups-panel-selector
    :FOR  ${panel}  in  @{panels}
    \    Select Item From Action or Panel Drop Menu  cic-enclosuregroups-panel-selector  ${panel}
    \    Panel Should Be Visible  ${panel}
    Dialog Element Should Be Visible  css=#cic-encgroups-submit.hp-primary
    Dialog Element Should Be Visible  id=cic-encgroups-submit-plus
    Click Element  id=cic-encgroups-cancel
    Dialog Should Not Be Visible  Create Enclosure Group
