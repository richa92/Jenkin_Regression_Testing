*** Settings ***
Library            RoboGalaxyLibrary
Library            FusionLibrary
Resource          ${fusion_api_resource}

Resource          ../Resources/api/resource.robot
Variables         ./ovf28_100_sbac_me_data.py
Variables         ./environment_data.py

*** Variables ***
${fusion_api_resource}    C:/Users/komerao/OVF1134/fusion/Resources/api/fusion_api_resource.txt
# ${X-API-VERSION}    600
${appliance_ip}        15.212.167.184
${blnVerifyPreReqs}    False
@{allResourcesCommonList}    ethernets    egs    servers    osdps
${profile}    ovf28_100_sp

*** Keywords ***
Create scopes to test OSBP SBAC
    [Documentation]    Create scopes to test OSBP SBAC
    [Arguments]    ${input}
    :FOR    ${in}    in    @{input}
    \    Update User    ${in['user_scope_update']}
    \    Fusion Api Login Appliance    ${appliance_ip}    ${User1_credentials}
    \    ${body} =     Populate resources in scope body    ${in['scope_creation']}
    \    ${resp} =    Fusion Api Create Scope    ${body}
    \    Run Keyword If    '${resp['status_code']}' != '202'    Fail    ${resp}    ELSE  log to console    \n-${in['scope_creation']['name']} : Scope Created successfully!
    \    Check if scope is created with resources    ${in['scope_creation']}    ${in['isNegative']}
    \    Fusion Api Logout Appliance

Create scopes and server profiles
    [Documentation]    Create scopes and server profiles to test OSBP SBAC
    [Arguments]    ${scopes}=None    ${user}=None    ${update_user}=None    ${user_login}=None    ${profiles}=None    ${update_scope}=None
    Fusion Api Login Appliance    ${appliance_ip}     ${admin_credentials}
    :FOR    ${in}    in    @{scopes}
    \    ${add_exists}    Run keyword and return status    Dictionary Should Contain Key    ${in}    addedResourceUris
    \    ${in_u}    Run keyword if    ${add_exists}==True    Run keyword if    ${add_exists}!=[]    Get resource Uris for scope creation    ${in}
    \    ${resp} =    Fusion Api Create Scope    ${in_u}
    \    Run Keyword If    '${resp['status_code']}' != '202'    Fail    ${resp}    ELSE  log to console    \n-${in_u['name']} : Scope Created successfully!
    Run keyword if    ${update_scope} != []    Run keyword if    ${update_scope} is not None    Update scope with resource uris    ${update_scope}
    Add Users from variable    ${user}
    Run keyword if    ${update_user} is not None    Update Users    ${update_user}
    :FOR    ${s}    in    @{profiles}
    \    Run keyword if    '${s['serverHardwareUri']}'!='None'    Power off Server    ${s['serverHardwareUri']}
    Fusion Api Logout Appliance
    Fusion Api Login Appliance    ${appliance_ip}    ${user_login}
    ${r} =    Add Non Existing Server Profiles    ${profiles}
    ${task_resp} =    Run Keyword If    ${r[0]['status_code']} == 202    Wait For Task    ${r[0]}    3600s    20s
    sleep    5 seconds
    :FOR    ${sp}    in    @{profiles}
    \    ${profileFound} =    Check Resource Existing    SP:${sp['name']}
    \    Run keyword if    ${profileFound}=='FAIL'    FAIL    Server profile creation failed
    # \    Delete Server Profile    ${sp['name']}
    Fusion Api Logout Appliance

Update scope with resource uris
    [Documentation]    Update scope with resource uris
    [Arguments]    ${update_scope}
    :FOR    ${res}    in    @{update_scope}
    \    Run keyword if    ${res[0]['scope_update_add']} is not None or ${res[0]['scope_update_delete']} is not None
    \    ...    Run keyword if    ${res[0]['scope_update_add']}!=[] or ${res[0]['scope_update_delete']}!=[]    Build body and update scope    ${res[0]['scope']}    ${res[0]['scope_update_add']}    ${res[0]['scope_update_delete']}

