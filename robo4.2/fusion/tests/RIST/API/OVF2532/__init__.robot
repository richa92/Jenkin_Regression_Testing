*** Settings ***
Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              Process
Library              SSHLibrary
Library              String
Library              Dialogs
Library              BuiltIn
Library              json
Library              Collections
Resource             ../Fusion_Env_Setup/keywords.txt
Resource             ./../../../../Resources/api/common/common.txt
Resource             ./../../../../Resources/api/security/login_domain.txt
Resource             ./../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}

Suite Setup  Precondition ENV Setup
Suite Teardown  Clear ENV


*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}                    SHQA
${login_message_item}           message
${2FA_switch}                   twoFactorAuthenticationEnabled
${default_login_domain_item}         defaultLoginDomain

*** Keywords ***
Precondition ENV Setup
    [Documentation]    Setup ENV for OVF2532 test
    Set Log Level           TRACE
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    
    Log    \n-Remove privious deployed root_ca from appliance    console=yes
    ${ret_val}=    Check Cert Exists    root_CA    
    ${resp}=    Run Keyword If    '${ret_val}'=='True'    Fusion Api Remove External CA Certificates    root_CA
    Run Keyword If    '${ret_val}'=='True'    Wait For Task2    ${resp}    3min    5
    
    Log    \n-Remove privious deployed inter_ca from appliance    console=yes
    ${ret_val}=    Check Cert Exists    shqa-WIN-H309UPI1LMV-CA
    ${resp}=    Run Keyword If    '${ret_val}'=='True'    Fusion Api Remove External CA Certificates    shqa-WIN-H309UPI1LMV-CA
    Run Keyword If    '${ret_val}'=='True'    Wait For Task2    ${resp}    3min    5
    
    Log    \n-Remove all existed directories from appliance    console=yes
    Remove Active Directory By Name    AD_Server
    Remove Active Directory By Name    ADServer
 
    Log    \n-Add CA certificates for multiple AD server to OV    console=yes
    ${resp} =  Fusion Api Import External CA Certificates    ${root_ca}
    Wait For Task2    ${resp}    3min    5
 
    ${resp} =  Fusion Api Import External CA Certificates    ${intermediate_ca}
    Wait For Task2    ${resp}    3min    5
 
 
    Log    \n-Setup 2FA login evn in linux    console=yes
    Setup 2FA login evn in linux
 
Clear ENV
    [Documentation]    Clear up environment for OVF2532 test:reset authenticaiton settings, remove AD directories , delete CAs for AD directories
    Set Log Level           TRACE
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
  
    Log    \n-Reset security authenticaiton settings    console=yes
    Fusion Api Edit Login Domains Login Certificates    ${default_2FA_validation}
    ${authentication_body} =  Edit authentication switch    ${2FA_switch}    ${False}
    ${resp} =  Fusion Api Edit Login Domains Global Settings    ${authentication_body}
  
    Log    \n-Reset login message    console=yes
    ${login_message_body} =  Get Global Setting Body With New Login Message    ${login_message_item}    ${default_login_message[0]}
    ${resp} =  Fusion Api Edit Login Domains Global Settings    ${login_message_body}
  
    Log    \n-Reset local domain as default login domain    console=yes
    ${reset_login_domain} =  Edit authentication switch    ${default_login_domain_item}    ${default_local_login_domain}
    ${resp} =  Fusion Api Edit Login Domains Global Settings    ${reset_login_domain}
  
    Log    \n-Remove AD directories    console=yes
    Remove Active Directory By Name    ADSERVER
    Remove Active Directory By Name    userad
  
  
    Log    \n-Delete CAs for AD directories    console=yes
    ${resp} =  Fusion Api Remove External CA Certificates    root_CA
    Wait For Task2    ${resp}    3min    5
  
    ${resp} =  Fusion Api Remove External CA Certificates    inter_CA
    Wait For Task2    ${resp}    3min    5
  
    Log    \n-Clear files uploaded to remote server    console=yes
    Clear evn in linux
  
    Fusion Api Logout Appliance