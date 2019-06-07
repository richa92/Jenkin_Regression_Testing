*** Settings ***
Resource          ../resource.txt
Suite Setup       Fusion Api Login Appliance  ${appliance_ip}  ${credentials}
Suite Teardown    Fusion Api Logout Appliance
Force Tags        TBIRD  C7000

*** Test Cases ***
Delete ENCLOSURES
    [Tags]  TEARDOWN  R-ENC  C7000
    [Documentation]   Remove Enclosures
    Remove All Enclosures async  ${VERIFY}

Delete DL SERVERS
    [Tags]  TEARDOWN  R-RS  C7000
    Remove All DL Server Hardware Async  ${VERIFY}  404  (?i)DL360 Gen9|DL360p Gen8|DL380p Gen8|DL380e Gen8|DL360 Gen9

Delete Logical Enclosure
    [Tags]  TEARDOWN  R-LE  TBIRD
    Remove All LEs Async

Delete Enclosure Groups
    [Tags]  TEARDOWN  R-EG  C7000  TBIRD
    Remove All Enclosure Groups  ${VERIFY}

Delete LIGs
    [Tags]  TEARDOWN  R-LIG  C7000  TBIRD
    Remove All LIGs  ${VERIFY}

Delete SASLIGs
    [Tags]  TEARDOWN  R-SAS-LIG  TBIRD
    Remove All SAS LIGs  ${VERIFY}

Delete Network Sets
    [Tags]  TEARDOWN  R-NS  C7000  TBIRD
    Remove All Networks Sets Async  ${VERIFY}

Delete FC Networks
    [Tags]  TEARDOWN  R-FC  C7000  TBIRD
    Remove All FC Networks Async  ${VERIFY}

Delete Ethernet Networks
    [Tags]  TEARDOWN  R-ETH  C7000  TBIRD
    Remove All Ethernet Networks Async  ${VERIFY}

Delete SAN Manager
    [Tags]  TEARDOWN  R-SM  C7000  TBIRD
    Remove All San Managers Async  ${VERIFY}

Delete Users
    [Tags]  TEARDOWN  R-USR  C7000  TBIRD
    Remove All Users  ${VERIFY}
