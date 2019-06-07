*** Settings ***
Library             RoboGalaxyLibrary
Resource            ../resource.txt
Documentation       Initial configuration for CDT Test Suite 01
Suite Setup         Initial Setup PreConditions
Suite Teardown      Initial Setup PostConditions

# Setup\Teardown for ALL test cases
Test Setup      Test Setup
Test Teardown   Test Teardown


*** Variables ***
${skipsuitesetup}       ${False}
#${BATCH_SIZE}          1
${WEB_USERNAME}         ${None}
${WEB_PASSWORD}         ${None}
${SPP_LOCALPATH}        .
${THREADNUM}            3
${SPP_LOCAL_FILE}       ${None}
${SYNERGY_ICM_LINK_MODULE_PATTERN}    .* Interconnect Link Module


*** Test Cases ***
Add Remote Enclosure to an existing OV
    [Documentation]             Add Remote Enclosures to OV
    [Tags]                      RE    SKIP_RE
    Add Remote Enclosure Setup    ${FLM_IPv6}

Wait For Devices To Reach Desired State
    [Documentation]             Wait for devices to go to Monitored state in OneView
    [Tags]                      State
    Wait For Resources To Reach Desired State    True

Enable OVF5956_APPMETRICS FT
    [Documentation]    Prerequisites: OV should have been installed on Synergy CIM
    ...    Step#1 : Enable OVF5956_APPMETRICS feature switch and ensure it does appliance reboot  
    ...    Step#2 : Wait for the appliance to be pingable
    ...    Step#3 : Wait for the appliance cluster to become OK
    ...    Step#4 : Wait for all the resources (enclosures, ICMs, servers, Drive enclosures) 
    ...             to go to desired terminal state
    ...    Step#5 : Enable appmetrics Feature switch and ensure it is enabled    
    ...    Step#6: Verifies that all the exportes are up and running in the appliance
    
    [Tags]    OVF5956_APPMETRICS
    
    Enable Feature Toggle    OVF5956_APPMETRICS
    Enable Feature Switch    /rest/appmetrics   
    Exporters Should Be Running In OV
    
Check Enclosure Interconnect Link Topology
    [Documentation]             Verify Interconnect Link Topology.
    [Tags]                      ilt    SKIP_ILT
    Enclosure Interconnect Link Topology Should Be In Expected State

Check Frame link Topology
    [Documentation]             Check Frame Link Topology
    [Tags]                      flt    SKIP_FLT
    Enclosure Manager Bays Should Be In Expected State    ${ENCLOSURES_MGRBays}

Create Users
    [Documentation]             Create users on OneView
    [Tags]                      System
    ${users} =                  Get Variable Value      ${users}
    Add Users from variable     ${users}

Set Time and Locale
   [Documentation]     Set Time and Locale
   [Tags]              System
   ${resp} =           Configure Appliance Time and Locale     ${Time_and_Locale}
   Wait for task2      ${resp}     timeout=60                  interval=10

Add Server Hardware Type
    [Documentation]    Adds the server hardware type to each of the entry in the assigned_sps variable
    [Tags]     Assigned_SP    SKIP_SHT
    ${sht_dict} =      Get All Server Hardware Type As Dictionary
    ${sht_type} =      Get All Server Hardware Uri As Dictionary
    ${sp_len}=      Evaluate                    len(${assigned_sps})
    :FOR    ${index}            in range    0                       ${sp_len}
    \   ${sht} =    Get From Dictionary    ${assigned_sps[${index}]}    serverHardwareUri
    \   ${uri} =    Get Variable Value    ${sht_type['${sht}']}
    \   ${sht_type_name} =    Get Variable Value    ${sht_dict['${uri}']}
    \   Set To Dictionary    ${assigned_sps[${index}]}   serverHardwareTypeUri    SHT:${sht_type_name}

