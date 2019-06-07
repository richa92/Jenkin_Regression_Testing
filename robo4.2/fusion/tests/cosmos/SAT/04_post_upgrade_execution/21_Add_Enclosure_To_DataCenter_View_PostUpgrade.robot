*** Settings ***
Documentation
...     This Test Suite uses AD Server Group User credentials to Edit Datacenter.
...     Test Data is defined in Python Data Variable file.
Resource                ../resource.txt
Suite Setup                     Regression Test Setup     ${ad_server_credentials}
Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
...                             AND  Regression Test Teardown
*** Test Cases ***
Edit Datacenters
    [Tags]      SETUP  EDIT-DC  C7000  4.0  3.10
    [Documentation]   Edit Datacenters post upgrade
    ${header_resp} =    fusion_api_get_headers
    Set To Dictionary    ${header_resp}   if-Match=*
    Edit Datacenter   ${dc_postupgrade}    headers=${header_resp}