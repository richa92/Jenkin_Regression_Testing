*** Settings ***
Documentation                 Delete Base Resources From OneView
Resource    resource.txt
Suite Setup                     QUAL Suite Setup    ${admin_credentials}
Suite Teardown                  QUAL Suite Teardown
*** Test Cases ***

Remove Logical Enclosure from OV
    [Documentation]    Remove LE
    [Tags]    REMOVELE
    Remove All LEs Async

Delete Base Resources Enclosure Groups
    [Documentation]    Remove Enclosure Groups
    [Tags]    TEARDOWN   R-EG
    Remove All Enclosure Groups  ${VERIFY}

Delete Base Resources LIGs
    [Documentation]    Remove LIGs
    [Tags]    TEARDOWN  R-LIG
    Remove All LIGs  ${VERIFY}

Delete Base Resources SASLIGs
    [Documentation]    Remove SASLIGs
    [Tags]    TEARDOWN  R-SASLIG
    Remove All SAS LIGs   ${VERIFY}

Delete Base Resources Network Sets
    [Documentation]    Remove Network Sets
    [Tags]    TEARDOWN  R-NS
    Remove All Networks Sets Async  ${VERIFY}

Delete Base Resources FC Networks
    [Documentation]    Remove FC Networks
    [Tags]    TEARDOWN  R-FC
    Remove All FC Networks Async  ${VERIFY}

Delete Base Resources Ethernet Networks
    [Documentation]    Remove Ethernet Networks
    [Tags]    TEARDOWN  R-ETH
    Remove All Ethernet Networks Async  ${VERIFY}

Delete Base Resources SAN Manager
    [Documentation]    Remove SAN Manager
    [Tags]    TEARDOWN   R-SM
    Remove All San Managers Async  ${VERIFY}

Delete Base Resources Users
    [Documentation]    Remove Users
    [Tags]    TEARDOWN  R-USR
    Remove All Users  ${VERIFY}