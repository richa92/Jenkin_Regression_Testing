*** Settings ***
Documentation                   Gen10 DL Server Licensing tests

Library             FusionLibrary
Library             RoboGalaxyLibrary
Library             BuiltIn
Library             Collections
Library             json
Library             XML
Library             String
Library             Dialogs

Resource            ./../../../../Resources/api/fusion_api_resource.txt
Resource            ../global_variables.robot
Variables           ${DATA_FILE}

Suite Setup         Setup
#Suite Teardown      Clean Up

*** Variables ***
${APPLIANCE_IP}     16.114.209.223
${DATA_FILE}        ./Regression_Data.py

*** Test Cases ***
OVS28827-Add Licenses without iLO
    [Tags]    Add-LiWOiLO
    Log To Console And Logfile    Adding new licenses without iLO
    Add Licenses From Variable    ${licensesWithoutIlo}

OVS28827-1
    [Tags]    V-E-Mon-1
    Add Enclosures from variable	${enclosureMonitored}
    Run Keyword If	${sh_standard} is not ${null}		Verify Resources For list	${sh_standard}
    Verify Enc SH Licenses      ${servers_IPs_keys}
    Verify Enclosures from list 	${Enc}  state=Monitored  licensingIntent=OneViewStandard
    Verify Licenses Count 	640
    Remove All Enclosures Async    VERIFY=${True}  timeout=600  interval=5

OVS28827-2
    [Tags]    V-E-WO-iLO-2
    ${li_type} =   Set Variable    'HPE OneView Advanced w/o iLO'
    Add Enclosures from variable	${enclosureWithOutIlo}
    Verify Enc SH Licenses      ${servers_IPs_keys}
    Run Keyword If	${sh_wo_ilo} is not ${null}		Verify Resources For list	${sh_wo_ilo}
    Verify Enclosures from list 	${Enc}  state=Configured  licensingIntent=OneViewNoiLO
    Verify Licenses Count 	635  ${li_type}
#    Remove All Enclosures Async    VERIFY=${True}  timeout=600  interval=5

OVS28827-3
    [Tags]    V-P-SH-3
    Run Negative Tasks for List     ${patch_server_task_bay3}
    #   The above operation should give error and intent of server does not get changed
    ${server} =  Get Resource  SH:${ENC20SHBAY3}
    Verify Resource  ${server}  licensingIntent=OneViewNoiLO

OVS28827-4
    [Tags]    V-P-SH-4
#   Not seeing any server with iLO intent to do patch


OVS28827-5
    [Tags]    V-P-E-5
    ${li_type} =   Set Variable    'HPE OneView Advanced w/o iLO'
    ${resp} =    Patch Enclosure  ${ENC20}  op=replace  path=/licensingIntent  value=OneView
    Verify Enc SH Licenses      ${servers_IPs_keys}
    Run Keyword If	${sh_wo_ilo} is not ${null}		Verify Resources For list	${sh_wo_ilo}
    Verify Enclosures from list 	${Enc}  state=Configured  licensingIntent=OneView
    Remove All Enclosures Async    VERIFY=${True}  timeout=600  interval=5

OVS28827-6
    [Tags]    V-E-W-iLO-6
    Remove All Enclosures Async    VERIFY=${True}  timeout=600  interval=5
    Delete All Fusion License with ssh
    Add Enclosures from variable	${enclosureWithIlo}
    Verify Enc SH Licenses      ${servers_IPs_keys}
    Run Keyword If	${sh_w_ilo} is not ${null}		Verify Resources For list	${sh_wo_ilo}
    Verify Enclosures from list 	${Enc}  state=Configured  licensingIntent=OneView
    Verify Licenses Count 	0  'HPE OneView Advanced'
    Verify Licenses Count 	636  'HPE OneView Advanced w/o iLO'

OVS28827-7
    [Tags]    V-P-SH-7
#    Patch Server Hardware  ${ENC20SHBAY3}  op=replace  path=/licensingIntent  value=OneView
#    ${server} =  Get Resource  SH:${ENC20SHBAY3}
#    Verify Resource  ${server}  licensingIntent=OneViewNoiLO
    Run Negative Tasks for List     ${patch_server_task}
    #   The above operation should give error and intent of server does not get changed
    ${server} =  Get Resource  SH:${ENC20SHBAY3}
    Verify Resource  ${server}  licensingIntent=OneViewNoiLO

