*** Settings ***
Documentation
...     This Test Suite uses Administrator credentials for Add San Manager, User, Networks, Network Sets, LIG and EG Tests.
...     These Setup Tests are prerequisite for other EPIC MAT Test Suites.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      SETUP
Resource                        ./resource.txt
Suite Setup                     MAT Suite Setup     ${admin_credentials}
Suite Teardown                  MAT Suite Teardown

*** Test Cases ***

Add San Manager Async
    [Tags]    SETUP  ADD-SM
    ${responses}=  Add San Managers Async  ${san_managers}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=120    interval=5
    Verify Resources for List  ${expected_san_managers}

Add User Async
    [Tags]    SETUP  ADD-USER
    ${responses}=  Add Users from variable  ${users}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Verify Users    ${expected_users}

Add Ethernet Networks Async
    [Tags]    SETUP  ADD-ENW
    Run Keyword If    ${ethernet_networks} is not ${null}      Add Ethernet Networks from variable async  ${ethernet_networks}  ${VERIFY}  ${expected_ethernet_networks}

Add FC Networks Async
    [Tags]    SETUP  ADD-FC
    ${responses} =    Run Keyword If    ${fc_networks} is not ${null}    Add Non Existing FC Networks  ${fc_networks}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Verify Resources for List  ${expected_fc_networks}

Add FCOE Networks
    [Tags]    SETUP  ADD-FCOE
    Run Keyword If  ${fcoe_networks} is not ${null}    Add FCoE Networks from variable async    ${fcoe_networks}    ${VERIFY}   ${expected_fcoe_networks}

Add Network Sets Async
    [Tags]    SETUP  ADD-NS
    Run Keyword If  ${network_sets} is not ${null}    Add Networks Sets from variable async    ${network_sets}  ${VERIFY}  ${expected_network_sets}

ADD LIGs
    [Tags]    SETUP  ADD-LIG
    Run Keyword If    ${ligs} is not ${null}   Add LIG   ${ligs}
    Verify Resources for List  ${expected_lig}

ADD EG
    [Tags]    SETUP  ADD-EG
    Run Keyword If  ${enc_groups} is not ${null}    Add Enclosure Group from variable sync    ${enc_groups}  ${VERIFY}  ${expected_enc_groups}
