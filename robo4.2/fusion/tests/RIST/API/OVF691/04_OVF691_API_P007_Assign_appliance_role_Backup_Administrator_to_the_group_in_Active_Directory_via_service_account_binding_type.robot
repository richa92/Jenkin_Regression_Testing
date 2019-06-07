*** Settings ***
Documentation        OVF691:[2FA] Enable OneView to use service account credentials to bind to an enterprise directory
...                  OVF691_API_P007_Assign appliance role_Backup_Administrator to the group in Active Directory via service account binding type
Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}         unknown


*** Test Cases ***
OVF691_API_P007_Assign appliance role_Backup_Administrator to the group in Active Directory via service account binding type
    [Documentation]  OVF691_API_P007_Assign appliance role_Backup_Administrator to the group in Active Directory via service account binding type

    Log    \n- Logging in OneView appliance    console=true
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.209.139'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    \n-Create group to role mapping...    console=true
    ${body}=  Generate Post Grouptorolemapping Payload     ${RN_BAK_A}
    ${resp}=  fusion api assign roles to directory group   ${body}
    Wait For Task2       ${resp}     50    5

    Log    \n-Verify group info...    console=true
    ${result}=  Verify Group Info    ${RN_BAK_A}

    Log    \n-Delete group to role mapping ...    console=true
    ${name}=  Get Directoy Logindomain Id By Name             ${LOGINDOMAIN}
    ${resp}=  fusion api delete group role assignment  uri=/rest/logindomains/grouptorolemapping/${name}/${BASE_EGROUP}
    Wait For Task2       ${resp}     50    5

    should be true       '${result}' == 'Expected'

    Log    \n-Logging out OneView appliance    console=true
    Fusion Api Logout Appliance
