*** Settings ***
Documentation    OVF423 Firmware SPT SBAC test
Resource    ../Fusion_Env_Setup/keywords.txt
Resource    ./keywords.txt
Resource    ../../UI/resource.txt
Variables   ./Regression_Data.py

Suite Setup  Precondition Setup
Suite Teardown  Clear Firmware And Scope


*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}                    SHQA
${Ring32}                       WPST32
${UIDataFile}                   OVF423_C7000/Regression_data.xml  # Data File Location
${FTS}                          false
${Add_Enclosure}                true
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Keywords ***
Precondition Setup
    [Documentation]   Precondition Setup
    Set Log Level           TRACE
    ${resp}  ${sessionID}=  Fusion Api Login Appliance
    ...                     ${APPLIANCE_IP}         ${admin_credentials}

    Clear Firmware And Scope

    Setup Env For C7000     ${Ring32}    ${FTS}    ${Add_Enclosure}

    ${resp} =   Add Repository       ${Http_repo_with_password}
    ${task} =   Wait For Task2           ${resp}     50    5
    Wait Until Keyword Succeeds    600s   5s    Verify Firmwares Exist    ${ValidateFirmwares}
    Wait Until Keyword Succeeds    600s   5s    Verify Firmwares Status   ${ValidateFirmwares}    ${ok_status}

    ${resps} =    Create Scopes    ${scopes}
    :FOR    ${resp}    IN    @{resps}
    \    Wait For Task2    ${resp}

    ${scope} =    Get Scope URI By Name    ${ia_scope_scope}
    ${scopes} =  Create List    ${scope}
    :FOR    ${scope_name}    IN    @{ia_user_scopes}
    \    ${scope} =    Get Scope URI By Name    ${scope_name}
    \    ${resp} =    Edit Resource Scope    ${scope}    ${scopes}
    \    Wait For Task2    ${resp}

    ${ia_permissions} =    Create List
    ${sa_permissions} =    Create List
    :FOR    ${user_scope}    IN    @{ia_user_scopes}
    \    ${uri} =    Get Scope URI By Name    ${user_scope}
    \    ${permission} =    Create Dictionary    roleName=${ia_role_name}    scopeUri=${uri}
    \    Append To List    ${ia_permissions}    ${permission}
    \    ${permission} =    Create Dictionary    roleName=${sa_role_name}    scopeUri=${uri}
    \    Append To List    ${sa_permissions}    ${permission}

    ${create_users} =    Create List
    :FOR    ${user}    IN    @{ia_users}
    \    Set To Dictionary    ${user}    permissions    ${ia_permissions}
    \    Append To List    ${create_users}    ${user}
    :FOR    ${user}    IN    @{sa_users}
    \    Set To Dictionary    ${user}    permissions    ${sa_permissions}
    \    Append To List    ${create_users}    ${user}
    Add Users From Variable async    ${create_users}

    ${eg_uri} = 	Get Enclosure Group URI    ${EG1}
    ${sh_uri} = 	Get Server Hardware URI    ${SH1}
    ${scopes} =  Create List
    :FOR    ${scope_name}    IN    @{ia_user_scopes}
    \    ${scope} =    Get Scope URI By Name    ${scope_name}
    \    Append To List    ${scopes}    ${scope}
    ${resp} =    Edit Resource Scope    ${eg_uri}    ${scopes}
    Wait For Task2    ${resp}
    ${resp} =    Edit Resource Scope    ${sh_uri}    ${scopes}
    Wait For Task2    ${resp}

    Fusion Api Logout Appliance

Clear Firmware And Scope
    [Documentation]   Clear All Firmware Bundle and Repo, and scope
    Run Keyword And Ignore Error    Fusion Api Logout Appliance
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    Run Keyword And Ignore Error    Remove All Server Profiles
    Run Keyword And Ignore Error    Remove All Server Profile Templates Async
    Run Keyword And Ignore Error    Remove All Repositories
    Run Keyword And Ignore Error    Remove All Users
    Run Keyword And Ignore Error    Remove All Scopes
    Run Keyword And Ignore Error    Remove All Enclosures
