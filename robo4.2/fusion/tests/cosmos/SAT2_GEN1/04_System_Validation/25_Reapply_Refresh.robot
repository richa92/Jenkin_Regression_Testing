*** Settings ***
Documentation
...     This Test Suite uses AD Server Group User credentials for Reapply_Refresh Tests.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      SETUP
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup     ${ad_server_credentials}
Suite Teardown                  Regression Test Teardown

*** Test Cases ***
Refresh Enclosure
    [Documentation]  Refresh Enclosure
    [Tags]      REFRESH  T-BIRD  C7000
    ${responses}=  Refresh Enclosures Async   ${refresh_enclosures}
    Run Keyword If  ${responses} is not ${null}   Run Keyword And Continue On Failure    Wait For Task2   ${responses}   timeout=6000    interval=20

Re-Apply Potash LI Coniguration
    [Documentation]  Re- Apply Potash LI Configuration.
    [Tags]   POTASH-LI  T-BIRD
    Reapply Logical Interconnect Configuration By Name    ${potash_li_name}

Re-Apply Carbon LI Coniguration
    [Documentation]  Re- Apply Carbon LI Configuration.
    [Tags]   CARBON-LI  T-BIRD
    Reapply Logical Interconnect Configuration By Name  ${carbon_li_name}

Re-Apply SAS LI Coniguration
    [Documentation]  Re- Apply SAS LI Configuration.This test suite makes sure to removes logical JBODS if found
    [Tags]   SAS-LI  T-BIRD
    Reapply SAS Logical Interconnect Configuration By Name and Verify  ${sas_li_name}
