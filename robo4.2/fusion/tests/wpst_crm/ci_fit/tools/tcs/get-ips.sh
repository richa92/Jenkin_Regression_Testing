#!/bin/bash

############################
# This script parses the HA_ipaddr.conf file looking for the first  IP
# address for each blade.  It writes the SP name and IP to a file.
# 
# USAGE: ./get-ip.sh <HA_FILE.CONF>
# Author: John Thigpen
# Contact: john.r.thigpen@hpe.com
# Version: 0.1-110717
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
echo -n "" > ip_addresses-new.ini

# Walk the HA file to get the ip.
cat $ipaddr_file | while read LINE
do
	# Get the number of fields in the line.
	field_count=$(echo $LINE |wc -w)
	# Get the blade/server name.
	name=$(echo $LINE | cut -d' ' -f1)
	# Get IP:
	ip=$(echo $LINE | cut -d' ' -f8)
	if [ "$ip" == "None" ]; then continue; fi

	# Check if line contains new profile data.
	if [ "$name" = "$orig_name" ]
	then
		# Already have entry for this blade. Get the next line.
		read LINE
	else
		echo "Name: $name, IP: $ip"
		# Write out name and IP to file:
		echo "$name=$ip" >> ip_addresses-new.ini
		# Save off name to temporary variable:
		orig_name=$name
	fi

done
echo -e "\e[1;30mServer Names and PXE addresses have been saved to \e[0m \e[1;34mip_addressess-new.ini \e[0m"

exit 0
