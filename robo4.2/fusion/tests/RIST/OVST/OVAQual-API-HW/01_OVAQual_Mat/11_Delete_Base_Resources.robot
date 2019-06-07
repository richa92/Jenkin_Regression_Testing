*** Settings ***
Documentation    Delete Base Resources
Resource                           ../resource.txt
Suite Setup                     QUAL Suite Setup    ${admin_credentials}
Suite Teardown                  QUAL Suite Teardown
Test Teardown                   Pause And Send EMail on Failure
*** Test Cases ***

Delete Base Resources ENCLOSURES
    [Documentation]    Remove Enclosures
    [Tags]    TEARDOWN  R-ENC
    Remove All Enclosures async  ${VERIFY}  timeout=720
    Log All Warning and Critical Alerts

Delete Base Resources DL SERVERS
    [Documentation]    Delete Base Resources DL SERVERS
    [Tags]    TEARDOWN  R-RS
    Remove All DL Server Hardware Async  ${VERIFY}  404  (?i)DL360 Gen9|DL360p Gen8|DL380p Gen8|DL380e Gen8|DL360 Gen9

Delete Base Resources Enclosure Groups
    [Documentation]    Delete Base Resources Enclosure Groups
    [Tags]    TEARDOWN   R-EG
    Remove All Enclosure Groups  ${VERIFY}

Delete Base Resources LIGs
    [Documentation]    Delete Base Resources LIGs
    [Tags]    TEARDOWN  R-LIG
    Remove All LIGs  ${VERIFY}

Delete Base Resources Network Sets
    [Documentation]    Delete Base Resources Network Sets
    [Tags]    TEARDOWN  R-NS
    Remove All Networks Sets Async  ${VERIFY}

Delete Base Resources FC Networks
    [Documentation]    Delete Base Resources FC Networks
    [Tags]    TEARDOWN  R-FC
    Remove All FC Networks Async  ${VERIFY}

Delete Base Resources Ethernet Networks
    [Documentation]    Delete Base Resources Ethernet Networks
    [Tags]    TEARDOWN  R-ETH
    Remove All Ethernet Networks Async  ${VERIFY}

Delete Base Resources SAN Manager
    [Documentation]    Delete Base Resources SAN Manager
    [Tags]    TEARDOWN   R-SM
    Remove All San Managers Async  ${VERIFY}

Delete Base Resources Users
    [Documentation]    Delete Base Resources Users
    [Tags]    TEARDOWN  R-USR
    Remove All Users  ${VERIFY}
