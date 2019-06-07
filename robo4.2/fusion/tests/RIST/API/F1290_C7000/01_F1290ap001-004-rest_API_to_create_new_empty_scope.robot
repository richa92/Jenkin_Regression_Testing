*** Settings ***
Documentation                   F1290ap001 rest API to create new empty scope
...                                 -post /rest/hardware { "type": "Scope", "name": "MySampleScope", "description": "Sample Scope description" }


Library				FusionLibrary
Library			    RoboGalaxyLibrary
Library  			BuiltIn
Library				Collections
Library             json
Resource            ./../../../../Resources/api/fusion_api_resource.txt
Variables  			${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}     unknown
${DATA_FILE}        ./Regression_Data.py

*** Test Cases ***
Create setting scope
    Log to Console and Logfile      \n- Logging in OneView appliance
	Fusion Api Login Appliance      ${APPLIANCE_IP}  ${admin_credentials}

	Log To Console                  Remove the scope if exists...
    ${resp_uri}=                    Get Scope URI By Name  ${test_scope_name}
    ${task}=                        Run Keyword If    '${resp_uri}' != '/bad_scope_uri'
    ...                             Fusion Api Delete Scope  ${resp_uri}
    Run Keyword If                  ${task} is not ${None}    Wait For Task2  ${task}  timeout=60


    ${response_create}=             Fusion Api Create Scope    body=${add_scope_body}
    Should Be Equal                 '${response_create["status_code"]}'   '202'    msg= Failed to create scope!!!!!${response_create}
    Wait For Task2      ${response_create}
    ${resp_uri}=                Get Scope URI By Name  ${test_scope_name}
    Should Not Be Equal                 ${resp_uri}   /bad_scope_uri    msg= Failed to create scope!!!!!

    Fusion Api Logout Appliance

