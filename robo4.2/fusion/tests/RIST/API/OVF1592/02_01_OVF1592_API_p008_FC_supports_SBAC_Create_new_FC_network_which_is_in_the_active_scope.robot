*** Settings ***
Documentation        FC supports SBAC Create new FC network which is in the active scope
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
FC supports SBAC Create new FC network which is in the active scope
    [Documentation]  OVF1592 API p008 FC supports SBAC Create new FC network which is in the active scope

    Log    Creating Networks    console=True
    ${resps}=      Add FC Networks from variable async  ${create_fc_network}

    Log    Check scopes information    console=True
    Validate Resource Assigned/Unassigned To Scope  ${Scope_List[0]}  FC:${new_fc_name}  ${FALSE}
    Validate Resource Assigned/Unassigned To Scope  ${Scope_List[1]}  FC:${new_fc_name}  ${TRUE}
