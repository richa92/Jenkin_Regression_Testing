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

Resource            ../../../fusion/Resources/api/fusion_api_resource.txt


Variables 		    ./Build_data.py

Variables          ${TEMPLATE_FILE}


*** Variables ***
${TEMPLATE_FILE}                ./templates.py

${X-API-VERSION}			    500

${IP}                 change_me
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
${VERBOSE}                ${False}

# Add new TYPE -> API calls here.
&{build_all}                ENC=Fusion Api Get Enclosures
...                         EG=Fusion Api Get Enclosure Groups
...                         DE=Fusion Api Get Drive Enclosures
...                         ETH=Fusion Api Get Ethernet Networks
...                         FC=Fusion Api Get FC Networks
...                         FCOE=Fusion Api Get FCOE Networks
...                         IC=Fusion Api Get Interconnect
...                         ICTYPE=Fusion Api Get Interconnect Types
...                         LE=Fusion Api Get Logical Enclosure
...                         LI=Fusion Api Get LI
...                         LIG=Fusion Api Get Lig
...                         NS=Fusion Api Get Network Set
...                         SASIC=Fusion Api Get SAS Interconnects
...                         SASICTYPE=Fusion Api Get SAS Interconnect Types
...                         SASLIG=Fusion Api Get SAS LIG
...                         SASLI=Fusion Api Get SAS LI
...                         SASLJBOD=Fusion Api Get SAS Logical JBODS
...                         SASLJBODATT=Fusion Api Get SAS Logical JBOD Attachments
...                         SH=Fusion Api Get Server Hardware
...                         SHT=Fusion Api Get Server Hardware Types
...                         SP=Fusion Api Get Server Profiles
...                         SPT=Fusion Api Get Server Profile Templates
...                         SSYS=Fusion Api Get Storage System
...                         SPOOL=Fusion Api Get Storage Pools
...                         SVOL=Fusion Api Get Storage Volumes
...                         SVT=Fusion Api Get Storage Volume Templates
...                         USER=Fusion Api Get User



&{warnCache}                key=value
                 
*** Test Cases ***
BUILD
    [DOCUMENTATION]    Builds the resource data files
    ...     You must supply the IP, RESOURSE_NAME, TYPE, TEMPLATE and TEMPLATE_FILE
    ...     pybot -v IP:#.#.#.# -v NAME:Profile-1  -v TYPE:SP  -v TEMPLATE:template -v TEMPLATE_FILE:Template_file.py Build.robot

    Log Variables    level=INFO

    Should Not Be Equal As Strings    ${IP}    change_me
    Should Not Be Equal As Strings    ${TYPE}    change_me
    Should Not Be Equal As Strings    ${TEMPLATE}    change_me

    ${status}    ${length} =    Run Keyword And Ignore Error    Get Length    ${TEMPLATE}
    Run Keyword If    '${status}'=='FAIL'     Fail   Unable to find dict: ${TEMPLATE}

    Set Log Level	DEBUG
    
    ${admin_session} =    Fusion Api Login Appliance 		${IP}		${admin_credentials}
    ${session} =    Get From List    ${admin_session}     0
    ${status}    ${error} =    Run Keyword And Ignore Error     Get From Dictionary     ${session}    message
    Run Keyword If     '${status}'=='PASS'    Fail    Unable to login: ${error}

    ${status}     ${api} =  Run Keyword and Ignore Error    Get From Dictionary    ${build_all}   ${TYPE}
    Return From Keyword If    '${status}'=='FAIL'    build_all does not contain that lookup.
    ${resp} =    Run Keyword    ${api}

    ${members} =    Get From Dictionary    ${resp}    members

    Create File    BUILT/${TYPE}.expt    [
    Create File    BUILT/${TYPE}.data    [

    ${num_members} =    Get Length    ${members}
    ${count} =    Set Variable    ${1}

	:For     ${resource}    In    @{members}
	\    ${NAME} =     Get From Dictionary    ${resource}    name
	\    Set Suite Variable    ${NAME}
	\
    \    ${expected}     ${pretty} =    Build Expected Response
    \    Run Keyword If    ${count} < ${num_members}    Append To File    BUILT/${TYPE}.expt    ${pretty},${\n}
    \    ...    ELSE    Append To File    BUILT/${TYPE}.expt    ${pretty}${\n}
    \
    \    ${data_dict}    ${pretty} =    Build Data Dict    ${${TEMPLATE}}
    \    Run Keyword If    ${count} < ${num_members}    Append To File    BUILT/${TYPE}.data    ${pretty},${\n}
    \    ...    ELSE    Append To File    BUILT/${TYPE}.data    ${pretty}${\n}
    \
    \    ${request_body} =    Build Request Body    ${data_dict}
    \    # Not part of Build actually but verification
    \    ${response} =    Get Resource    ${TYPE}:${NAME}
    \
	\    ${results} =    Fusion Api Validate Response Follow    ${expected}    ${response}    wordy=${true}
    \
    \    Should Be Equal    ${results}    ${True}
    \
    \    ${count} =    Evaluate    ${count} + 1
    \
    \    # For a full test, delete and re-create the resouce with the build data
    \    Run Keyword If    ${DELETE_CREATE}==${True}    Delete Create Resource    ${expected}    ${request_body}

    Append To File    BUILT/${TYPE}.expt    ]
    Append To File    BUILT/${TYPE}.data    ]

	Fusion Api Logout Appliance
	
