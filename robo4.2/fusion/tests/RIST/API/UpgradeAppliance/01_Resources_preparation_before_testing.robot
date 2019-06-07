*** Settings ***
Documentation             Download Update Bin File, Upload it into Appliance, and Update Appliance with it.
Library                   FusionLibrary
Library                   RoboGalaxyLibrary
Library                   BuiltIn
Library                   robot.api.logger
Library                   Collections
Library                   OperatingSystem
Resource                  ./../../../../Resources/api/fusion_api_resource.txt
Resource                  ./keywords.txt
Variables                 ./Regression_Data.py

Test Setup                Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}
Test Teardown             Fusion Api Logout Appliance

*** Variables ***
${APPLIANCE_IP}           'DCS APPLIANCE IP'
${Ring}                   TBird13
${Team_Name}              SHQA
${Add_User}               true
${Add_LE}                 true
${Add_Storage}            true
${PASS_BUILD}             UNDEFINED
${Import_appliance_cert_param}    /certificaterequest

*** Test Cases ***
Set Api Version
    Set Appliance Version Variable
    Set Data Version Variable

Create Base Resources Befre Upgrade
    Set log level  TRACE
    Log    \nCheck the appliance version   console=True
    Setup TBird Env Befre Upgrade   ${Ring}  ${Add_LE}  ${Add_Storage}  ${Team_Name}  Version=${Version}

Create Server Profile Befre Upgrade
    Set log level  TRACE
    Log    \nCreate server profiles with connections, storage    console=True
    Power off Server  ${SH_NAME}
    ${resps}=    Add Server Profiles from variable  ${${Version}.server_profile}
    :FOR   ${resp}  IN  @{resps}
    \       Wait For Task2    ${resp}    timeout=60m  interval=10

Add AD server on appliance, Add group, relogin with AD user
    [Documentation]    add AD and group, then relogin with AD user
    Add Dirctory Server and Assign Roles    ${addadrequestbody_3_10}    ${createadgrouprequestbody_3_10}
    Fusion Api Logout Appliance
    ${resp} =    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${ad_user}
    Should Be Equal As Numbers  ${resp[0]['status_code']}  200

Add LDAP server on appliance, Add group, relogin with LDAP user
    [Documentation]    add Ldap and group, then relogin with Ldap user
    Add Dirctory Server and Assign Roles    ${addldaprequestbody_3_10}    ${createldapgrouprequestbody_3_10}
    Fusion Api Logout Appliance
    ${resp} =    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${ldap_user}
    Should Be Equal As Numbers  ${resp[0]['status_code']}  200

Add exteral self-signed repository
    [Documentation]    add repo
    ${base64Data} =    Get Remote Sever Cert    ${REPO_IP}
    Set to Dictionary    ${addselfsignedreporequestbody}    base64Data    ${base64Data}
    ${resp} =    Fusion Api Add Repository    ${addselfsignedreporequestbody}
    Should Be Equal As Numbers  ${resp['status_code']}  202
    Wait Until Keyword Succeeds    600s   5s    Verify Firmwares Exist    ${ValidateFirmwares}
    Wait Until Keyword Succeeds    600s   5s    Verify Firmwares Status   ${FirmwareVersions}    ${ok_status}

Add ipdu
    [Documentation]    add ipdu
    ${base64Data} =    Get Remote Sever Cert    ${IPDU182_IP}
    Set to Dictionary    ${addipducertificate}    base64SSLCertData    ${base64Data}
    ${resp} =    Fusion Api Import Client Certificate    ${addipducertificate}
    Should Be Equal As Numbers  ${resp['status_code']}  200
    ${resp} =    Fusion Api Discover Power Device    ${addipdurequestbody}
    Should Be Equal As Numbers  ${resp['status_code']}  202
    Wait For Task2    ${resp}    timeout=150    interval=30

Import CA Signed Web Server Certificate Before Upgrade
    Set Log level    TRACE
    Log    \nGenerate certificate signing request    console=Yes
    ${csr} =  Generate Certificate Signing Request  ${CSRinfo}
    ${cert} =  Issue Appliance Certificate by CSR    ${csr}    ${Issuer_IP}    ${ssh_credentials}
    Log    ${cert}    console=Yes
    Set to Dictionary    ${appliance_cert}    base64Data    ${cert}
    ${resp} =  Fusion Api Import Appliance Certificate    body=${appliance_cert}    param=${Import_appliance_cert_param}
    Wait For Task2    ${resp}    200    5    None Expected    Completed

# TODO: Check RabitMq
# TODO: iLO single Sign On (SSO)
# TODO: Check SBAC part
