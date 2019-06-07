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
F85p0004-check_EM_reset_of_redundancy_active_enclosure_in_monitor_status

      ${Result} =  Fusion UI Delete Logical Enclosure      @{TestData.Tbird14LogicalEnclosure}
      Should be True   ${Result}   msg=Failed to delete logical enclosure

       ${Result} =   Fusion UI Validate Enclosure Configuration   @{TestData.Enclosure_monitored}
       should be true      ${Result}  msg=Failed to validate enclosure in monitor state

       ${Result} =   Fusion UI Reset Link Module By Name    ${TestData.active_reset[0].name}   ${TestData.active_reset[0].link_module_type}
       should be true      ${Result}  msg=Failed to reset link module in active way

       ${Result} =   Fusion UI Validate Tbird Enclosure Configuration        @{TestData.active_reset}
       should be true      ${Result}  msg=Failed to validate enclosure link module info



