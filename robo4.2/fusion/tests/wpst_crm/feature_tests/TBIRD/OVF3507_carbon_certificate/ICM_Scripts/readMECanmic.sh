#!/bin/bash
# (C) Copyright 2015-2016 Hewlett Packard Enterprise Development LP
#
######################################################################
# This script will read CANMIC Block 10 to obtain the password for
# the OneView account of a Carbon ICM. The script accepts the EM IP
# address and Bay number as inputs. It must be run from the CIM or
# VM that owns/manages the enclosure
#
# Note: Please run this script from the CIM (or VM) that owns the
#       Enclosure.
#
# Author: Sebastian Schagerer
# Version 0.7
# Last update: 2016-02-12
#
# Change Log:
#    2016-02-12 -- v0.7 -- Added support for optional block number
#    2015-08-19 -- v0.6 -- Added more pre-requisite checks
#    2015-08-18 -- v0.5 -- Initial version
#
######################################################################


if [ $# -lt 1 -o $# -gt 2 ]; then
    echo "Missing parameter."
    echo "Usage: $0 <Bay> [Block]"
    exit 1
fi

bay=$1

# Default to block 10
block=10
if [ $# -gt 1 ]; then
    block=$2
fi

# Check for required utilities
req_utilities=(python base64 curl)
for utility in ${req_utilities[@]} ; do
    which $utility > /dev/null 2>&1
    if [ $? -ne 0 ]; then
        echo "Missing required utility: $utility"
        exit 2
    fi
done

if [ ! -e /ci/bin/tbird/appliance-hal.sh ] ; then
    echo "Missing /ci/bin/tbird/appliance-hal.sh. This utility must be run from a CIM."
    exit 3
fi


echo 'Get Enclosure Serial Number(s)...'
serial_numbers=`/ci/bin/tbird/appliance-hal.sh list-enclosures`

for serial_number in $serial_numbers; do

    echo '#################################################################'
    echo 'Getting Details for the Enclosure With Serial Number ' $serial_number
    echo '#################################################################'

    echo 'Get EM password...'
    em_admin_passwd=`/ci/bin/tbird/appliance-hal.sh get-enclosure-credentials -s $serial_number -o p`

    echo 'Get the EM IP address'
    em_ip=`/ci/bin/tbird/appliance-hal.sh get-enclosure-credentials -s $serial_number -o i`

    echo 'Create new RIS Session with EM...'
    auth_json_body="{\"UserName\":\"Administrator\",\"Password\":\"$em_admin_passwd\"}"
    x_auth_token=`curl -x '' -k -i -s --tlsv1 -X POST -H 'Content-Type: application/json' -d $auth_json_body https://[$em_ip%bond0]/rest/v1/Sessions | grep 'X-Auth-Token' | sed -e 's/ //' -e 's/\r//'`

    echo "Read Canmic Block $block ..."
    read_block_json_body="{\"Action\":\"ReadCanmicBlocks\",\"List\":[$block]}"
    json_resp=`curl -x '' -k -s --tlsv1 -X POST -H $x_auth_token -H 'Content-Type: application/json' -d $read_block_json_body https://[$em_ip%bond0]/rest/v1/InterconnectManager/$bay`

    echo 'Decode response...'
    block_decoded=`echo $json_resp | python -m json.tool | grep Data | cut -d "\"" -f 4 | base64 -d`

    echo
    if [ $block -eq 10 ]; then
        # 30 is the default password length
        echo "$serial_number ICM Bay $bay (Block $block) OneView password is: ${block_decoded:1:30}"
    else
        echo "$serial_number ICM Bay $bay Block $block is: ${block_decoded}"
    fi

done

#echo 'Get Enclosure Serial Number...'
#serial_number=`/ci/bin/tbird/appliance-hal.sh list-enclosures`

#echo 'Get EM password...'
#em_admin_passwd=`/ci/bin/tbird/appliance-hal.sh get-enclosure-credentials -s $serial_number -o p`

#echo 'Get the EM IP address'
#em_ip=`/ci/bin/tbird/appliance-hal.sh get-enclosure-credentials -s $serial_number -o i`

#echo 'Create new RIS Session with EM...'
#auth_json_body="{\"UserName\":\"Administrator\",\"Password\":\"$em_admin_passwd\"}"
#x_auth_token=`curl -x '' -k -i -s -X POST -H 'Content-Type: application/json' -d $auth_json_body https://$em_ip%bond0/rest/v1/Sessions | grep 'X-Auth-Token' | sed -e 's/ //' -e 's/\r//'`

#echo "Read Canmic Block $block ..."
#read_block_json_body="{\"Action\":\"ReadCanmicBlocks\",\"List\":[$block]}"
#json_resp=`curl -x '' -k -s -X POST -H $x_auth_token -H 'Content-Type: application/json' -d $read_block_json_body https://$em_ip%bond0/rest/v1/InterconnectManager/$bay`

#echo 'Decode response...'
#block_decoded=`echo $json_resp | python -m json.tool | grep Data | cut -d "\"" -f 4 | base64 -d`

#echo
#if [ $block -eq 10 ]; then
    # 30 is the default password length
    #echo "ICM Bay $bay (Block $block) OneView password is: ${block_decoded:1:30}"
#else
    #echo "ICM Bay $bay Block $block is: ${block_decoded}"
#fi
