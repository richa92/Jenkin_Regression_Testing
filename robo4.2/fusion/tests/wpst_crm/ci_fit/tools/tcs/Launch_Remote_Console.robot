*** Settings ***
Documentation        Open all remote consoles in configuration.
...                  The script will open all remote consoles in the server hardware page of the OneView accessed.
...                  This script uses Internet Explorer, and is designed for use in Windows.
...                  Example:
...                          time pybot -d /tmp/logs/Launch_Remote_Console/ -LTRACE -v APPLIANCE_IP:15.186.9.10 -v ENC_NAME:CN7544044K -v BAYS:"1 2 12" Launch_Remote_Console.robot
...                  OPTIONAL: ENC_NAME --> Will open all remote consoles on the given enclosure, instead of all consoles in the ME.
...                  OPTIONAL: BAYS --> Will open the remote consoles on the bay numbers given.  Can be used across all enclosures in an ME.

Variables           ../../tests/robustness/resources/data_variables.py
Resource            ../../../crm_austin/resources/keywords_ovcli.txt
Resource            ../../../../resource/fusion_api_all_resource_files.txt
Resource            ../../tests/robustness/resources/common.robot
Library            ../../tests/robustness/resources/robustness-helper.py
Library             Collections


*** Variables ***
${FUSION_IP}                    ${APPLIANCE_IP}
${ENC_NAME}                     None
${BAYS}                         None
${IEPATH}                       C:/Program Files (x86)/Internet Explorer/iexplore.exe %s

*** Test Cases ***
Login Appliance And Set Test
    Authenticate And Set Login

Launch Remote Console
    ${operation} =   Set Variable   console
	${Enclosures} =   Run Keyword If   "${ENC_NAME}" != "${null}"   fusion api get enclosures   param=?filter="name=='${ENC_NAME}'"
	...       ELSE   fusion api get enclosures
	Should Not Be Empty   ${Enclosures['members']}   msg=Given enclosure name not found.
    :FOR   ${enc}   IN   @{Enclosures['members']}
	\   Verify Device Bays    ${enc['deviceBays']}   ${operation}
