*** Settings ***
Documentation
...     This Test Suite uses admin credentials for Ethernet and Storage connectivity check Tests.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      SETUP
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup    ${admin_credentials}
Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
...                             AND  Regression Test Teardown

*** Test Cases ***
ESXi Server Should Be Pinging And Volume Should Be Active
    [Documentation]  ESXi Server Should Be Pinging And Volume Should Be Active
    [Tags]   T-BIRD
    Power On Server Profile And Wait For POST State   ${esxi_os_servers}
    :FOR  ${esxi_os_server}  IN   @{esxi_os_servers}
    \    Run Keyword And Continue On Failure   ESXi Server Should Be Pinging And Volume Should Be Active   ${esxi_os_server}