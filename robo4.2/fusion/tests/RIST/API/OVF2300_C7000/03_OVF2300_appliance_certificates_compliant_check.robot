*** Settings ***
Documentation      04_OVF2300_p004_appliance_certificates_compliant_check.robot

Resource             ./resources_ovf2300.txt
Variables            ./Regression_Data.py

Suite Setup         Login By IA User

*** Variables ***
${APPLIANCE_IP}         unknown

*** Test Cases ***
C1:Switch From LEGACY To FIPS And Check Appliance Certficates
    [Documentation]  this will validate: apache/ rabbitmq server/ rabbitmq client / internal CA
    ...                 1. apache will validate the certificate and SSL connection
    ...                 2. rabbitmq server/client and internal CA will validate only its certificate
    ...                 3. certificates of apache and rabbitmq server will be receieved by openssl
    ...                 4. certificates of rabbitmq client and internal CA will be received by API
    Security Mode Check: Current Mode Is:  LEGACY
    ${apache_server_cert}=      Get SSL Server Certificate  ${APPLIANCE_IP}  443
    ${rabbit_server_cert}=      Get SSL Server Certificate  ${APPLIANCE_IP}  5671
    ${rabbit_client_cert}=      Get Rabbitmq Client Certificate
    ${internal_ca_cert}=        Get Internal CA Certificate
    ${apache_srv_cert_finger_original}=         Show Certificate FingerPrint  ${apache_server_cert}
    ${rabbit_server_cert_finger_original}=      Show Certificate FingerPrint  ${rabbit_server_cert}
    ${rabbit_client_cert_finger_original}=      Show Certificate FingerPrint  ${rabbit_client_cert}
    ${internal_ca_finger_original}=             Show Certificate FingerPrint  ${internal_ca_cert}
    ${is_compliance_apache}=            Compliance Validator: Validate Apache Server Of Appliance For Mode:  FIPS
    ${is_compliance_rabbit_server}=     Compliance Validator: Validate Certificate For Mode:  FIPS  ${rabbit_server_cert}
    ${is_compliance_rabbit_client}=     Compliance Validator: Validate Certificate For Mode:  FIPS  ${rabbit_client_cert}
    ${is_compliance_internal_ca}=       Compliance Validator: Validate Certificate For Mode:  FIPS  ${internal_ca_cert}

    Switch Security Mode To:  FIPS
    Login By IA User
    Security Mode Check: Current Mode Is:  FIPS

    ${apache_server_cert}=      Get SSL Server Certificate  ${APPLIANCE_IP}  443
    ${rabbit_server_cert}=      Get SSL Server Certificate  ${APPLIANCE_IP}  5671
    ${rabbit_client_cert}=      Get Rabbitmq Client Certificate
    ${internal_ca_cert}=        Get Internal CA Certificate
    Check Current Apache Server Certificate Is Compliant After Mode Switch To:  FIPS  ${apache_srv_cert_finger_original}  ${is_compliance_apache}
    Check Current RabbitMQ Server Certificate Is Compliant After Mode Switch To:  FIPS  ${rabbit_server_cert_finger_original}  ${is_compliance_rabbit_server}  ${rabbit_server_cert}
    Check Current RabbitMQ Client Certificate Is Compliant After Mode Switch To:  FIPS  ${rabbit_client_cert_finger_original}  ${is_compliance_rabbit_client}  ${rabbit_client_cert}
    Check Current Internal CA Is Compliant After Mode Switch To:  FIPS  ${internal_ca_finger_original}  ${is_compliance_internal_ca}  ${internal_ca_cert}

