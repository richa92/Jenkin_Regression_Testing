***Settings***
Documentation        Network Page Test Suite
Resource             ../resource.txt
Suite Setup          Suite Setup
Suite Teardown       Logout And Close Browser
Force Tags           smoke  networks  tbird  c7000
Test Timeout     ${TEST_TIMEOUT}


*** Variables ***
@{network_types}  FCoE  FibreChannel  Ethernet

***Test Case***
Network Page Elements Should Appear as Expected
    [Documentation]  Network Page Elements Should Appear as Expected
    ...   \n Navigate to Network Sets page
    ...   \n Click "Create Network"
    ...   \n Create Network Dialog box Should be visible
    ...   \n Verify text can be input into the Network name field
    ...   \n Click ehternet network type radio buttons to ensure they work
    ...   \n For each radio button
    ...      Click Ethernet, Fibre Channel and FCoE radio button
    ...   \n Ensure that anyone of "Tagged", "Untagged" and 'Tunnel' can both be selected as VLAN.
    ...   \n Ensure that anyone of "Fabric Attach" and "Direct Attach" can both be selected as Fabric Type
    ...   \n Create button should be visible and primary in Create Network Dialog box
    ...   \n Create+ button should be visible in Create Network Dialog box
    ...   \n Click Cancel button in Create Network Dialog box
    ...   \n Create Network Dialog should not be visible

    Open Sub Menu   Networking   Networks
    Navigate To Page  Networks
    Click Link        Link=Create network
    Dialog Should Be Visible  Create Network

    ${network_name}=  Generate Random String  8  chars=[LETTERS][NUMBERS]
    Input Text        id=cic-network-name  ${network_name}

    :FOR  ${type}  In  @{network_types}
    \    Click Element  xpath=//li[label[@data-localize='networks.common.type']]//input[@type='radio' and @value='${type}']

    ${vlan_types}=  Create List From Drop Down Menu  cic-network-add-ethernet-network-type
    Remove values From List  ${vlan_types}  Tagged
    :FOR  ${vlan}  In  @{vlan_types}
    \    Select Item From Drop Down Menu  networks.add.vlan  ${vlan}
    \    Message Should Be Displayed To Confirm Element Selection  ${vlan}

    # Iterate through add network purpose list
    ${purpose_list}=  Create List From Drop Down Menu  cic-network-add-purpose
    Remove values From List  ${purpose_list}  General
    :FOR  ${purpose}  In  @{purpose_list}
    \    Select Item From Drop Down Menu  networks.common.purpose  ${purpose}
    \    Message Should Be Displayed To Confirm Element Selection  ${purpose}

    Click Element  id=cic-network-add-fc-type
    ${fabric_list}=  Create List From Drop Down Menu  cic-network-add-fabricType
    Remove values From List  ${fabric_list}  Fabric attach
    :FOR    ${fabric }    In    @{fabric_list}
    \    Select Item From Drop Down Menu  networks.common.fabricType  ${fabric}
    \    Message Should Be Displayed To Confirm Element Selection  ${fabric}

    Dialog Element Should Be Visible    css=#cic-network-add.hp-primary
    Dialog Element Should Be Visible    id=cic-network-add-again
    Click Element                       id=cic-network-add-close
    Dialog Should Not Be Visible        Create Network
