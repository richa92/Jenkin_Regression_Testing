*** Settings ***
Documentation        Save all profiles data in a json file

Variables           ../../tests/robustness/resources/data_variables.py
Resource            ../../../crm_austin/resources/keywords_ovcli.txt
Resource            ../../../../resource/fusion_api_all_resource_files.txt
Resource            ../../tests/robustness/resources/common.robot
Library            ../../tests/robustness/resources/robustness-helper.py
Library             Collections


*** Variables ***
${FUSION_IP}   ${APPLIANCE_IP}
${JSON_FILE}   all_profiles.json

*** Test Cases ***
Save all profiles in json file
    Authenticate And Set Login
    ${resourceList} =   Create List   profiles
    ${ovData} =   Get OneView Resources   ResourcesList=${resourceList}
    Write JSONfile   ${ovData}  ${JSON_FILE}

