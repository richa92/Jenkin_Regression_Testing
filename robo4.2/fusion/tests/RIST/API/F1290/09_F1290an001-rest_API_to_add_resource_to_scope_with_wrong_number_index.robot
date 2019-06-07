*** Settings ***
Documentation                   F1290an001-rest API to add resource to scope with wrong number index (negative)
...                                 -patch /rest/hardware/aaaaaxxx [{"op":"add", "path":"/scopeUris/X", "value":"/rest/scopes/59301182-9de1-4db9-a5 }

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

Negative Test Patch - add_resource_to_scope_with_wrong_number_index
	Fusion Api Login Appliance      ${APPLIANCE_IP}  ${admin_credentials}
    ${scope_uri}=                   Get Scope URI    ${test_scope_name}
    log to console and logfile      ${scope_uri}

	#F1290an001-rest API to add resource to scope with wrong number index (negative)
    Set to Dictionary	            ${update_scope_resource}	op=add
    Set to Dictionary	            ${update_scope_resource}	path=/scopeUris/9999
    Set to Dictionary	            ${update_scope_resource}	value=${scope_uri}

    ${enclosure_uri}=               Get Enclosure URI   ${ENC1}
    ${server_uri}=                  Get Server Hardware URI   ${SH1}

    ${body}=                        Create List         ${update_scope_resource}
    ${enclosure}=                   Fusion Api Get Enclosures    ${enclosure_uri}
    ${response_patch}=              Fusion Api Patch Scope    uri=${enclosure_uri}  body=${body}    etag=${enclosure['eTag']}

    log to console                  patch response = ${response_patch}
    Should Be Equal                 '${response_patch["status_code"]}'   '202'    msg= enclosure should allow number dismatch scoep update!!!!!
    ${task}=                        Wait For Task   ${response_patch}
    ${valDict} = 	                Create Dictionary	taskState=Completed
    Validate Response               ${task}    ${valDict}

    log to console and logfile      serverhardware uri= ${server_uri}
    ${server}=                      Fusion Api Get Server Hardware    ${server_uri}
    ${response_patch}=              Fusion Api Patch Scope    uri=${server_uri}  body=${body}    etag=${server['eTag']}
    Should Be Equal                 '${response_patch["status_code"]}'   '400'    msg= Failed to update server hardware resource to scope, path could not resolved!!!!!

    Fusion Api Logout Appliance

