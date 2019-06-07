*** Settings ***
Documentation        F1022p019_API_force_change_potash_LE_licenses_should_be_failed

Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              copy
Library              Collections
Library              String
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt

Variables            ${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Validate Change Potash FC licenses Status Will Return Error Message
    [Documentation]  F1022p019_API_force_change_potash_LE_licenses_should_be_failed
    ...              Send put API to change potash to use/unuse the FC licenses will return error message

    Log    \n- Logging in OneView appliance    console=true
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.209.231'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    \nVerify can not manually modify the FC license intent for Potash    console=true
    ${le_uri}=    Get Logical Enclosure URI    ${LE_name}
    ${task}=      Update Logical Enclosure License From Variable  ${logical_enc_put}  ${le_uri}
    Should Be Equal As Strings   ${task["taskState"]}  Error
    ${errorList}=    Create List
    :FOR    ${errorBody}    IN    @{task["taskErrors"]}
    \       Append To List  ${errorList}    ${errorBody["errorCode"]}
    Should Contain  ${errorList}  LOGICAL_ENCLOSURE_LICENSEINTENT_UNSUPPORTED

    Log    \n- Logging out OneView appliance    console=true
    Fusion Api Logout Appliance
