*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Pause And Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F85/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}    # Appliance Url


*** Test Cases ***
F85p0021_check_SH_ilo_reset_when_power_is_off_in_configured_status.robot

     ${Result} =    Fusion UI Validate Server Hardware Managed       @{TestData.ResetIlo}
     should be true            ${Result}    msg=Failed to validate server hardware is managed
     ${Result} =    Fusion UI Power Off Server Hardware    @{TestData.ResetIlo}
     should be true            ${Result}    msg=Failed to power off server hardware
     ${Result} =    Fusion UI Reset Ilo   @{TestData.ResetIlo}
     should be true            ${Result}    msg=Failed to reset lio for server hardware

     ${Result} =   Fusion UI Validate Server Hardware Task Status From Activity View  ${TestData.ResetIlo[0].name}   ${TestData.Message[0].Restore_network_msg}  ${TestData.Message[0].Action_name}   ok
     should be true        ${Result}       msg=Failed to validate network connectivity lost

     ${Result} =   Fusion UI Validate Server Hardware Task Status From Activity View  ${TestData.ResetIlo[0].name}    ${TestData.Message[0].Lost_network_msg}  ${TestData.Message[0].Action_name}   error
     should be true        ${Result}       msg=Failed to validate network connectivity restore

     ${power_state} =   Fusion UI Get Server Powerstatus   ${TestData.ResetIlo[0].name}
     should be equal   ${power_state}   Off





