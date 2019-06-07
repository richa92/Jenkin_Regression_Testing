*** Settings ***
Documentation        Ethernet supports SBAC Bulk creating network which in active scope
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
Ethernet supports SBAC Bulk creating network which in active scope
    [Documentation]  OVF1592 API p007 ethernet supports SBAC Bulk creating network which in active scope

     ${resps}=  Create Bulk Ethernet Networks  ${bulk_create_ethernet}

     Log   check result information    console=True

     Validate Resource Assigned/Unassigned To Scope   ${Scope_List[0]}  ETH:${Bulk_Create_Ethernet[0]["namePrefix"]}_${vlanId[0]}  ${FALSE}
     Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  ETH:${Bulk_Create_Ethernet[0]["namePrefix"]}_${vlanId[0]}  ${TRUE}

     Validate Resource Assigned/Unassigned To Scope   ${Scope_List[0]}  ETH:${Bulk_Create_Ethernet[0]["namePrefix"]}_${vlanId[1]}  ${FALSE}
     Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}   ETH:${Bulk_Create_Ethernet[0]["namePrefix"]}_${vlanId[1]}  ${TRUE}

     Validate Resource Assigned/Unassigned To Scope   ${Scope_List[0]}  ETH:${Bulk_Create_Ethernet[0]["namePrefix"]}_${vlanId[2]}  ${FALSE}
     Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  ETH:${Bulk_Create_Ethernet[0]["namePrefix"]}_${vlanId[2]}  ${TRUE}

     Validate Resource Assigned/Unassigned To Scope   ${Scope_List[0]}  ETH:${Bulk_Create_Ethernet[0]["namePrefix"]}_${vlanId[3]}  ${FALSE}
     Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  ETH:${Bulk_Create_Ethernet[0]["namePrefix"]}_${vlanId[3]}  ${TRUE}

     Validate Resource Assigned/Unassigned To Scope   ${Scope_List[0]}  ETH:${Bulk_Create_Ethernet[0]["namePrefix"]}_${vlanId[4]}  ${FALSE}
     Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  ETH:${Bulk_Create_Ethernet[0]["namePrefix"]}_${vlanId[4]}  ${TRUE}

     Log    deleting all bulk network    console=True
     ${resp}=    Fusion Api Delete Ethernet Network  ${Bulk_Create_Ethernet[0]["namePrefix"]}_${vlanId[0]}
     Wait For Task2  ${resp}
     ${resp}=    Fusion Api Delete Ethernet Network  ${Bulk_Create_Ethernet[0]["namePrefix"]}_${vlanId[1]}
     Wait For Task2  ${resp}
     ${resp}=    Fusion Api Delete Ethernet Network  ${Bulk_Create_Ethernet[0]["namePrefix"]}_${vlanId[2]}
     Wait For Task2  ${resp}
     ${resp}=    Fusion Api Delete Ethernet Network  ${Bulk_Create_Ethernet[0]["namePrefix"]}_${vlanId[3]}
     Wait For Task2  ${resp}
     ${resp}=    Fusion Api Delete Ethernet Network  ${Bulk_Create_Ethernet[0]["namePrefix"]}_${vlanId[4]}
     Wait For Task2  ${resp}