C2:Switch From FIPS To CNSA And Check Appliance Certficates
    [Documentation]  this will validate: apache/ rabbitmq server/ rabbitmq client / internal CA
    ...                 1. apache will validate the certificate and SSL connection
    ...                 2. rabbitmq server/client and internal CA will validate only its certificate
    ...                 3. certificates of apache and rabbitmq server will be receieved by openssl
    ...                 4. certificates of rabbitmq client and internal CA will be received by API
    Security Mode Check: Current Mode Is:  FIPS
    ${apache_server_cert}=      Get SSL Server Certificate  ${APPLIANCE_IP}  443
    ${rabbit_server_cert}=      Get SSL Server Certificate  ${APPLIANCE_IP}  5671
    ${rabbit_client_cert}=      Get Rabbitmq Client Certificate
    ${internal_ca_cert}=        Get Internal CA Certificate
    ${apache_srv_cert_finger_original}=         Show Certificate FingerPrint  ${apache_server_cert}
    ${rabbit_server_cert_finger_original}=      Show Certificate FingerPrint  ${rabbit_server_cert}
    ${rabbit_client_cert_finger_original}=      Show Certificate FingerPrint  ${rabbit_client_cert}
    ${internal_ca_finger_original}=             Show Certificate FingerPrint  ${internal_ca_cert}
    ${is_compliance_apache}=            Compliance Validator: Validate Apache Server Of Appliance For Mode:  CNSA
    ${is_compliance_rabbit_server}=     Compliance Validator: Validate Certificate For Mode:  CNSA  ${rabbit_server_cert}
    ${is_compliance_rabbit_client}=     Compliance Validator: Validate Certificate For Mode:  CNSA  ${rabbit_client_cert}
    ${is_compliance_internal_ca}=       Compliance Validator: Validate Certificate For Mode:  CNSA  ${internal_ca_cert}

    Switch Security Mode To:  CNSA
    Login By IA User
    Security Mode Check: Current Mode Is:  CNSA

    ${apache_server_cert}=      Get SSL Server Certificate  ${APPLIANCE_IP}  443
    ${rabbit_server_cert}=      Get SSL Server Certificate  ${APPLIANCE_IP}  5671
    ${rabbit_client_cert}=      Get Rabbitmq Client Certificate
    ${internal_ca_cert}=        Get Internal CA Certificate
    Check Current Apache Server Certificate Is Compliant After Mode Switch To:  CNSA  ${apache_srv_cert_finger_original}  ${is_compliance_apache}
    Check Current RabbitMQ Server Certificate Is Compliant After Mode Switch To:  CNSA  ${rabbit_server_cert_finger_original}  ${is_compliance_rabbit_server}  ${rabbit_server_cert}
    Check Current RabbitMQ Client Certificate Is Compliant After Mode Switch To:  CNSA  ${rabbit_client_cert_finger_original}  ${is_compliance_rabbit_client}  ${rabbit_client_cert}
    Check Current Internal CA Is Compliant After Mode Switch To:  CNSA  ${internal_ca_finger_original}  ${is_compliance_internal_ca}  ${internal_ca_cert}

C3:Switch From CNSA To LEGACY And Check Appliance Certficates
    [Documentation]  this will validate: apache/ rabbitmq server/ rabbitmq client / internal CA
    ...                 1. apache will validate the certificate and SSL connection
    ...                 2. rabbitmq server/client and internal CA will validate only its certificate
    ...                 3. certificates of apache and rabbitmq server will be receieved by openssl
    ...                 4. certificates of rabbitmq client and internal CA will be received by API
    Security Mode Check: Current Mode Is:  CNSA
    ${apache_server_cert}=      Get SSL Server Certificate  ${APPLIANCE_IP}  443
    ${rabbit_server_cert}=      Get SSL Server Certificate  ${APPLIANCE_IP}  5671
    ${rabbit_client_cert}=      Get Rabbitmq Client Certificate
    ${internal_ca_cert}=        Get Internal CA Certificate
    ${apache_srv_cert_finger_original}=         Show Certificate FingerPrint  ${apache_server_cert}
    ${rabbit_server_cert_finger_original}=      Show Certificate FingerPrint  ${rabbit_server_cert}
    ${rabbit_client_cert_finger_original}=      Show Certificate FingerPrint  ${rabbit_client_cert}
    ${internal_ca_finger_original}=             Show Certificate FingerPrint  ${internal_ca_cert}
    ${is_compliance_apache}=            Compliance Validator: Validate Apache Server Of Appliance For Mode:  LEGACY
    ${is_compliance_rabbit_server}=     Compliance Validator: Validate Certificate For Mode:  LEGACY  ${rabbit_server_cert}
    ${is_compliance_rabbit_client}=     Compliance Validator: Validate Certificate For Mode:  LEGACY  ${rabbit_client_cert}
    ${is_compliance_internal_ca}=       Compliance Validator: Validate Certificate For Mode:  LEGACY  ${internal_ca_cert}

    Switch Security Mode To:  LEGACY
    Login By IA User
    Security Mode Check: Current Mode Is:  LEGACY

    ${apache_server_cert}=      Get SSL Server Certificate  ${APPLIANCE_IP}  443
    ${rabbit_server_cert}=      Get SSL Server Certificate  ${APPLIANCE_IP}  5671
    ${rabbit_client_cert}=      Get Rabbitmq Client Certificate
    ${internal_ca_cert}=        Get Internal CA Certificate
    Check Current Apache Server Certificate Is Compliant After Mode Switch To:  LEGACY  ${apache_srv_cert_finger_original}  ${is_compliance_apache}
    Check Current RabbitMQ Server Certificate Is Compliant After Mode Switch To:  LEGACY  ${rabbit_server_cert_finger_original}  ${is_compliance_rabbit_server}  ${rabbit_server_cert}
    Check Current RabbitMQ Client Certificate Is Compliant After Mode Switch To:  LEGACY  ${rabbit_client_cert_finger_original}  ${is_compliance_rabbit_client}  ${rabbit_client_cert}
    Check Current Internal CA Is Compliant After Mode Switch To:  LEGACY  ${internal_ca_finger_original}  ${is_compliance_internal_ca}  ${internal_ca_cert}

