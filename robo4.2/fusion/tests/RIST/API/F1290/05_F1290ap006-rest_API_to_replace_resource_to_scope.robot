*** Settings ***
Documentation                   F1290ap006-rest API to replace resource to scope
...                               -  patch /rest/hardware/aaaaaxxx [{"op":"replace", "path":"/scopeUris/-"}


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

Update resource to scope - replace_resource

	Fusion Api Login Appliance      ${APPLIANCE_IP}  ${admin_credentials}

	${resp}=                        Get Enclosure    ${ENC1}
	${enclosure_scope}=             Set Variable  ${resp["scopeUris"]}
	log to console                  "enclosure original scope=" ${enclosure_scope}

    ${scope_uri}=                   Get Scope URI    ${test_scope_name}
    Append To List                  ${enclosure_scope}    ${scope_uri}
    log to console                  "enclosure change scope=" ${enclosure_scope}

    ${enclosure_uri}=               Get Enclosure URI   ${ENC1}
    ${server_uri}=                  Get Server Hardware URI   ${SH1}

    Set to Dictionary	            ${update_scope_resource}	op=replace  path=/scopeUris
    Set to Dictionary	            ${update_scope_resource}	value=${enclosure_scope}
    log to console                  ${update_scope_resource}
    ${body}=                        Create List         ${update_scope_resource}
    ${enclosure}=                   Fusion Api Get Enclosures    ${enclosure_uri}
    ${response_patch}=              Fusion Api Patch Scope    uri=${enclosure_uri}  body=${body}    etag=${enclosure['eTag']}
    Should Be Equal                 '${response_patch["status_code"]}'   '202'    msg= Failed to update enclosure resource to scope!!!!!
    ${task}=                        Wait For Task   ${response_patch}
    ${valDict} = 	                Create Dictionary	taskState=Completed
    Validate Response               ${task}    ${valDict}

    log to console                  ${enclosures[0]["deviceBays"][0]["deviceUri"]}
    ${server}=                      Fusion Api Get Server Hardware    ${server_uri}
    ${response_patch}=              Fusion Api Patch Scope    uri=${server_uri}  body=${body}    etag=${server['eTag']}
    Should Be Equal                 '${response_patch["status_code"]}'   '202'    msg= Failed to update server hardware resource to scope!!!!!
    ${task}=                        Wait For Task   ${response_patch}
    ${valDict} = 	                Create Dictionary	taskState=Completed
    Validate Response               ${task}    ${valDict}

    Fusion Api Logout Appliance