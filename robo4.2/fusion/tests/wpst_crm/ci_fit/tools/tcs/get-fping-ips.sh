#!/bin/bash
############################
# This script parses the HA_ipaddr.conf gets the profile name.
# Gets all entries fromt he HA file for that profile.
# Randomly gets one entry for that profile and writes it to 
# a file.  I also writes the full entry to a log file for each
# ip it adds to the ip text file.
# 
# USAGE: ./get-ip.sh <HA_FILE.CONF>
# Author: John Thigpen
# Contact: john.r.thigpen@hpe.com
# Version: 0.1-212718
############################
NAME=$0
orig_name="DUMMY"
out_file="fping-ips.txt"
ips_file="ips.txt"
ip_details_file="ips-details.log" 
entries_per_profile=1

# Check if the HA file was passed in.
if [ $# -eq 1 ]; then
        ipaddr_file=$1
else
        echo "usage: $0 </path to conf file>"
        echo "example:  $0 HA_ipaddr.conf"
        exit
fi

# Clear out the mg ini ip list file:
echo -n "" > $out_file
echo -n "" > $ips_file 
echo -n "" > $ip_details_file 

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
	# Get the vlan
	vlan=$(echo $LINE | cut -d' ' -f7)

	# Check if line contains new profile data.
	if [ "$name" = "$orig_name" ]
	then
		# Already have entry for this blade. Get the next line.
		read LINE
	else
		#> Need to add ability to specify how many lines per profile.
		#> Can use counter and pull random.  Set default to 1 line per.
		#> Use while loop to get entries while counter <= $entries_per_profile.

		#echo "Getting random vlan/IP for $name from $ipaddr_file"
		mapfile -t myarray < <( grep -w ${name} $ipaddr_file  )
		my_array_len=${#myarray[@]}
		my_array_len=$( expr $my_array_len - 1 )
		random_num=$( python -c "import random; print random.randint(0,${my_array_len})" )
		random_line=${myarray[$random_num]}
		echo "Random Line: $random_line" 
		# Get the number of fields in the line.
		field_count=$(echo $random_line |wc -w)
		# Get IP:
		ip=$(echo $random_line | cut -d' ' -f8)
		echo "$name=$ip"
		# Write out name and IP to file:
		echo "$name=$ip" >> $out_file
		echo "$ip" >> $ips_file 
		echo "$random_line" >> $ip_details_file 
		orig_name=$name
	fi

done
echo -e "\e[1;30mServer Names and IP addresses have been saved to \e[0m \e[1;34m$out_file \e[0m"
echo -e "\e[1;30mIP addresses have been saved to \e[0m \e[1;34m$ips_file \e[0m"
echo -e "\e[1;30mServer details have been saved to \e[0m \e[1;34m$ip_details_file \e[0m"

exit 0
