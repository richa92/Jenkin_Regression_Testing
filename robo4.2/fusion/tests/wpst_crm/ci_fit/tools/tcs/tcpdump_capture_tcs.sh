#!/bin/bash

interface=$1
vlanId=$2

myDir="/home/mytmp/mytmp_tcpdump"
logDir="${myDir}/logs/`date +"%F_%T"`"
stop_file="/root/stop_tcpdump"
time_out=120


if [ ${vlanId} == "X" ]; then
  slave1_if="${interface}"
else
  slave1_if="${interface}.${vlanId}"
fi
slave2_if="${interface}"

if [ -e $stop_file ]; then
  rm -f $stop_file
fi

if [ ! -d "$myDir" ]; then
  mkdir -p $myDir
fi
cd $myDir

if [ ! -d "$logDir" ]; then
  mkdir -p $logDir
fi

timeout $time_out tcpdump -pni $slave1_if -w $logDir/${slave1_if}.pcap &
timeout $time_out tcpdump -pni $slave2_if -w $logDir/${slave2_if}.pcap &

ethtool ${slave1_if} > $logDir/ethtool_${slave1_if}.log
ethtool ${slave2_if} > $logDir/ethtool_${slave2_if}.log
ifconfig -a > $logDir/ifconfig_all.log

for i in  {1..15}
do
  echo "++++++ `date +"%F %T:%3N"` Iteration $i ++++++" >> $logDir/if_stat.log
  echo "" >> $logDir/if_stat.log

  echo "==> ifconfig ${slave1_if}" >> $logDir/if_stat.log
  ifconfig ${slave1_if} >> $logDir/if_stat.log
  echo "" >> $logDir/if_stat.log

  echo "==> ifconfig ${slave2_if}" >> $logDir/if_stat.log
  ifconfig ${slave2_if} >> $logDir/if_stat.log
  echo "" >> $logDir/if_stat.log

  echo "==> ethtool -S ${slave2_if}" >> $logDir/if_stat.log
  ethtool -S ${slave2_if} >> $logDir/if_stat.log
  echo "" >> $logDir/if_stat.log
done

