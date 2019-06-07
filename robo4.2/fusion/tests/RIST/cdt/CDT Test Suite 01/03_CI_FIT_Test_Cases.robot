*** Settings ***
Library             Collections
Resource            ../resource.txt
Resource            ../../../../Resources/api/settings/appliance_networking.txt
Documentation       CDT CI-FIT Test Cases.
Suite Setup         Setup for CI-FIT
Suite Teardown      CI FIT Execution PostConditions

# Setup\Teardown for ALL test cases
Test Setup      Test Setup
Test Teardown   Test Teardown



*** Test Cases ***
Update server profile from template test
    [Documentation]     Implementation of Update server profile from template
     Edit Server Profile template from variable      ${profile_template_list}
     verify server profile error alert
     SP Compliance check  ${sp_name}  NonCompliant
     ${resplist}=  Update Server Profiles from Template     ${sp_name_update}
     Wait For Task2  ${resplist}   timeout=600    interval=10
     verify server profile error alert
     SP Compliance check  ${sp_name}  Compliant

#Reapply LI Configuration
#   [Documentation]     Reapply Logical Interconnect Configurations and validate
#   pass execution      Not implemented yet.

Server rip and replace
    [Documentation]    server rip and replace test
    ${item}    Select list Item Randomly    ${rhel_server_ips}
    ${p_name}    Get dictionary keys    ${item}
    ${values}    Get dictionary values    ${item}
    ${hardware}    Set variable    ${assigned_sp_to_bay_map['${p_name[0]}']}
    Log    ${hardware}    console=True
    ${bay}    Fetch from right    ${hardware}    ${SPACE}
    ${enc}    Fetch from left    ${hardware}    ,
    ${EM_IP}    Get EM IP    ${enc}
    ${EM_TOKEN}    Get EM Token    ${enc}
    EFuse Blade    EFuseOn     ${bay}
    ${task} =  Get Task By Param  param=?filter='name'='Remove' AND associatedResource.resourceName='${hardware}'&sort=created:descending&count=1
    Wait for task2  ${task}  timeout=600  interval=10
    ${t}     Get Appliance Time and Locale
    EFuse Blade    EFuseOff    ${bay}
    Wait Until Keyword Succeeds  300s  5ms  Get task by param  param=?filter='name'='Add' AND associatedResource.resourceName='${hardware}' AND taskState='Running'
    ${task} =  Get Task By Param  param=?filter='name'='Add' AND associatedResource.resourceName='${hardware}' AND taskState='Running'
    Wait for task2  ${task}  timeout=1200  interval=10
    ${ping_status}=     Run And Return RC   ping ${values[0]['name']} -n 1
    Run keyword if    ${ping_status}!=0    FAIL    Pinging OS failed
    ${resp} =     Fusion Api Get Server Hardware    param=?filter="'name'=='${hardware}'"
    Run keyword If    ${resp['count']}==0  FAIL    Server hardware not_found
    Run keyword and continue on failure     Check Any Active Alerts on resources    ${resp}     ${t['dateTime']}
    ${dport_list}    Create list
    :FOR    ${each}    in    @{resp['members'][0]['portMap']['deviceSlots']}
    \    ${intp}    Gather interconnect uri and port number and status    ${each['physicalPorts']}
    \    ${dport_list}    combine lists    ${dport_list}    ${intp}
    ${mlist}    Create list
    :FOR    ${entry}    in    @{dport_list}
    \    Run keyword if    '${entry['port_status']}'=='Unlinked'    Append to list    ${mlist}    ${entry}
    ${len}    Get length    ${mlist}
    Run keyword if    ${len}!=0    FAIL    ${len} downlink ports are unlinked.

Failover of Natasha Interconnect
    [Documentation]     Trigger Natasha ICM failover and verify behavior
    [Tags]              effuseNatasha
    #[Setup]            Failover Setup
    :FOR    ${natasha_li}    IN    @{NATASHA_LIs}
    \       Initialize Natasha Effuse Test Variables    ${natasha_li}
    \       Perform ICM Failover    ${testvar_encl_natasha}                  ${testvar_low_bay}
    \       ...                     ${testvar_li_after_effuse_on}
    \       ...                     ${testvar_li_after_effuse_off}
    \       ...                     ${testvar_natasha_lowbay_icm_after_effuse_on}
    \       ...                     ${testvar_natasha_after_effuse_off}      ${None}    SAS
    \       Perform ICM Failover    ${testvar_encl_natasha}                  ${testvar_high_bay}
    \       ...                     ${testvar_li_after_effuse_on}
    \       ...                     ${testvar_li_after_effuse_off}
    \       ...                     ${testvar_natasha_highbay_icm_after_effuse_on}
    \       ...                     ${testvar_natasha_after_effuse_off}     ${None}     SAS
    #[Teardown]             Failover Teardown


Failover of Carbon Interconnect
    [Documentation]     Trigger Carbon ICM failover and verify behavior
    [Tags]              effuseCarbon
    #[Setup]            Failover Setup

    Initialize Carbon Effuse Test Variables                         ${CARBON_LI}
    Perform ICM Failover    ${testvar_encl_carbon}                  ${testvar_low_bay}
    ...                     ${testvar_li_after_effuse_on}
    ...                     ${testvar_li_after_effuse_off}
    ...                     ${testvar_carbon_lowbay_icm_after_effuse_on}
    ...                     ${testvar_carbon_after_effuse_off}      ${testvar_sp_carbon_pat_list_lowbay}
    ...                     Carbon    
    Perform ICM Failover    ${testvar_encl_carbon}                  ${testvar_high_bay}
    ...                     ${testvar_li_after_effuse_on}
    ...                     ${testvar_li_after_effuse_off}
    ...                     ${testvar_carbon_highbay_icm_after_effuse_on}
    ...                     ${testvar_carbon_after_effuse_off}      ${testvar_sp_carbon_pat_list_highbay}
    ...                     Carbon
    #[Teardown]             Failover Teardown

