*** Settings ***
Documentation      Power Delivery Devices Page Test Suite
Resource           ../resource.txt
Suite Setup        Suite Setup
Suite Teardown     Logout and Close Browser
Force Tags         smoke  powerdeliverydevices  tbird  c7000
Test Timeout       ${TEST_TIMEOUT}


*** Test Cases ***
'Add' Dialog Elements Should Appear As Expected
    [Documentation]  Power Delivery Devices dialog 'Add' Elements Should Appear As Expected
    ...    \n Navigate to "Unmanaged Devices" page
    ...    \n Click "Add Power Delivery Device"
    ...    \n "Add Power Delivery Device" Dialog Should box be visible
    ...    \n Verify text can be input into the name field in "Add Power Delivery Device" Dialog box
    ...    \n Select Type value from the list
    ...    \n Verify text can be input into the name field in "Add Power Delivery Device" Dialog box
    ...    \n Select Volts value from the list
    ...    \n Select Power feed value from the list
    ...    \n Click "Add Connections"
    ...    \n "Add Connections" Dialog box Should be visible
    ...    \n Add button should be visible and primary in "Add Connections" Dialog box
    ...    \n Add+ button should be visible in "Add Connections" Dialog box
    ...    \n Click Cancel button in "Add Connections" Dialog box
    ...    \n "Add Connections" Dialog box should not be visible
    ...    \n Click Cancel button in "Add Power Delivery Device" Dialog box
    ...    \n "Add Power Delivery Device" Dialog box should not be visible

    Open Sub Menu   Facilities   Power Delivery Devices
    Navigate to Page  Power Delivery Devices
    Click Link        link=Add power delivery device
    Dialog Should Be Visible  Add Power Delivery Device
    Dialog Element Should Be Visible  id=cic-pdd-add-cancel

    ${pdd_types}=  Create List From Drop Down Menu  cic-pdd-type
    Remove values From List  ${pdd_types}  HPE Intelligent Power Distribution Unit  # Remove default value
    :FOR  ${pdd_type}  In  @{pdd_types}
    \    Select Item From Drop Down Menu  pdds.add.type  ${pdd_type}
    \    Message Should Be Displayed To Confirm Element Selection  ${pdd_type}

    ${pdd_name}=  Generate Random String  8  chars=[LETTERS][NUMBERS]
    Input Text  id=cic-pdd-name  ${pdd_name}

    ${model_name}=  Generate Random String  8  chars=[LETTERS][NUMBERS]
    Input Text  id=cic-pdd-model  ${model_name}

    ${rated_capacity} =  Evaluate  random.randint(1, 9999)  modules=random
    Input Text  id=cic-pdd-ratedCapacity  ${rated_capacity}

    ${line_voltage} =  Evaluate  random.randint(1, 9999)  modules=random
    Input Text  id=cic-pdd-lineVoltage  ${line_voltage}

    ${device_phases}=  Create List From Drop Down Menu  cic-pdd-phaseType
    :FOR  ${device_phase}  In  @{device_phases}
    \    Select Item From Drop Down Menu  pdds.show.lineVoltage.label  ${device_phase}

    ${power_feeds}=  Create List From Drop Down Menu  cic-pdd-powerFeed
    :FOR  ${power_feed}  In  @{power_feeds}
    \    Select Item From Drop Down Menu  pdds.show.powerFeed.label  ${power_feed}

    ${part_pumber}=  Evaluate  random.randint(1, 9999)  modules=random
    Input Text  id=cic-pdd-partNumber  ${part_pumber}

    ${serial_number}=  Evaluate  random.randint(1, 9999)  modules=random
    Input Text  id=cic-pdd-serialNumber  ${serial_number}

    Click Element  id=cic-pdd-add-addPwrConn
    Dialog Should Be Visible  Add connections
    Dialog Element Should Be Visible  css=button.hp-add.hp-primary
    Dialog Button Should Be Visible  Add +
    Dialog Element Should Be Visible  xpath=//button[@class='hp-cancel' and text()='Cancel']
    Click Element  xpath=//button[@class='hp-cancel' and text()='Cancel']

    Click Element  id=cic-pdd-add-cancelManual
    Dialog Should Not Be Visible  Add Power Delivery Device
