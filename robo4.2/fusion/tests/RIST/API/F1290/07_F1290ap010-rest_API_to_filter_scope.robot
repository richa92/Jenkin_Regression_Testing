*** Settings ***
Documentation                   F1290ap010-rest API to filter scope, to clear
...                               -  get /rest/index/


Library				FusionLibrary
Library			    RoboGalaxyLibrary
Library  			BuiltIn
Library				Collections
Library             json
Resource            ./../../../../Resources/api/fusion_api_resource.txt
Resource            ./scope.txt

Variables  			${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}     unknown
${DATA_FILE}        ./Regression_Data.py

*** Test Cases ***

Update resource to scope - filter_scope

	Fusion Api Login Appliance      ${APPLIANCE_IP}  ${admin_credentials}
    #Delete Scope     ${scopes}         ${Verify}=${True}   ${Status_Code}=202

    ${scope_uri}=                   Get Scope URI    ${test_scope_name}
    ${response_create}=             fusion api get scope     ${scope_uri}

    Should Be Equal                 '${response_create["status_code"]}'   '200'    msg= get scope!!!!!

    Fusion Api Logout Appliance