#Restart Unconfigured Appliance
    #[Documentation]    Restart Appliance
    #[Tags]    Appliance_Restart    System
    #${payload}=    resource.Restart Appliance
    # Re-login to the appliance
    #Fusion Api Login Appliance      ${APPLIANCE_IP}             ${admin_credentials}
    #Login to Fusion Via SSH
    # Post data to ELK
    #Set To Dictionary    ${payload}    condition    unconfigured
    #Run Keyword If    "${production_env}" == "${True}"
    #...    Post Data to ELK    ${cdt-ci-restart_elk_index}    ${payload}

Get Synergy Composer Startup Time
    [Documentation]    Prerequisites: OV should have been installed on Synergy CIM via Nuvo Reimage tool
    ...    Step#1 : Get the path to nuvo.log from variable ${NUVO_LOG}
    ...    Step#2 : Parse the Nuvo log file and extract both the CIMs startup time
    ...    Step#3 : Create CIM startup time payload for ELK and Post the same
    ...    Expected Result : Verify that it is possible to locate the nuvo.log, parse and extract the CIMs startup time and post them to ELK
    
    [Tags]    CIM-StartUp
    ${nodes} =    Get Fusion Nodes 
    ${no_of_cims} =    Get Length    ${nodes}

    ${logfile}=    Get Variable Value    ${NUVO_LOG}
    Run Keyword If    '${logfile}' == '${None}'    FAIL
    ...                Actual Result: Could not get the Path to nuvo.log file. Won't be able to proceed with the rest of the test steps. Ensure that NUVO_LOG variable is set to aboslute path of nuvo.log file.
    ${cim1_reimage_ts}    ${cim1_complete_ts}    ${cim2_reimage_ts}    ${cim2_complete_ts} =
    ...                   Parse Nuvo Log And Extract CIM Startup Time    ${logfile}   ${no_of_cims}

    ${payload} =       Create CIM Startup Time Payload    ${no_of_cims}    ${cim1_reimage_ts}
    ...                ${cim1_complete_ts}    ${cim2_reimage_ts}    ${cim2_complete_ts}

    Login to Fusion Via SSH
    Run Keyword If    "${production_env}" == "${True}"
    ...    Post Data to ELK    ${cdt-ci-restart_elk_index}    ${payload} 
    Close Connection
    
