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

# Clear out the server pxe ip list file:
echo -n "" > blade_pxe_addresses-new.ini

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
		
		# Check if the names match. If they do get next line else get the PXE IP and save results.
		if [ "$name" = "$orig_name" ]
		then
			read LINE
		else
			new_name=$( echo $name |cut -d- -f1,2,3 | sed s/_Bay/-/)
			rhv=$(ssh -n root@$ip cat /etc/redhat-release)
			case $rhv in
				"Red Hat Enterprise Linux Server release 7."*) pxe_ip=$(ssh -n root@$ip ifconfig |grep -F 192.168 |sed -e 's/^[ \t]*//' |cut -d' ' -f2);;
				*) pxe_ip=$(ssh -n root@$ip ifconfig |grep -F 192.168 |sed -e 's/^[ \t]*//' |cut -d: -f2 |cut -d' ' -f1);;
			esac
			#JRT pxe_ip=$(ssh -n root@$ip ifconfig |grep -F 192.168 |sed -e 's/^[ \t]*//' |cut -d: -f2 |cut -d' ' -f1)
			if [ -z "$pxe_ip" ]; then
				pxe_ip="<No PXE IP Found.  ISCSI?>"
			fi
			echo "Server: $name, IP: $pxe_ip"
			echo "$new_name=$pxe_ip" >> blade_pxe_addresses-new.ini
		fi

		# Set the Original Name Var.
		orig_name=$name
		
	fi
done
echo -e "\e[1;30mServer Names and PXE addresses have been saved to \e[0m \e[1;34mblade_pxe_addressess-new.ini \e[0m"

exit 0
