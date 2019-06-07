*** Settings ***
Documentation                   F1290an003-rest API to add resource to scope with wrong alphabetindex (negative)
...                                 -patch /rest/hardware/aaaaaxxx [{"op":"add", "path":"/scopeUris/a", "value":"/rest/scopes/59301182-9de1-4db9-a5 }


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

Negative Test Patch - add_resource_to_scope_with_wrong_alphabetindex
	Fusion Api Login Appliance      ${APPLIANCE_IP}  ${admin_credentials}
    ${scope_uri}=                   Get Scope URI    ${test_scope_name}
    log to console and logfile      ${scope_uri}

    Set to Dictionary	            ${update_scope_resource}	op=add
    Set to Dictionary	            ${update_scope_resource}	path=/scopeUris/aa
    Set to Dictionary	            ${update_scope_resource}	value=${scope_uri}

    ${enclosure_uri}=               Get Enclosure URI   ${ENC1}
    ${server_uri}=                  Get Server Hardware URI   ${ENC1SHBAY1}

    ${body}=                        Create List         ${update_scope_resource}
    ${enclosure}=                   Fusion Api Get Enclosures    ${enclosure_uri}
    ${response_patch}=              Fusion Api Patch Scope    uri=${enclosure_uri}  body=${body}    etag=${enclosure['eTag']}

    log to console                  patch response = ${response_patch}
    Should Be Equal                 '${response_patch["status_code"]}'   '400'    msg= enclosure should not allow alphabetindex dismatch scoep update!!!!!
    Should Contain                  ${response_patch}  errorCode

    log to console and logfile      serverhardware uri= ${server_uri}
    ${server}=                      Fusion Api Get Server Hardware    ${server_uri}
    ${response_patch}=              Fusion Api Patch Scope    uri=${server_uri}  body=${body}    etag=${server['eTag']}
    Should Be Equal                 '${response_patch["status_code"]}'   '400'    msg= Failed to update server hardware resource to scope, path could not resolved!!!!!
    Should Contain                  ${response_patch}  errorCode

    Fusion Api Logout Appliance