Get RMs Performance Data
    [Documentation]         Get the RMs Perf data from appliance. It does this by downloading the atlas-devmode and ...
    ...                     atlas-flog packages, extract the RPMs, copies the perl script files to /usr/local/share of ...
    ...                     appliance. Then run the perl script cic-start-performance which is part of the
    ...                     atlas-devmode package. It would create a csv file with RMs startup time data.
    ...                     Download this file from the applaince to Testhead directory from where the tests are
    ...                     executing, parse it and upload the RM startup time to ELK
    [Tags]                  RMPerf
    ${time} =               Get Time        epoch
    ${dir} =                Set Variable    /tmp/perf_${time}
    Fusion Api Login Appliance              ${APPLIANCE_IP}     ${admin_credentials}
    Login to Fusion Via SSH
    ${flogrpm} =            Set Variable    atlas-flog-*\\.rpm
    ${flogpattern} =        Set Variable    atlas-flog-.*\\.rpm
    ${devmoderpm} =         Set Variable    atlas-devmode-*\\.rpm
    ${devmodepattern} =     Set Variable    atlas-devmode-.*\\.rpm
    ${execfile} =           Set Variable    cic-start-performance
    ${flogextracts} =       Set Variable    usr/local/share/perl5
    ${csvfilename} =        Set Variable    rm_csv
    ${plugrpm} =            Set Variable    perl-Module-Pluggable-*\\.rpm
    ${plugrpmpattern} =     Set Variable    perl-Module-Pluggable-.*\\.rpm

    ${version} =        Get OneView Version
    #Fusion Version: 4.20.00-0354094,2018-07-23T17:40:45+0000
    ${major} =          Evaluate    re.search(r'(\\d+\\.\\d+\\.\\d+)-(\\d+),.*', "${version}").group(1)     modules=re
    #${major} would be 4.20.00
    ${major_part} =     Evaluate    re.search(r'(\\d+\\.\\d+)\\.\\d+-\\d+,.*', "${version}").group(1)       modules=re
    #${major_part} would be 4.20
    ${minor} =          Evaluate    re.search(r'(\\d+\\.\\d+\\.\\d+)-(\\d+),.*', '${version}').group(2)     modules=re
    #${minor} would be 0354094
    ${OVRel} =           Evaluate    '${version}'.split('.')[0]  # This gives left most version digit. for e.g. '4'
    ${devbuildhost} =    Get From Dictionary    ${dev_pack_host}    ${OVRel}
    
    ${command} =     Set Variable     rpm -qa | grep perl-Module-Pluggable
    ${response}         Execute Command     ${command}
    ${stdout}           ${stderr}       ${rc}=      Execute Command     ${command}      return_stderr=True
    ...                 return_rc=True
    Run Keyword If   ${rc} != 0    Download And Install perl-Module-Pluggable    ${RPM_WEB_URL}    ${dir}    ${plugrpm}   ${plugrpmpattern}   
    
    ${floguri} =        Evaluate
    ...                 "http://%s/Atlas/release/%s/YUM/Builds/Latest/" %('${devbuildhost}', '${major}')

    ${atlasdevuri} =    Evaluate
    ...                 "http://%s/Fusion/rel/%s/YUM/Builds/Latest/" %('${devbuildhost}', '${major_part}')
    
    ${path}         ${flogrpm}=     Download File In Remote System      ${dir}      ${floguri}      ${flogrpm}
    ...             ${flogpattern}
    Extract RPM     ${path}         ${flogrpm}

    SSHLibrary.Directory Should Exist                   ${path}/${flogextracts}
    ${command} =                Set Variable            cd ${path}/usr/local/share/;cp -rf perl5 /usr/local/share/
    ${stdout}                   ${stderr}               ${rc}=      Execute Command         ${command}      return_stderr=True
    ...                         return_rc=True
    Should Be Equal As Integers                         ${rc}       0
    ...                         msg=Failed to copy perl5 folder ${stderr}
    ${path}                     ${devmoderpmfile}=      Download File In Remote System      ${dir}          ${atlasdevuri}
    ...                         ${devmoderpm}
    ...                         ${devmodepattern}
    Extract RPM                 ${path}                 ${devmoderpmfile}
    ${execpath} =               Set Variable            ${path}/ci/bin
    Get RM Performance Data     ${execpath}             ${execfile}

    Parse CSV And Post Webapp Startup Time      path=.      filename=${csvfilename}


# This is not yet supported on Production Daisy/Rose run.
Add FC License
       [Documentation]                 Add FC License
       [Tags]                          System
       #Remove All FC Licenses
       ${validLicenses}=               Get From Dictionary         ${newLicenses}              license
       Add Licenses From Variable      ${validLicenses}
       Should Exist Valid Licenses In License Pool But Unassigned To ICM                       ${newLicenses}

#FC License Should Be Consumed And Assigned To ICM
#       [Documentation]                 FC License Should Be Consumed And Assigned To ICM
#       [Tags]                          System
#       Add FC Uplinkset For LI If Not Existing
#       ${li_resp}=                     Logical Interconnect FC License Should Be Consumed      ${LI_name}          ${2}
#...     Yes
#       Should Exist Valid Licenses In License Pool And Assigned To ICM                         ${newLicenses}      ${li_resp}
#       Remove Uplinkset By Name        ${US_name}
#
#Remove All Custom Address Ranges
#       [Documentation]                 Remove any existing Custom Address ranges.
#       [Tags]                          System
#       ${pools} =                      Create List                 /rest/id-pools/vmac
#...     /rest/id-pools/vwwn/rest/id-pools/vsn
#       Run Keyword for List            ${pools}                    Remove Custom Range
#
#Create Custom Address Ranges
#       [Documentation]                 Disable Generated Address Ranges and Create Custom Address ranges.
#       [Tags]                          System
#       ${ranges} =                     Get Variable Value          ${ranges}
#       ${pools} =                      Run Keyword If              ${ranges} is not ${null}    Create List
#...     /rest/id-pools/vmac
#...     /rest/id-pools/vwwn
#...     /rest/id-pools/vsn
#       Run Keyword If                  ${ranges} is not ${null}    Run Keyword for List        ${pools}
#...     Disable ALL Generated ID Ranges
#       Run Keyword If                  ${ranges} is not ${null}    Add Ranges From variable    ${ranges}
#
#Change Appliance Certificates To Be CA Signed
#       Import Gobaba Root CA And Intermediate CA                   ${cert_body_example}
#       Change Appliance Certificates To Gobaba CA Signed           FIPS                        sha256rsa
#       Wait Until Keyword Succeeds     2 min                       5 sec
#...     Apache And Rabbitmq Server Certificate Should Be Same

