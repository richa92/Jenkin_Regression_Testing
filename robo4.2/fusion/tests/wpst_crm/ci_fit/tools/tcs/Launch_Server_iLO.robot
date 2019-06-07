*** Settings ***
Documentation        Open all iLO pages in configuration.
...                  The script will open all iLO webpages in the server hardware page of the OneView accessed.
...                  This script uses Internet Explorer, and is designed for use in Windows.
...                  Example:
...                          time pybot -d /tmp/logs/Launch_Server_iLO/ -LTRACE -v APPLIANCE_IP:15.186.9.10 -v ENC_NAME:CN7544044K -v BAYS:"1 2 12" Launch_Server_iLO.robot
...                  OPTIONAL: ENC_NAME --> Will open all iLO pages on the given enclosure, instead of all consoles in the ME.
...                  OPTIONAL: BAYS --> Will open the iLO pages on the bay numbers given.  Can be used across all enclosures in an ME.

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

Launch iLO
    ${operation} =   Set Variable   web
	${Enclosures} =   Run Keyword If   "${ENC_NAME}" != "${null}"   fusion api get enclosures   param=?filter="name=='${ENC_NAME}'"
	...       ELSE   fusion api get enclosures
	Should Not Be Empty   ${Enclosures['members']}   msg=Given enclosure name not found.
    :FOR   ${enc}   IN   @{Enclosures['members']}
	\   Verify Device Bays    ${enc['deviceBays']}   ${operation}
