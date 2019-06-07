*** Settings ***
Library             RoboGalaxyLibrary
Resource            ../resource.txt
Resource            ../resource_i3s_clrm.robot
Documentation       CLRM
Suite Setup         Set log level    TRACE

# Setup\Teardown for ALL test cases
Test Setup      Test Setup
Test Teardown   Test Teardown

*** Test Cases ***

Add Hypervisor Managers
    [Documentation]    Add Hypervisor Manager
    ${HM_IP}=    Get From Dictionary        ${Hypervisor_manager[0]}        name
    Import Certificate to OV    ${HM_IP}        ${APPLIANCE_IP}    ${admin_credentials}        Vcenter
    Add Hypervisor Manager    ${Hypervisor_manager}    True    202

Create Hyperv Server Profile Templates
       [Tags]              CREATE_HYPERV_SPTS
       [Documentation]     Create Hypervisor Server Profile Templates
       Assign Sht To Server Profile Template    ${hyperv_spts}
       ${spts_list} =    Evaluate    copy.deepcopy(${hyperv_spts})    modules=copy
       ${resplist}=    Run Keyword for List    ${spts_list}    Add Server Profile Template

       ${resp}=    Run Keyword for List    ${resplist}    Wait for Task2    timeout=5m    interval=10 

Create Hypervisor Cluster Profiles
    [Documentation]    Create Hypervisor cluster profiles 
    [Tags]    Create_HCP
    ${server_list} =    Create List
    :FOR    ${profile}    IN    @{hyperv_cluster_profiles}
    \    ${servers} =    Get Host List   ${profile}
    \    ${len} =    Get Length    ${servers}
    \    ${server_list} =    Run Keyword If    ${len} > 0    Combine Lists    ${server_list}    ${servers}
    \    ...                          ELSE     ${server_list}
    Power Off Servers Async    ${server_list}    control=PressAndHold  
    ${profnamelist}    ${proflist} =    Add Cluster Profiles     ${hyperv_cluster_profiles}
    Perform Post HCP Creation Validations    ${profnamelist}    ${proflist}

Compliance Between Edit SPT and HCP
    [Documentation]     Updating an existing connection in SPT with a new network uri
    ...     should cause inconsistency Between SPT and HCP
    Remediation Between Edit SPT and HCP    ${HCP_Profiles_for_edit_SPT}

Compliance Between Del_conn SPT and HCP
    [Documentation]     Deleting the existing connection in server profile template should cause
    ...     inconsistency between SPT and HCP
    Remediation Between Delete_conn SPT and HCP    ${HCP_Profiles_for_del_add_SPT}

Complaince Between Add_conn SPT and HCP
    [Documentation]     Adding the new connection in server profile template should cause
    ...     inconsistency between SPT and HCP
    Remediation Between Add_conn SPT and HCP    ${HCP_Profiles_for_del_add_SPT}

Compliance Between Edit SP and HCP
    [Documentation]     Cahnge Bandwidth of an existing connection in SP
    ...     should cause inconsistency in HCP and HP
    Remediation Between Edit SP and HCP    ${HCP_Profiles_for_edit_SP}

Compliance Between Del_conn SP and HCP
   [Documentation]     Deleting the existing connection in server profile should cause
   ...     inconsistency with state "HostProfileInconsistent"
   Remediation Between Delete_conn SP and HCP    ${HCP_Profiles_for_del_conn_SP}

Complaince Between Add_Vol SPT and HCP
    [Documentation]     Add Extra volume in SPT should cause inconsistency
    Remediation Between Add_Vol SPT and HCP    ${HCP_Profiles_for_add_vol_SPT}
