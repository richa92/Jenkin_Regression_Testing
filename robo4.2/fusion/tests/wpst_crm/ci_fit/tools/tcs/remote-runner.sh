#!/bin/bash

############################
# Script will parse an IP list file and run a specified command on the server from TCS.
# 
# USAGE: ./remote-runner.sh <iplist.txt>
############################

NAME=$0
LOG="remote-runner.log"

# Check if the file was passed in.
if [ $# -eq 2 ]; then
        ipaddr_file=$1
	command=$2
else
        echo "usage: $0 </path to IP file> <command>"
        echo "example:  $0 iplist.txt \"cd /root/tools/scripts; ./configure_bond_interface-rhel7 -ip 192.168.0.2 -sn vcuttt000b\""
        exit
fi

cat $ipaddr_file | while read LINE
do
	name=$(echo $LINE | cut -d'=' -f1)
	ip=$(echo $LINE | cut -d'=' -f2)
	echo "####################" >> $LOG
	echo "# ${name} [${ip}] " >> $LOG
	echo "# command: ${command} " >> $LOG
	echo "####################" >> $LOG
	ssh -n root@$ip $command >> $LOG 2>&1
	echo "####################" >> $LOG
done
echo -e "\e[1;30mLogs were saved to \e[0m \e[1;34m${LOG} \e[0m"

exit 0
