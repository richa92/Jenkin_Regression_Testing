*** Settings ***
Documentation    Try some stuff

Library				RoboGalaxyLibrary
Library				FusionLibrary
Library             json
#Library             Dialogs
#Library             OperatingSystem
#Library             String
#Library             copy
#Library             Instance.py     # private module that returns my local RG instance
#Variables 		    data_variables.py
#Variables 		    a.py
Variables           data.py
#Resource            ../../../resources/resource.txt
Resource            ../../../../../Resources/api/fusion_api_resource.txt
#Resource            ../../../../resource/fusion_api_all_resource_files.txt

Suite Setup         Set Log Level   TRACE
#Suite Teardown		Suite Teardown


# Setup\Teardown for ALL test cases
#Test Setup     Run Keyword and Ignore Error    Write To ciDebug Log
#Test Teardown  Run Keyword If    '${TEST_STATUS}' == 'FAIL'   Get Errors


*** Variables ***
#${X-API-Version} =    299
#${APPLIANCE_IP}    15.245.131.206
${APPLIANCE_IP}    16.114.208.62
${FUSION_IP}     ${APPLIANCE_IP}
${IP}            ${APPLIANCE_IP}
${FUSION_PROMPT}     \#     # Fusion Appliance Prompt
${FUSION_TIMEOUT}    15    # Timeout.  Move this out???
${FUSION_NIC} =     bond0   # Fusion Appliance Primary NIC
${FUSION_NIC_SUFFIX} =   %${FUSION_NIC}
${FUSION_USERNAME} =   Administrator  # Fusion Appliance Username
${FUSION_PASSWORD} =    hpvse123  # Fusion Appliance Password
${FUSION_SSH_USERNAME} =   root  # Fusion SSH Username
${FUSION_SSH_PASSWORD} =   hpvse1  # Fusion SSH Password
${SSH_HOST}      ${APPLIANCE_IP}

*** test cases ***
update HPIP
    [Tags]   hpip
    ${uri} =         set variable     /rest/server-hardware/34343738-3036-584D-5138-323530304D54
    ${token} =       Get Trusted Token        ${IP}
    ${iSERVER} =     Get iLO ipv6     ${token}   ${uri}
    ${iUSER} =       set variable     _HPOneViewAdmin
    ${iPASSWORD} =   Get _HPOneViewAdmin iLO credentials   ${token}   ${uri}
    ${output} =      Get Storage info    ${iUSER}    ${iPASSWORD}   ${iSERVER}
	${admin_credentials} =      json.loads    {"userName": "Administrator", "password": "hpvse123"}

A
    ${uri} =         set variable     /rest/server-hardware/30373737-3237-324B-3539-4E5030303439
    ${token} =       Get Trusted Token        ${IP}
    ${iSERVER} =     Get iLO ipv6     ${token}   ${uri}
    ${iUSER} =       set variable     _HPOneViewAdmin
    ${iPASSWORD} =   Get _HPOneViewAdmin iLO credentials   ${token}   ${uri}
    ${output} =      Factory reset server    ${iUSER}    ${iPASSWORD}   ${iSERVER}
	${admin_credentials} =      json.loads    {"userName": "Administrator", "password": "hpvse123"}
    Fusion Api Login Appliance         ${IP}        ${admin_credentials}
    ${bl} =          fusion api get resource    ${uri}
    ${enc} =         Fetch from left     ${bl['name']}    ,
    ${bay} =         Fetch from right    ${bl['name']}    ${SPACE}
    Get EM IP        ${enc}
    Get EM Token     ${enc}
    # check blade power
    Efuse Blade      EFuseOn     ${bay}
    #wait for tasks to complete
    sleep    3m
    Efuse Blade      EFuseOff     ${bay}
    #wait for tasks to complete


test
    [Tags]   a1
    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
 	${server_profiles} =	Get Variable Value	${server_profiles_nohw}
 	Run Keyword If	${server_profiles} is not ${null}		Add Server Profiles from variable no hardware	${server_profiles}   ${server_profile_to_bay_map}





test1
    [Tags]   a3
	Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
    #${resp} =    Create SP from SPT    SPT_EG_SY_480_Gen9_1   NewProfileName
    Run Keyword for List	${ligs}    Add LIG from variable

A very special test case
    [Tags]   a10
    Set Log Level	TRACE
	Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
	Run Keyword and Ignore Error    Write To ciDebug Log
	[Teardown]   Get errors

