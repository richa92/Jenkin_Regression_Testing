*** Settings ***
Documentation      OVF2300_C7000\06_OVF2300_p006_factory_reset.robot

Resource             ./resources_ovf2300.txt
Variables            ./Regression_Data.py

Suite Setup         Run Keywords    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}
...                  AND             Switch Security Mode To:  LEGACY
...                  AND             Login By IA User

*** Variables ***
${APPLIANCE_IP}         unknown

*** Test Cases ***
C1:Legacy Mode: Factory Reset With PRESERVE NETWORK
    ${apache_srv_cert_finger_original}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  443
    ${rabbit_srv_cert_finger_original}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  5671
    Factory Reset With PRESERVE NETWORK
    Accept Appliance EULA
    Change Default OV Password
    Login By IA User
    Security Mode Check: Current Mode Is:  LEGACY
    SSH Check For Mode:  LEGACY  ${APPLIANCE_IP}

    ${apache_srv_cert_finger_current}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  443
    ${rabbit_srv_cert_finger_current}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  5671
    Server Certificate Should Not Be Changed  ${apache_srv_cert_finger_original}  ${apache_srv_cert_finger_current}
    Server Certificate Should Not Be Changed  ${rabbit_srv_cert_finger_original}  ${rabbit_srv_cert_finger_current}

C2:Legacy Mode: Factory Reset Without PRESERVE NETWORK
    ${apache_srv_cert_finger_original}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  443
    ${rabbit_srv_cert_finger_original}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  5671

    Factory Reset Without PRESERVE NETWORK
    Accept Appliance EULA
    Change Default OV Password
    Login By IA User
    Configure Appliance Interfaces By DHCP

    Security Mode Check: Current Mode Is:  LEGACY
    SSH Check For Mode:  LEGACY  ${APPLIANCE_IP}
    ${apache_srv_cert_finger_current}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  443
    ${rabbit_srv_cert_finger_current}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  5671
    Server Certificate Should Be Changed  ${apache_srv_cert_finger_original}  ${apache_srv_cert_finger_current}
    Server Certificate Should Be Changed  ${rabbit_srv_cert_finger_original}  ${rabbit_srv_cert_finger_current}

C3:FIPS Mode: Factory Reset With PRESERVE NETWORK
    Switch Security Mode To:  FIPS
    Login By IA User
    Security Mode Check: Current Mode Is:  FIPS

    ${apache_srv_cert_finger_original}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  443
    ${rabbit_srv_cert_finger_original}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  5671
    Factory Reset With PRESERVE NETWORK
    Accept Appliance EULA
    Change Default OV Password
    Login By IA User
    Security Mode Check: Current Mode Is:  FIPS
    SSH Check For Mode:  FIPS  ${APPLIANCE_IP}

    ${apache_srv_cert_finger_current}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  443
    ${rabbit_srv_cert_finger_current}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  5671
    Server Certificate Should Not Be Changed  ${apache_srv_cert_finger_original}  ${apache_srv_cert_finger_current}
    Server Certificate Should Not Be Changed  ${rabbit_srv_cert_finger_original}  ${rabbit_srv_cert_finger_current}

C4:FIPS Mode: Factory Reset Without PRESERVE NETWORK
    Login By IA User
    Security Mode Check: Current Mode Is:  FIPS
    ${apache_srv_cert_finger_original}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  443
    ${rabbit_srv_cert_finger_original}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  5671

    Factory Reset Without PRESERVE NETWORK
    Accept Appliance EULA
    Change Default OV Password
    Login By IA User
    Configure Appliance Interfaces By DHCP

    Security Mode Check: Current Mode Is:  LEGACY
    SSH Check For Mode:  LEGACY  ${APPLIANCE_IP}
    ${apache_srv_cert_finger_current}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  443
    ${rabbit_srv_cert_finger_current}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  5671
    Server Certificate Should Be Changed  ${apache_srv_cert_finger_original}  ${apache_srv_cert_finger_current}
    Server Certificate Should Be Changed  ${rabbit_srv_cert_finger_original}  ${rabbit_srv_cert_finger_current}

C5:CNSA Mode: Factory Reset With PRESERVE NETWORK
    Switch Security Mode To:  CNSA
    Login By IA User
    Security Mode Check: Current Mode Is:  CNSA
    ${apache_srv_cert_finger_original}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  443
    ${rabbit_srv_cert_finger_original}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  5671

    Factory Reset With PRESERVE NETWORK
    Accept Appliance EULA
    Change Default OV Password
    Login By IA User
    Security Mode Check: Current Mode Is:  CNSA
    SSH Check For Mode:  CNSA  ${APPLIANCE_IP}

    ${apache_srv_cert_finger_current}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  443
    ${rabbit_srv_cert_finger_current}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  5671
    Server Certificate Should Not Be Changed  ${apache_srv_cert_finger_original}  ${apache_srv_cert_finger_current}
    Server Certificate Should Not Be Changed  ${rabbit_srv_cert_finger_original}  ${rabbit_srv_cert_finger_current}

C6:CNSA Mode: Factory Reset Without PRESERVE NETWORK
    Login By IA User
    Security Mode Check: Current Mode Is:  CNSA
    ${apache_srv_cert_finger_original}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  443
    ${rabbit_srv_cert_finger_original}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  5671

    Factory Reset Without PRESERVE NETWORK
    Accept Appliance EULA
    Change Default OV Password
    Login By IA User
    Configure Appliance Interfaces By DHCP

    Security Mode Check: Current Mode Is:  LEGACY
    SSH Check For Mode:  LEGACY  ${APPLIANCE_IP}
    ${apache_srv_cert_finger_current}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  443
    ${rabbit_srv_cert_finger_current}=    Show Server Certificate FingerPrint  ${APPLIANCE_IP}  5671
    Server Certificate Should Be Changed  ${apache_srv_cert_finger_original}  ${apache_srv_cert_finger_current}
    Server Certificate Should Be Changed  ${rabbit_srv_cert_finger_original}  ${rabbit_srv_cert_finger_current}