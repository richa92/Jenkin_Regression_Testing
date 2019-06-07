#!/usr/bin/bash

# Get interconnect IPv6 Link Local Address, User, and Password
# Required arguments: $1 - enclosure serial number, $2 - list of icm bays you want to query
encSN=$1
icmBayNumList=($2)

token=`/ci/bin/tbird/appliance-hal.sh get-enclosure-credentials -s ${encSN} -o t`
ip=`/ci/bin/tbird/appliance-hal.sh get-enclosure-credentials -s ${encSN} -o i`
for b in "${icmBayNumList[@]}"
do
    echo -n EnclosureSN=${encSN},
    echo -n Bay=${b},
    Block10Data=`curl -s -k -X POST -d "{ \"Action\": \"ReadCanmicBlocks\", \"List\": [ 10 ] }" -H "X-Auth-Token:${token}" https://[${ip}%bond0]/rest/v1/InterconnectManager/${b} | jq -r .List[].Data`
    ipv6Address=`curl -s -k -X GET -H "X-Auth-Token:${token}" https://[${ip}%bond0]/rest/v1/InterconnectManager/${b} | jq -r .Oem.Hp.IPv6NetworkConfiguration.LinkLocalAddress`
    echo -n ipv6LinkLocal=${ipv6Address},
    if [ -z ${Block10Data} ]
    then
        echo "No block 10 data"
    else
        echo -n "User="
        echo ${Block10Data} | base64 -d -w 0 | xxd -l 32 -s +32 -c 32 | awk '{print $NF}' | sed 's/\.//g' | tr -d '\n'
        echo -n ","
        echo -n "Password="
        echo ${Block10Data} | base64 -d -w 0 | xxd -l 31 -s +1 -c 32 | awk '{print $NF}' | sed 's/\.//g' | tr -d '\n'
    fi
    echo
done