Clean Up Left-over VLUNs in Existing Volumes
    [Documentation]    Remove any left over presentations on the Volumes to be imported.
    ...    This allows reimaging OneView without deleting profiles with 3par storage.
    [Tags]    Storage    SKIP    Clean
    Storage3par Open Connection    ${storage_systems[0]['hostname']}    ${storage_systems[0]['credentials']['username']}    ${storage_systems[0]['credentials']['password']}
    :FOR  ${volume}    IN  @{existing_volumes}
    \  ${vluns}=    Get VLUNs for Volume ${volume['deviceVolumeName']}
    \  ${num_vluns}=    Get Length    ${vluns}
    \  Run Keyword If    ${num_vluns} > 0  Delete VLUNs  ${vluns}
    Storage3par Close Connection

Add SAN Managers
    [Documentation]             Add SAN Managers to OneView
    [Tags]                      Storage
    Add San Managers Async      ${san_managers}

Add the Storage System to OV
    [Documentation]     Add the Storage System to OV
    [Tags]              Storage    Storage_System
    ${resplist} =       Add Storage Systems Async       ${storage_systems}
    Wait for task2      ${resplist}                     timeout=60      interval=10
    ${resp} =           Fusion Api Get Storage System   param=?filter="'name'=='${storage_systems[0]['name']}'"
    Run Keyword If      ${resp['count']}==0             FAIL            Addition of ${storage_systems[0]['name']} failed

Edit StoreServ Storage Sytem to be managed in OV
    [Documentation]     Edit StoreServ Storage Sytem to manage in OV
    [Tags]              Storage    Storage_System  StoreServ
    ${storage_system}    Get Data from Array by name    ${storage_systems}  ${STORESERV_NAME}
    ${store_serv}=      Create List    ${storage_system}
    ${resplist} =       Edit Storage Systems Async      ${store_serv}
    Wait for task2      ${resplist}                     timeout=180     interval=10
    ${resp} =           Fusion Api Get Storage System   param=?filter="'name'=='${store_serv[0]['name']}'"
    Run Keyword If      ${resp['count']}==0             FAIL            Addition of ${store_serv[0]['name']} failed
    Run keyword if      '${resp['members'][0]['status']}'!='OK' or '${resp['members'][0]['state']}'!='Managed'      FAIL
    ...                 Failed to manage StoreServ storage system

Configure Storage Pools in OV
    [Documentation]     Configure Storage Pools in OV
    [Tags]              Storage
    ${resplist} =       Edit Storage Pools Async    ${storage_pools}
    Wait for task2      ${resplist}                 timeout=120     interval=10
    Verify Storage Pool is Managed                  ${storage_pools}

Add Storage Volume Templates
    [Documentation]             Add Storage VOLUME TEMPLATES to OneView
    [Tags]                      Storage
    ${responses} =              Add Storage Volume Templates Async      ${storage_volume_templates}
#    Verify Resources for List   ${expected_storage_volume_templates}

Import Existing Storage Volumes
    [Tags]              Storage         EXISTING_VOLUMES
    [Documentation]     Import existing Storage Volumes from 3par
    ${resplist} =       Add Existing Storage Volumes Async      ${existing_volumes}
    Wait for task2      ${resplist}     timeout=120             interval=10
    #TODO: Verify storage volumes were added.

