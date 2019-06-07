*** Settings ***
Documentation                   F1290ap003-rest API to add resource to scope
...                               -  patch /rest/hardware/aaaaaxxx [{"op":"add", "path":"/scopeUris/-", "value":"/rest/scopes/59301182-9de1-4db9-a5 }


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

Update resource to scope - add_resource_to_scope

	Fusion Api Login Appliance      ${APPLIANCE_IP}  ${admin_credentials}

    ${scope_uri}=                   Get Scope URI    ${test_scope_name}
    log to console and logfile      ${scope_uri}
    ${enclosure_uri}=               Get Enclosure URI   ${ENC1}
    ${server_uri}=                  Get Server Hardware URI   ${SH1}

    Set to Dictionary	            ${update_scope_resource}	op=add  value=${scope_uri}

    ${body}=                        Create List         ${update_scope_resource}
    ${enclosure}=                   Fusion Api Get Enclosures    ${enclosure_uri}
    ${response_patch}=              Fusion Api Patch Scope    uri=${enclosure_uri}  body=${body}    etag=${enclosure['eTag']}
    ${task}=                        Wait For Task   ${response_patch}
    ${valDict} = 	                Create Dictionary	taskState=Completed
    Validate Response               ${task}    ${valDict}


    log to console                  patch response = ${response_patch}
    Should Be Equal                 '${response_patch["status_code"]}'   '202'    msg= Failed to update enclosure resource to scope!!!!!

    log to console and logfile      serverhardware uri= ${server_uri}
    ${server}=                      Fusion Api Get Server Hardware    ${server_uri}
    ${response_patch}=              Fusion Api Patch Scope    uri=${server_uri}  body=${body}    etag=${server['eTag']}
    Should Be Equal                 '${response_patch["status_code"]}'   '202'    msg= Failed to update server hardware resource to scope!!!!!
    ${task}=                        Wait For Task   ${response_patch}
    ${valDict} = 	                Create Dictionary	taskState=Completed
    Validate Response               ${task}    ${valDict}

    Fusion Api Logout Appliance