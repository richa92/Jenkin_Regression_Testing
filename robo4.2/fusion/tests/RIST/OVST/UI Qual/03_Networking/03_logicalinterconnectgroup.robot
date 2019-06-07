*** Settings ***
Documentation     LIG Page Test Suite
Resource          ../resource.txt
Suite Setup       Suite Setup
Suite Teardown    Logout And Close Browser
Force Tags        smoke  lig
Test Timeout      ${TEST_TIMEOUT}


*** Variables***
${hostname_or_ip}    hponeview@hpe.net

*** Test Cases ***
Tbird LIG Page Elements Should Appear as Expected
    [Tags]  tbird
    [Documentation]    Tbird LIG page elements should appear as expected
    ...   \n Navigate to Logical Interconnect Groups
    ...   \n Click "Logical Interconnect Groups"
    ...   \n Create Logical Interconnect Groups Dialog box Should be visible
    ...   \n Verify text can be input into the LIG name field
    ...   \n Select Interconnect Type from the list
    ...   \n Select Enclosure count from the list
    ...   \n Select Interconnect bay set from the list
    ...   \n Click "Select Interconnects" Button
    ...   \n Iterate through items in panel selection menu
    ...   \n Click "Add Uplink Set"
    ...   \n Create "Uplink Set" Dialog box Should be visible
    ...   \n Select value from the type list
    ...   \n Ensure Networks and uplink ports pane is visible in Create Uplink Set Dialog box
    ...   \n Create button should be visible and primary in Create Uplink Set Dialog box
    ...   \n Create+ button should be visible in Create Uplink Set Dialog box
    ...   \n Click Cancel button in Create Uplink Set Dialog box
    ...   \n Click "Add Trap Destination"
    ...   \n Create "Add Trap Destination" Dialog box Should be visible
    ...   \n Add button should be visible and primary in "Add Trap Destination" Dialog box
    ...   \n Add+ button should be visible in "Add Trap Destination" Dialog box
    ...   \n Click Cancel button in "Add Trap Destination" Dialog box
    ...   \n Create button should be visible and primary in Create Logical Interconnect Groups Dialog box
    ...   \n Create+ button should be visible in Create Logical Interconnect Groups Dialog box
    ...   \n Click Cancel button in Create Logical Interconnect Groups Dialog box

    Open Sub Menu   Networking   Logical Interconnect Groups
    Navigate To Page  Logical Interconnect Groups
    Click Link  Link=Create logical interconnect group
    ${le_name}=  Generate Random String  8  chars=[LETTERS][NUMBERS]
    Input Text  id=cic-switchtemplate-add-name  ${le_name}

    ${interconnect_types}=  Create List From Drop Down Menu  cic-switchtemplate-add-module-type-synergy-value
    Remove values From List  ${interconnect_types}  Select
    :FOR  ${interconnect}  In  @{interconnect_types}
    \    Select Item From Drop Down Menu  switchtemplates.common.interconnectType  ${interconnect}
    \    Message Should Be Displayed To Confirm Element Selection  ${interconnect}

    Click Element  xpath=//div[@id='cic-switchtemplate-add-module-type-synergy-value-container']//div[@class='hp-value' and attribute::data-id]
    Click Element  xpath=//li/span[text()='Virtual Connect SE 40Gb F8 Module for Synergy']

    ${enclosurecount_list}=  Create List From Drop Down Menu  cic-switchtemplate-add-enclosure-count-value
    :FOR  ${enclosurecount}  In  @{enclosurecount_list}
    \    Select Item From Drop Down Menu  switchtemplates.common.enclosure_count  ${enclosurecount}

    Click Element  xpath=//div[@id='cic-switchtemplate-add-enclosure-count-container']//div[@class='hp-value' and attribute::data-id]
    Click Element  xpath=//li/span[text()='1']
    Click Element  id=cic-switchtemplate-add-select-synergy-interconnects-button
    Click Element  id=cic-add-uplink-li
    Dialog Should Be Visible  Create Uplink Set

    ${type_list}=  Create List From Drop Down Menu  cic-switchtemplate-dialog-type
    Remove values From List  ${type_list}  Select type
    :FOR  ${type}  In  @{type_list}
    \    Select Item From Drop Down Menu  networks.common.type  ${type}

    Dialog Element Should Be Visible  id=cic-switchtemplate-panel-dialog-networks
    Dialog Element Should Be Visible  id=cic-switchtemplate-panel-dialog-uplinks
    Dialog Element Should Be Visible  css=#cic-switchtemplate-dialog-add.hp-primary
    Dialog Element Should Be Visible  id=cic-switchtemplate-dialog-add-again
    Click Element  css=#cic-switchtemplate-dialog-form>footer>div>a
    Dialog Should Not Be Visible  Create Uplink Set
    Click Element  id=cic-snmp-general-add-trap-destination
    Dialog Should Be Visible  Add Trap Destination
    Dialog Element Should Be Visible  css=#cic-snmp-trap-destination-add-button.hp-primary
    Dialog Element Should Be Visible  id=cic-snmp-trap-destination-add-again
    Click Element  css=#cic-snmp-trap-destination-form>footer>div>a
    Dialog Should Not Be Visible  Add Trap Destination

    ${qos_list}=  Create List From Drop Down Menu  cic-qos-select-configtype-content
    Remove values From List  ${qos_list}  Passthrough
    :FOR  ${qos}  In  @{qos_list}
    \    Select Item From Drop Down Menu  qos.general.configType  ${qos}

    Dialog Element Should Be Visible  css=#cic-switchtemplate-add.hp-primary
    Dialog Element Should Be Visible  id=cic-switchtemplate-again
    Dialog Element Should Be Visible  id=cic-switchtemplate-add-close
    Click Element  id=cic-switchtemplate-add-close
    Dialog Should Not Be Visible  Create Logical Interconnect Group