C4:Switch From LEGACY To CNSA And Check Appliance Certficates
    [Documentation]  this will validate: apache/ rabbitmq server/ rabbitmq client / internal CA
    ...                 1. apache will validate the certificate and SSL connection
    ...                 2. rabbitmq server/client and internal CA will validate only its certificate
    ...                 3. certificates of apache and rabbitmq server will be receieved by openssl
    ...                 4. certificates of rabbitmq client and internal CA will be received by API
    Security Mode Check: Current Mode Is:  LEGACY
    ${apache_server_cert}=      Get SSL Server Certificate  ${APPLIANCE_IP}  443
    ${rabbit_server_cert}=      Get SSL Server Certificate  ${APPLIANCE_IP}  5671
    ${rabbit_client_cert}=      Get Rabbitmq Client Certificate
    ${internal_ca_cert}=        Get Internal CA Certificate
    ${apache_srv_cert_finger_original}=         Show Certificate FingerPrint  ${apache_server_cert}
    ${rabbit_server_cert_finger_original}=      Show Certificate FingerPrint  ${rabbit_server_cert}
    ${rabbit_client_cert_finger_original}=      Show Certificate FingerPrint  ${rabbit_client_cert}
    ${internal_ca_finger_original}=             Show Certificate FingerPrint  ${internal_ca_cert}
    ${is_compliance_apache}=            Compliance Validator: Validate Apache Server Of Appliance For Mode:  CNSA
    ${is_compliance_rabbit_server}=     Compliance Validator: Validate Certificate For Mode:  CNSA  ${rabbit_server_cert}
    ${is_compliance_rabbit_client}=     Compliance Validator: Validate Certificate For Mode:  CNSA  ${rabbit_client_cert}
    ${is_compliance_internal_ca}=       Compliance Validator: Validate Certificate For Mode:  CNSA  ${internal_ca_cert}

    Switch Security Mode To:  CNSA
    Login By IA User
    Security Mode Check: Current Mode Is:  CNSA

    ${apache_server_cert}=      Get SSL Server Certificate  ${APPLIANCE_IP}  443
    ${rabbit_server_cert}=      Get SSL Server Certificate  ${APPLIANCE_IP}  5671
    ${rabbit_client_cert}=      Get Rabbitmq Client Certificate
    ${internal_ca_cert}=        Get Internal CA Certificate
    Check Current Apache Server Certificate Is Compliant After Mode Switch To:  CNSA  ${apache_srv_cert_finger_original}  ${is_compliance_apache}
    Check Current RabbitMQ Server Certificate Is Compliant After Mode Switch To:  CNSA  ${rabbit_server_cert_finger_original}  ${is_compliance_rabbit_server}  ${rabbit_server_cert}
    Check Current RabbitMQ Client Certificate Is Compliant After Mode Switch To:  CNSA  ${rabbit_client_cert_finger_original}  ${is_compliance_rabbit_client}  ${rabbit_client_cert}
    Check Current Internal CA Is Compliant After Mode Switch To:  CNSA  ${internal_ca_finger_original}  ${is_compliance_internal_ca}  ${internal_ca_cert}

