*** Settings ***
Documentation        Scopes Support Scope Remove Scope resources scopes via Scope Interface
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

Test Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["sa_credentials"]}
Test Teardown        Logout Appliance


*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Scopes supports SBAC Create new Scope which is in the active scope
    [Documentation]  OVF1592 API p130 Scopes supports SBAC Create new Scope which is in the active scope
    Log  Create scope5 with scope Test
    ${resp}=   Create Scope   ${create_scope2}
    Wait For Task2  ${resp}
    Validate Resource Assigned/Unassigned To Scope    ${Scope_List[1]}  Scope:${new_scope_name2}   ${TRUE}

    ${resp}=  Remove Scope By Name   ${new_scope_name2}
    Wait For Task2   ${resp}
