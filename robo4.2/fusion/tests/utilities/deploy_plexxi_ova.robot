*** Settings ***
Documentation       This suite is used to deploy a Plexxi OVA to the specified vCenter with the specified options
...    usage:  pybot -v "VCENTER_ADDRESS:10.0.0.1"  -v "VCENTER_USERNAME:Administrator" -v "VCENTER_PASSWORD:password"
...    -v "OVA_LOCATION:https://ova_url.vse.rdlabs.hpecorp.net/plexxi.ova" -v "HOSTNAME:plexxi-r3-cfm"
...    -v "DOMAINNAME:vse.rdlabs.hpecorp.net" -v "VM_NAME:plexxi-r3-cfm" deploy_plexxi_ova.robot
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
${OVA_LOCATION}             ${None}
${VM_NAME}                  ${None}
${DISK_PROVISIONING}        thin
${importSpecParams}         ${None}
${HOSTNAME}                 ${None}
${DOMAINNAME}               ${None}
${NTP_ADDRESS}              ${None}
${DHCP}                     True
${STATIC_IP_ADDRESS}        0.0.0.0
${NETMASK}                  255.255.255.0
${GATEWAY}                  0.0.0.0
${DNS1}                     ${None}
${DNS2}                     ${None}

*** Test Cases ***
Connect to vCenter
    connect to vi server  ${VCENTER_ADDRESS}  ${VCENTER_USERNAME}  ${VCENTER_PASSWORD}

Deploy Plexxi OVA
    ${importSpecParams} =   json.loads  {"entityName": "${VM_NAME}", "diskProvisioning": "${DISK_PROVISIONING}", "propertyMapping": {"Hostname": "${HOSTNAME}", "Domainname": "${DOMAINNAME}", "NTP1": "${NTP_ADDRESS}", "DHCP": "${DHCP}", "IP": "${STATIC_IP_ADDRESS}", "Netmask": "${NETMASK}", "Gateway": "${GATEWAY}", "DNS1": "${DNS1}", "DNS2": "${DNS2}"}}
    ${resp} =  deploy ova   ova=${OVA_LOCATION}
    ...                     importSpecParams=${importSpecParams}
    ...                     datacenter=${VCENTER_DATACENTER}
    ...                     resource_pool=${VCENTER_RESOURCE_POOL}
    ...                     cluster=${VCENTER_CLUSTER}
    ...                     datastore=${VCENTER_DATASTORE}
    should not be true  ${resp}
