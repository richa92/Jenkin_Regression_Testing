*** Settings ***
Documentation        Update a server profile with a new volume, the storage pool is in the inactive scope
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

Test Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["spo_credentials"]}
Test Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
[SPO] - Update a server profile with a new volume, the storage pool is in the inactive scope
    [Documentation]  OVF1592_UI_n183 [Server Profile Operator] Update a server profile with a new volume, the storage pool is in the inactive scope

    Log     Edit server profiles sp2 with new volume active pool4      console=True
    ${resp}=  Edit Server Profile  ${Edit_server_profile_pool3}    param=?force=ignoreServerHealth,ignoreSANWarnings
    Wait For Task2   ${resp}   timeout=600   PASS=Error  errorMessage=${ASSOCIATION_FORBIDDEN_BY_SCOPE}    VERBOSE=True
