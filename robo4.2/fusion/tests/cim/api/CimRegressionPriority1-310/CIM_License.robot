*** Settings ***
Documentation     Adding License to One View


Library           RoboGalaxyLibrary
Library           FusionLibrary
Library           SSHLibrary
Library           OperatingSystem
Library           String
Library           Collections
Library           XML
Resource          ../Resource/CIM_Common_Resource.txt

*** Test Cases ***

Add License to the appliance
    [Documentation]     Add a valid License to the appliance
    Login    ${admin_credentials}
    Delete All Fusion License
    Log To Console And Logfile    Adding new licenses
    Add License and Verify that License is added     ${newLicenses["license"]}    ${newLicenses["licenseType"]}
    Logout


Add Invalid License
    [Documentation]     Try to add invalid license to appliance
    Login    ${admin_credentials}
    Delete All Fusion License
    Log To Console And Logfile    Adding invalid licenses
    Run Keyword and expect error    Invalid License Key    Add License and Verify that License is added     ${newLicenses["invalidLicense"]}    ${newLicenses["licenseType"]}
    Log To COnsole and Logfile    License key is invalid so cannot add license
    Logout

***Keywords***

Add License and Verify that License is added
    [Documentation]     Add license
    [Arguments]    ${licenses}    ${type}
    :FOR    ${ovLic}  IN  @{licenses}
    \    ${resp}=     Fusion Api Add License     ${ovLic['key']}    ${type}
    \    Run Keyword If    ${resp['status_code']}==400     Run Keyword If    '${resp['errorCode']}'=='EXPIRED_LICENSE_KEY'       Fail    License Key expired
    \    Run Keyword If    ${resp['status_code']}==400     Run Keyword If    '${resp['errorCode']}'=='INVALID_LICENSE_KEY'       Fail    Invalid License Key
    \    Run Keyword If    ${resp['status_code']}==400     Run Keyword And Continue On Failure	 Fail    Failed to add License Key ${ovLic['key']}
    \    Should Be Equal    '${resp['status_code']}'    '201'    msg=Failed to Add License.
    \    Log to console and logfile    License is added to appliance
    \    ${lic-res} =    Get All OV Licenses
    \    ${response}=    Convert to Dictionary    @{lic-res}[0]
    \    ${key} =    Get From Dictionary    ${response}    key
    \    Log    ${key}
    \    Should Contain    ${ovLic['key']}    ${key}    msg=not added
    \    Log to console and logfile    "Verification on Adding a License into HP OneView has PASSED"