a1
    [Tags]   a0
    Set Log Level	TRACE
	Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
    ${resp} =   Fusion Api Upload Backup   /root/Downloads/f749-f751_backup_2017-01-20_184637.bkp
    ${task_uri} =   Get From Dictionary   ${resp}   taskUri
    Should Not Be Empty    ${task_uri}    msg=No task uri could be retreived from response
    ${resp} =   Fusion Api Get Task    uri=${task_uri}
    ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}

ba
    [Tags]   ba
    Set Log Level	TRACE
	Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
	${body} = 	json.loads    {"bandwidth": {"maximumBandwidth": 15000, "minimumBandwidth": 5000}}
    ${resp} =   update connection template    net_999   ethernet    ${body}

aa
    [Tags]   aa
    Set Log Level	TRACE
	Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
    ${resp} =    Fusion Api Get Appliance Version
    Set Suite Metadata     OneView Version      ${resp['softwareVersion']}    top=True
    ${uri} =   set variable   /rest/alerts?filter="alertState='Active'"&filter="healthCategory='ConnectionInstance'"
    ${resp} =   fusion api get resource     ${uri}

aaa
    [Tags]   aaa
    Set Log Level	TRACE
	${admin_credentials} =      json.loads    {"userName": "Administrator", "password": "hpvse123"}
    ${resp} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
    ${icms} = 	 json.loads    ["CN75016BG8, interconnect 2", "CN75016BG8, interconnect 3"]
	:FOR	${x}	IN 	 @{icms}
    \    ${resp} =    Fusion Api Get Interconnect    param=?filter="'name'=='${x}'"
    \    Log to console and logfile    \n${resp['members'][0]['name']} state:${resp['members'][0]['state']}


b
    [Tags]   b
    Set Log Level	TRACE
    Get EM IP
    Get EM IP   CN750202SK


c
    [Tags]   c
	Set Log Level	TRACE
	${admin_credentials} =      json.loads    {"userName": "Administrator", "password": "hpvse123"}
    ${resp} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
    ${lig} =     json.loads    { "enclosureIndexes": null, "enclosureType": "C7000", "ethernetSettings": null, "interconnectBaySet": null, "interconnectMapTemplate": { "interconnectMapEntryTemplates": [ { "enclosureIndex": 1, "logicalLocation": { "locationEntries": [ { "relativeValue": 1, "type": "Bay" }, { "relativeValue": 1, "type": "Enclosure" } ] }, "permittedInterconnectTypeUri": "/rest/interconnect-types/7e6d3be1-d738-4fb3-8d6a-9ab8c8167b4e" }, { "enclosureIndex": 1, "logicalLocation": { "locationEntries": [ { "relativeValue": 2, "type": "Bay" }, { "relativeValue": 1, "type": "Enclosure" } ] }, "permittedInterconnectTypeUri": "/rest/interconnect-types/7e6d3be1-d738-4fb3-8d6a-9ab8c8167b4e" } ] }, "internalNetworkUris": null, "name": "LIG1", "qosConfiguration": null, "redundancyType": null, "snmpConfiguration": null, "stackingMode": null, "state": "Active", "telemetryConfiguration": null, "type": "logical-interconnect-groupV300", "uplinkSets": [ { "ethernetNetworkType": "Tagged", "lacpTimer": "Short", "logicalPortConfigInfos": [ { "desiredSpeed": "Auto", "logicalLocation": { "locationEntries": [ { "relativeValue": 1, "type": "Enclosure" }, { "relativeValue": 5, "type": "Bay" }, { "relativeValue": "22", "type": "Port" } ] } }, { "desiredSpeed": "Auto", "logicalLocation": { "locationEntries": [ { "relativeValue": 1, "type": "Enclosure" }, { "relativeValue": 6, "type": "Bay" }, { "relativeValue": "22", "type": "Port" } ] } } ], "mode": "Auto", "name": "badUS", "nativeNetworkUri": null, "networkType": "Ethernet", "networkUris": [], "primaryPort": null } ] }
    ${resp} =    fusion api create lig    body=${lig}



deepcopy
    [Tags]   deepcopy
	Set Log Level	TRACE
    #${x} =    copy.deepcopy    ${admin_credentials}
    ${x} =    Copy Dictionary    ${admin_credentials}

bbbb
    [Tags]   b
	Set Log Level	TRACE

	${admin_credentials} =      json.loads    {"userName": "Administrator", "password": "hpvse123"}
    ${resp} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
    ${head} =    fusion api get http headers
    ${myauth} =    Get From Dictionary    ${head}   auth
    ${myauth} =    Set Variable   ${myauth}:xxxx

    Set to Dictionary   ${head}    auth   ${myauth}
    ${head} =    json.dumps    ${head}
	${resp} =    Fusion Api Get FC Networks    headers=${head}
    #${head} =    Get From Dictionary    ${resp}   headers


