*** Settings ***
Documentation        Cannot 2FA login with wrong validaiton configurations
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
Resource             ./keywords.txt
Variables            ${DATA_FILE}


*** Variables ***
${cert_domain}    certificateDomainIdentifier
${domain_pattern}   certificateDomainIdentifierPattern
${cert_OID}    validationOids
${SAN_certowner}    subjectAlternateNamePatterns
${Subject_certowner}    subjectPatterns

*** Test Cases ***
2FA login with wrong validation configurations
    [Documentation]    Cannot 2FA login with validation configurations that not meet the attirbutes in client cert
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${status} =  Run Keyword And Return Status    Edit successful 2FA login configurations    ${successful_2FA_validation1}
    Should Be True    ${status}    msg=Fail to edit successful 2FA login validation configurations

    Log    \n-2FA login with SAN domain    console=yes
    ${validation_body} =  Update 2FA Validation Domain Values    ${cert_domain}    ${correct_domain_names[1]}    ${domain_pattern}    DC=(.*)
    ${resp1} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    Should be equal    '${resp1['status_code']}'    '200'    msg= Fail to configure domain value
    Check updated 2FA validation configurations    ${cert_domain}    ${correct_domain_names[1]}

    ${resp} =  2FA Login    ${curl_commands['part2']}
    Should Be Equal    '${resp}'    '400 Bad Request'    msg=Cannot 2FA login with SAN domain


    Log    \n-2FA login with incorrect manually specify domain    console=yes
    :For    ${item}    In    @{manually_specify_domain_values[5:8]}
    \    ${validation_body} =  Update 2FA Validation Domain Values    ${cert_domain}    ${correct_domain_names[3]}    ${domain_pattern}    ${item}
    \    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    \    Should be equal    '${resp['status_code']}'    '200'    msg= Fail to configure incorrect domain values
    \    Check updated 2FA validation configurations    ${cert_domain}    ${correct_domain_names[3]}
    \    Check updated 2FA validation configurations    ${domain_pattern}    ${item}
    \    ${resp} =  2FA Login    ${curl_commands['part2']}
    \    Should Be Equal    '${resp}'    '400 Bad Request'    msg=Cannot 2FA login with incorrect manually specify domain
    Fusion Api Logout Appliance


    Log    \n-2FA login with incorrect OID boxes    console=yes
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${status} =  Run Keyword And Return Status    Edit successful 2FA login configurations    ${successful_2FA_validation1}
    Should Be True    ${status}    msg=Fail to edit successful 2FA login validation configurations
    ${validation_body} =  Update 2FA Validation Values    ${cert_OID}    ${OIDs[5:6]}
    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    Should be equal    '${resp['status_code']}'    '200'    msg= Fail to update login domains login certificates
    Check updated 2FA validation configurations    ${cert_OID}    ${OIDs[5:6]}
    Fusion Api Logout Appliance

    ${resp} =  2FA Login    ${curl_commands['part2']}
    Should Be Equal    '${resp}'    '400 Bad Request'    msg=Cannot 2FA login with incorrect OID boxes


    Log    \n-2FA login with incorrect SAN cert owner    console=yes
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${status} =  Run Keyword And Return Status    Edit successful 2FA login configurations    ${successful_2FA_validation1}
    Should Be True    ${status}    msg=Fail to edit successful 2FA login validation configurations  
    :For    ${index}    IN RANGE    7    9
    \    ${validation_body} =  Update 2FA validation values    ${SAN_certowner}    ${SAN_certowner_info1[${index}]}
    \    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    \    Should be equal    '${resp['status_code']}'    '200'    msg=Fail to configure SAN cert owner
    \    Check updated 2FA validation configurations    ${SAN_certowner}    ${SAN_certowner_info1[${index}]}
    \    ${resp} =  2FA Login    ${curl_commands['part2']}
    \    Should Be Equal    '${resp}'    '400 Bad Request'    msg=Cannot 2FA login with incorrect SAN cert owner
    Fusion Api Logout Appliance


    Log    \n-2FA login with incorrect Subject cert owner    console=yes
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${status} =  Run Keyword And Return Status    Edit successful 2FA login configurations    ${successful_2FA_validation2}
    Should Be True    ${status}    msg=Fail to edit successful 2FA login validation configurations
    :For    ${index}    IN RANGE    7    8
    \    ${validation_body} =  Update 2FA validation values    ${Subject_certowner}    ${Subject_certowner_info1[${index}]}
    \    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    \    Should be equal    '${resp['status_code']}'    '200'    msg= Fail to configure Subject cert owner
    \    Check updated 2FA validation configurations    ${Subject_certowner}    ${Subject_certowner_info1[${index}]}
    \    ${resp} =  2FA Login    ${curl_commands['part2']}
    \    Should Be Equal    '${resp}'    '400 Bad Request'    msg= Cannot 2FA login with incorrect Subject cert owner
    Fusion Api Logout Appliance