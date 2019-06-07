*** Settings ***
Documentation                   F1290ap002-rest API to create duplicate empty scope
...                               -  post /rest/hardware { "type": "Scope", "name": "MySampleScope", "description": "Sample Scope description" }


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

Create duplicate scope

	Fusion Api Login Appliance          ${APPLIANCE_IP}  ${admin_credentials}

    ${response_create}=                 Fusion Api Create Scope    body=${add_scope_body}


    Should Be Equal                     '${response_create["status_code"]}'   '409'    msg= Failed to create duplicate scope!!!!!
    should contain                      ${response_create}  errorSource
    should contain                      ${response_create}  message
    Should Be Equal                     '${response_create["message"]}'   'A scope with name \'MyRISTScope\' already exists.'    msg= No error message alert!!!!!
    log to console and logfile          ${response_create["message"]}

    Fusion Api Logout Appliance