OVS28827-8
    [Tags]    V-P-SH-8
    Patch Server Hardware  ${ENC20SHBAY8}  op=replace  path=/licensingIntent  value=OneView
    ${server} =  Get Resource  SH:${ENC20SHBAY8}
    Verify Resource  ${server}  licensingIntent=OneView

OVS28827-8-1
    [Tags]    V-P-SH-8-1
    Patch Server Hardware  ${ENC20SHBAY8}  op=replace  path=/licensingIntent  value=OneViewNoiLO
    ${server} =  Get Resource  SH:${ENC20SHBAY8}
    Verify Resource  ${server}  licensingIntent=OneViewNoiLO

OVS28827-8-2
    [Tags]    V-P-SH-8-2
    Run Negative Tasks for List     ${patch_server_task_bay8}
    ${server} =  Get Resource  SH:${ENC20SHBAY8}
    Verify Resource  ${server}  licensingIntent=OneViewNoiLO

OVS28827-9
    [Tags]    V-P-E-9
    ${li_type} =   Set Variable    'HPE OneView Advanced w/o iLO'
    ${resp} =    Patch Enclosure  ${ENC20}  op=replace  path=/licensingIntent  value=OneViewNoiLO
    Verify Enc SH Licenses      ${servers_IPs_keys}
    Run Keyword If	${sh_wo_ilo} is not ${null}		Verify Resources For list	${sh_wo_ilo}
    Verify Enclosures from list 	${Enc}  state=Configured  licensingIntent=OneView

OVS28827-10
    [Tags]    V-P-E-10
    Remove All Enclosures Async    VERIFY=${True}  timeout=600  interval=5
    Verify Licenses Count 	640  'HPE OneView Advanced w/o iLO'

OVS28827-Add Licenses with iLO
    [Tags]    Add-LiWiLO
    Log To Console And Logfile    Adding new licenses with iLO
    Add Licenses From Variable    ${licensesWithIlo}

OVS28827-1-2-1
    [Tags]    V-E-Mon2
    Add Enclosures from variable	${enclosureMonitored}
    Run Keyword If	${sh_standard} is not ${null}		Verify Resources For list	${sh_standard}
    Verify Enc SH Licenses      ${servers_IPs_keys}
    Verify Enclosures from list 	${Enc}  state=Monitored  licensingIntent=OneViewStandard
    Verify Licenses Count 	640
    Remove All Enclosures Async    VERIFY=${True}  timeout=600  interval=5

OVS28827-1-2-2
    [Tags]    V-E-WO-iLO2
#    Add Enclosures from variable	${enclosureWithOutIlo}
    ${li_type} =   Set Variable    'HPE OneView Advanced'
    Verify Enc SH Licenses      ${servers_IPs_keys}
    Run Keyword If	${sh_wo_ilo} is not ${null}		Verify Resources For list	${sh_wo_ilo}
    Verify Enclosures from list 	${Enc}  state=Configured  licensingIntent=OneViewNoiLO
    Verify Licenses Count 	640  ${li_type}
    Remove All Enclosures Async    VERIFY=${True}  timeout=600  interval=5

OVS28827-1-2-6
    [Tags]    V-E-W-iLO2
    ${li_type} =   Set Variable    'HPE OneView Advanced'
    Add Enclosures from variable	${enclosureWithIlo}
    Verify Enc SH Licenses      ${servers_IPs_keys}
    Run Keyword If	${sh_w_ilo} is not ${null}		Verify Resources For list	${sh_w_ilo}
    Verify Enclosures from list 	${Enc}  state=Configured  licensingIntent=OneView
    Verify Licenses Count 	639  ${li_type}
    Remove All Enclosures Async    VERIFY=${True}  timeout=600  interval=5
    Delete All Fusion License with ssh

OVS28827-1-3-7
    [Tags]    V-E-Mon3
    Add Enclosures from variable	${enclosureMonitored}
    Run Keyword If	${sh_standard} is not ${null}		Verify Resources For list	${sh_standard}
    Verify Enc SH Licenses      ${servers_IPs_keys}
    Verify Enclosures from list 	${Enc}  state=Monitored  licensingIntent=OneViewStandard
    Remove All Enclosures Async    VERIFY=${True}  timeout=600  interval=5

