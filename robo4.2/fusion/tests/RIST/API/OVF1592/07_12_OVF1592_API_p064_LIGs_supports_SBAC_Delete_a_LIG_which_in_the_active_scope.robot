*** Settings ***
Documentation        Logical Interconnect Groups supports SBAC_Delete a LIG which in the active scope
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
Logical Interconnect Groups supports SBAC Delete a LIG which in the active scope
    [Documentation]  OVF1592 API p0654Logical Interconnect Groups supports SBAC Delete a LIG which in the active scope

    Log   Can delete LIG5    console=True

    ${resp}=    Delete Resource    LIG:${new_LIG_name}
    Wait For Task2  ${resp}
    ${lig_uri_result}=    Get LIG Uri  ${new_LIG_name}
    Should Contain  '${lig_uri_result}'   '/rest/Logical_interconnect_group_${new_LIG_name}_not_found'
