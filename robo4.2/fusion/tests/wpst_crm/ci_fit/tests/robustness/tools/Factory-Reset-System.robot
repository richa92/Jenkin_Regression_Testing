*** Settings ***
Documentation        Factory reset EM, CIM and server blades.
...                  The script will prompt you to accept the operation by entering 'yes' (excluding quote) to avoid accidental reset.
...                  If a standby CIM exists, the script will remove it first before factory resetting the active CIM.
...                  Optional arguments:
...                      To proceed with PressAndHold when MomentaryPress fails with this errorCode, use -vPROCEED_WITH_PRESS_AND_HOLD:SERVER_MOMENTARY_PRESS_OFF_TIMEOUT
...                      To use graceful power off via ssh (this will require -v HA_FILE:<your ha file> arg, use -vPOWER_OFF_MODE:ssh
...                  Example:
...                          time pybot -d /tmp/logs/Factory-Reset-System/ -LTRACE -V/root/ci-fit/config_files/tools/factory-reset-tools.py Factory-Reset-System.robot

Resource            ../../../../../wpst_crm/crm_austin/resources/keywords_ovcli.txt
Resource            ../../../../../resource/fusion_api_all_resource_files.txt
Resource            ../resources/common.robot
Library             Collections
Library             ../resources/robustness-helper.py
Variables           ../resources/data_variables.py


*** Variables ***
${FUSION_IP}                    ${APPLIANCE_IP}
${EMAIL_FROM}                   ${EMAIL_TO}
${POWER_OFF_MODE}               api
${PROCEED_WITH_PRESS_AND_HOLD}  None
${HA_FILE}                      None
${tbirdEnv}                     None

*** Test Cases ***
Prompt User To Continue
    Variable File Should Be Passed
    Run Keyword If   '${POWER_OFF_MODE}' == 'ssh' and '${HA_FILE}' == '${Null}'   Fail   msg=Power off mode via ssh was selected while HA_FILE is ${Null}. Please set your HA_FILE!
    ${continue} =   Get Value From User On Console   This will reset your system to factory defaults. Continue[yes|no] (Enter defaults to no)?${SPACE}
    Run Keyword If   '${continue}' != 'yes'   Fatal Error   msg=User chose not to continue. Script terminated...

Login Appliance And Set Test
    [Tags]   LOGIN
    Authenticate And Set Login

Factory Reset Tbird System
    # Power off all servers
    Run Keyword If   '${poweroff_mode}' == 'api'   Power Off All Servers In Parallel   proceedPressAndHold=${PROCEED_WITH_PRESS_AND_HOLD}
    ...    ELSE IF   '${poweroff_mode}' == 'ssh'   Power Off All Servers Via Ssh In Parallel
    # We don't need this if we don't have iLO factory reset
    # Build our own iLO host info dictionary
    # ${iLOHostInfo} =   Get iLO IP Addresses
    # Build our roles dictionary
    ${roles} =   Get HA Nodes
    ${standby} =   Evaluate   $roles.get('Standby', ${null})
    # This is to avoid failing over during factory reset
    Run Keyword If   ${standby} is not ${null}   Remove Standby CIM   ${standby}
    Log To Console  SSH to appliance and do factory reset to all discovered enclosures...
    Execute SSH Command   ${FACTORY_RESET_ENCS}
    Log To Console   Factory reset appliance saving network settings...
    ${resp} =   Fusion Api Appliance Factory Reset   mode=PRESERVE_NETWORK
    ${statusCode} =   Check Response For Error   ${resp}
    Log To Console   NOTE: Cases where script appeared to have stuck because taskState remained 'Running' for long time.
    Log To Console   NOTE: You can monitor using curl this taskUri below to see and kill the script if needed, mark out lines 30-51 then re-run the script so it will proceed to accepting EULA, changing password, and perform HW discovery.
    Log To Console   Task Uri: ${resp['headers']['Location']}
    ${task} =   Run Keyword If   ${statusCode} == ${202}   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=${APPLIANCE_FACTORY_RESET_TIMEOUT}
    ...                   ELSE   Fail   msg=Status code is not equal to 202.
    Check Asynchronous Task Response For Error   ${task}
    Sleep And Log Reason To Console   60s   reason=Sleeping 60s after factory reset to workaround OVD15970.
    Log To Console   Accept EULA and enable service access...
    ${resp} =  Fusion Api Save Eula   ${APPLIANCE_IP}
    Run Keyword If   ${resp['status_code']} != ${200}   Fail   msg=Failed during EULA acceptance: ${resp}
    Log To Console   Change default Administrator password...
    ${resp} =   Fusion Api Change Administrator Password   ${APPLIANCE_IP}   ${NEW_ADMINISTRATOR_CREDENTIAL}
    Run Keyword If   ${resp['status_code']} != ${200}   Fail   msg=Failed attempt to change the default Administrator password: ${resp}
    Log   Getting trusted component token - needed if you don't have devmode-package installed...   console=${True}
    ${token} =    Execute SSH Command   ${GET_TRUSTED_TOKEN}
    Log   Running atlas FTS...   console=${True}
    Execute SSH Command   curl -k -H "Auth: ${token}" https://localhost/perm/rest/tbird/atlas/fts
    # This is redundant to the factory reset done during HW discovery below and also when we reimage OneView
    # Log To Console   Reset iLOs to Factory default...
    # :FOR   ${k}   IN   @{iLOHostInfo.keys()}
    # \   Log To Console   DEBUG: Resetting to factory default...${k} 
    # \   ${output} =   Run   perl ../../../tools/tcs/locfg.pl -s ${iLOHostInfo['${k}']['mpIpAddresses'][0]} -f ../../../tools/tcs/Factory_Defaults.xml -u Administrator -p hpvse123 -${iLOHostInfo['${k}']['mpModel']}
    Log   Checking if hardware discovery is needed...   console=${True}
    # Re-authenticate
    ${Response}    ${AUTHTOKEN}    Fusion Api Login Appliance   ${APPLIANCE_IP}   ${admin_credentials}
    Set Suite Variable   ${AUTHTOKEN}
    ${resp} =   Fusion Api Get Enclosures
    Run Keyword If   ${resp['count']} == ${0}   Log   Performing hardware discovery...   console=${True}
    ...       ELSE   Log   No hardware discovery needed at this time...   console=${True}
    Run Keyword If   ${resp['count']} == ${0}   Execute SSH Command   curl -k -X POST -H "X-API-Version:${resp['headers']['X-Api-Version']}" https://localhost/rest/appliance/tech-setup
    # TODO: figure out how to set back the Administrator password after factory reset.

Send Email Notification
    ${EMAIL_TO} =   Get Variable Value   ${EMAIL_TO}
    Pass Execution If   '${EMAIL_TO}' == '${null}'  EMAIL_TO was set to None, no email notification will be sent.
    ${suitename} =   Fetch From Left   ${SUITE NAME}  --
    Send Email    ${EMAIL_FROM}   ${EMAIL_TO}   [Tools] ${suitename} complete   [Tools] ${suitename} on ${APPLIANCE_IP} complete, check your system and or RoboGalaxy log for the result.