*** Keywords ***
Build Expected Response
    [DOCUMENTATION]  Builds an expected data dict for future regressions

    ${resource} =    Get Resource    ${TYPE}:${NAME}

    ${expected} =    Build_Expected_From_Response.get    ${resource}   parentKey=""  wordy=${True}

    ${nicelyFormated}    json.dumps    ${expected}    indent=${4}

    ${nicelyFormated} =    Replace String    ${nicelyFormated}    null    None
    ${nicelyFormated} =    Replace String    ${nicelyFormated}    true    True
    ${nicelyFormated} =    Replace String    ${nicelyFormated}    false    False

    Run Keyword If    ${VERBOSE}==${True}    Log To Console and Logfile    ${nicelyFormated}

    Return From Keyword    ${expected}    ${nicelyFormated}

Build Data Dict
    [DOCUMENTATION]  Using a pre-created template, build a data dict that can be used to re-create the resource
    [Arguments]    ${template}

    ${Resource} =    Get Resource    ${TYPE}:${NAME}

    ${data_dict} =    Build_Data_Dict.get    ${template}    ${resource}    wordy=${True}

    ${nicelyFormated}    json.dumps    ${data_dict}    indent=${4}

    ${nicelyFormated} =    Replace String    ${nicelyFormated}    null    None
    ${nicelyFormated} =    Replace String    ${nicelyFormated}    true    True
    ${nicelyFormated} =    Replace String    ${nicelyFormated}    false    False

    Run Keyword If    ${VERBOSE}==${True}    Log To Console and Logfile    ${nicelyFormated}

    Return From Keyword    ${data_dict}    ${nicelyFormated}

Build Request Body
    [DOCUMENTATION]  Using a pre-created data dict create a POST requestbody
    [Arguments]    ${data_dict}

    ${responseBody} =    Build_Request_Body.get    ${data_dict}        wordy=${True}

    ${nicelyFormated}    json.dumps    ${responseBody}    indent=${4}

    Run Keyword If    ${VERBOSE}==${True}    Log To Console and Logfile    ${nicelyFormated}

    Return From Keyword    ${responseBody}

Delete Create Resource
    [DOCUMENTATION]  Deletes then attempts to re-create the resource and Validate the Response
    [ARGUMENTS]    ${expected}    ${request_body}

	${resp} =    Delete Resource    ${TYPE}:${NAME}

    Wait For Task2	${resp}		timeout=300		interval=10

    ${resp} =    Create Resource		${TYPE}    ${request_body}

	Wait For Task2	${resp}		timeout=300		interval=10

    ${response} =    Get Resource    ${TYPE}:${NAME}

    ${results} =    Fusion Api Validate Response Follow    ${expected}    ${response}    wordy=${true}

    Should Be Equal    ${results}    ${True}