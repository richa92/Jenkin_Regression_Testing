#!/bin/sh
#set -x

verbose=0
trap_listener='TrapListener.py'
status_file='/root/trap_forwarding/status_file'

while getopts "vt:s:" opt; do
  case "$opt" in
  v)  verbose=1
      ;;
  t)  trap_listener=$OPTARG
      ;;
  s)  status_file=$OPTARG
      ;;
  esac
done

[[ $verbose == 1 ]] && { echo $trap_listener; }
[[ $verbose == 1 ]] && { echo $status_file; }

count=`ps -ef | grep $trap_listener |grep -v $0 | wc -l`
[[ $verbose == 1 ]] && { echo $count; }
if [ $count -gt 1 ]
then
  count=$((count-1))
  [[ $verbose == 1 ]] && { echo $count; }
  ps -ef | grep $trap_listener |grep -v $0 |head -$count | while read line ; do
    [[ $verbose == 1 ]] && { echo $line; }
    pid=`echo $line|awk '{print $2}'`
    [[ $verbose == 1 ]] && { echo $pid; }
    kill $pid
    echo "PURGE" > $status_file
  done
fi