Create Ethernet Networks
    [Documentation]             Create Ethernet Networks based on data definition
    [Tags]                      Networking
    ${ethernet_networks} =      Get Variable Value                      ${ethernet_networks}
    Run Keyword If              ${ethernet_networks} is not ${null}     Add Ethernet Networks from variable async
    ...                         ${ethernet_networks}

Create FCoE Networks
    [Documentation]         Create FCoE Networks based on data definition
    [Tags]                  Networking
    ${fcoe_networks} =      Get Variable Value                  ${fcoe_networks}
    Run Keyword If          ${fcoe_networks} is not ${null}     Add FCoE Networks from variable     ${fcoe_networks}

Create FC Networks
    [Documentation]     Create FC Networks based on data definition
    [Tags]              Networking
    ${fc_networks} =    Get Variable Value              ${fc_networks}
    Run Keyword If      ${fc_networks} is not ${null}   Add FC Networks from variable   ${fc_networks}

Create Network Sets
    [Documentation]     Create Network Sets based on data definition
    [Tags]              Networking
    ${network_sets} =   Get Variable Value                  ${network_sets}
    Run Keyword If      ${network_sets} is not ${null}      Add Network Sets from variable      ${network_sets}

Add Network to StoreVirtual Storage
    [Documentation]     Edit StoreVirtual Storage Sytem to manage in OV
    [Tags]              Networking    Storage_System  StoreVirtual
    ${storage_system}    Get Data from Array by name    ${storage_systems}  ${STOREVIRTUAL_NAME}
    ${store_virtual}=       Create List    ${storage_system}
    ${resplist} =       Edit Storage Systems Async      ${store_virtual}
    Wait for task2      ${resplist}                     timeout=180     interval=10
    ${resp} =           Fusion Api Get Storage System   param=?filter="'name'=='${store_virtual[0]['name']}'"
    Run Keyword If      ${resp['count']}==0             FAIL            Addition of ${store_virtual[0]['name']} failed
    Run keyword if      '${resp['members'][0]['status']}'!='OK' or '${resp['members'][0]['state']}'!='Managed'      FAIL
    ...                 Failed to manage StoreVirtual storage system

Add Rack Servers
    [Documentation]     Add Rack servers to OneView if available
    [Tags]              Networking
    ${racks} =          Get Variable Value          ${racks}
    Run Keyword If      ${racks} is not ${null}     Add Racks from variable     ${racks}

Add Proxy Server
    [Tags]    REMSUPP
    [Documentation]        Add Proxy Server to OV
    ${responses}=  Add Proxy Server to OV    ${proxy_servers}
    Run Keyword for List with kwargs  ${responses}  Wait For Task2   timeout=60

Enable HPE Remote Support Settings
    [Tags]    REMSUPP
    [Documentation]    Enable remote support registration in oneview settings
    First Time Remote Support Registration     ${remotesupport_edit}
    HPE Remote Support Connection Should Be    ${TRUE}
    Wait Until Enclosures Reached State           Enabled    15 min   1 min
    ...        stateStr=['supportState']
    Wait Until Interconnects Reached State        Enabled    60 sec   10 sec
    ...        stateStr=['remoteSupport']['supportState']    skipPattern=${SYNERGY_ICM_LINK_MODULE_PATTERN}
    Wait Until SAS Interconnects Reached State    Enabled    60 sec   10 sec
    ...        stateStr=['remoteSupportSettings']['supportState']
    Wait Until Servers Reached State              Enabled    60 sec   10 sec
    ...        stateStr=['supportState']

Create LIGs
    [Documentation]     Create LIGs
    [Tags]              Networking
    ${sas_ligs} =       Get Variable Value              ${sas_ligs}
    ${sas_resplist}=    Run Keyword If      ${sas_ligs} is not ${null}      Run Keyword for Dict    ${sas_ligs}     Add SAS LIG

    ${ligs} =           Get Variable Value          ${ligs}
    ${lig_resplist}=    Run Keyword If      ${ligs} is not ${null}      Run Keyword for Dict    ${ligs}     Add LIG from variable async

    ${resplist}=    Combine Lists    ${sas_resplist}    ${lig_resplist}
    Wait for task2      ${resplist}                     timeout=20m      interval=10

