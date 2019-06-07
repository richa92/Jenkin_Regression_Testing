*** Settings ***
Documentation
...     This Test Suite uses AD Server Group User credentials to Edit Datacenter.
...     Test Data is defined in Python Data Variable file.
Resource                ../resource.txt
Suite Setup             Regression Test Setup     ${ad_server_credentials}
Suite Teardown          Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
...                     AND  Regression Test Teardown

*** Test Cases ***
Edit Datacenters
    [Tags]      SETUP  EDIT-DC  C7000
    [Documentation]   Edit Datacenters
    ${header_resp} =    fusion_api_get_headers
    Set To Dictionary    ${header_resp}   if-Match=*
    Edit Datacenter   ${dc}    headers=${header_resp}

Add Racks
    [Tags]  SETUP   RACKS   T-BIRD
    [Documentation]   Add Racks
    Add Racks from variable     ${racks}

Edit Datacenters Synergy
    [Tags]      SETUP  EDIT-DC  T-BIRD
    [Documentation]   Edit Datacenters
    ${resourceUri} =  Get Rack Uri    ${rack_name}
    Run Keyword If  '${resourceUri}'=='/rest/rack_${rack_name}_not_found'   Fail    Rack with name ${rack_name} not found
    Set To Dictionary   ${dc[0]['contents'][0]}    resourceUri   ${resourceUri}
    ${header_resp} =    fusion_api_get_headers
    Set To Dictionary    ${header_resp}   if-Match=*
    Edit Datacenter   ${dc}    headers=${header_resp}