*** Settings ***
Documentation
...     This Test Suite uses Administrator credentials for  SPP Upload Test.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      SETUP
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup     ${admin_credentials}
Suite Teardown                  Regression Test Teardown

*** Test Cases ***
Download SPP Bundle
    [Tags]  DOWNLOAD-SPP  T-BIRD  C7000
    [Documentation]        Download SPP bundle
    Log    ${WEB_URL_SPP}   console=True
    Download Specified SPP to Local Path   ${WEB_URL_SPP}    ${WEB_USERNAME_SPP}   ${WEB_PASSWORD_SPP}

SPP Upload
    [Documentation]    Upload SPP bundle to OV
    [Tags]    ADDSPP    T-BIRD  C7000
    :FOR    ${spp_local_path}   IN    @{buildup_spp_local_paths}
    \   Upload Firmware Bundle Async    ${spp_local_path}   ${TRUE}