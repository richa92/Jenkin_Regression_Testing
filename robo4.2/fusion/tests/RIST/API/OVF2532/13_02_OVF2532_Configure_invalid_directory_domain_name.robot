*** Settings ***
Documentation        Cannot configure directory domain with invalid domain names
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
Resource             ./../../../../Resources/api/common/common.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}


*** Variables ***
${cert_doamin}    certificateDomainIdentifier
${domain_pattern}   certificateDomainIdentifierPattern


*** Test Cases ***
Configure invlaid directory domain name
    [Documentation]    Configure invalid directory domain name , it should fail
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}

    Log    \nConfigure invalid directory domain names for SAN / Subject / Issuer options    console=yes
    :For    ${name}    IN    @{invalid_domain_names1}
    \    ${validation_body} =  Update 2FA Validation Domain Values    ${cert_doamin}    ${name}    ${domain_pattern}    DC=(.*)
    \    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    \    Should be equal    '${resp['status_code']}'    '400'    msg=Cannot configure invlaid directory domain name
    \    Should be equal    '${resp['message']}'    '${TwoFA_errorMessages['Invalid_domain_name']}'    msg=Show incorrect error message when configure invalid domain name

    Log    \nConfigure invalid directory domain names for manually specify option    console=yes
    :For    ${name}    IN    @{invalid_domain_names2}
    \    ${validation_body} =  Update 2FA Validation Domain Values    ${cert_doamin}    ${name}    ${domain_pattern}    ${manually_specify_domain_values[0]}
    \    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    \    Should be equal    '${resp['status_code']}'    '400'    msg=Cannot configure invlaid directory domain name
    \    Should be equal    '${resp['message']}'    '${TwoFA_errorMessages['Invalid_domain_name']}'    msg= Show incorrect error message when configure invalid domain name

    Fusion Api Logout Appliance