OVS28827-1-3-8
    [Tags]    V-E-WO-iLO3
    Add Enclosures from variable	${enclosureWithOutIlo}
    ${li_type} =   Set Variable    'HPE OneView Advanced'
    Verify Enc SH Licenses      ${servers_IPs_keys}
    Run Keyword If	${sh_wo_ilo} is not ${null}		Verify Resources For list	${sh_wo_ilo}
    Verify Enclosures from list 	${Enc}  state=Configured  licensingIntent=OneViewNoiLO
    Remove All Enclosures Async    VERIFY=${True}  timeout=600  interval=5

OVS28827-1-3-12
    [Tags]    V-E-W-iLO3
    ${li_type} =   Set Variable    'HPE OneView Advanced'
    Add Enclosures from variable	${enclosureWithIlo}
    Verify Enc SH Licenses      ${servers_IPs_keys}
    Run Keyword If	${sh_w_ilo} is not ${null}		Verify Resources For list	${sh_w_ilo}
    Verify Enclosures from list 	${Enc}  state=Configured  licensingIntent=OneView
    Remove All Enclosures Async    VERIFY=${True}  timeout=600  interval=5

OVS28827-Get-Licenses-blob
    [Tags]    GET-Li-blob
    ${licenses} =  Run cpqlocfg and Get Licenses from blob  ${DL380_IP}
    log to console		${licenses}

#OVS28827-Add Monitored Enc
#    OVS28827-Add Enclosure as Monitored
#    [Tags]    Add-EncMon
#    Add Enclosures from variable	${enclosureMonitored}
#
#OVS28827-Verify Monitored Enc
#    [Tags]    V-EncMon
#    Verify Enclosures from list 	${Enc}  state=Monitored  licensingIntent=OneViewStandard

#OVS28827-Verify Licenses640
#    [Tags]    V-LI640
#    Verify Licenses640
#
#OVS28827-Verify SH Standard
#    [Tags]    V-SH
#    Run Keyword If	${sh_standard} is not ${null}		Verify Resources For list	${sh_standard}
#
#OVS28827-Verify-all-SH-Licenses
#    [Tags]    V-SH-LI
#    Verify Enc SH Licenses      ${servers_IPs_keys}
#
#OVS28827-Remove Enclosure as Monitored
#    [Tags]    Remove-EncMon
#    Remove All Enclosures Async    VERIFY=${True}  timeout=600  interval=5
#
#OVS28827-Add Enclosure as Managed without iLO
#    [Tags]    Add-E-WO-ilo
#    Add Enclosures from variable	${enclosureWithOutIlo}
#
#OVS8663-DL-TestCase Add DL380 Gen10 server as managed
#    [Tags]    Add-DLs
#    Add DL380 Gen10 server as managed

#OVS28827-Get-Licenses
#    [Tags]    GET-Li
#    ${licenses} =  Run cpqlocfg and Get Licenses  ${DL360_IP}
#    log to console		${licenses}

OVS28827-Remove-Licenses
    [Tags]    Remove-LI
    ${licenses} =  Run cpqlocfg and Remove Licenses  ${DL180_IP}
#    ${licenses} =  Run cpqlocfg and Remove Licenses  ${DL120_IP}

OVS28827-Remove-Licenses-with-ssh
    [Tags]    Remove-LI-ssh
    Delete All Fusion License with ssh

#OVS28827-Set-Licenses
#    [Tags]    Set-LI
#    ${licenses} =  Run cpqlocfg and Remove Licenses  ${DL180_IP}
#    ${licenses} =  Run cpqlocfg and Set Licenses  ${DL120_IP}

#OVS28827-Add-Enc-withILO
#    [Tags]    Add-Enc-withILO
#	Add Enclosures from variable	${enclosureWithIlo}

#OVS28827-Add-Enc-withOutILO
#    [Tags]    Add-Enc-withOutILO
#	Add Enclosures from variable	${enclosureWithoutIlo}

Negative Tests
    [Documentation]   Negative Tests
    ${negative_server_profile_tasks} =	Get Variable Value	${negative_server_profile_tasks}
    Run Negative Tasks for List     ${negative_server_profile_tasks}

*** Keywords ***
Setup
    [Documentation]    OVS8663 Gen10 Setup
    Set Log Level  TRACE
    ${admin_session} =    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
#    Add LIG from list	            ${ligs}
#	Add Enclosure Group from list	${enc_groups}

Clean Up
    [Documentation]    OVS8663 Gen10 Teardown
    Power off Servers in Profiles    ${DL_gen10_server_profiles_imported_drives}
    ${resp} =    Remove Server Profiles from variable    ${DL_gen10_server_profiles_imported_drives}
    Wait For Task2    ${resp}       timeout=2400    interval=15
    Remove Server Profile Templates from variable  ${DL_gen10_profile_templates}
    Remove All DL Server Hardware Async
    Fusion Api Logout Appliance

