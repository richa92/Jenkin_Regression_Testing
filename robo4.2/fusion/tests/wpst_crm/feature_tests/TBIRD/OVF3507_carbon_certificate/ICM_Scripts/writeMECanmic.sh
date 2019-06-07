#!/bin/bash
# (C) Copyright 2016 Hewlett Packard Enterprise Development LP
#
######################################################################
# This script will write CANMIC Block 190 to obtain the password for
# the root account of a Carbon ICM. The script accepts the EM IP
# address and Bay number as inputs. It must be run from the CIM
# that owns/manages the enclosure
#
# Note: Please run this script from the CIM that owns the Enclosure.
#
# Author: Sebastian Schagerer
# Version 0.5
# Last update: 2016-01-07
#
# Change Log:
#    2016-01-07 -- v0.5 -- Initial version
#
######################################################################


if [ $# -ne 2 ]; then
    echo "Missing parameters."
    echo "Usage: $0 <Bay> <data>"
    echo "    Bay : Interconnect Bay number"
    echo "   data : Data for Block 190, in base64 encoding. AA== to clear bit, AQ== to set bit."
    echo
    exit 1
fi

# Interconnect Bay Number
bay=$1
# Base64 encoded data
b64=$2

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
    echo "Missing /ci/bin/tbird/appliance-hal.sh. This script must be run from the CIM"
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
    json_body="{\"UserName\":\"Administrator\",\"Password\":\"$em_admin_passwd\"}"
    auth_header=`curl -x '' -k -i -s --tlsv1 -X POST -H 'Content-Type: application/json' -d $json_body https://[$em_ip%bond0]/rest/v1/Sessions | grep 'X-Auth-Token' | sed -e 's/ //' -e 's/\r//'`

    echo 'Write Canmic Block 190...'
    json_data="{\"Action\":\"WriteCanmicBlocks\",\"List\":[{\"Block\":190,\"Format\":\"Base64\",\"Data\":\"$b64\"}]}"
    curl -x '' -k --tlsv1 -X POST -H $auth_header -H 'Content-Type: application/json' -d $json_data https://[$em_ip%bond0]/rest/v1/InterconnectManager/$bay


done

#echo 'Get Enclosure Serial Number...'
#serial_number=`/ci/bin/tbird/appliance-hal.sh list-enclosures`

#echo 'Get EM password...'
#em_admin_passwd=`/ci/bin/tbird/appliance-hal.sh get-enclosure-credentials -s $serial_number -o p`

#echo 'Get the EM IP address'
#em_ip=`/ci/bin/tbird/appliance-hal.sh get-enclosure-credentials -s $serial_number -o i`

#echo 'Create new RIS Session with EM...'
#json_body="{\"UserName\":\"Administrator\",\"Password\":\"$em_admin_passwd\"}"
#auth_header=`curl -x '' -k -i -s -X POST -H 'Content-Type: application/json' -d $json_body https://$em_ip%bond0/rest/v1/Sessions | grep 'X-Auth-Token' | sed -e 's/ //' -e 's/\r//'`

#echo 'Write Canmic Block 190...'
#json_data="{\"Action\":\"WriteCanmicBlocks\",\"List\":[{\"Block\":190,\"Format\":\"Base64\",\"Data\":\"$b64\"}]}"
#curl -x '' -k -X POST -H $auth_header -H 'Content-Type: application/json' -d $json_data https://$em_ip%bond0/rest/v1/InterconnectManager/$bay

