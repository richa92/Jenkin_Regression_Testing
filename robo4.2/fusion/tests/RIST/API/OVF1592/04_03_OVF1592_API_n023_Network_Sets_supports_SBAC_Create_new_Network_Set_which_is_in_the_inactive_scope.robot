*** Settings ***
Documentation        Network Sets supports SBAC Create new Network Set which is in the inactive scope
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
Network Sets supports SBAC Create new Network Set which is in the inactive scope
    [Documentation]  OVF1592 API n023 Network Sets supports SBAC Create new Network Set which is in the inactive scope

    Log    Creating Network net-set6 with Stage scope   console=True
    ${resp}=     Add Networks Sets from variable async  ${create_network_set2}    status_code=403

    ${resps}=    Get Network Set URI    ${new_NS_name2}
    should be equal  '${resps}'    '/rest/network_set_uri_${new_NS_name2}_not_found'  msg=Create new NS which is in the inactive is faild
