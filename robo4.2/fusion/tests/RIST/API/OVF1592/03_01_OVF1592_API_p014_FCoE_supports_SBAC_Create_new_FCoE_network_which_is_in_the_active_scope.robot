*** Settings ***
Documentation        FCoE supports SBAC Create new FCoE network which is in the active scope
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

Test Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["na_credentials"]}
Test Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
FCoE supports SBAC Create new FCoE network which is in the active scope
    [Documentation]  OVF1592 API p014 FCoE supports SBAC Create new FCoE network which is in the active scope

    Log    Creating Networks fcoe5    console=True
    ${resps}=    Add FCoE Networks from variable     ${create_fcoe_network}
    wait for task2  ${resps}
    Validate Resource Assigned/Unassigned To Scope  ${Scope_List[0]}  FCOE:${new_fcoe_name}  ${FALSE}
    Validate Resource Assigned/Unassigned To Scope  ${Scope_List[1]}  FCOE:${new_fcoe_name}  ${TRUE}
