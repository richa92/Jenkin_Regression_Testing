"""
Data File for OVS MAT-I Testing
"""

OA_ip = "15.212.144.11"
stor_ip = "15.212.144.135"
ilo4_ip = "15.212.144.90"
ilo5_ip = "15.212.144.95"
ilo3_ip = "15.212.144.16"
ipdu_ip = "15.212.144.94"
ipdu = "IPDU"

#######################################################################
admin1_credentials = {'userName': 'Administrator', 'password': 'admin123'}
ssh_cred = {'username': 'root', 'password': 'hpvse1'}
dev_cred = {'OA_user': 'Administrator', 'OA_pass': 'hpinvent', 'ilo4_user': 'admin', 'ilo4_pass': 'admin123',
            'ilo5_user': 'admin', 'ilo5_pass': 'admin123', 'ilo3_user': 'admin',
            'ilo3_pass': 'admin123', 'iPDU_user': 'admin', 'iPDU_pass': 'admin123'}
###############################################################
add_enclosure_uri = '/rest/enclosures'
add1_enclosure_body = {"hostname": OA_ip, "username": dev_cred['OA_user'], "password": dev_cred['OA_pass'],
                       "licensingIntent": "OneViewStandard", "state": "Monitored", "force": "true"}

##############################################################

ipdu_systems = {"force": True, "hostname": ipdu_ip, "username": dev_cred['iPDU_user'],
                "password": dev_cred['iPDU_pass']}

CERTIFICATE = {"aliasName": "", "base64SSLCertData": "", "status": None, "type": "SSLCertificateDTO"}

###############################################################

storage1_systems = {"hostname": stor_ip, "username": "3paradm", "password": "3pardata", "family": "StoreServ"}

#############################################################################

rackservers1 = {"hostname": ilo4_ip, "username": "admin", "password": "admin123", "force": "true",
                "licensingIntent": "OneView", "configurationState": "Monitored"}
#############################################################################

rackservers2 = {"hostname": ilo5_ip, "username": "admin", "password": "admin123", "force": "true",
                "licensingIntent": "OneView", "configurationState": "Monitored"}
##############################################################################

dbsync_Index_body = {"type": "IndexResourceV300", "attributes": {}, "ownerId": "tasks", "name": "ResourceV3001",
                     "uri": "/rest/server-hardware/test-1", "category": "server-hardware",
                     "scopeUris": ["/rest/scope/production", "/rest/scope/dev"]}
dbsync_db_query = '''psql -d cidb -U postgres -h 127.0.0.1 -c "Select uri from index.node where uri='/rest/server-hardware/test-1'";'''
######################################################################################################################

rabbitmq_var = {'RM_Name': 'PM', 'exchange_name': 'mat_test_exchange', 'routing_key': 'test_key',
                'queue_name': 'mat_test_queue'}
######################################################################################################################
port_help = '''usage: check_port_communication.py [-h] -ip IPADDRESS [-devtype DEVICETYPE]
                                   [-p PORT]

optional arguments:
  -h, --help            show this help message and exit
  -ip IPADDRESS, --ipaddress IPADDRESS
                        remote host ip address
  -devtype DEVICETYPE, --deviceType DEVICETYPE
                        deviceType of the host i.e ILO or OA or IPDU or 3PAR
                        or I3S or EM
  -p PORT, --port PORT  port number to check whether port is open or not'''

######################################################################################################################

task = {"type": "TaskResourceV2", "taskState": "Running", "owner": "Administrator", "userInitiated": "true",
        "name": "ROBO TASK", "taskType": "User",
        "associatedResource": {"associationType": "MANAGED_BY", "resourceCategory": "enclosures",
                               "resourceName": "enclosure789", "resourceUri": "/rest/enclosures/ABCD789"}}

######################################################################################################################
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

######################################################################################################################

dtask_help = '''usage: dtask.py [-h] [-l LIST] [-i ID] [-t TIME] [-r] [-a ALERTS] [-da] [-tt]
                [-dt] [-f OUTPUTFILE]

optional arguments:
  -h, --help            show this help message and exit
  -l LIST, --list LIST  List tasks on appliance which are in state provided by
                        argumenet value. Argument value can be
                        running,interrupted,completed,pending,error,warning or
                        all
  -i ID, --id ID        Used with -tt (terminating a task) and -dt (deleting a
                        task)options. When used alone it lists down the task
                        details
  -t TIME, --time TIME  List tasks in running state and created certain time
                        ago. Valid format for time is '6d' for 6 days and '4h'
                        for 4 hours ago
  -r, --runningtask     List running tasks on the appliance
  -a ALERTS, --alerts ALERTS
                        List all Alerts on appliance which are in particular
                        state provided by argument value. Argument value can
                        be locked,cleared,or active
  -da, --deletealert    Delete Alert/Alerts on appliance. When no argument is
                        provided then all alerts in locked state are deleted.
                        When -i option is provided along with alertId then
                        alert with that particular alertId is deleted
  -tt, --terminatetask  Interuppt Running/Pending task provided by id
  -dt, --deletetask     Delete a Completed/Interuupted task or delete a task
                        which is in terminal state provided by id. If the task
                        is running or pending then it is first interrupted and
                        then deleted
  -f OUTPUTFILE, --outputFile OUTPUTFILE
                        Write the output of command to provided file'''

