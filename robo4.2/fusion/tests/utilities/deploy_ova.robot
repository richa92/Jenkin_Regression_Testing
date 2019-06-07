*** Settings ***
Documentation       This suite is used to deploy an OVA to the specified vCenter with the specified options
...    usage:  pybot -v "VCENTER_ADDRESS:10.0.0.1"  -v "VCENTER_USERNAME:Administrator" -v "VCENTER_PASSWORD:password"
...    -v "OVA_URL:https://ova_url.vse.rdlabs.hpecorp.net/oneview.ova" -v "VM_NAME:OneView_PASS119" deploy_ova.robot
Library             json
Library             FusionLibrary
Library             RoboGalaxyLibrary

*** Variables ***
${VCENTER_ADDRESS}          ${None}
${VCENTER_USERNAME}         ${None}
${VCENTER_PASSWORD}         ${None}
${VCENTER_DATACENTER}       ${None}
${VCENTER_RESOURCE_POOL}    ${None}
${VCENTER_CLUSTER}          ${None}
${VCENTER_DATASTORE}        ${None}
${OVA_URL}                  ${None}
${VM_NAME}                  ${None}
${DISK_PROVISIONING}        thin
${importSpecParams}         ${None}

*** Test Cases ***
Connect to vCenter
    connect to vi server  ${VCENTER_ADDRESS}  ${VCENTER_USERNAME}  ${VCENTER_PASSWORD}

Deploy OVA
    ${importSpecParams} =   json.loads  {"entityName": "${VM_NAME}", "diskProvisioning": "${DISK_PROVISIONING}"}
    ${resp} =  deploy ova   ova=${OVA_URL}
    ...                     importSpecParams=${importSpecParams}
    ...                     datacenter=${VCENTER_DATACENTER}
    ...                     resource_pool=${VCENTER_RESOURCE_POOL}
    ...                     cluster=${VCENTER_CLUSTER}
    ...                     datastore=${VCENTER_DATASTORE}
    should not be true  ${resp}