Create EGs
    [Documentation]     Create EGs
    [Tags]              Networking
    ${enc_group_dict} =    Evaluate    copy.deepcopy(${enc_groups})    modules=copy
    ${resplist}=           Run Keyword for Dict    ${enc_group_dict}
    ...                 Add Enclosure Group from variable
    Wait for task2      ${resplist}                     timeout=5m      interval=10

Create LEs
    [Documentation]     Create LEs
    [Tags]              Networking                     Create_LE               Performance
    ...                 logical_enclosure-condition-single
    ${les} =            Get Variable Value              ${les}
    Create Logical Enclosures    ${les}
    Wait For Resources To Reach Desired State    False
    ${task}    Get Task By Param    param=?filter="'name'='Create' AND associatedResource.resourceName='${les[0]['name']}'"&sort=created:descending&count=1
    ${alt}    Get Active Alert List    ${task['created']}
    ${len}    Get length    ${alt}
    Run keyword and continue on failure    Run keyword if    ${len}!=0    FAIL    Critical/Active alerts exist.
    Check uplink sets and uplink ports

Create SAS LJBODs
    [Tags]    Create_Logical_JBODs    SKIP_JBOD
    [Documentation]     Create SAS Logical JBOD
    ${resplist}=    Create Logical JBODs from variable     ${ljbod}
    Wait for task2      ${resplist}                     timeout=5m      interval=10

Create Server Profile Templates
       [Tags]              CREATE_SPT
       [Documentation]     Create Server Profile Templates
       Assign Hardware type to SPT
       ${spts_dict} =    Evaluate    copy.deepcopy(${spts})    modules=copy
       ${resplist}=    Run Keyword for Dict    ${spts_dict}    Add Server Profile Template
       ${resp}=    Run Keyword for List    ${resplist}    Wait for Task2    timeout=5m    interval=10

#Create Unassigned Server Profiles from Server Profile Templates
#   [Tags]              Unassigned_SP           SPT                     Profiles
#   [Documentation]     Create Server Profiles from Server Profile Templates
#   ${sp_from_spts} =   Get Variable Value      ${sp_from_spts}
#   ${items} =          Get Dictionary Items    ${sp_from_spts}
#   ${servers}=         Get Dictionary Values   ${unassigned_sp_to_bay_map}
#   Power Off Servers Async                     ${servers}
#   :FOR                ${key}                  ${value}                IN          @{items}
#   \                   Run Keyword             Create SP from SPT      ${key}      ${value}

#Assign Server Profiles to Server Hardware
#       [Tags]                  Assign_SP           Profiles                Performance     server_profiles-condition-jbods
#       [Documentation]         Assign Server Profiles to Server Hardware and check for failures
#       ${server_profile_to_bay_map} =              Get Variable Value      ${unassigned_sp_to_bay_map}
#       ${tasks} =              Run Keyword If      ${unassigned_sp_to_bay_map} is not ${null}
#       ...                     Assign Server Hardware To Existing Profiles From Variable   ${unassigned_sp_to_bay_map}
#...     concurrent_profiles=4
#       Validate Task List      ${tasks}
# TODO: Use physical mac address and wwn from the server in the profile.

Download Firmware Bundle To Current Machine
    [Tags]              DOWNLOAD_SPP
    [Documentation]     Download SPP from http/ftp share latest file into current directory
    Download Latest File From Web Folder    ${SPP_WEB_URL}   WEB_USERNAME=${WEB_USERNAME}   WEB_PASSWORD=${WEB_PASSWORD}

