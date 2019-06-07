*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Pause And Close Browser

*** Variables ***
${DataFile}         F289/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}    # Appliance Url

*** Test Cases ***
As an Administrator I want to delete SP with all configure forcibly and server power on
    ${Result} =      Fusion UI Create Server Profile  @{TestData.F289P036.Create}
    should be true   ${Result}   msg=Failed to create Server Profiles

    ${Result} =      Fusion UI Power On Server Profile  @{TestData.F289P036.Create}
    should be true   ${Result}   msg=Failed to power on Server Profiles

#    comment these two lins until QXCR1001491715 is fixed
#    ${Result} =      Fusion UI Validate Server Profile Cannot Be Deleted When Power On  ${TestData.F289P036.Create[0].name}
#    should be true   ${Result}  msg=Failed to verify Server Profile can not be deleted when power on

    ${Result} =      Fusion UI Delete Server Profile  @{TestData.F289P036.Delete}
    should be true   ${Result}  msg=Failed to delete Server Profile
