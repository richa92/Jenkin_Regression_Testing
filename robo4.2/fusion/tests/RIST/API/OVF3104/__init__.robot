*** Settings ***
Library        FusionLibrary
Library        RoboGalaxyLibrary
Library        OperatingSystem
Library        Process
Library        SSHLibrary
Library        String
Library        Dialogs
Library        BuiltIn
Library        json
Library        Collections
Resource       ./../../../../Resources/api/fusion_api_resource.txt
Resource       ./keywords.txt
Variables      ${DATA_FILE}


Suite Setup  Setup EVN Before Test
Suite Teardown  Clear EVN

*** Variables ***
${APPLIANCE_IP}        ${None}    #leave it as ${None} if you want this test to create a new one
${Team_Name}        SHQA


*** Keywords ***
Setup EVN Before test
    [Documentation]    Setup environment before F3104 test
    Set Log Level    TRACE
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}

    Log    \n-Add CA certs for AD server to OV    console=yes
    ${add_rootCAcert} =  Fusion Api Import External CA Certificates    ${root_ca}
    Wait For Task2    ${add_rootCAcert}    300    5

    ${add_intermediateCAcert} =  Fusion Api Import External CA Certificates    ${intermediate_ca}
    Wait For Task2    ${add_intermediateCAcert}    300    5

    Log    \n-Remove all existed directories from appliance
    Remove All Directories

    Log    \n-Add AD server to OV    console=yes
    ${AD_server} =  Fusion Api Add Directory    ${service_ad}
    Wait For Task2    ${AD_server}    300    5

    Log    \n-Mapping AD group to role , create an ordinary user    console=yes
    ${mappingrole} =  Fusion Api Assign Roles To Directory Group    ${mapping_role}
    Wait For Task2    ${mappingrole}    300    5
    ${resp} =  Fusion Api Add User    ${ordinary_user_body}

    Log    \n-Set AD as the default login domain    console=yes
    Set directory server login domain as default    configuredLoginDomains    defaultLoginDomain    ADSERVER

    Log    \n-Enable 2FA and configure 2FA validations    console=yes
    ${authenticaiton_body} =  Update Authentication Body    ${enable_2fa}
    Fusion Api Edit Login Domains Global Settings    ${authenticaiton_body}
    Fusion Api Edit Login Domains Login Certificates    ${validation_body}

    Log    \n-Setup 2FA login evn in linux    console=yes
    Setup 2FA login evn in linux

    Log    \n-Get current authenticaiton settings via curl    console=yes
    ${auth} =  2FA Login
    ${auth_body} =  Get current auth body    ${auth}
    Set Global Variable    ${current_auth_body}    ${auth_body}

    Fusion Api Logout Appliance

Clear EVN
    [Documentation]    Clear up environment for OVF3104 test:reset authenticaiton settings, remove AD directories , delete CAs for AD directories
    Set Log Level           TRACE
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}

    Log    \n-Reset security 2FA validations and authenticaiton settings    console=yes
    Fusion Api Edit Login Domains Login Certificates    ${default_2FA_validation}
    ${authenticaiton_body} =  Update Authentication Body    ${reset_auth_settings}
    ${resp} =  Fusion Api Edit Login Domains Global Settings    ${authenticaiton_body}

    Log    \n-Remove AD directories    console=yes
    Remove Active Directory By Name    ${service_ad['name']}
    Remove Active Directory By Name    ${user_ad['name']}

    Log    \n-Remove the ordinary user    console=yes
    ${uri}=    Get User URI    ${ordinary_user_body['userName']}
    Fusion Api Remove User    uri=${uri}

    Log    \n-Delete CAs for AD directories    console=yes
    ${delete_rootCAcert} =  Fusion Api Remove External CA Certificates    root_CA
    Wait For Task2    ${delete_rootCAcert}    300    5
    ${delete_intermediateCAcert} =  Fusion Api Remove External CA Certificates    inter_CA
    Wait For Task2    ${delete_intermediateCAcert}    300    5

    Log    \n-Clear files uploaded to remote server    console=yes
    Clear evn in linux

    Fusion Api Logout Appliance
