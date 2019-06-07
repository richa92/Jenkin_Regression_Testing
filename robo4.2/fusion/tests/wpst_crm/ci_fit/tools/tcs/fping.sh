#!/bin/bash
# Description: This is an fping wrapper script that reads the arguments and run fping accordingly.
#              User can pass an IP Address, IP File, or a directory containing IP Files.
#              Important to note that this will spawn fping per IP File and the max number of IP may vary from system to system based on resource. This script will also be logging fping output in logs/<run timestamp>/[<ip it pings>|<ip file>].log.
#
#              Testing in Eagle62-63 showed that it works fine there up to 700 IP Address distributed in 7 IP Files with 100 IP Addressess each. Your testing env mileage may vary.
#
# Exit Status:
#              -1 for Usage(), help, or incorrect syntax
#              1 for no ping loss
#              0 for ping loss
# 
# Author: Jason Mascarinas Pernito <jason.mas.pernito@hpe.com>
# 
# (c) Copyright 2019. Hewlett-Packard Enterprise

LOGDIR="logs/`date +"%F_%H%M%S"`"
QUIET=0

# FUNCTIONS:
function usage() {
    echo "$0"
    echo
    echo "NAME"
    echo "$0 - run fping to a specified IP Address, IP File, or IP Dir."
    echo "Syntax:"
    echo "        $0 [-q] [-m <perSecond(default)> | <seqPing>] [<IP Address> | <IP File> | <IPDIR>]"
    echo "Examples:"
    echo "        $0 172.16.1.2"
    echo "        $0 /root/fping/fping_ips.lst"
    echo "        $0 /root/fping/ipdir"
    echo "        $0 -m seqPing 172.16.1.2"
    echo "        $0 -m seqPing /root/fping/fping_ips.lst"
    echo "        $0 -m seqPing /root/fping/ipdir"
    echo
    echo "Options:"
    echo "        -q"
    echo "           Quiet. Typically used when calling the wrapper programatically so it will not print unnecessary STDOUT."
    echo "        -m"
    echo "           Mode. Can be perSecond which is also the default or seqPing to run it as sequential ping"
    echo "Exit Status:"
    echo "        -1 for incorrect syntax, help, or usage"
    echo "        1 for zero(0) ping loss"
    echo "        0 for when ping loss was found"
    echo "        NOTE: these exit status is to maintain compatibility with sequential ping script."
}

function sequential_fping() {
    for ip in `cat $1`
    do
	if [ $QUIET -eq 1 ]; then
	    fping -c 1 -p 20 -i 1 -u -o -r 0 $ip 2>&1 | xargs -n1 -i bash -c 'echo `date +"%F %T:%3N"`" {}"' > ${LOGDIR}/${ip}.log &
	    child_pid=($!)
	else
	    fping -c 1 -p 20 -i 1 -u -o -r 0 $ip 2>&1 | xargs -n1 -i bash -c 'echo `date +"%F %T:%3N"`" {}"' | (tee -a ${LOGDIR}/${ip}.log)
	fi
    done
}

TARGET=$(echo ${@:${#@}})

# Validate command line parameters
while getopts ':h:qm:' opt; do
    case ${opt} in
        m)
          FPING_METHOD=$OPTARG;
	  case $FPING_METHOD in
              perSecond|seqPing) break ;;
	      *) usage; exit -1 ;;
          esac
          ;;
	q) QUIET=1 ;;
        h|*)
          usage;
          exit -1;
          ;;
    esac
done
shift $((OPTIND -1))
# set default to legacy (perSecond)
if [ -z $FPING_METHOD ]; then
    FPING_METHOD="perSecond"
fi