Check if scope is created with resources
    [Documentation]    Check if scope is created with resources
    [Arguments]    ${input}    ${isNegative}=False
    :FOR    ${i}    in    @{input['addedResourceUris']}
    \    sleep    5 seconds
    \    ${s_uri} =    Get Scope URI By Name    ${input['name']}
    \    Run keyword if    ${isNegative}==True    Validate Resource Not Assign To Scope    ${s_uri}    ${i}
    \    Run keyword if    ${isNegative}==False    Validate Resource Assign To Scope    ${s_uri}    ${i}

Populate resources in scope body
    [Documentation]    Populate and add resource uri's in scope body
    [Arguments]    ${input}
    ${add}    Create list
    ${delete}    Create list
    :FOR    ${res}    in    @{input['addedResourceUris']}
    \    ${get_res}=    Run keyword and ignore error    Get Resource    ${res}
    \    Run keyword and ignore error    Append to list    ${add}    ${get_res[1]['uri']}
    :FOR    ${res}    in    @{input['removedResourceUris']}
    \    ${get_res} =    Run keyword and ignore error    Get Resource    ${res}
    \    Run keyword and ignore error    Append to list    ${delete}    ${get_res[1]['uri']}
    Set to dictionary    ${input}    addedResourceUris    ${add}
    Set to dictionary    ${input}    removedResourceUris    ${delete}
    [Return]    ${input}

Update User
    [Documentation]    Update scope and User roles if requested
    [Arguments]    ${data}
    Fusion Api Login Appliance    ${appliance_ip}    ${admin_credentials}
    ${r_state} =    Run keyword and return status    Dictionary should contain key    ${data}    replaceRoles
    ${body} =    Run keyword if    ${r_state} == True    Build body for user update    ${data['role']}    ${data['scope']}    ${data['userName']}
    ...                      ELSE    Build body for user update    ${data['role']}    ${data['scope']}    ${data['userName']}
    ${result}    ${task} =    Update Users    ${body}
    Fusion Api Logout Appliance

Setup Environment
    [Documentation]    Setup Environment for tao SBAC tests
    Fusion Api Login Appliance    ${appliance_ip}     ${admin_credentials}
    Remove All Users
    Remove All Scopes
    Add Users from variable    ${users}
    :FOR    ${scope}    in    @{scopes}
    \    ${resp} =    Fusion Api Create Scope    ${scope}
    \    Run Keyword If    '${resp['status_code']}' != '202'    Fail    ${resp}    ELSE  log to console   \n-${scope['name']} : Scope Created successfully!
    Add Ethernet Networks from variable    ${ethernet_networks}
    Fusion Api Logout Appliance

Deployment servers SBAC Create scope
    [Documentation]    Update scope and User roles if requested
    [Arguments]    ${scopes}
    :FOR    ${scope}    in    @{scopes}
    \    ${sc} =    Run keyword if    ${scope['addedResourceUris']} != [] or ${scope['removedResourceUris']} != []    Populate resources in scope body    ${scope}
    \    ${resp} =   Run keyword if    ${sc} == None    Fusion Api Create Scope    ${scope}
    \    ...    ELSE    Fusion Api Create Scope    ${sc}
    \    Run Keyword If    '${resp['status_code']}' != '202'   Fail    ${resp}    ELSE  log to console    \n-${scope['name']} : Scope Created successfully!
    \    ${task} =   Wait For Task   ${resp}   5s   5s

Deployment servers SBAC Add SP and check existence
    [Documentation]    Add SP and check existence
    [Arguments]    ${sps}
    :FOR    ${s}    in    @{sps}
    \    Run keyword and ignore error    Power off Server    ${s['serverHardwareUri']}
    ${r} =    Add Non Existing Server Profiles    ${sps}
    ${task_resp} =    Run Keyword If    ${r[0]['status_code']}==202    Wait For Task    ${r[0]}    3600s    20s
    sleep    5 seconds
    :FOR    ${sp}    in    @{sps}
    \    ${profileFound} =    Check Resource Existing  SP:${sp['name']}
    \    Run keyword if    ${profileFound}=='FAIL'    FAIL    Server profile creation failed