bbbbbb
    [Tags]   b
	${admin_credentials} =      json.loads    {"userName": "Administrator", "password": "hpvse123"}
    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
    ${f} =     json.loads    {"name": "fcoe_1002a", "type": "fcoe-networkV300", "vlanId": 1002}
    fusion api create fcoe network    ${f}

arp
    [Tags]   arp
	Set Log Level	TRACE
	log variables   level=DEBUG
    ${output} =     Run      arp -a
    ${l} =    Get Lines Containing String   ${output}    a0-1d-48-95-92-30
    ${m}   ${ip} =  Should Match Regexp     ${l}    (\\d+.\\d+.\\d+.\\d+)
    Log    ${ip}   console=True


log
    [Tags]   log
	Set Log Level	TRACE
	log variables   level=DEBUG
	${admin_credentials} =      json.loads    {"userName": "Administrator", "password": "hpvse123"}
    ${resp} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
    ${resp} =    fusion api get interconnect types

power
    [Tags]   power
	${admin_credentials} =      json.loads    {"userName": "Administrator", "password": "hpvse123"}
    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
    Power off ALL servers

ic
    [Tags]   ic
	${admin_credentials} =      json.loads    {"userName": "Administrator", "password": "hpvse123"}
    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
    ${resp} =   fusion api get interconnect types

upgrade
   [Tags]   upgrade
	${admin_credentials} =      json.loads    {"userName": "Administrator", "password": "hpvse123"}
    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
    #${resp} =         Fusion Api Upload Appliance Firmware            localfile=c:\\update.bin
    ${resp} =         Fusion Api Upload Firmware Bundle                localfile=c:\\spp.iso

dd
   [Tags]   dd
   ${websrvr} =    Set variable   http://15.199.229.198/files/ddimage
   ${ddimage} =    Set Variable   crap.zip
   ${Command} =    Set variable   /ci/etc/usb-reimage/developer_usb_reimage.sh -F -I -u ${websrvr} -f ${ddimage}
   Run Command Via SSH   15.199.229.190   root   hpvse1   ${Command}   \#   500

blah
   [Tags]   s
   ${uri} =   Set Variable    https://15.199.229.190/rest/tasks/FAA5B6AC-E743-4D29-A75B-7DFECB0CCDED
   ${uri} =   Remove String   ${uri}    https://    ${APPLIANCE_IP}

one
    [Tags]  one
	Set Log Level	TRACE
	log variables   level=DEBUG
	Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
	#${resp} =    Fusion Api generic post     ${None}   /rest/appliance/tech-setup
	Set Suite Variable   ${FUSION_IP}    ${APPLIANCE_IP}
    ${Output}    Execute SSH Command
    ...    curl -k -X POST -H "X-API-Version:200" https://localhost/rest/appliance/tech-setup
    ${resp} =    Fusion Api Get Task   param=?filter="'name'=='Discover hardware'"
    ${task} =    Get From List   ${resp['members']}   0
    Wait For Task   ${task}  30m  20s

    #AUTH=$(psql -A -t --dbname=ueproto --user=postgres -c "select session_id from session.session where username='erm'";); curl -ik -H "auth:${AUTH}" https://127.0.0.1/perm/rest/tbird/atlas/fts
	${inst} =    Instance.get
	call method   Instance    get
    #Fusion Api Get Internal Link Sets
    #Run Keyword for List	${ligs}    Add LIG from variable

version
    [Tags]  version
	Set Log Level	TRACE
	log variables   level=DEBUG
	Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}

    fusion api set default api version    api=101

    fusion srm ui verify sans

	Fusion Api Get Ethernet Networks
	Fusion Api Get FC Networks
    fusion api set default api version    api=120
	Fusion Api Get Ethernet Networks
	Fusion Api Get Ethernet Networks      api=299
	Fusion Api Get Ethernet Networks

test00
    [Tags]  x
	Set Log Level	TRACE
	log variables   level=DEBUG
	${admin_credentials} =      json.loads    {"userName": "Administrator", "password": "hpvse123"}
	Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
    #Add Users from variable     ${users}
    Login all users     ${users}
    ${resp} =   run keyword as user     Networkadmin    Fusion Api Get Ethernet networks    ${empty}    ?filter="'name'=='eth-102'"

