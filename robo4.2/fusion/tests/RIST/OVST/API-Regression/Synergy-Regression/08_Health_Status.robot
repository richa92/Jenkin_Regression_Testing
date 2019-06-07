*** Settings ***
Resource    resource.txt
Documentation    Health check for OneView by performing
...              EFuse Action on Server Blade with and without Server Profile
...              Injecting Fan and Power Failures in EM
...              Performing SNMP trap to get alerts on OneView
Suite Setup   Run Keywords  QUAL Suite Setup    ${admin_credentials}  AND  Login to Fusion via SSH

*** Test Cases ***
EFuse Action on Server Blade with and without Server Profile and removing the Server Profile
    [TAGS]  EFUSE
    [Documentation]  EFuse Action on Server Blade with and without Server Profile
    # Power off ALL servers
    ${enc_serial} =  Set variable  ${health_status['enc_serial']}
    ${efuse_action} =  Set variable  ${health_status['efuse_action']}
    ${efuse_bay_number} =  Set variable  ${health_status['efuse_bay_number']}
    Get EM IP   ${enc_serial}
    Get EM Token  ${enc_serial}
    # Efuse action on server blade before server profile creation
    EFuse Blade  ${efuse_action}  ${efuse_bay_number}
    Sleep  ${EFUSE_SLEEP}
    Power off ALL servers   control=PressAndHold
    ${responses}=  Add Server Profiles from variable  ${efuse_server_profile}
    Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}
    ...  timeout=1200  interval=5
    Verify Resources for List  ${expected_efuse_server_profile}
    # Efuse action on server blade after server profile creation
    EFuse Blade  ${efuse_action}  ${efuse_bay_number}
    ${responses}=  Remove Server Profiles from variable  ${efuse_server_profile}
    Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}
    ...  timeout=1200  interval=5

Inject Fan Failures and verifying the Log events
    [TAGS]  FAN
    [Documentation]  Inject fan failure in EM and verifying the Log events
    : FOR  ${fan}  IN  @{fan_failures}
    \  ${enc_serial} =  Set variable  ${fan['enc_serial']}
    \  ${fan_action} =  Set variable  ${fan['fan_action']}
    \  ${fan_bay_number} =  Set variable  ${fan['fan_bay_number']}
    \  ${fan_fault_type} =  Set variable  ${fan['fan_fault_type']}
    \  ${inject_failure} =  Set variable  ${fan['inject_failure']}
    \  ${filter} =  Set variable  ${fan['filter']}
    \  Get EM IP   ${enc_serial}
    \  Get EM Token  ${enc_serial}
    \  EM Diags Fault Injection    ${fan_action}    ${fan_bay_number}    ${fan_fault_type}    ${inject_failure}
    \  Sleep  ${EFUSE_SLEEP}
    \  ${fan_event}=  EM Diags Get Audit Log Events  ${EM_IP}  ${EM_TOKEN}  ${filter}
    \  ${state}=  Run Keyword If  '${inject_failure}' == 'true'  Get Regexp Matches  '${fan_event}'  emRegistry.1.0.FanFault
    ...  ELSE  Get Regexp Matches  '${fan_event}'  emRegistry.1.0.FanFaultCleared
    \  Run Keyword If  "${state}" == "[]"  FAIL  msg=FAN failure has failed

Inject Power Failures and verifying the Log events
    [TAGS]  POWER
    [Documentation]  Inject power failure in EM and verifying the Log events
    : FOR  ${power}  IN  @{power_failures}
    \  ${enc_serial} =  Set variable  ${power['enc_serial']}
    \  ${power_action} =  Set variable  ${power['power_action']}
    \  ${power_bay_number} =  Set variable  ${power['power_bay_number']}
    \  ${power_fault_type} =  Set variable  ${power['power_fault_type']}
    \  ${inject_failure} =  Set variable  ${power['inject_failure']}
    \  ${filter} =  Set variable  ${power['filter']}
    \  Get EM IP   ${enc_serial}
    \  Get EM Token  ${enc_serial}
    \  EM Diags Fault Injection    ${power_action}    ${power_bay_number}    ${power_fault_type}    ${inject_failure}
    \  Sleep  ${EFUSE_SLEEP}
    \  ${power_event}=  EM Diags Get Audit Log Events  ${EM_IP}  ${EM_TOKEN}  ${filter}
    \  ${state}=  Run Keyword If  '${inject_failure}' == 'true'  Get Regexp Matches  '${power_event}'  emRegistry.1.0.PowerInputFault
    ...  ELSE  Get Regexp Matches  '${power_event}'  emRegistry.1.0.PowerInputFaultCleared
    \  Run Keyword If  "${state}" == "[]"  FAIL  msg=Power failure has failed

Setting up SNMP Trap and verifying the alerts after creating Server Profiles and removing the Server Profiles
    [TAGS]  SNMP
    [Documentation]  Setting up SNMP Trap and verifying the alerts after creating Server Profiles and removing the Server Profiles
    ${responses}=  Add Server Profiles from variable  ${snmp_server_profile}
    Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}
    ...  timeout=1200  interval=5
    Verify Resources for List  ${expected_snmp_server_profile}
    Remove All Alerts
    ${alert_uri} =  Create Dictionary
    : FOR  ${snmp}  IN  @{snmp_trap}
    \  ${trap_tool_path} =  Set variable  ${snmp['trap_tool_path']}
    \  ${source_server_hardware_name} =  Set variable  ${snmp['source_server_hardware_name']}
    \  ${source_server_hardware} =  Set variable  ${snmp['source_server_hardware']}
    \  ${trap_name} =  Set variable  ${snmp['trap_name']}
    \  ${trap_value} =  Set variable  ${snmp['trap_value']}
    \  Run  powershell ${trap_tool_path} -d ${appliance_ip} -a ${source_server_hardware} -t ${trap_name} -v ${trap_value}
    \  ${alerts}=  Get Alert by Param   param=?filter=alertTypeID like 'Trap.${trap_name}'
    \  Run Keyword If  '${alerts['alertState']}' != 'Active'  FAIL  msg=Alert is not active
    \  Run Keyword If  '${trap_name}' == 'cpqHe4FltTolPowerSupplyFailed'  Set To Dictionary  ${alert_uri}  uri=${alerts['uri']}
    \  ${resp} =  Fusion Api Get Server Hardware  param=?filter="'name'=='${source_server_hardware_name}'"
    \  Run Keyword If  '${resp['members'][0]['status']}' == 'Ok'  FAIL  msg=Trap is not set for Server Hardware
    Clear Alert  ${alert_uri}
    Sleep  ${EFUSE_SLEEP}
    ${resp} =   Fusion Api Get Server Hardware  param=?filter="'name'=='${source_server_hardware_name}'
    Run Keyword If  '${resp['members'][0]['status']}' == 'Warning'  Remove All Alerts  param=?filter=description like 'The Advanced Memory Protection subsystem has engaged the LockStep memory.'
    ${responses}=  Remove Server Profiles from variable  ${snmp_server_profile}
    Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}
    ...  timeout=1200  interval=5