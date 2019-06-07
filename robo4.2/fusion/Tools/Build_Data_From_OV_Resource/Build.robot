*** Settings ***
Documentation                   Build data dicts
Library                         FusionLibrary
Library                         RoboGalaxyLibrary
Library                         OperatingSystem
Library                         BuiltIn
Library                         Collections
Library                         XML
Library                         String
Library                         json

Library                         ./Build_Data_Dict.py
Library                         ./Build_Request_Body.py
Library                         ./Build_Expected_from_Response.py

Resource            ./../../Resources/api/fusion_api_resource.txt


Variables 		    ./Build_data.py

Variables          ${TEMPLATE_FILE}


*** Variables ***
${TEMPLATE_FILE}                ./templates.py

${X-API-VERSION}			    500

${IP}                 change_me
${NAME}                change_me
${TYPE}                change_me
${TEMPLATE}                     change_me

#${NAME}                CN75120D7B
#${TYPE}                ENC
#${TEMPLATE}                     tbird_enclosure

#${NAME}                wpst10Bay1
#${TYPE}                SP
#${TEMPLATE}                     server_profile_virtual_addr_manage_boot_storage_vol

#${NAME}                wpst10-eg
#${TYPE}                EG
#${TEMPLATE}                     wpst10_eg_template

#${NAME}                Lan100-200
#${TYPE}                NS
#${TEMPLATE}                     network_sets_template

#${NAME}                UnAssigned BL660 Gen9
#${TYPE}                SP
#${TEMPLATE}                     unassignedGen9SanStorage

${DELETE_CREATE}                ${False}
${VERBOSE}                      ${False}
${WRITEFILE}                    ${True}

*** Test Cases ***
BUILD
    [DOCUMENTATION]    Builds the resource data files
    ...     You must supply the IP, NAME, TYPE, TEMPLATE and TEMPLATE_FILE
    ...     pybot -v IP:#.#.#.# -v NAME:Profile-1  -v TYPE:SP  -v TEMPLATE:template -v TEMPLATE_FILE:Template_file.py Build.robot

    Log Variables    level=TRACE

    Should Not Be Equal As Strings    ${IP}    change_me
    Should Not Be Equal As Strings    ${NAME}    change_me
    Should Not Be Equal As Strings    ${TYPE}    change_me
    Should Not Be Equal As Strings    ${TEMPLATE}    change_me

    ${status}    ${length} =    Run Keyword And Ignore Error    Get Length    ${${TEMPLATE}}
    Run Keyword If    '${status}'=='FAIL'     Fail   Unable to find dict: ${TEMPLATE}

    Set Log Level	TRACE
    
    ${admin_session} =    Fusion Api Login Appliance 		${IP}		${admin_credentials}
    ${session} =    Get From List    ${admin_session}     0
    ${status}    ${error} =    Run Keyword And Ignore Error     Get From Dictionary     ${session}    message
    Run Keyword If     '${status}'=='PASS'    Fail    Unable to login: ${error}

    ${expected} =    Build Expected Response

    ${data_dict} =    Build Data Dict    ${${TEMPLATE}}

	${request_body} =    Build Request Body    ${data_dict}

    # Not part of Build actually but verification
    ${response} =    Get Resource    ${TYPE}:${NAME}

	${results} =    Fusion Api Validate Response Follow    ${expected}    ${response}    wordy=${true}

    Should Be Equal    ${results}    ${True}

    # For a full test, delete and re-create the resouce with the build data
    Run Keyword If    ${DELETE_CREATE}==${True}    Delete Create Resource    ${expected}    ${request_body}

	Fusion Api Logout Appliance
	
*** Keywords ***
Build Expected Response
    [DOCUMENTATION]  Builds an expected data dict for future regressions

    ${resource} =    Get Resource    ${TYPE}:${NAME}

    ${expected} =    Build_Expected_From_Response.get    ${resource}    parentKey=""    wordy=${True}

    ${nicelyFormated}    json.dumps    ${expected}    indent=${4}
    ${nicelyFormated} =    Replace String    ${nicelyFormated}    null    None
    ${nicelyFormated} =    Replace String    ${nicelyFormated}    true    True
    ${nicelyFormated} =    Replace String    ${nicelyFormated}    false    False

    Run Keyword If    ${VERBOSE}==${True}    Log To Console and Logfile    ${nicelyFormated}
    Run Keyword If    ${WRITEFILE}==${True}    Create File    BUILT/${TYPE}_${NAME}.expt    ${nicelyFormated}

    Return From Keyword    ${expected}


Build Data Dict
    [DOCUMENTATION]  Using a pre-created template, build a data dict that can be used to re-create the resource
    [Arguments]    ${template}

    ${Resource} =    Get Resource    ${TYPE}:${NAME}

    ${datadict} =    Build_Data_Dict.get    ${template}    ${resource}    wordy=${True}

    ${nicelyFormated}    json.dumps    ${datadict}    indent=${4}
    ${nicelyFormated} =    Replace String    ${nicelyFormated}    null    None
    ${nicelyFormated} =    Replace String    ${nicelyFormated}    true    True
    ${nicelyFormated} =    Replace String    ${nicelyFormated}    false    False

    Run Keyword If    ${VERBOSE}==${True}    Log To Console and Logfile    ${nicelyFormated}
    Run Keyword If    ${WRITEFILE}==${True}    Create File    BUILT/${TYPE}_${NAME}.data    ${nicelyFormated}


    Return From Keyword    ${data_dict}

Build Request Body
    [DOCUMENTATION]  Using a pre-created data dict create a POST requestbody
    [Arguments]    ${data_dict}

    ${requestBody} =    Build_Request_Body.get    ${data_dict}        wordy=${True}

    ${nicelyFormated}    json.dumps    ${requestBody}    indent=${4}
    ${nicelyFormated} =    Replace String    ${nicelyFormated}    null    None
    ${nicelyFormated} =    Replace String    ${nicelyFormated}    true    True
    ${nicelyFormated} =    Replace String    ${nicelyFormated}    false    False

    Run Keyword If    ${VERBOSE}==${True}    Log To Console and Logfile    ${nicelyFormated}
    Run Keyword If    ${WRITEFILE}==${True}    Create File    BUILT/${TYPE}_${NAME}.requ    ${nicelyFormated}

    Return From Keyword    ${requestBody}

Delete Create Resource
    [DOCUMENTATION]  Deletes then attempts to re-create the resource and Validate the Response
    [ARGUMENTS]    ${expected}    ${requestBody}

    ${timeout} =    Set Variable If
    ...             '${TYPE}'=='LE'      3600
    ...             '${TYPE}'=='SP'      2700
    ...             300

    ${interval} =    Set Variable If
    ...             '${TYPE}'=='LE'      60
    ...             '${TYPE}'=='SP'      60
    ...             10

	${resp} =    Delete Resource    ${TYPE}:${NAME}

    Wait For Task2	${resp}		timeout=${timeout}		interval=${interval}

    @{requestBodyList} =    Create List    ${requestBody}

    ${resp} =		Run Keyword If    '${type}' == 'ETH'      Add Ethernet Networks from variable    ${requestBodyList}
	...             ELSE              Create Resource		${TYPE}    ${requestBody}

	Run Keyword if    '${resp}'!='None'    Wait For Task2	${resp}		timeout=${timeout}		interval=${interval}

    ${response} =    Get Resource    ${TYPE}:${NAME}

    ${results} =    Fusion Api Validate Response Follow    ${expected}    ${response}    wordy=${true}

    Should Be Equal    ${results}    ${True}