test0
    [Tags]  0
	Set Log Level	TRACE
	log variables   level=DEBUG
	${admin_credentials} =      json.loads    {"userName": "Administrator", "password": "hpvse123"}
	Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}

	${ipv4Type} = 		Get Variable Value 	${appliance['applianceNetworks'][0]['ipv4Type']}
	${app1Ipv4Addr} = 	Get Variable Value	${appliance['applianceNetworks'][0]['app1Ipv4Addr']}
    ${virtIpv4Addr} = 	Get Variable Value	${appliance['applianceNetworks'][0]['virtIpv4Addr']}

    Run Keyword If	'${virtIpv4Addr}' is not 'None'                 Log     'virtIpv4Addr:' ${virtIpv4Addr}    WARN
	...             ELSE IF     '${app1Ipv4Addr}' is not 'None'     Log     'app1Ipv4Addr:' ${app1Ipv4Addr}    WARN
	...             ELSE    Log     Either app1Ipv4Addr or virtIpv4Addr must be provided in the 'appliance' variable in your data file     WARN

    #${resp} =       Common URI Lookup by name   LI:LE-BFS-IBS3-HA

test100
    [Tags]  1
	Set Log Level	TRACE
	log variables   level=DEBUG
    log     ${data.admin_credentials}
    ${creds} =  Copy Dictionary        ${data.admin_credentials}
    Set to Dictionary   ${creds}    password    xxx
    log     ${creds}

    ${creds2} =  Copy Dictionary        ${data.admin_credentials}
    Set to Dictionary   ${data.admin_credentials}    password    yyy
    log     ${data.admin_credentials}
    ${creds3} =  Copy Dictionary        ${data.admin_credentials}

test2
    [Tags]  2
	Set Log Level	TRACE
    log variables   level=DEBUG
    log     ${admin_credentials}

#    log     ${VAR.admin_credentials}
#    ${creds} =  Copy Dictionary        ${VAR.admin_credentials}
#    Set to Dictionary   ${creds}    password    xxx
#    ${creds2} =  Copy Dictionary        ${VAR.admin_credentials}

deploy vm
    [Tags]  testvm
    connect to vi server    15.199.229.100  rbriggs     hpvse1
    Rename VM   russell-RH6.3-rb    russell-RH6.3
    #deploy ovf ova template to folder in cluster    wpstvcbd110.usa.hp.com      rbriggs     hpvse1  0-hpCorpNET     test    "Z:\\ftp\\fusion\\2.0\\OVA\\HPOneView-SSH_2.00.00_30792_PASS19.ova"    Cluster_DataStore2      Russell     Palo Alto - 6A Lab (Cluster)     WPST-Cluster


	#${pools} =  Fusion Api Get Pool
	#${uri} =    Fusion Api Get Vmac Range   uri=/rest/id-pools/vmac
	#${resp} =   Fusion Api Delete Vmac Range    uri=/rest/id-pools/vmac/ranges/686da79c-3039-4cd0-aa1d-b206e0e33627

*** Keywords ***
Copy Dictionary
    [Documentation]     ...
	[Arguments]	${obj}
	Log   Deep copy version!!!
	${obj} =   copy.deepcopy   ${obj}
    [Return]	${obj}


Create fcoe range
    [Documentation]     ...
	[Arguments]	${range}
	#Set Log Level	TRACE
	:FOR	${x}	IN RANGE	${range['start']}	${range['end']}+1
	\	${body} = 	Create Dictionary	name=${range['prefix']}${x}${range['suffix']}	vlanId=${x}	 type=fcoe-network
	\	${resp} = 	Fusion Api Create Fcoe Network	body=${body}
	#\	Wait For Task	${resp}

update connection template
    [Documentation]   takes a network uri, finds it's ct uri, and then updates it
    [Arguments]    ${net}   ${body}   ${type}=ethernet
    ${ct_uri} =    Get connectionTemplateUri   ${net}   ${type}   ${body}
    ${resp} =      fusion api update connection template     ${ct_uri}   ${body}
    [Return]   ${resp}

Get Errors
    [Documentation]     ...
    ${ERRORS}=   Run Keyword and Ignore Error    Get Test Errors from ciDebug Log     ${TEST_NAME}

Create SP from SPT
    [Documentation]   Creates a new server profile named <spname> from SPT named <spt>
    [Arguments]    ${spt}   ${spname}    ${timeout}=10m   ${interval}=20s
    ${spt_uri} =    common.Common URI lookup by name     SPT:${spt}
    ${resp} =    Fusion Api Get Server Profile Template New Profile  ${spt_uri}
    # remove status code and headers
    remove from dictionary  ${resp}  status_code
	remove from dictionary  ${resp}  headers
	set to dictionary       ${resp}  name   ${spname}
	${resp} =    fusion api create server profile    body=${resp}
	${task} =	 fusion_api_appliance_setup.Wait For Task 	${resp}   ${timeout}   ${interval}
    Should Match Regexp   ${task['taskState']}	 ((?i)Warning|Completed)
    [Return]   ${resp}