#####################################################################################################################

event = {
    "description": "Test Event",
    "eventDetails":
        [
            {
                "eventItemName": "ipv4Address",
                "eventItemValue": "15.212.144.90",
                "isThisVarbindData": "false",
                "varBindOrderIndex": "-1"
            },
            {
                "eventItemName": "clearPriorEvents",
                "eventItemValue": "false",
                "isThisVarbindData": "false",
                "varBindOrderIndex": "-1"
            },
            {
                "eventItemName": "correctiveAction",
                "eventItemValue": "Posted an Event",
                "isThisVarbindData": "false",
                "varBindOrderIndex": "-1"
            }
        ],
    "eventTypeID": "hp.justATest",
    "healthCategory": "PROCESSOR",
    "rxTime": "2012-05-14T20:23:56.688Z",
    "serviceEventDetails": {
        "caseId": "1234",
        "primaryContact": "contactDetails",
        "remoteSupportState": "Submitted"},
    "serviceEventSource": "true",
    "severity": "OK",
    "type": "EventResourceV3",
    "urgency": "None"
}

########################################################################################################

alert_uri = '/rest/alerts/'
########################################################################################################

FixmeUiLog = 'c:/fixmelog'

#######################################################################################################
appliance_commands = ['cat.out', 'crm.out', 'df.out', 'du.out', 'ethtool.out', 'free.out', 'grep.out', 'head.out',
                      'hostname.out', 'ifconfig.out', 'iostat.out', 'ip.out', 'iptables.out', 'last.out', 'ls.out',
                      'lvdisplay.out', 'mount.out', 'mpstat.out', 'netstat.out', 'ps.out', 'route.out', 'rpm.out',
                      'top.out', 'uname.out', 'vgdisplay.out', 'virt-what.out', 'vmstat.out',
                      'vmware-toolbox-cmd.out']
pd_appliance = ['ci', 'commands', 'var']
pd_app_var_log = ['boot.log']
pd_version = ['version']
pd_boot = ['boot.log']
pd_pg_cmds = ['alerts.txt', 'psql.out', 'tasks.txt']
decryptingfiles = ['Decryption-Util.jar', 'decrypt-support-dump.bat', 'decrypt-support-dump.sh']
CMD_LIST = ['cat /proc/net/if_inet6', 'cat /proc/partitions', 'crm status', 'df -a', 'df -h', 'df -i',
            'du -h --max-depth=5 / | sort -hr', 'ethtool eth0', 'free', 'grep "model name" /proc/cpuinfo',
            'head -n1 /etc/issue', 'hostname', 'ifconfig -a', 'iostat', 'ip route show', 'iptables -S', 'iptables -L',
            'last reboot', 'ls -l /etc/pki/tls/certs/', 'ls -l /etc/pki/tls/private/',
            'ls -l /var/lib/pgsql/postgres/data/', 'lvdisplay', 'mount | column -t', 'mpstat -P ALL', 'netstat -anp',
            'netstat -g', "ps -e -ww -o pcpu,cpu,nice,state,cputime,args --sort pcpu | sed '/^ 0.0 /d'", 'ps -ef -ww',
            'ps -ww -eo pcpu,pid,user,args | sort -k 1 -r | head -10', 'route -n', 'rpm -qa',
            'rpm -qa hp-firmware\* | sort', 'top -n 1 -b -c', 'uname -a', 'vgdisplay', 'virt-what', 'vmstat',
            'vmware-toolbox-cmd -v']
alerts_CMD = ["""psql -d cidb -U postgres -c 'select id,activityuri,alertstate,assignedtouser,clearedbyuser,clearedtime,correctiveaction,healthcategory,created,description,lifecycle,modified,resourceid,physicalresourcetype,resourceuri,alerttypeid,resourcename,severity,urgency,serviceeventsource,caseid,primarycontact,remotesupportstate,parent_alert_id from "health-services".alert where CAST(CAST(created AS TIMESTAMP) AS DATE) > CURRENT_DATE - INTERVAL '"'"'3 days;'"'" > /backup_staging/support-dumps/dump1/postgres/commands/alerts.txt"""]
tasks_CMD = ["""psql -d cidb -U postgres -c "select id,associatedtaskuri,completedsteps,created,modified,name,owner,parenttaskid,parenttaskuri,taskstate,taskstatus,totalsteps,userinitiated,storedpercentcomplete,percentcomplete,expectedduration,data,tasktype,statereason,hidden,version from taskt.taskentity where CAST(CAST(created AS TIMESTAMP) AS DATE) > CURRENT_DATE - INTERVAL '3 days';" > /backup_staging/support-dumps/dump1/postgres/commands/tasks.txt"""]