C5:Switch From CNSA To FIPS And Check Appliance Certficates
    [Documentation]  this will validate: apache/ rabbitmq server/ rabbitmq client / internal CA
    ...                 1. apache will validate the certificate and SSL connection
    ...                 2. rabbitmq server/client and internal CA will validate only its certificate
    ...                 3. certificates of apache and rabbitmq server will be receieved by openssl
    ...                 4. certificates of rabbitmq client and internal CA will be received by API
    Security Mode Check: Current Mode Is:  CNSA
    ${apache_server_cert}=      Get SSL Server Certificate  ${APPLIANCE_IP}  443
    ${rabbit_server_cert}=      Get SSL Server Certificate  ${APPLIANCE_IP}  5671
    ${rabbit_client_cert}=      Get Rabbitmq Client Certificate
    ${internal_ca_cert}=        Get Internal CA Certificate
    ${apache_srv_cert_finger_original}=         Show Certificate FingerPrint  ${apache_server_cert}
    ${rabbit_server_cert_finger_original}=      Show Certificate FingerPrint  ${rabbit_server_cert}
    ${rabbit_client_cert_finger_original}=      Show Certificate FingerPrint  ${rabbit_client_cert}
    ${internal_ca_finger_original}=             Show Certificate FingerPrint  ${internal_ca_cert}
    ${is_compliance_apache}=            Compliance Validator: Validate Apache Server Of Appliance For Mode:  FIPS
    ${is_compliance_rabbit_server}=     Compliance Validator: Validate Certificate For Mode:  FIPS  ${rabbit_server_cert}
    ${is_compliance_rabbit_client}=     Compliance Validator: Validate Certificate For Mode:  FIPS  ${rabbit_client_cert}
    ${is_compliance_internal_ca}=       Compliance Validator: Validate Certificate For Mode:  FIPS  ${internal_ca_cert}

    Switch Security Mode To:  FIPS
    Login By IA User
    Security Mode Check: Current Mode Is:  FIPS

    ${apache_server_cert}=      Get SSL Server Certificate  ${APPLIANCE_IP}  443
    ${rabbit_server_cert}=      Get SSL Server Certificate  ${APPLIANCE_IP}  5671
    ${rabbit_client_cert}=      Get Rabbitmq Client Certificate
    ${internal_ca_cert}=        Get Internal CA Certificate
    Check Current Apache Server Certificate Is Compliant After Mode Switch To:  FIPS  ${apache_srv_cert_finger_original}  ${is_compliance_apache}
    Check Current RabbitMQ Server Certificate Is Compliant After Mode Switch To:  FIPS  ${rabbit_server_cert_finger_original}  ${is_compliance_rabbit_server}  ${rabbit_server_cert}
    Check Current RabbitMQ Client Certificate Is Compliant After Mode Switch To:  FIPS  ${rabbit_client_cert_finger_original}  ${is_compliance_rabbit_client}  ${rabbit_client_cert}
    Check Current Internal CA Is Compliant After Mode Switch To:  FIPS  ${internal_ca_finger_original}  ${is_compliance_internal_ca}  ${internal_ca_cert}

C6:Switch From FIPS To LEGACY And Check Appliance Certficates
    [Documentation]  this will validate: apache/ rabbitmq server/ rabbitmq client / internal CA
    ...                 1. apache will validate the certificate and SSL connection
    ...                 2. rabbitmq server/client and internal CA will validate only its certificate
    ...                 3. certificates of apache and rabbitmq server will be receieved by openssl
    ...                 4. certificates of rabbitmq client and internal CA will be received by API
    Security Mode Check: Current Mode Is:  FIPS
    ${apache_server_cert}=      Get SSL Server Certificate  ${APPLIANCE_IP}  443
    ${rabbit_server_cert}=      Get SSL Server Certificate  ${APPLIANCE_IP}  5671
    ${rabbit_client_cert}=      Get Rabbitmq Client Certificate
    ${internal_ca_cert}=        Get Internal CA Certificate
    ${apache_srv_cert_finger_original}=         Show Certificate FingerPrint  ${apache_server_cert}
    ${rabbit_server_cert_finger_original}=      Show Certificate FingerPrint  ${rabbit_server_cert}
    ${rabbit_client_cert_finger_original}=      Show Certificate FingerPrint  ${rabbit_client_cert}
    ${internal_ca_finger_original}=             Show Certificate FingerPrint  ${internal_ca_cert}
    ${is_compliance_apache}=            Compliance Validator: Validate Apache Server Of Appliance For Mode:  LEGACY
    ${is_compliance_rabbit_server}=     Compliance Validator: Validate Certificate For Mode:  LEGACY  ${rabbit_server_cert}
    ${is_compliance_rabbit_client}=     Compliance Validator: Validate Certificate For Mode:  LEGACY  ${rabbit_client_cert}
    ${is_compliance_internal_ca}=       Compliance Validator: Validate Certificate For Mode:  LEGACY  ${internal_ca_cert}

    Switch Security Mode To:  LEGACY
    Login By IA User
    Security Mode Check: Current Mode Is:  LEGACY

    ${apache_server_cert}=      Get SSL Server Certificate  ${APPLIANCE_IP}  443
    ${rabbit_server_cert}=      Get SSL Server Certificate  ${APPLIANCE_IP}  5671
    ${rabbit_client_cert}=      Get Rabbitmq Client Certificate
    ${internal_ca_cert}=        Get Internal CA Certificate
    Check Current Apache Server Certificate Is Compliant After Mode Switch To:  LEGACY  ${apache_srv_cert_finger_original}  ${is_compliance_apache}
    Check Current RabbitMQ Server Certificate Is Compliant After Mode Switch To:  LEGACY  ${rabbit_server_cert_finger_original}  ${is_compliance_rabbit_server}  ${rabbit_server_cert}
    Check Current RabbitMQ Client Certificate Is Compliant After Mode Switch To:  LEGACY  ${rabbit_client_cert_finger_original}  ${is_compliance_rabbit_client}  ${rabbit_client_cert}
    Check Current Internal CA Is Compliant After Mode Switch To:  LEGACY  ${internal_ca_finger_original}  ${is_compliance_internal_ca}  ${internal_ca_cert}
