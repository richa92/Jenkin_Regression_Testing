| *** Settings *** |
| Documentation | OVF411 - Carbon trunking. |
| Library | json |
| Library | FusionLibrary |
| Library |	RoboGalaxyLibrary |
| Library | Collections |
| Library | String |
| Library | BuiltIn |
| Library | SSHLibrary |
| Variables | data_variables.py |
| Resource | ../../../resources/resource.txt |

| *** Test cases *** |
| Step1 Create SessionID through API | [Documentation] | Creating the session ID through rest calls |
| | Set Log Level | TRACE |
| | ${Login_response} | Fusion Api Login Appliance | ${APPLIANCE_IP} | ${admin_credentials} |
| | Run keyword unless | ${Login_response[0]['status_code']}== 200 | Fail | ${Login_response[0]['message']} |
| | Log to console and logfile | Test Step-1 completed successfully |

| | Get LIG names,uris and FC uris |
| | ${uri} | Get Enclosure URI | ${Enclosure_Name[0]} |
| | Set Global Variable | ${ENC_0_uri} | ${uri} |

| step2(TC#10): | [Documentation] | Deleting the ULS from LIG, LI and clearing the trunk group in switch | 
| | Clear ULS in LIG & LI | ${LIG_uri_list[0]} | ${LIG_name_list[0]} |
| | ${show_command_output} | Check For Trunk Group in Brocade | ${FC_switch_details} | ${Trunk_Commands} |
| | ${lines} | Get Lines Containing String | ${show_command_output} | ${no_trunk_message} |
| | ${line_count} | Get Line Count | ${lines} |
| | Pass Execution If | ${line_count} == 1 | No trunk groups available |
| | ${TG_count} | ${TG_data} | Get the number of Trunk Group in switch | ${show_command_output} |
| | :FOR | ${x} | IN RANGE | 0 | ${TG_count} |
| | \ | @{lines} | Split String | ${TG_data[${x}]} | \n |
| | \ | ${TG_number} | Evaluate | ${x}+1 |
| | \ | ${Ports_count} | ${Master_port} | ${Ports_in_TG} | Check For Ports in Trunk Group | ${lines} | ${TG_number} |
| | \ | Delete trunk group and release ports | ${FC_switch_details} | ${Trunk_Commands} | ${Ports_in_TG} |
| | ${show_command_output} | Check For Trunk Group in Brocade | ${FC_switch_details} | ${Trunk_Commands} |
| | ${lines} | Get Lines Containing String | ${show_command_output} | ${no_trunk_message} |
| | ${line_count} | Get Line Count | ${lines} |
| | Pass Execution If | ${line_count} == 1 | Trunk Groups deleted succeesfully | ELSE | FAIL |

| step3(TC#10): | [Documentation] | OVF411_API_TC_Create 1 ULS with ports 1-4, with trunking disabled, and trunking disabled on TOR |
| | Create uls in LI | ${fcmodes[1]} |  ${US_details[2]['name']} | ${FC_uris[2]} | ${desiredSpeeds[0]} | ${US_details[2]['bay']} | ${ENC_0_uri} | ${US_details[2]['Act_ports'][0:4]} |
| | Sleep | 60s |

| | :FOR | ${port} | IN | @{US_details[2]['Act_ports'][0:4]} |
| | \ | ${portStatus} | ${trunkMaster} | ${enabled} | Get port details | ${Enclosure_Name[0]} | ${US_details[2]['bay']} | ${port} |
| | \ | Run Keyword Unless | '${portStatus}'=='Linked' | FAIL |

| step4(TC#11): | [Documentation] | OVF411_API_TC_Create 1 ULS with ports 1-4, with trunking disabled, and trunking enabled on TOR |
| | Create Trunk Group with ports | ${FC_switch_details} | ${Trunk_Commands} | ${FC_switch_ports['segment3'][0:4]} |
| | Sleep | 60s |

| | :FOR | ${port} | IN | @{US_details[2]['Act_ports'][0:4]} |
| | \ | ${portStatus} | ${trunkMaster} | ${enabled} | Get port details | ${Enclosure_Name[0]} | ${US_details[2]['bay']} | ${port} |
| | \ | Run Keyword Unless | '${portStatus}'=='Unlinked' | FAIL |

| step5(TC#12): | [Documentation] | Deleting the ULS from LIG, LI and clearing the trunk group in switch | 
| | Clear ULS in LIG & LI | ${LIG_uri_list[0]} | ${LIG_name_list[0]} |
| | ${show_command_output} | Check For Trunk Group in Brocade | ${FC_switch_details} | ${Trunk_Commands} |
| | ${lines} | Get Lines Containing String | ${show_command_output} | ${no_trunk_message} |
| | ${line_count} | Get Line Count | ${lines} |
| | Pass Execution If | ${line_count} == 1 | No trunk groups available |
| | ${TG_count} | ${TG_data} | Get the number of Trunk Group in switch | ${show_command_output} |
| | :FOR | ${x} | IN RANGE | 0 | ${TG_count} |
| | \ | @{lines} | Split String | ${TG_data[${x}]} | \n |
| | \ | ${TG_number} | Evaluate | ${x}+1 |
| | \ | ${Ports_count} | ${Master_port} | ${Ports_in_TG} | Check For Ports in Trunk Group | ${lines} | ${TG_number} |
| | \ | Delete trunk group and release ports | ${FC_switch_details} | ${Trunk_Commands} | ${Ports_in_TG} |
| | ${show_command_output} | Check For Trunk Group in Brocade | ${FC_switch_details} | ${Trunk_Commands} |
| | ${lines} | Get Lines Containing String | ${show_command_output} | ${no_trunk_message} |
| | ${line_count} | Get Line Count | ${lines} |
| | Pass Execution If | ${line_count} == 1 | Trunk Groups deleted succeesfully | ELSE | FAIL |

| step6(TC#12): | [Documentation] | OVF411_API_TC_Create 1 ULS with ports 1-4, with trunking enabled, and trunking disabled on TOR |
| | Create uls in LI | ${fcmodes[0]} |  ${US_details[2]['name']} | ${FC_uris[2]} | ${desiredSpeeds[0]} | ${US_details[2]['bay']} | ${ENC_0_uri} | ${US_details[2]['Act_ports'][0:4]} |
| | Sleep | 60s |

| | :FOR | ${port} | IN | @{US_details[2]['Act_ports'][0:4]} |
| | \ | ${portStatus} | ${trunkMaster} | ${enabled} | Get port details | ${Enclosure_Name[0]} | ${US_details[2]['bay']} | ${port} |
| | \ | Run Keyword Unless | '${portStatus}'=='Unlinked' | FAIL |

| step7(TC#13): | [Documentation] | OVF411_API_TC_Create 1 ULS with ports 1-4, with trunking enabled, and trunking enabled on TOR but with no trunk group |
| | ${resp} | Fusion Api Delete Alert |
| | Sleep | 60s |

| | Enable trunk ports but with no trunk group | ${FC_switch_details} | ${Trunk_Commands} | ${FC_switch_ports['segment3'][0:4]} |
| | Sleep | 100s |

| | :FOR | ${port} | IN | @{US_details[2]['Act_ports'][0:4]} |
| | \ | ${portStatus} | ${trunkMaster} | ${enabled} | Get port details | ${Enclosure_Name[0]} | ${US_details[2]['bay']} | ${port} |
| | \ | Run Keyword Unless | '${portStatus}'=='Linked' | FAIL |

| | ${resp} | Fusion Api Get Alerts |
| | ${mem_resp} | Get From Dictionary | ${resp} | members |
| | ${len} | Get Length | ${mem_resp} |
| | ${Alert_msg} | Create List |
| | :FOR | ${x} | IN RANGE | 0 | ${len} |
| | \ | ${desc_alert} | Get From Dictionary | ${mem_resp[${x}]} | description | 
| | \ | Run Keyword If | '${desc_alert}' != '${alert_message}' | Continue For Loop |	
| | \ | Append To List | ${Alert_msg} | ${desc_alert} |
| | ${len}  | Get Length | ${Alert_msg} |
| | Run keyword if | ${len} == 0 | Fail | "No Critical Alert Message Observed" |
| | Log to console and logfile | \n${alert_message} is observed |

| step8(TC#14): | [Documentation] | OVF411_API_TC_Create 1 ULS with ports ports from different segment with trunking enabled, OV should throw error and ULS should not be created |
| | ${li_resp} | Fusion Api Get Li |
| | Set Global Variable | ${LI_uri} | ${li_resp['members'][0]['uri']} |
| | Set To Dictionary | ${li_upsbody[0]} | fcMode | ${fcmodes[0]} |
| | Set To Dictionary | ${li_upsbody[0]} | name | ${US_details[0]['name']} |
| | Append To List | ${li_upsbody[0]['fcNetworkUris']} | ${FC_uris[0]} |
| | ${port_list} | Create List |
| | ${ports_length} | Get Length | ${neg_ports} |
| | :FOR | ${x} | IN RANGE | 0 | ${ports_length} |
| | \ | Set To Dictionary | ${portConfigInfos[${x}]} | desiredSpeed | ${desiredSpeeds[0]} |
| | \ | Set To Dictionary | ${portConfigInfos[${x}]['location']['locationEntries'][1]} | value | ${US_details[0]['bay']} | 
| | \ | Set To Dictionary | ${portConfigInfos[${x}]['location']['locationEntries'][2]} | value | ${ENC_0_uri} 
| | \ | ${tmp_list} | Create List |
| | \ | ${tmp_var} | Copy Dictionary | ${portConfigInfos[${x}]} |
| | \ | Set To Dictionary | ${tmp_var['location']['locationEntries'][0]} | value | ${neg_ports[${x}]} |
| | \ | Append To List | ${port_list} | ${tmp_var} 
| | Set To Dictionary | ${li_upsbody[0]} | portConfigInfos | ${port_list} |
| | Set To Dictionary | ${li_upsbody[0]} | logicalInterconnectUri | ${LI_uri} |
| | ${resp_li} | Fusion Api Create Uplink Set | body=${li_upsbody[0]} |
| | Run Keyword Unless | '${resp_li['errorCode']}'=='CRM_PORTS_NOT_IN_SAME_TRUNK_AREA' | FAIL |

| *** Keywords *** |
| Get LIG names,uris and FC uris |
| | [Documentation] | This keyword will fetvh exixting LIG and FC uris |
| | ${LIG_name_list} | Create List |
| | ${LIG_uri_list} | Create List |
| | ${FC_uris} | Create List |
| | ${resp} | Fusion Api Get Lig | 
| | :FOR | ${member} | IN | @{resp['members']} |
| | \ | Append To List | ${LIG_name_list} | ${member['name']} |
| | \ | Append To List | ${LIG_uri_list} | ${member['uri']} |
| | Set Global Variable | ${LIG_name_list} | ${LIG_name_list} |
| | Set Global Variable | ${LIG_uri_list} | ${LIG_uri_list} |
| | ${resp} | Fusion Api Get Fc Networks |
| | :FOR | ${member} | IN | @{resp['members']} |
| | \ | Append To List | ${FC_uris} | ${member['uri']} |
| | Set Global Variable | ${FC_uris} | ${FC_uris} |

| Clear ULS in LIG & LI | [Arguments] | ${LIG_uri} | ${LIG_name} |
| | [Documentation] | This keyword will clear uplink sets in both LI and LIG |
| | ${resp} | fusion_api_get_lig | uri=${LIG_uri} |
| | Remove From Dictionary | ${resp} | headers |
| | Remove From Dictionary | ${resp} | status_code |
| | Set To Dictionary | ${resp} | uplinkSets | ${empty_list} |
| | ${resp1} | Fusion Api Edit Lig | ${resp} | ${LIG_uri} |
| | ${task} | Wait For Task | ${resp1} | 20s | 2s |
| | LI update from Group | ${les[0]['name']} | ${LIG_name}-1 |

| Steps for Redundant bay type | [Arguments] | ${Current_position_scope} | ${resource_uri} |
| | [Documentation] | These steps are going to set icmap templates if the respective bay position is in Redundant bay type |
| | Set To Dictionary | ${interconnectBayMappings[${Current_position_scope}]} | logicalInterconnectGroupUri | ${resource_uri} |
| | ${Current_position_scope} | Evaluate | ${Current_position_scope}+1 |
| | Set To Dictionary | ${interconnectBayMappings[${Current_position_scope}]} | logicalInterconnectGroupUri | ${resource_uri} |
| | ${Current_position_scope} | Evaluate | ${Current_position_scope}+1 |
| | [Return] | ${Current_position_scope} |

| Steps for NonRedundantASide bay type | [Arguments] | ${Current_position_scope} | ${resource_uri} |
| | [Documentation] | These steps are going to set icmap templates if the respective bay position is in NonRedundantASide bay type |
| | Set To Dictionary | ${interconnectBayMappings[${Current_position_scope}]} | logicalInterconnectGroupUri | ${resource_uri} |
| | ${Current_position_scope} | Evaluate | ${Current_position_scope}+1 |
| | [Return] | ${Current_position_scope} |

| Steps for NonRedundantBSide bay type | [Arguments] | ${Current_position_scope} | ${resource_uri} |
| | [Documentation] | These steps are going to set icmap templates if the respective bay position is in NonRedundantBSide bay type |
| | Set To Dictionary | ${interconnectBayMappings[${Current_position_scope}]} | logicalInterconnectGroupUri | ${resource_uri} |
| | ${Current_position_scope} | Evaluate | ${Current_position_scope}+1 |
| | [Return] | ${Current_position_scope} |

| Create Trunk Group with ports | [Arguments] | ${FC_switch_details} | ${Trunk_Commands} | ${Ports_to_trunk} |
| | [Documentation] | Creating Trunk Group with ports on switch
| | ${First_port} | Set Variable | ${Ports_to_trunk[0]} |
| | ${Last_port} | Set Variable | ${Ports_to_trunk[-1]} |
| | Open Connection | ${FC_switch_details['ip']} | 
| | Login | ${FC_switch_details['userName']} | ${FC_switch_details['password']} |
| | Execute Command | ${Trunk_Commands[1]} ${First_port}-${Last_port} |
| | Sleep | 3s |
| | :FOR | ${y} | IN  | @{Ports_to_trunk} |
| | \ | Execute Command | ${Trunk_Commands[3]} ${y} 1 |
| | \ | Sleep | 3s |
| | Execute Command | ${Trunk_Commands[5]} ${First_port}-${Last_port} -index ${First_port} |
| | Sleep | 3s |
| | Execute Command | ${Trunk_Commands[4]} ${First_port}-${Last_port} |
| | Sleep | 3s |
| | Close Connection | 

| Disable/Enable all trunk ports in each trunk group | [Arguments] | ${FC_switch_details} | ${Trunk_Commands} | ${Ports_to_trunk} |
| | [Documentation] | Disable/Enable all trunk ports in each trunk group 
| | ${First_port} | Set Variable | ${Ports_to_trunk[0]} |
| | ${Last_port} | Set Variable | ${Ports_to_trunk[-1]} |
| | Open Connection | ${FC_switch_details['ip']} | 
| | Login | ${FC_switch_details['userName']} | ${FC_switch_details['password']} |
| | Execute Command | ${Trunk_Commands[1]} ${First_port}-${Last_port} |
| | Sleep | 3s |
| | Execute Command | ${Trunk_Commands[4]} ${First_port}-${Last_port} |
| | Sleep | 3s |
| | Close Connection | 


| Check For Trunk Group in Brocade | [Arguments] | ${FC_switch_details} | ${Trunk_Commands} |
| | [Documentation] | Checking for the trunk group existence in switch |
| | Log to console and logfile | Checking for trunk group details in the Brocade switch |
| | Open Connection | ${FC_switch_details['ip']} | 
| | Login | ${FC_switch_details['userName']} | ${FC_switch_details['password']} |
| | ${stdout} | Execute Command | ${Trunk_Commands[0]} |
| | Log to console and logfile | Show command output is \n ${stdout} |
| | Close Connection |
| | [Return] | ${stdout} |

| Get the number of Trunk Group in switch | [Arguments] | ${show_command_output} |
| | [Documentation] | Getting the number of trunk groups in switch |
| | @{words} | Split String | ${show_command_output} | ------------------------------------- |
| | Log to console and logfile | The output splitted with dots is \n ${words} |
| | Remove From List | ${words} | -1 |
| | Remove From List | ${words} | 0 |
| | ${group_count} | Get Length | ${words} |
| | Log to console and logfile | The number of trunk groups present is ${group_count} |
| | [Return] | ${group_count} | ${words} |

| Check For Ports in Trunk Group | [Arguments] | ${Ports_data} | ${TG_number} |
| | [Documentation] | Checking for the master port and port count in the trunk group |
| | Log to console and logfile | Checking the ports present in each trunk group |
| | Remove From List | ${Ports_data} | -1 |
| | Remove From List | ${Ports_data} | 0 |
| | ${Ports_count} | Get Length | ${Ports_data} |
| | Log to console and logfile | The number of ports present in TG${TG_number} is ${Ports_count} |
| | ${Ports_list} | Create List |
| | :FOR | ${y} | IN RANGE | 0 | ${Ports_count} |
| | \ | ${data1} | Split String | ${Ports_data[${y}]} |
| | \ | ${data2} | Get Length | ${data1} |
| | \ | Append To List | ${Ports_list} | ${data1[-1]} |
| | ${Master_port} | Set Variable | ${data1[-2]} |
| | [Return] | ${Ports_count} | ${Master_port} | ${Ports_list} |

| Delete trunk group and release ports | [Arguments] | ${FC_switch_details} | ${Trunk_Commands} | ${Ports_in_TG} |
| | [Documentation] | Deleting the trunk group |
| | ${First_port} | Set Variable | ${Ports_in_TG[0]} |
| | ${Last_port} | Set Variable | ${Ports_in_TG[-1]} |
| | Open Connection | ${FC_switch_details['ip']} | 
| | Login | ${FC_switch_details['userName']} | ${FC_switch_details['password']} |
| | Execute Command | ${Trunk_Commands[1]} ${First_port}-${Last_port} |
| | Sleep | 3s |
| | Execute Command | ${Trunk_Commands[2]} ${First_port}-${Last_port} |
| | Sleep | 3s |
| | :FOR | ${y} | IN  | @{Ports_in_TG} |
| | \ | Execute Command | ${Trunk_Commands[3]} ${y} 0 |
| | \ | Sleep | 3s |
| | Execute Command | ${Trunk_Commands[4]} ${First_port}-${Last_port} |
| | Sleep | 3s |
| | Close Connection | 

| Create uls in LIG | [Arguments] | ${LIG_uri} | ${fcmode} | ${FC_uri} | ${uls_name} | ${desiredSpeed} | ${IC_bay_set} | ${ports} | 
| | [Documentation] | Creating Uplinkset with network in LIG through rest calls
| | ${port_list} | Create List |
| | ${resp} | fusion_api_get_lig | uri=${LIG_uri}
| | Log to console and logfile | ${resp} |
| | Set To Dictionary | ${lig_uls_body1} | fcMode | ${fcMode} |
| | Set To Dictionary | ${lig_uls_body1} | name | ${uls_name} |
| | Append To List | ${lig_uls_body1['networkUris']} | ${FC_uri} |
| | ${ports_length} | Get Length | ${ports} |
| | :FOR | ${x} | IN RANGE | 0 | ${ports_length} |
| | \ | Set To Dictionary | ${logicalPortConfigInfos[${x}]} | desiredSpeed | ${desiredSpeed}
| | \ | Set To Dictionary | ${logicalPortConfigInfos[${x}]['logicalLocation']['locationEntries'][0]} | relativeValue | ${IC_bay_set} 
| | \ | ${tmp_list} | Create List |
| | \ | ${tmp_var} | Copy Dictionary | ${logicalPortConfigInfos[${x}]} |
| | \ | Set To Dictionary | ${tmp_var['logicalLocation']['locationEntries'][1]} | relativeValue | ${ports[${x}]} |
| | \ | Append To List | ${port_list} | ${tmp_var} |
| | Log to console and logfile | ${port_list} |
| | Set To Dictionary | ${lig_uls_body1} | logicalPortConfigInfos | ${port_list} |
| | Log to console and logfile | ${lig_uls_body1} |
| | Remove From Dictionary | ${resp} | headers |
| | Remove From Dictionary | ${resp} | status_code |
| | Append to List | ${resp['uplinkSets']} | ${lig_uls_body1} |
| | ${resp1} | Fusion Api Edit Lig | ${resp} | ${LIG_uri_list[0]} |
| | ${task} | Wait For Task | ${resp1} | 20s | 2s |
| | Remove From List | ${lig_uls_body1['networkUris']} | 0 | 

| Create uls in LI | [Arguments] | ${fcmode} | ${uls_name} | ${FC_uri} | ${desiredSpeed} | ${IC_bay_set} | ${ENC_uri} | ${ports} | 
| | [Documentation] | Creating uplinkset with network in LI through rest calls |
| | ${li_resp} | Fusion Api Get Li |
| | Set Global Variable | ${LI_uri} | ${li_resp['members'][0]['uri']} |
| | Set To Dictionary | ${li_upsbody[0]} | fcMode | ${fcMode} |
| | Set To Dictionary | ${li_upsbody[0]} | name | ${uls_name} |
| | Append To List | ${li_upsbody[0]['fcNetworkUris']} | ${FC_uri} |
| | ${port_list} | Create List |
| | ${ports_length} | Get Length | ${ports} |
| | :FOR | ${x} | IN RANGE | 0 | ${ports_length} |
| | \ | Set To Dictionary | ${portConfigInfos[${x}]} | desiredSpeed | ${desiredSpeed} |
| | \ | Set To Dictionary | ${portConfigInfos[${x}]['location']['locationEntries'][1]} | value | ${IC_bay_set} 
| | \ | Set To Dictionary | ${portConfigInfos[${x}]['location']['locationEntries'][2]} | value | ${ENC_uri} 
| | \ | ${tmp_list} | Create List |
| | \ | ${tmp_var} | Copy Dictionary | ${portConfigInfos[${x}]} |
| | \ | Set To Dictionary | ${tmp_var['location']['locationEntries'][0]} | value | ${ports[${x}]} |
| | \ | Append To List | ${port_list} | ${tmp_var} 
| | Set To Dictionary | ${li_upsbody[0]} | portConfigInfos | ${port_list} |
| | Set To Dictionary | ${li_upsbody[0]} | logicalInterconnectUri | ${LI_uri} |
| | ${resp_li} | Fusion Api Create Uplink Set | body=${li_upsbody[0]} 
| | ${task} | Wait For Task | ${resp_li} | 240s | 10s |
| | Remove From List | ${li_upsbody[0]['fcNetworkUris']} | 0 | 

| LI update from Group | [Arguments] | ${LE} | ${LIG} |
| | [Documentation] | Performing update from group in LI through rest call |
| | ${li_uri} | Get LI URI | ${LE}-${LIG}
| | Set Global Variable | ${LI_uri} | ${li_uri} |
| | ${resp_update} | Fusion Api Update From Group | ${LI_uri} |
| | Run keyword unless | ${resp_update['status_code']}== 202 | Fail | ${resp_update['message']} |
| | ${task} | Wait For Task | ${resp_update} | 300s | 30s |
| | Sleep | 60s |
| | Log to console and logfile | LI updated from group successfully. |

| Get port details | [Arguments] | ${Enc_name} | ${bay_num} | ${Port_num} |
| | [Documentation] | Getting the port details of respective port number. |
| | ${resp} | Fusion Api Get Interconnect | param=?filter="'name'=='${Enc_name}, interconnect ${bay_num}'" |
| | ${ports} | Get Variable Value | ${resp['members'][0]['ports']} |
| | :FOR | ${port} | IN | @{ports} |
| | \ | Run Keyword If | '${port['portName']}' != '${Port_num}' | Continue For Loop |
| | \ | ${portStatus} | Set Variable | ${port['portStatus']} |
| | \ | ${trunkMaster} | Set Variable | ${port['fcPortProperties']['trunkMaster']} |
| | \ | ${enabled} | Set Variable | ${port['enabled']} |
| | \ | Exit For Loop |
| | [Return] | ${portStatus} | ${trunkMaster} | ${enabled} |

| Edit desired speed in LI | [Arguments] | ${uplinksetname} | ${ports} | ${desiredSpeed} |
| | [Documentation] | Editing desired speed to 4G/8G/16G in LI |
| | ${uplinksets} | Fusion Api Get Uplink Set | param=?filter="'name'=='${uplinksetname}'" |
| | ${us} | Get From List | ${uplinksets['members']} | 0 |   
| | ${us_uri} | Get From Dictionary | ${us} | uri | 
| | ${ports_length} | Get Length | ${ports} |
| | :FOR | ${x} | IN RANGE | 0 | ${ports_length} |
| | \ | Set To Dictionary | ${uplinksets['members'][0]['portConfigInfos'][${x}]} | desiredSpeed | ${desiredSpeed} |
| | ${resp} | Fusion Api Edit Uplink Set | body=${uplinksets['members'][0]} | uri=${us_uri} |
| | ${task} | Wait For Task | ${resp} | 100s | 10s |


| Power Off/on ICM | [Arguments] | ${ICM_name} | ${power_state_value} |
| | [Documentation] | This keyword with powers on/off the ICM according to the passed power_state_value |
| | ${resp} | Fusion Api Get Interconnect | param=?filter="'name'=='${ICM_name}'" |
| | ${IC_uri} | Get From Dictionary | ${resp['members'][0]} | uri |
| | Set To Dictionary | ${IC_powerstate_body[0]} | value | ${power_state_value} |
| | ${patch_resp} | Fusion Api Patch Interconnect | ${IC_powerstate_body} | ${IC_uri} |
| | ${task} | Wait For Task | ${patch_resp} | 120s | 10s |
| | ${resp} | Fusion Api Get Interconnect | param=?filter="'name'=='${ICM_name}'" |
| | Log to console and logfile | The power state if ICM ${ICM_name} is ${resp['members'][0]['powerState']} |

| Get IC State | [Arguments] | ${ICM_name} |
| | [Documentation] | This keyword retrieves the current powerstate of the IC |
| | ${resp} | Fusion Api Get Interconnect | param=?filter="'name'=='${ICM_name}'" |
| | ${IC_state} | Get From Dictionary | ${resp['members'][0]} | state |
| | [Return] | ${IC_state} |

| Restore From Backup |
| | [Documentation] | This keyword will perform restore from backup |
| | ${status} | Set Variable | ${EMPTY} |
| | ${Response} | Fusion Api Get Backup |
| | Run keyword unless | ${Response['status_code']}== 200 | Fail | "Unable to Get the latest backup" |
| | ${restore_body} | Create Dictionary | type=RESTORE |
| | ... | uriOfBackupToRestore=${Response['members'][0]['uri']} |
| | ${output} | Fusion Api Restore Backup | ${restore_body} |
| | Log to console and logfile | ${output} |
| | Sleep | 200sec |
| | Run keyword unless | ${output['status_code']}== 202 | Fail | "Unable to perform the restore from backup operation" |
| | ${restore_resp} | Fusion API Get Restore Status |
| | Run keyword unless | ${restore_resp['status_code']}== 200 | Fail | "Unable to get the restore details" |
| | :FOR | ${index} | IN RANGE | ${restore_resp['count']} |
| | \ | Run Keyword If | '${restore_resp['members'][${index}]['backupIdToRestore']}' != '${Response['members'][0]['id']}' | Continue For Loop |
| | \ | ${restore_id} | Set Variable | ${restore_resp['members'][${index}]['id']} |
| | :FOR | ${index} | IN RANGE | 50 |
| | \ | Sleep | 60sec
| | \ | Log to console and logfile | "Restoring is in Progress..." |
| | \ | ${resp} | Fusion API Get Restore Status | ${restore_id} |
| | \ | Run keyword unless | ${resp['status_code']}== 200 | Fail | "Unable to get the restore id details" |
| | \ | Run Keyword If | '${resp['progressStep']}' != 'COMPLETED' | Continue For Loop |
| | \ | ${status} | Set Variable | ${resp['status']} |
| | \ | Run Keyword If | '${resp['progressStep']}' == 'COMPLETED' | Exit For Loop |
| | Should Be Equal | ${status} | SUCCEEDED |
| | Log to console and logfile | "Exited from the for loop" |
| | Sleep | 30 |
| | ${resp} | Fusion Api Login Appliance | ${APPLIANCE_IP} | ${admin_credentials} |

| IC is in configured state | [Arguments] | ${enc_name} | ${ic_num} |
| | [Documentation] | This keyword will run until the IC state become configured state  |
| | ${IC_state} | Get IC State | ${enc_name}, interconnect ${ic_num} |
| | Run Keyword Unless | '${IC_state}'=='Configured' | FAIL |

| Edit port status | [Arguments] | ${Enc_name} | ${bay_num} | ${Port_num} | ${enabled_mode} |
| | [Documentation] | Editing the port either to disabled or enabled status |
| | ${test_dict} | Create Dictionary |
| | ${test_list} | Create List |
| | ${resp} | Fusion Api Get Interconnect | param=?filter="'name'=='${Enc_name}, interconnect ${bay_num}'" |
| | ${ports} | Get Variable Value | ${resp['members'][0]['ports']} |
| | :FOR | ${port} | IN | @{ports} |
| | \ | Run Keyword If | '${port['portName']}' != '${Port_num}' | Continue For Loop |
| | \ | Set To Dictionary | ${test_dict} | associatedUplinkSetUri | ${port['associatedUplinkSetUri']} |
| | \ | Set To Dictionary | ${test_dict} | interconnectName | ${port['interconnectName']} |
| | \ | Set To Dictionary | ${test_dict} | portType | ${port['portType']} |
| | \ | Set To Dictionary | ${test_dict} | portId | ${port['portId']} |
| | \ | Set To Dictionary | ${test_dict} | type | ${port['type']} |
| | \ | Set To Dictionary | ${test_dict} | portName | ${port['portName']} |
| | \ | Set To Dictionary | ${test_dict} | capability | ${port['capability']} |
| | \ | Set To Dictionary | ${test_dict} | configPortTypes | ${port['configPortTypes']} |
| | \ | Set To Dictionary | ${test_dict} | enabled | ${enabled_mode} |
| | \ | Exit For Loop |
| | Append to List | ${test_list} | ${test_dict} |
| | ${edit_resp} | Fusion Api Edit Interconnect Ports | ${test_list} | ${resp['members'][0]['uri']}
| | Run keyword unless | ${edit_resp['status_code']} == 202 | Fail |
| | ${task} | Wait For Task | ${edit_resp} | 120s | 20s |
| | Remove From List | ${test_list} | 0 |
| | [Return] | ${task} |

| Enable trunk ports but with no trunk group | [Arguments] | ${FC_switch_details} | ${Trunk_Commands} | ${Ports_to_trunk} |
| | [Documentation] | Creating Trunk ports but without creating trunk group |
| | ${First_port} | Set Variable | ${Ports_to_trunk[0]} |
| | ${Last_port} | Set Variable | ${Ports_to_trunk[-1]} |
| | Open Connection | ${FC_switch_details['ip']} | 
| | Login | ${FC_switch_details['userName']} | ${FC_switch_details['password']} |
| | Execute Command | ${Trunk_Commands[1]} ${First_port}-${Last_port} |
| | Sleep | 3s |
| | :FOR | ${y} | IN  | @{Ports_to_trunk} |
| | \ | Execute Command | ${Trunk_Commands[3]} ${y} 1 |
| | \ | Sleep | 3s |
| | Execute Command | ${Trunk_Commands[6]} ${First_port}-${Last_port} |
| | Sleep | 3s |
| | Close Connection |