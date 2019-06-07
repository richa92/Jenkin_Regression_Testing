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
F85p0024- check EM reset of redundancy standby enclosure in configured status

       ${Result} =   Fusion UI Validate Enclosure Configuration   @{TestData.Enclosure_Configured}
       should be true      ${Result}  msg=Failed to validate enclosure in configured state

       ${Result} =   Fusion UI Reset Link Module By Name    ${TestData.standby_reset[0].name}   ${TestData.standby_reset[0].link_module_type}
       should be true      ${Result}  msg=Failed to reset link module in standby way

        ${Result} =   Fusion UI Validate Tbird Enclosure Configuration        @{TestData.standby_reset}
       should be true      ${Result}  msg=Failed to validate enclosure link module info

