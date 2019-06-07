*** Settings ***
Library           json
Library           copy
Resource          ${fusion_api_resource}
Resource          ../Resources/api/resource.robot
Variables         ./ovf_1092_me_data.py
# Variables         ./ovf_1092_se_data.py
Variables         ./environment_data.py


*** Variables ***
# ${X-API-VERSION}    600
${fusion_ip}        15.212.167.184
${blnVerifyPreReqs}    False
@{allResourcesCommonList}    ethernets    egs    servers    osdps
${fusion_api_resource}       C:/Users/komerao/OVF1134/fusion/Resources/api/fusion_api_resource.txt