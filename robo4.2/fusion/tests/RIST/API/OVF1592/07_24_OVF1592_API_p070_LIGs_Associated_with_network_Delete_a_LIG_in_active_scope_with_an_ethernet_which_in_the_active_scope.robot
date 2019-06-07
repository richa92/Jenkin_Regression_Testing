*** Settings ***
Documentation        LIGs Associated with network Delete a LIG in active scope with an ethernet which in the active scope
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

Test Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["admin_credentials"]}
Test Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
LIGs Associated with network Delete a LIG in active scope with an ethernet which in the active scope
    [Documentation]  OVF1592 API p070 LIGs Associated with network_Delete a LIG in active scope with an ethernet which in the active scope
    Log    Create the lig LIG5 which contains an active ethernet eth2.  console=True
    ${resp}=   Add LIG from variable async    ${create_LIG_network1}
    Wait For Task2   ${resp}

    Log   Delete Logical interconnect group LIG5    console=True
    Active Permission Session  ${edit_ia_users_permission}    ${credentials['ia_credentials']}
    ${resp}=   Fusion Api Delete Lig    ${new_LIG_name}
    Wait For Task2    ${resp}
    ${URI}=  Get Lig Uri  ${new_LIG_name}
    Should Be Equal  ${URI}  /rest/Logical_interconnect_group_${new_LIG_name}_not_found