C7000 LIG Page Elements Should Appear as Expected
    [Tags]  c7000
    [Documentation]    c7000 LIG page elements should appear as expected
    ...   \n Navigate to Logical Interconnect Groups
    ...   \n Click "Logical Interconnect Groups"
    ...   \n Create Logical Interconnect Groups Dialog box Should be visible
    ...   \n Verify text can be input into the LIG name field
    ...   \n Select Interconnect Type from the list
    ...   \n Click "Select Interconnects" Button
    ...   \n Iterate through items in panel selection menu
    ...   \n Click "Add Trap Destination"
    ...   \n Create "Add Trap Destination" Dialog box Should be visible
    ...   \n Verify text can be input into the Trap destination name field
    ...   \n Select Trap format Radio Button
    ...   \n Add button should be visible and primary in "Add Trap Destination" Dialog box
    ...   \n Add+ button should be visible in "Add Trap Destination" Dialog box
    ...   \n Click Cancel button in "Add Trap Destination" Dialog box
    ...   \n "Add Trap Destination" Dialog box Should Not be visible
    ...   \n Click "Add SNMP Access"
    ...   \n Create "Add SNMP Access" Dialog box Should be visible
    ...   \n Verify text can be input into the IP or Subnet field
    ...   \n Add button should be visible and primary in "Add SNMP Access" Dialog box
    ...   \n Add+ button should be visible in "Add SNMP Access" Dialog box
    ...   \n Click Cancel button in "Add SNMP Access" Dialog box
    ...   \n "Add SNMP Access" Dialog box Should Not be visible
    ...   \n Create button should be visible and primary in Create Logical Interconnect Groups Dialog box
    ...   \n Create+ button should be visible in Create Logical Interconnect Groups Dialog box
    ...   \n Click Cancel button in Create Logical Interconnect Groups Dialog box

    Open Sub Menu   Networking   Logical Interconnect Groups
    Navigate To Page  Logical Interconnect Groups
    Click Link  Link=Create logical interconnect group
    ${le_name}=  Generate Random String  8  chars=[LETTERS][NUMBERS]
    Input Text  id=cic-switchtemplate-add-name  ${le_name}
    Click Element  xpath=//div[@id='cic-switchtemplate-add-module-type-c7000-value-container']//div[@class='hp-value' and attribute::data-id]
    Click Element  xpath=//li/span[text()='Virtual Connect']
    Click Element  id=cic-switchtemplate-add-select-c7000-interconnects-button
    Click Element  id=cic-snmp-general-add-trap-destination
    Dialog Should Be Visible  Add Trap Destination
    Input Text  id=cic-snmp-trap-destination-trap-destination  ${hostname_or_ip}
    Click Element  id=cic-snmp-trap-destination-snmpv2
    Dialog Element Should Be Visible  css=#cic-snmp-trap-destination-add-button.hp-primary
    Dialog Element Should Be Visible  cic-snmp-trap-destination-add-again
    Click Element  css=#cic-snmp-trap-destination-form>footer>div>a
    Dialog Should Not Be Visible  Add Trap Destination
    Click Element  id=cic-snmp-general-add-snmp-access
    Dialog Should Be Visible  Add SNMP Access
    Input Text  id=cic-snmp-add-access-address  ${hostname_or_ip}
    Dialog Element Should Be Visible  css=#cic-snmp-access-add-button.hp-primary
    Dialog Element Should Be Visible  id=cic-snmp-access-add-again-button
    Click Element  css=#cic-snmp-access-add-again-button+.hp-button.hp-cancel
    Dialog Should Not Be Visible  Add SNMP Access
    Dialog Element Should Be Visible  css=#cic-switchtemplate-add.hp-primary
    Dialog Element Should Be Visible  id=cic-switchtemplate-again
    Click Element  id=cic-switchtemplate-add-close
    Dialog Should Not Be Visible  Create Logical Interconnect Group
