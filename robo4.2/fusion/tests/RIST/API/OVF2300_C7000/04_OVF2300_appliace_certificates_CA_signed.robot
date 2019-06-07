*** Settings ***
Documentation      05_OVF2300_p005_appliace_certificates_CA_signed.robot

Resource             ./resources_ovf2300.txt
Variables            ./Regression_Data.py

Suite Setup         Run Keywords    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}
...                  AND             Import Gobaba Root CA And Intermediate CA
...                  AND             Delete A Compatibility Report And Ignore Error

Suite Teardown      Run Keywords    Switch Security Mode To:  LEGACY
...                  AND             Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}
...                  AND             Delete Gobaba Root CA And Intermediate CA

*** Variables ***
${APPLIANCE_IP}                 unknown

*** Test Cases ***
C1:Change Appliance Certificates CA Signed To Be FIPS Not Compliant And Switch To FIPS
    [Documentation]  switch should be failed
    Change Appliance Certificates To Gobaba CA Signed  FIPS  sha1rsa
    Update Compatibility Report And Check Apache RabbitMQ Servers Are Not Compliant For Mode:  FIPS
    Security Mode Check: Current Mode Is:  LEGACY
    ${apache_srv_cert_finger_original}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  443
    ${rabbit_srv_cert_finger_original}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  5671

    Mode Switch Should Be Failed To Mode:  FIPS
    Security Mode Check: Current Mode Is:  LEGACY
    ${apache_srv_cert_finger_current}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  443
    ${rabbit_srv_cert_finger_current}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  5671
    Server Certificate Should Not Be Changed  ${apache_srv_cert_finger_original}  ${apache_srv_cert_finger_current}
    Server Certificate Should Not Be Changed  ${rabbit_srv_cert_finger_original}  ${rabbit_srv_cert_finger_current}

C2:Change Appliance Certificates CA Signed To Be FIPS Compliant And Switch To FIPS
    [Documentation]  switch to FIPS ok
    Change Appliance Certificates To Gobaba CA Signed  FIPS  sha256rsa
    Update Compatibility Report And Check Apache RabbitMQ Servers Are Compliant For Mode:  FIPS
    Security Mode Check: Current Mode Is:  LEGACY
    ${apache_srv_cert_finger_original}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  443
    ${rabbit_srv_cert_finger_original}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  5671

    Switch Security Mode To:  FIPS
    Login By IA User
    Security Mode Check: Current Mode Is:  FIPS
    ${apache_srv_cert_finger_current}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  443
    ${rabbit_srv_cert_finger_current}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  5671
    Server Certificate Should Not Be Changed  ${apache_srv_cert_finger_original}  ${apache_srv_cert_finger_current}
    Server Certificate Should Not Be Changed  ${rabbit_srv_cert_finger_original}  ${rabbit_srv_cert_finger_current}

C3:Change Appliance Certificates CA Signed To Be CNSA Not Compliant And Switch To CNSA: Signature Algorithm Not Compliant
    [Documentation]  switch to CNSA failed due to signature algorithm
    Switch Security Mode To:  LEGACY
    Login By IA User
    Change Appliance Certificates To Gobaba CA Signed  CNSA  sha256rsa
    Update Compatibility Report And Check Apache RabbitMQ Servers Are Not Compliant For Mode:  CNSA
    Security Mode Check: Current Mode Is:  LEGACY
    ${apache_srv_cert_finger_original}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  443
    ${rabbit_srv_cert_finger_original}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  5671

    Mode Switch Should Be Failed To Mode:  CNSA
    Security Mode Check: Current Mode Is:  LEGACY
    ${apache_srv_cert_finger_current}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  443
    ${rabbit_srv_cert_finger_current}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  5671
    Server Certificate Should Not Be Changed  ${apache_srv_cert_finger_original}  ${apache_srv_cert_finger_current}
    Server Certificate Should Not Be Changed  ${rabbit_srv_cert_finger_original}  ${rabbit_srv_cert_finger_current}

C4:Change Appliance Certificates CA Signed To Be CNSA Not Compliant And Switch To CNSA: Key Length Not Compliant
    [Documentation]  switch to CNSA failed due to public key length
    Switch Security Mode To:  LEGACY
    Change Appliance Certificates To Gobaba CA Signed  FIPS  sha384rsa
    Update Compatibility Report And Check Apache RabbitMQ Servers Are Not Compliant For Mode:  CNSA
    Security Mode Check: Current Mode Is:  LEGACY
    ${apache_srv_cert_finger_original}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  443
    ${rabbit_srv_cert_finger_original}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  5671

    Mode Switch Should Be Failed To Mode:  CNSA
    Security Mode Check: Current Mode Is:  LEGACY
    ${apache_srv_cert_finger_current}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  443
    ${rabbit_srv_cert_finger_current}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  5671
    Server Certificate Should Not Be Changed  ${apache_srv_cert_finger_original}  ${apache_srv_cert_finger_current}
    Server Certificate Should Not Be Changed  ${rabbit_srv_cert_finger_original}  ${rabbit_srv_cert_finger_current}

C5:Change Appliance Certificates CA Signed To Be CNSA Compliant And Switch To CNSA
    [Documentation]  switch to CNSA OK
    Switch Security Mode To:  LEGACY
    Change Appliance Certificates To Gobaba CA Signed  CNSA  sha384rsa
    Update Compatibility Report And Check Apache RabbitMQ Servers Are Compliant For Mode:  CNSA
    Security Mode Check: Current Mode Is:  LEGACY
    ${apache_srv_cert_finger_original}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  443
    ${rabbit_srv_cert_finger_original}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  5671

    Switch Security Mode To:  CNSA
    Login By IA User
    Security Mode Check: Current Mode Is:  CNSA
    ${apache_srv_cert_finger_current}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  443
    ${rabbit_srv_cert_finger_current}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  5671
    Server Certificate Should Not Be Changed  ${apache_srv_cert_finger_original}  ${apache_srv_cert_finger_current}
    Server Certificate Should Not Be Changed  ${rabbit_srv_cert_finger_original}  ${rabbit_srv_cert_finger_current}
