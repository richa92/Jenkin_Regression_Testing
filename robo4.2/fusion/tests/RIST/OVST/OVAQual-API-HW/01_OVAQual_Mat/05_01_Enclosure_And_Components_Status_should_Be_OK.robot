*** Settings ***
Documentation    Tests to verify status of Enclosures, Servers
...              Interconnects, Fan and Power Supply.
Resource                        ../resource.txt
Suite Setup                     QUAL Suite Setup    ${admin_credentials}
Suite Teardown                  QUAL Suite Teardown
Test Teardown                   Pause And Send EMail on Failure

*** Test Cases ***
All Enclosure Status Should Be OK or Warning
    [Documentation]  Verify status of all Enclosures
    ...  Verify status of all Interconnects
    ...  Verify status of all SAS Interconnects
    ...  Verify status of all Servers
    ...  Verify status of all Fan
    ...  Verify status of all PS
    [Tags]      ENCS-STATUS
    All Enclosures Status Should Be OK or Warning
    All Interconnects Status Should Be OK or Warning
    All Servers Status Should Be OK or Warning
    All Fan Status Should Be OK or Warning
    All Power Supply Status Should Be OK or Warning