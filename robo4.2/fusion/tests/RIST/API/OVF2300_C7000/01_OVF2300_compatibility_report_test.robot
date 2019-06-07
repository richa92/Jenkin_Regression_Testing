*** Settings ***
Documentation       01_OVF2300_p001_compatibility_report_test.robot

Resource             ./resources_ovf2300.txt
Variables            ./Regression_Data.py

Suite Setup         Run Keywords    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}
...                  AND             Generate Default RabbitMQ Client Certificate
...                  AND             Delete A Compatibility Report And Ignore Error

Test Teardown      Delete A Compatibility Report

*** Variables ***
${APPLIANCE_IP}         unknown

*** Test Cases ***
C1:Create A FIPS Compatibility Report And Do The Check Point
    Create Compatibility Report:  FIPS
    ${report_response}=    Get A Compatibility Report
    Check Compatibility Report: Report Is For Mode:  FIPS  ${report_response}
    Check Compatibility Report: Compliant Item:  WEBSERVER CERTIFICATE  ${report_response}
    Check Compatibility Report: Compliant Item:  RABBITMQ SERVER CERTIFICATE  ${report_response}
    Check Compatibility Report: Compliant Item:  RABBITMQ CLIENT CERTIFICATE  ${report_response}

C2:Update A FIPS Compatibility Report And Do The Check Point
    Create Compatibility Report:  FIPS
    Update Compatibility Report:  FIPS
    ${report_response}=    Get A Compatibility Report
    Check Compatibility Report: Report Is For Mode:  FIPS  ${report_response}
    Check Compatibility Report: Compliant Item:  WEBSERVER CERTIFICATE  ${report_response}
    Check Compatibility Report: Compliant Item:  RABBITMQ SERVER CERTIFICATE  ${report_response}
    Check Compatibility Report: Compliant Item:  RABBITMQ CLIENT CERTIFICATE  ${report_response}

C3:Create A CNSA Compatibility Report And Do The Check Point
    Create Compatibility Report:  CNSA
    ${report_response}=    Get A Compatibility Report
    Check Compatibility Report: Report Is For Mode:  CNSA  ${report_response}
    Check Compatibility Report: Not Compliant Item:  WEBSERVER CERTIFICATE  ${report_response}  ${expected_WEBSERVER_CERTIFICATE_nonCompatibilityDetails}
    Check Compatibility Report: Not Compliant Item:  RABBITMQ SERVER CERTIFICATE  ${report_response}  ${expected_RABBITMQ_SERVER_CERTIFICATE_nonCompatibilityDetails}
    Check Compatibility Report: Not Compliant Item:  RABBITMQ CLIENT CERTIFICATE  ${report_response}  ${expected_RABBITMQ_CLIENT_CERTIFICATE_nonCompatibilityDetails}

C4:Update A CNSA Compatibility Report And Do The Check Point
    Create Compatibility Report:  CNSA
    Update Compatibility Report:  CNSA
    ${report_response}=    Get A Compatibility Report
    Check Compatibility Report: Report Is For Mode:  CNSA  ${report_response}
    Check Compatibility Report: Not Compliant Item:  WEBSERVER CERTIFICATE  ${report_response}  ${expected_WEBSERVER_CERTIFICATE_nonCompatibilityDetails}
    Check Compatibility Report: Not Compliant Item:  RABBITMQ SERVER CERTIFICATE  ${report_response}  ${expected_RABBITMQ_SERVER_CERTIFICATE_nonCompatibilityDetails}
    Check Compatibility Report: Not Compliant Item:  RABBITMQ CLIENT CERTIFICATE  ${report_response}  ${expected_RABBITMQ_CLIENT_CERTIFICATE_nonCompatibilityDetails}

C5:Create A FIPS Compatibility Report And Fetch Metadata of the Non-Compatibility Report And Check
    Create Compatibility Report:  FIPS
    ${report_response}=    Fetch Metadata Of The Non-Compatibility Report
    Check Compatibility Report: Report Is For Mode:  FIPS  ${report_response}
    Check Compatibility Report: Total Count Is Correct  ${report_response}  0

C6:Create A CNSA Compatibility Report And Fetch Metadata of the Non-Compatibility Report And Check
    Create Compatibility Report:  CNSA
    ${report_response}=    Fetch Metadata Of The Non-Compatibility Report
    Check Compatibility Report: Report Is For Mode:  CNSA  ${report_response}
    Check Compatibility Report: Total Count Is Correct  ${report_response}  0