Failover of Potash Interconnect
    [Documentation]     Trigger Potash ICM failover and verify behavior
    [Tags]              effusePotash
    #[Setup]            Failover Setup

    Initialize Potash Effuse Test Variables                     ${POTASH_LI}
    Perform ICM Failover    ${testVar_enc1}                     ${testvar_low_bay}
    ...                     ${testvar_li_after_effuse_on}
    ...                     ${testvar_li_after_effuse_off}
    ...                     ${testvar_kcl_lowbay_icm_after_effuse_on}
    ...                     ${testvar_kcl_after_effuse_off}     ${testvar_sp_kcl_alert_pat_list_lowbay}     Potash
    Perform ICM Failover    ${testVar_enc2}                     ${testvar_high_bay}
    ...                     ${testvar_li_after_effuse_on}
    ...                     ${testvar_li_after_effuse_off}
    ...                     ${testvar_kcl_highbay_icm_after_effuse_on}
    ...                     ${testvar_kcl_after_effuse_off}     ${testvar_sp_kcl_alert_pat_list_highbay}    Potash
    #[Teardown]             Failover Teardown

HA Cluster Validation
    [Documentation]     Cluster Synchronization Validation
    ${CIM_count}=       Get Existing CIManager Presence Count
    Run Keyword If      ${CIM_count} == 2    cluster synchronization validation
    ...                 ELSE                Log     No standby appliance found. Skipping "HA Cluster Validation" test case.
    ...                 level=WARN

Failover of Synergy Composer
    [Documentation]     Trigger failover of Synergy Composer (CIM) and verify behavior.
    [Tags]              Appliance_Failover
    ${roles}=           Get HA Nodes
    ${num_ci_mgrs}=     Get Length              ${roles}
    Run Keyword If      ${num_ci_mgrs} > 1      CIM Failover
    ...                 ELSE                    Log
    ...                 No standby appliance found. Skipping "Failover of Synergy Composer" test case.
    ...                 level=WARN

#Rip and Replace Server
#   [Documentation]     Rip and Replace Servers and verify behavior
#   pass execution      Not implemented yet.

#Failover Frame Link Module
#   [Documentation]     Trigger Failover of Frame Link Module (EM) and verify behavior
#   pass execution      Not implemented yet.

#Failover TOR IRF
#   [Documentation]     Trigger Failover of TOR IRF and verify behavior
#   pass execution      Not implemented yet.
#

Edit LIG and LI Update from group along with consistency check
    [Documentation]             Performing the edit LIG and LI update from group
    [Tags]                      EDIT_SP_LI_UPDATEFROMGROUP
    ${Net_2200} =               Get Variable Value      ${Net_2200}
    Run Keyword If              ${Net_2200} is not ${null}                      Add Ethernet Networks from variable async
    ...                         ${Net_2200}
    ${lig_uri}=                 Get LIG URI             ${PotashLIG['name']}
    ${networks} =               Get From Dictionary     ${Ethernet_Tagged_new}                  networkUris
    ${ethernetUris} =           Get Ethernet URIs       ${networks}
    ${Ethernet_Tagged_us_old}=                          Get From Dictionary     ${potash_us}    Ethernet-Tagged
    ${networks_1} =             Get From Dictionary     ${Ethernet_Tagged_us_old}               networkUris
    ${ethernetUris_1} =         Get Ethernet URIs       ${networks_1}
    ${network_combined} =       combine lists           ${networks_1}           ${networks}
    Set to dictionary           ${Ethernet_Tagged_us_old}                       networkUris=${network_combined}
    Set to dictionary           ${potash_us}            Ethernet-Tagged=${Ethernet_Tagged_us_old}
    ${potash_dict_values} =     Get Dictionary Values   ${potash_us}
    Set to dictionary           ${PotashLIG}            uplinkSets=${potash_dict_values}
    ${body} =                   Build LIG Body          ${PotashLIG}
    ${resp_edit}=               Fusion API Edit LIG     ${body}                 ${lig_uri}
    ${task} =                   Wait For Task           ${resp_edit}            120s            10s
    ${valDict} =                Create Dictionary       status_code=${200}
    ...                         taskState=Completed
    Validate Response           ${task}                 ${valDict}
    Update Logical Interconnect from Group              ${LI}
    Update Network Set          ${network_sets_update_add}

#Power Outage
#   [Documentation]     Trigger a Power Outage on the System Under Test and verify behavior.
#   pass execution      Not implemented yet.


*** Keywords ***

Setup for CI-FIT
    [Documentation]     Pre-conditions for CDT Test Suite to prevent test executions if Setup/Initial Config fails.
    ...                 Initial Configuration Suite should pass.
    ...                 Environment Validation should pass.
    #Should be true      ${initialConfigSuccess}     Initial Configuration failed to complete successfully.
    Validate Environment

CI FIT Execution PostConditions
    [Documentation]    CI FIT Suite Post execution condition status check
    Set Global variable     ${ciFitSuiteSuccess}     ${None}
    Run Keyword If      '${SUITE_STATUS}' == 'PASS'     Set Global variable     ${ciFitSuiteSuccess}     ${TRUE}