Deployment servers SBAC Delete SP and check existence
    [Documentation]    Delete SP and check existence
    [Arguments]    ${sps}
    ${result}=    Remove Server Profiles from variable    ${sps}
    :FOR    ${res}    in    @{result}
    \    Wait For Task    ${res}    3600s    10s
    sleep    5 seconds
    :FOR    ${sp}    in    @{sps}
    \    ${profileFound} =   Check Resource Existing    SP:${sp['name']}
    \    Run keyword if    ${profileFound}=='PASS'    FAIL    Server profile deletion failed

Populate scope Uri for user payload
    [Documentation]    Populate scope Uri for user payload
    [Arguments]    ${users}
    :FOR    ${user}    in    @{users}
    \    Fetch and replace scope uri in user payload    ${user}

Fetch and replace scope uri in user payload
    [Documentation]    Fetch and replace scope uri in user payload
    [Arguments]    ${user}
    :FOR    ${us}    in    @{user['permissions']}
    \    ${uri} =    Get Scope URI By Name    ${us['scopeUri']}
    \    Run keyword if    '${uri}'!='None'    Set to dictionary    ${us}    scopeUri    ${uri}

Get resource Uris for scope creation
    [Documentation]    Get resource Uris for scope creation
    [Arguments]    ${scope}
    ${lst}    Create list
    :FOR    ${i}    in    @{scope['addedResourceUris']}
    \    ${get_res} =    Run keyword if    '${i}' is not None    Get Resource    ${i}
    \    Run keyword if    ${get_res} is not None    Append to list    ${lst}    ${get_res['uri']}
    ${len}    Get Length    ${lst}
    Run keyword if    ${len}>0    Set to dictionary    ${scope}    addedResourceUris    ${lst}
    [Return]    ${scope}

Build body for user update
    [Documentation]    Build body for user update
    [Arguments]    ${role}    ${scope}    ${userName}
    ${up_list}    Create List
    ${up_dict}    Create dictionary
    ${bt}    convert to boolean    True
    Set to Dictionary    ${up_dict}    type    UserAndPermissions
    Set to Dictionary    ${up_dict}    userName    ${userName}
    Set to Dictionary    ${up_dict}    replaceRoles    ${bt}
    ${aP_list}    Create list
    ${aP_dict}    Create dictionary
    Set to Dictionary    ${aP_dict}    roleName    ${role}
    Set to Dictionary    ${aP_dict}    scopeUri    ${scope}
    append to list    ${aP_list}    ${aP_dict}
    Set to Dictionary    ${up_dict}    permissions    ${aP_list}
    append to list    ${up_list}    ${up_dict}
    [Return]    ${up_list}

Build body and update scope
    [Documentation]    Build required payload to update scope
    [Arguments]    ${scope}    ${add_resources}    ${delete_resources}    ${new_name}=${None}
    ${add}    Create list
    ${delete}    Create list
    ${new_name} =    Set Variable If    '${scope}'=='${None}'    ${scope}    ${new_name}
    ${add_resources} =    Set Variable If    ${add_resources}==${None}    ${add}    ${add_resources}
    :FOR    ${res}    in    @{add_resources}
    \    ${get_res} =    Get Resource    ${res}
    \    Append to list    ${add}    ${get_res['uri']}
    ${delete_resources} =    Set Variable If    ${delete_resources}==${None}    ${delete}    ${delete_resources}
    :FOR    ${res}    in    @{delete_resources}
    \    ${get_res} =    Get Resource    ${res}
    \    Append to list    ${delete}    ${get_res['uri']}
    Edit Scope    ${scope}    ${add}    ${delete}    ${new_name}

OVF28_100 Test Teardown
    [Tags]    teardown
    Delete Server Profile    ${profile}