Add Firmware Bundle
    [Tags]              UPLOAD_SPP
    [Documentation]     Upload SPP bundle ${SPP_LOCAL_FILE} to OneView
    ${status}           ${message}          Run Keyword And Ignore Error                    OperatingSystem.File Should Exist
    ...                 ${SPP_LOCAL_FILE}
    Run Keyword If      '${status}'=='FAIL'
    ...                 Log                 SPP File is not download from HTTP Url.Pick up latest SPP file from local path
    ...                 WARN
    ...                 console=True
    Create Folder If Not Exists             ${SPP_LOCALPATH}
    ${file}=            Run Keyword If      '${status}'=='FAIL'         Get File From Local Path        ${SPP_LOCALPATH}
    ${filestatus}       ${filemsg}          Run Keyword And Ignore Error                    OperatingSystem.File Should Exist
    ...                 ${file}
    ${SPP_FILE}=        Set Variable If     '${filestatus}' == 'FAIL'   ${SPP_LOCAL_FILE}   ${file}
    Log                 SPP to be Installed:${SPP_FILE}                 console=True
    # Unset proxy environ variables
    ${HTTP_PROXY}=  Get Environment Variable  HTTP_PROXY    default=${EMPTY}
    ${HTTPS_PROXY}=   Get Environment Variable  HTTPS_PROXY    default=${EMPTY}
    Set Environment Variable    HTTP_PROXY   ${EMPTY}
    Set Environment Variable    HTTPS_PROXY   ${EMPTY}

    Run Keyword If      '${SPP_FILE}' != '${None}'                      Upload Firmware Bundle Async    ${SPP_FILE}
    ...                 VERIFY=${TRUE}
    ...                 ELSE                Log                         No SPP Bundle available in local path to upload
    ...                 WARN
    ...                 console=True
    # Set proxy environ variables back to its actual value
    Set Environment Variable    HTTP_PROXY   ${HTTP_PROXY}
    Set Environment Variable    HTTPS_PROXY   ${HTTPS_PROXY}
    
Create Assigned Server Profiles
    [Tags]              Assigned_SP     Profiles    Performance     cdt-performance-scale    server_profiles-condition-jbods
    [Documentation]     Create Assigned Server Profiles

    # Power Off Servers
    ${servers}=     Get Dictionary Values       ${assigned_sp_to_bay_map}
    Power Off Servers Async                     ${servers}    control=PressAndHold

    # Create Assigned Server Profiles asynchronously
    # Create Assigned Server Profiles    ${assigned_sps}
    Run Keyword If     ${BATCH_SIZE} == ${None}    Create Assigned Server Profiles    ${assigned_sps}
    ...       ELSE     Create Assigned Server Profiles by Batch size    ${assigned_sps}    ${BATCH_SIZE}

    # Create Assigned Server Profiles by Batch size
    #Create Assigned Server Profiles by Batch size    ${assigned_sps}    ${BATCH_SIZE}


#Power on all blades
#   [Documentation]     Power on all blades
#   [Tags]              Profiles
#   Power On ALL Servers Async
#   All Servers Should Be Powered On

#Deploy and configure OS
#   pass execution      Not implemented yet.
#
#Generate Traffic on Servers
#   pass execution      Not implemented yet.



*** Keywords ***
Initial Setup PreConditions
    [Documentation]     Perform setup of all necessary resources for all additional tests
    [Tags]              TSS     Setup

    Return from keyword if      ${skipsuitesetup} is ${True}    # allows you to override running Suite Setup on cmd line

    Set RoboGalaxyLibrary Version Metadata
    Set FusionLibrary Version Metadata

    Set Suite Variable              ${WFT2_CONTINUE_ON_ERROR}   ${TRUE}
    Run Keyword and Ignore Error    Write To ciDebug Log        TEST-SPECIFIC SETUP
    Fusion Api Login Appliance      ${APPLIANCE_IP}             ${admin_credentials}
    Login to Fusion Via SSH

Initial Setup PostConditions
    [Documentation]     Perform all post-condition actions for Initial Config. Sets global steup success flag.
    Run Keyword If      '${SUITE_STATUS}' == 'PASS'     Set Global variable     ${initialConfigSuccess}     ${TRUE}
