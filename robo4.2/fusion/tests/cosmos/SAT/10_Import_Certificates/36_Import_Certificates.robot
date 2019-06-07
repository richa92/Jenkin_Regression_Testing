*** Settings ***
Documentation    Import CA Signed Leaf And Chain Certificate
...     TAGS:                   EXECUTION
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup     ${admin_credentials}
Suite Teardown                  Regression Test Teardown
Library                         OperatingSystem

*** Test Cases ***
Import CA Signed Leaf Certificate
    [Tags]    CERT   C7000-ImportCertificate
    [Documentation]     Import Leaf Certificate
    ${body} =  Generate Certificate Payload   ${ca_remote_server}   ${certificate}
    ${resp} =  Fusion Api Import Server Certificate    ${body}
    Run Keyword If  ${resp['status_code']}==200  Log  Successful Import Leaf Certificate  console=True
    ...    ELSE IF  ${resp['status_code']}==202  Wait For Task2  ${resp}     50    5
    ...    ELSE     Fail  msg=Failed to Import Leaf Certificate

Import CA Signed Chain Certificate
    [Tags]    CERT   C7000-ImportCertificate    4.0    3.10
    [Documentation]     Import Chain Certificate
    ${body} =  Generate Certificate Chain Payload   ${ca_remote_server}   ${certificate_chain}  ${root_certificate}
    ${resp} =  Fusion Api Import Server Certificate    ${body}
    Run Keyword If  ${resp['status_code']}==200  Log  Successful Import Chain Certificate  console=True
    ...    ELSE IF  ${resp['status_code']}==202  Wait For Task2  ${resp}     50    5
    ...    ELSE     Fail  msg=Failed to Import Chain Certificate