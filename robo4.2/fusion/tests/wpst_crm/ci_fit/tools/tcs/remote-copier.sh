#!/bin/bash

############################
# Script will parse an IP list file and scp the specified file on the TCS to blade servers.
# 
# USAGE: ./remote-copier.sh <iplist.txt> <source file path> <destination file path>
############################

NAME=$0
LOG="remote-copier.log"

# Check if the file was passed in.
if [ $# -eq 3 ]; then
    ipaddr_file=$1
	source=$2
	dest=$3
else
        echo "usage: $0 </path to IP file> <source file> <destination file>" 
        echo "example:  $0 /root/ip_addresses.txt /root/start_io.sh /root/start_io.sh"
        exit
fi

cat $ipaddr_file | while read LINE
do
	name=$(echo $LINE | cut -d'=' -f1)
	ip=$(echo $LINE | cut -d'=' -f2)
	echo "####################" >> $LOG
	echo "# ${name} [${ip}] " >> $LOG
	echo "# scp ${source} root@${ip}:${dest} " >> $LOG
	echo "####################" >> $LOG
	scp $source root@$ip:$dest >> $LOG 2>&1
	echo "####################" >> $LOG
done
echo -e "\e[1;30mLogs were saved to \e[0m \e[1;34m${LOG} \e[0m"

exit 0
