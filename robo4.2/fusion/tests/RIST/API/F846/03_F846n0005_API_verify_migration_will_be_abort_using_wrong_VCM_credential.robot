*** Settings ***
Documentation        Verify Migration Will Be Abort Using Wrong VCM Credential

Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              Collections

Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt

Variables            ./Regression_Data.py


*** Variables ***
${APPLIANCE_IP}      unknown
${Enclosure}         WPST22

*** Test Cases ***
Verify Migration Will Be Abort Using Wrong VCM Credential
    Log    Logging in OneView appliance    console=true
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.220.131'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    Cleaning base Resources    console=true
    Clear Base Resources

    Log    Getting request body and parsing data file to get credentials...    console=true
    ${requestBody}=               Get From Dictionary    ${all_hardware_info}    ${Enclosure}
    ${requestBody3}=              Wpst Deep Copy    ${requestBody}

    Log    Generating an error OA hostname for request body...    console=true
    ${expectVCMPwd}=               Get From Dictionary    ${requestBody3["credentials"]}  vcmPassword
    Set To Dictionary             ${requestBody3["credentials"]}  vcmPassword=hpvse15555
    ${actualVCMPwd}=               Get From Dictionary    ${requestBody3["credentials"]}  vcmPassword
    Should Not Be Equal           ${expectVCMPwd}  ${actualVCMPwd}  msg=This case used to verify wrong password, please provide a wrong VCM password

    Log    Generating Compatibility Report...    console=true
    ${resourceUri}=               Create Migration Compatibility Report   ${requestBody3}
    Should Be Equal               ${resourceUri}  ${None}  msg=The task should be failed

    Log    Verifying Server Hardware Types can not be imported    console=true
    ${SHTs}=                      Fusion Api Get Server Hardware Types
    Should Be Empty               ${SHTs["members"]}  msg=The server hardware types shoud not be created, please check.

    Log    Verifing Server Profiles same as expect...    console=true
    ${SPs}=                       Fusion Api Get Server Profiles
    Should Be Empty               ${SPs["members"]}  msg=The server profiles shoud not be created, please check.

    Log    Logging out OneView appliance    console=true
    Fusion Api Logout Appliance
