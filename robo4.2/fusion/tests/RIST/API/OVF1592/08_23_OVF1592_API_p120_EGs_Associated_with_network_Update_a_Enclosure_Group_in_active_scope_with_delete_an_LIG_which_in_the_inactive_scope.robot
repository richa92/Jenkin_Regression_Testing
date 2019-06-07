*** Settings ***
Documentation        Enclosure Groups Associated with network_Update a Enclosure Group in active scope with delete an LIG which in the inactive scope
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
Enclosure Groups Associated with network_Update a Enclosure Group in active scope with delete an LIG which in the inactive scope
    [Documentation]  OVF1592 API p120 Enclosure Groups Associated with network_Update a Enclosure Group in active scope with delete an LIG which in the inactive scope

    Log   ADD lig3 to EG5     console=True
    ${resps}=  Edit Enclosure Group    ${Edit_EG8}
    Wait For Task2   ${resps}
    Logout Appliance

    Log   remove lig4 from EG5     console=True
    Active Permission Session  ${edit_sa_users_permission}    ${credentials['sa_credentials']}
    ${resps}=  Edit Enclosure Group    ${Edit_EG3}
    Wait For Task2   ${resps}   timeout=60
