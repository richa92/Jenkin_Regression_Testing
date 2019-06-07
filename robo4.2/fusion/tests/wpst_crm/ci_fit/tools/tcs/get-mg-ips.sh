#!/bin/bash

############################
# This script parses the HA_ipaddr.conf file looking for the first none tagged
# private IP address for each blade.  It uses that ip to get find the PXE IP
# address for the blade.  It displays the results to the screen and writes them
# to the blade_pxe_addresses file.
# 
# USAGE: ./get-pxe-ip.sh <HA_FILE.CONF>
# Author: John Thigpen
# Contact: john.r.thigpen@hpe.com
# Version: 0.1-83016
############################

NAME=$0
orig_name="DUMMY"

# Check if the HA file was passed in.
if [ $# -eq 1 ]; then
        ipaddr_file=$1
else
        echo "usage: $0 </path to conf file>"
        echo "example:  $0 HA_ipaddr.conf"
        exit
fi

# Clear out the mg ini ip list file:
echo -n "" > mg_addresses-new.ini

# Add MG Headers to the file:
echo "[Echo Servers]" >> mg_addresses-new.ini
echo "[MeatGrinder Servers]" >> mg_addresses-new.ini

# Walk the HA file to get the first non tagged ip.
cat $ipaddr_file | while read LINE
do
	# Get the number of fields in the line.
	field_count=$(echo $LINE |wc -w)
	# Get the blade/server name.
	name=$(echo $LINE | cut -d' ' -f1)
	untagged=$(echo $LINE | cut -d' ' -f7)
	# If the vlanId is X that is the untagged network. 
	if [ "$untagged" == "X" ] #|| [ "$name" != "$orig_name" ]
	then
		# Get the IP
		ip=$(echo $LINE | cut -d' ' -f8)
		if [ "$ip" == "None" ]; then continue; fi
		# Get SN, Enc, Bay Number and create a new name:
		sn=$(echo $LINE | cut -d' ' -f9)
		enc=$(echo $name |cut -d_ -f1)
		bay=$(echo $LINE |cut -d' ' -f2)
		# Some bay numbers may be 'None'.  Workaround by get bay from profile name:
		if [ "$bay" = "None" ]
		then
			new_bay=$(echo $name | cut -d_ -f2 |sed s/Bay//)
			bay=$new_bay
		fi
		
        	new_name=$enc\_$sn-$bay
		
		# Check if the names match. If they do get next line else get the PXE IP and save results.
		if [ "$name" = "$orig_name" ]
		then
			read LINE
		else
			echo "$new_name=$ip" >> mg_addresses-new.ini
		fi

		# Set the Original Name Var.
		orig_name=$name
		
	fi
done
echo -e "\e[1;30mServer Names and PXE addresses have been saved to \e[0m \e[1;34mmg_addressess-new.ini \e[0m"

exit 0
