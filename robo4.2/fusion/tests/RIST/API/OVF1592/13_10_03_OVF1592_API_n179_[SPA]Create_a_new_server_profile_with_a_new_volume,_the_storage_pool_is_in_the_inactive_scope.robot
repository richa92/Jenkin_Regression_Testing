*** Settings ***
Documentation        Create a new server profile with a new volume, the storage pool is in the inactive scope
Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              copy
Library              Collections
Library              String
Library              json
Library              XML
Library              SSHLibrary
Library              Dialogs
Variables            ${DATA_FILE}
Resource             ./../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt

Test Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["spa_credentials"]}
Test Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
[SPA] - Create a new server profile with a new volume, the storage pool is in the inactive scope
    [Documentation]  OVF1592_UI_n179 [Server Profile Administrator] Create a new server profile with a new volume, the storage pool is in the inactive scope
    Log     Create new server profiles sp5 with new volume active pool4      console=True
    ${resp}=  Add Server Profile  ${create_server_profile_pool3}    param=?force=ignoreServerHealth,ignoreSANWarnings
    Wait For Task2   ${resp}   timeout=600    PASS=Error  errorMessage=${ASSOCIATION_FORBIDDEN_BY_SCOPE}    VERBOSE=True
    ${sp_uri}=  Get Server Profile Uri  ${new_sp_name}
    should be equal  ${sp_uri}  /rest/server_profile_uri_${new_sp_name}_not_found