# main
mkdir -p $LOGDIR
child_pid=("")
if [[ $TARGET =~ [[:digit:]]{1,3}\.[[:digit:]]{1,3}\.[[:digit:]]{1,3}\.[[:digit:]]{1,3} ]]; then
    logfile=$TARGET
    if [ $FPING_METHOD = "perSecond" ]; then
	# ci-fit's original use (aligned with CRM and Aricent)
	if [ $QUIET -eq 1 ]; then
	    echo "[INFO] Spawning infinite loop of fping for $TARGET. Logfile: ${LOGDIR}/${TARGET}.log"
            fping -Q 1 -l -p 20 -i 1 -r 0 $TARGET 2>&1 | xargs -n1 -i bash -c 'echo `date +"%F %T:%3N"`" {}"' > ${LOGDIR}/${TARGET}.log &
	    child_pid=($!)
	else
            fping -Q 1 -l -p 20 -i 1 -r 0 $TARGET 2>&1 | xargs -n1 -i bash -c 'echo `date +"%F %T:%3N"`" {}"' | (tee -a ${LOGDIR}/${TARGET}.log)
	fi 
    elif [ $FPING_METHOD = "seqPing" ]; then
	# simulates our ping_ips_sequential but in milliseconds
	if [ $QUIET -eq 1 ]; then
	    fping -c 1 -p 20 -i 1 -u -o -r 0 $TARGET 2>&1 | xargs -n1 -i bash -c 'echo `date +"%F %T:%3N"`" {}"' > ${LOGDIR}/${TARGET}.log &
	    child_pid=($!)
	else
	    fping -c 1 -p 20 -i 1 -u -o -r 0 $TARGET 2>&1 | xargs -n1 -i bash -c 'echo `date +"%F %T:%3N"`" {}"' | (tee -a ${LOGDIR}/${TARGET}.log)
	fi
    fi
elif [ -f "$TARGET" ]; then
    if [ $FPING_METHOD = "perSecond" ]; then
	logfile=$(basename $TARGET)
	if [ $QUIET -eq 1 ]; then
            fping -Q 1 -l -p 20 -i 1 -r 0 -f $TARGET 2>&1 | xargs -n1 -i bash -c 'echo `date +"%F %T:%3N"`" {}"' > ${LOGDIR}/${logfile}.log &
	    child_pid=($!)
        else
            fping -Q 1 -l -p 20 -i 1 -r 0 -f $TARGET 2>&1 | xargs -n1 -i bash -c 'echo `date +"%F %T:%3N"`" {}"' | (tee -a ${LOGDIR}/${logfile}.log)
	fi
    elif [ $FPING_METHOD = "seqPing" ]; then
        sequential_fping $TARGET
    fi
elif [ -d "$TARGET" ]; then
    for ipFile in ${TARGET}/*
    do
	[ -d $ipFile ] && continue
	if [ $FPING_METHOD = "perSecond" ]; then
	    logfile=$(basename $ipFile)
	    echo "[INFO] Spawning infinite loop of fping for IPs in $ipFile. Logfile: ${LOGDIR}/${logfile}.log"
            fping -Q 1 -l -p 20 -i 1 -r 0 -f $ipFile 2>&1 | xargs -n1 -i bash -c 'echo `date +"%F %T:%3N"`" {}"' > ${LOGDIR}/${logfile}.log &
	    child_pid+=($!)
	elif [ $FPING_METHOD = "seqPing" ]; then
	    sequential_fping $ipFile
	fi
    done
else
    usage
    exit -1
fi

# loop while child process is running (child_running is 0)
child_running=0
while [ $child_running -eq 0 ];
do
    for pid in "${child_pid[@]}";
    do
        kill -0 $pid >/dev/null 2>&1
        child_running=$?
	if [ $child_running -eq 0 ]; then
	    sleep 1
	    break;
	else:
	    # remove pid from the list(child_pid)
	    for p in "${!child_pid[@]}";
            do
	        if [ ${child_pid[p]} -eq $child_running ];
		then
		    unset 'child_pid[p]'
		fi
            done
        fi
    done
    if [ ${#child_pid[@]} -eq 0 ];
    then
	# no more running process
        child_running=1
    fi
done
echo
grep -o -E '.*[[:digit:]]{1,3}\/[[:digit:]]{1,3}\/[1-9].*%.*' ${LOGDIR}/*.log > /tmp/.allLoss.log
ping_loss=$?
if [ $ping_loss -eq 0 ]; then   echo "Targets with ping loss:"; cat /tmp/.allLoss.log; fi
exit $ping_loss
