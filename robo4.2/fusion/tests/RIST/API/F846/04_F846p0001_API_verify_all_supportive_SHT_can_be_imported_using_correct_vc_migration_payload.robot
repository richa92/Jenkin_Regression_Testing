*** Settings ***
Documentation        Verify All Supportive SHT Can Be Imported Using Correct VC Migration Payload

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
Verify All Supportive SHT Can Be Imported Using Correct VC Migration Payload
    Log    Logging in OneView appliance    console=true
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.220.131'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    Cleaning base Resources    console=true
    Clear Base Resources

    Log    Getting request body and parsing data file to get credentials...    console=true
    ${requestBody}=               Get From Dictionary    ${all_hardware_info}    ${Enclosure}
    ${requestBody4}=              Wpst Deep Copy    ${requestBody}

    Log    Generating Compatibility Report...    console=true
    ${resourceUri}=               Create Migration Compatibility Report   ${requestBody4}

    Log    Getting Compatibility Report...    console=true
    ${resp}  ${respState}=        Get Migration Compatibility Report      saveConfig=${False}

    Log    Migrating Enclosure from VC to OneView...    console=true
    Set TO Dictionary             ${migrationBody}    uri=${resourceUri}
    ${messages}=                  Get From Dictionary    ${resp}    items
    ${taskStatus}=                Run Keyword If    "${respState}" != "ReadyToMigrate"
    ...                           Fail    msg= The report state is not ReadyToMigrate, please manually fix error.\n${messages}.
    ...                           ELSE    Add Enclosure By Migration  ${resourceUri}  ${migrationBody}
    should Not Be Equal               '${taskStatus}'    'Error'    msg=Migration task status should be "Completed"

    Log    Verifying Server Hardware Types same as expect...    console=true
    ${expectSHTs}=                Get From Dictionary  ${expect_sever_hardware_types}  ${Enclosure}
    ${shts}=                      Fusion Api Get Server Hardware Types
    Length Should Be              ${shts['members']}  5
    :FOR                          ${sht}    IN    @{shts['members']}
    \                             Validate Response Regex    ${sht}    ${expectSHTs}

    Log    Verifing Server Profiles same as expect...    console=true
    ${expectSPs}=                 Get From Dictionary  ${expect_sever_profiles}  ${Enclosure}
    ${sps}=                       Fusion Api Get Server Profiles
    Length Should Be              ${sps['members']}  5
    :FOR                          ${sp}    IN    @{sps['members']}
    \                             Validate Response Regex    ${sp}    ${expectSPs}

    Log    Logging out OneView appliance    console=true
    Fusion Api Logout Appliance
