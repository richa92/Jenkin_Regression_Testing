*** Settings ***
Documentation        Server Profiles supports SBAC Update a SP scope which is the inactive scope
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

Test Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["ia_credentials"]}
Test Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Server Profiles supports SBAC Update a SP scope which is the inactive scope

    Log   Add scope3 for SP4     console=True
    ${resp}=  Patch Resources Scopes   SP:${sp_list[3]}   ${Patch_add_Scope5}
    Wait For Task2   ${resp}   timeout=60   PASS=Error  errorMessage=${NOT_AUTHORIZED_ERROR}    VERBOSE=True
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[2]}  SP:${sp_list[3]}   ${True}
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[5]}  SP:${sp_list[3]}   ${False}