Add Licenses
    [Documentation]    Add licenses
    Log To Console And Logfile    Adding new licenses
    Add Licenses From Variable    ${licenses}

Remove Monitored Enclosures
    [Documentation]  Remove Monitored Enclosures
    Remove All Enclosures Async    VERIFY=${True}  timeout=600  interval=5

Get SH Licenses
    [Documentation]    Get SH Licenses
    [Arguments]  ${sh_ip}
    ${licenses} =  Run cpqlocfg and Get Licenses  ${sh_ip}
#    ${licenses180_2} =  Run cpqlocfg and Get Licenses  ${DL180_2_IP}
    log to console		${licenses}

Verify Enc SH Licenses
    [Documentation]    Verify Enc SH Licenses
    Log To Console And Logfile    Verify Enc SH Licenses
    [Arguments]  ${sh_list}
    :FOR    ${sh}    IN    @{sh_list}
    \       ${sh_ip} =   Set Variable    ${sh['IP']}
    \       ${sh_li} =   Set Variable    ${sh['key']}
    \       ${resp} =    Run cpqlocfg and Get Licenses  ${sh_ip}
    \       ${resp_xml}=    Parse XML    ${resp}
    \       ${li} =  Get Element  ${resp_xml}  LICENSE
    \       ${realSH_li} =   XML.Get Element Attribute  ${li}  VALUE  LICENSE_KEY
    \       Should Match    ${sh_li}    ${realSH_li}

Verify Licenses640
    [Documentation]    Verify Licenses640
    Log To Console And Logfile    Verify Licenses640
    ${licenses} =  Get All Licenses
    ${availCap}=    Set Variable    ${licenses[0]['availableCapacity']}
    log to console		${availCap}
    should be equal as integers   ${availCap}   640

Verify Licenses Count
    [Documentation]    Verify Licenses Count
    Log To Console And Logfile    Verify Licenses Count
    [Arguments]  ${count}  ${product}
    ${availCap} =   Set Variable    0
    ${resp} =  Get All Licenses
    :FOR    ${li}    IN    @{resp}
#    \       ${li} =     Copy dictionary     ${li}
#    \       ${p} =  set variable if  ${li['product']}==${product}
#    \       ${status1}  ${return} =  Run Keyword and Ignore Error  Get From Dictionary  ${li}  availableCapacity
#    \       ${availCap} =  set variable if  '${status1}'=='PASS'  ${return}  error
#    \       ${availCap} =  Run Keyword if  '${li['product']}' == ${product}  Get From Dictionary  ${li}  availableCapacity
#    \       break
    \       Continue For Loop If  '${li['product']}' != ${product}
    \       ${availCap} =  Run Keyword if  '${li['product']}' == ${product}  Get From Dictionary  ${li}  availableCapacity
    log to console		${availCap}
    should be equal as integers   ${availCap}   ${count}

Delete All Fusion License with ssh
    [Documentation]    Deletes all the licenses from the appliance with ssh.
	${cmd} =   Set Variable    echo y | /ci/bin/licmgr --type key --delete all
	Run Command Via SSH   ${APPLIANCE_IP}   ${ssh_credentials['userName']}   ${ssh_credentials['password']}   ${cmd}   ${FUSION_PROMPT}   ${FUSION_TIMEOUT}

Patch Server Hardware2
    [Documentation]  Patch server sardware.
    ...              Example:
    ...                Patch Server Hardware2  ${ENC1SHBAY3}
    ...              Data Required:
    ...                Server Hardware name
    [Arguments]  ${name}
    ${name} =  replace string using regexp  ${name}  SH:  ${EMPTY}
    ${op} =   Set Variable    replace
    ${path} =   Set Variable    /licensingIntent
    ${value} =   Set Variable    OneView
    Log    Patching Server Hardware ${name} with op=${op} path=${path} and value=${value}    console=True
    ${uri} =  Get Server Hardware URI  ${name}
    ${dict} =  Create Dictionary  op=${op}  path=${path}  value=${value}
    ${payload} =  Create List  ${dict}
    ${resp} =  fusion api patch server hardware  ${payload}  ${uri}
#    Wait for task2  ${resp}  300  10
    [return]  ${resp}
