*** Settings ***
Documentation
...     This Test Suite uses Administrator credentials for SPP Upload Test.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      SETUP
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup     ${admin_credentials}
Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
...                             AND  Regression Test Teardown

*** Test Cases ***
Download SPP Bundle
    [Tags]  DOWNLOAD-SPP  C7000
    [Documentation]        Download SPP bundle
    Log    ${WEB_URL_SPP}   console=True
    Download Specified SPP to Local Path   ${WEB_URL_SPP}    ${WEB_USERNAME_SPP}   ${WEB_PASSWORD_SPP}

Validate Existing SPP Accessible
    [Documentation]  Validate existing SPP accessible
    [Tags]  VALIDATE-SPP  T-BIRD  C7000
    ${getresp} =   Fusion Api Get Firmware Driver
    Run Keyword If  ${getresp['count']} == 0  Fail  msg=\nSPP ${buildup_spp_name} is not found\n
    :FOR    ${spp_fw}  IN   @{getresp['members']}
    \   ${status} =  Get From Dictionary  ${spp_fw}  status
    \   ${version} =  Get From Dictionary  ${spp_fw}  version
    \   Run Keyword If  '${version}' == '${buildup_spp_version}' and '${status}' != 'OK'  Fail  msg=\nSPP ${buildup_spp_name} is not in OK status\n

SPP Upload
    [Documentation]    Upload SPP bundle to OV
    [Tags]    ADDSPP  C7000  T-BIRD
    Upload Firmware    ${spp_local_paths}   ${TRUE}