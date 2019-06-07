*** Settings ***
Documentation        Can configure directory domain with correct domain names
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
${cert_domain}    certificateDomainIdentifier
${domain_pattern}   certificateDomainIdentifierPattern


*** Test Cases ***
Configure valid directory domain name
    [Documentation]    Can configure correct directory domain names
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}

    Log    \nConfigure valid directory domain name for SAN / Subject / Issuer options    console=yes
    :For    ${name}    IN    @{correct_domain_names[0:3]}
    \    ${validation_body1} =  Update 2FA Validation Domain Values    ${cert_domain}    ${name}    ${domain_pattern}    DC=(.*)
    \    ${resp1} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body1}
    \    Should be equal    '${resp1['status_code']}'    '200'    msg= Fail to configure SAN / Subject / Issuer domain name with valid values
    \    Check updated 2FA validation configurations    ${cert_domain}    ${name}

    Log    \nConfigure valid directory domain name for manually specify option    console=yes
    ${validation_body2} =  Update 2FA Validation Domain Values    ${cert_domain}    ${correct_domain_names[3]}    ${domain_pattern}    ${manually_specify_domain_values[0]}
    ${resp2} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body2}
    Should be equal    '${resp2['status_code']}'    '200'    msg= Fail to configure manually specify domain name with values
    Check updated 2FA validation configurations    ${cert_domain}    ${correct_domain_names[3]}

    Fusion Api Logout Appliance
