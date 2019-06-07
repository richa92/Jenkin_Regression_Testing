sender_appliance_ip = "16.83.14.82"

admin_credentials_sender_ov = {'userName': 'Administrator', 'password': 'hpvse123'}

sender_ov_root_username = "root"

sender_ov_root_password = "hpvse1"

receiver_appliance_ip = "16.83.13.162"

admin_credentials_receiver_ov = {'userName': 'Administrator', 'password': 'hpvse123'}

receiver_ov_root_username = "root"

receiver_ov_root_password = "hpvse1"

server_hardware_name = "ILO7CE712P2MF.lr.eml.lab"

ilo_ip = "16.83.13.48"

trap_type = "cpqHo2GenericTrap"

server_hardware_uri = "/rest/server-hardware/53325056-554B-4337-4537-313250324D46"

ilo_credentials = {'username': 'Administrator', 'password': 'password'}

server_hardware = [{"name": "ILO7CE712P2MF.lr.eml.lab", "hostname": "16.83.13.48", "username": "Administrator",
                    "password": "password", "force": True, "licensingIntent": "OneViewNoiLO",
                    "configurationState": "Managed", 'initialScopeUris': None}]

trap_forwarding_user = {"type": "Users", "userName": "Administrator", "securityLevel": "Authentication",
                        "authenticationProtocol": "MD5", "authenticationPassphrase": "123456789"}

trap_destination = {"type": "Destination", "destinationAddress": receiver_appliance_ip, "port": 1161, "userId": "", "userUri": ""}

trap_destination_user = {"type": "Users", "userName": "Administrator", "securityLevel": "Authentication", "authenticationProtocol": "MD5", "authenticationPassphrase": "123456789"}

trap_forwadring_destination = {"type": "Destination", "destinationAddress": sender_appliance_ip, "port": 1161, "userId": "", "userUri": ""}

alert_validation = {"type": "AlertResourceV3",
                    "resourceUri": server_hardware_uri,
                    "physicalResourceType": "server-hardware",
                    "alertState": "Active",
                    "severity": "Warning",
                    "category": "alerts",
                    "alertTypeID": "Trap." + trap_type,
                    "description": "Remote Insight Test Trap",
                    }

trap_storm_validation = {'category': 'alerts',
                         'resourceUri': server_hardware_uri,
                         'severity': 'Warning',
                         'alertTypeID': 'Events-TrapStorm.' + trap_type,
                         'healthCategory': 'Appliance',
                         'physicalResourceType': 'server-hardware',
                         'description': 'A trap storm from ' + ilo_ip + ' for the trap ' + trap_type + ' has been detected, started filtering traps of the same type for this resource.',
                         'alertState': 'Active',
                         'type': 'AlertResourceV3',
                         'urgency': 'Medium'
                         }

trap_clearance_validation = {'category': 'alerts',
                             'resourceUri': server_hardware_uri,
                             'severity': 'OK',
                             'alertTypeID': 'Events-TrapStorm.' + trap_type,
                             'healthCategory': 'Appliance',
                             'physicalResourceType': 'server-hardware',
                             'description': 'A trap storm from ' + ilo_ip + ' for the trap ' + trap_type + ' has ended. A total of 6 traps were filtered.',
                             'clearedByUser': 'System',
                             'alertState': 'Cleared',
                             'type': 'AlertResourceV3',
                             'urgency': 'Medium'
                             }

cmd_sender_ov = ["sed -i -e 's/<\/configuration>/    <logger name=\"com.hp.ci.mgmt.health.trapforwarding\" level=\"TRACE\" additivity=\"false\"\/>\\n<appender-ref ref=\"DebugLogFile\"\/>\\n<\/logger>\\n<\/configuration>/g' /ci/etc/cilogback.xml"]

cmd_receiver_ov = ["sed -i -e 's/<\/configuration>/    <logger name=\"com.hp.ci.mgmt.health.snmptrapreceiver\" level=\"TRACE\" additivity=\"false\"\/>\\n<appender-ref ref=\"DebugLogFile\"\/>\\n<\/logger>\\n<\/configuration>/g' /ci/etc/cilogback.xml"]

pcap_filename = "somefile.pcap"

pcap_text_file = "pcaptextfile.txt"

pcap_file_process = "tcpdump -r " + pcap_filename + " > " + pcap_text_file

search_string_pcap_file = "16.83.14.82"
