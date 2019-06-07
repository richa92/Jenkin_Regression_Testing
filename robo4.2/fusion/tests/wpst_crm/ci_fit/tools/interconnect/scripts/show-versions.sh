#!/bin/bash

function usage {
    echo "Prints switch info for all switches on an OA."
    echo "Usage:  show-versions.sh -s switch || -o oaHostname [-l oaLoginId]"
    exit 1
}

OA_LOGIN=Administrator
CLI=/usr/local/vceth/bin/cli
TEMP_OUTPUT=`mktemp /tmp/$OA.XXX`

function script_trap {
    echo; echo `basename $0:`  Dangit!
    rm -f $TEMP_OUTPUT
    exit
}

trap script_trap INT TERM

# Get command line args
while getopts "s:o:l:" OPTION ; do
    case $OPTION in
        s)
            SWITCHES=${SWITCHES}\ ${OPTARG} ;;
        l)
            OA_LOGIN=$OPTARG ;;
        o)
            OA=$OPTARG ;;
        ?)
            usage ;;
    esac
done

if [ -z "$SWITCHES" ] && [ -z "$OA" ]  ; then
    usage
fi

# Get the switch list from the OA
# TODO:  How do we get the return value?
if [ ! -z "$OA" ] ; then
   SWITCHES=${SWITCHES}\ `ssh -o "StrictHostKeyChecking no" ${OA_LOGIN}@${OA} "show interconnect list" | grep "^ .[0-9] " | grep -v "\[Absent\]\|\[Subsumed\]" | awk '{print $NF;}'`
fi

echo

# Get switch info for all the switches
for SWITCH in $SWITCHES ; do
    if [ "$SWITCH" != "0.0.0.0" ] ; then
        ssh -q -o "StrictHostKeyChecking no" root@${SWITCH} " \
        THE_INFO=\`$CLI \"show -display properties=bay_id /\" | grep bay_id | tr '=' ' ' | awk '{print \$2;}'; \
        echo -n \"$SWITCH \"; \
        $CLI \"show -display properties=part_number /\" | grep part_number | tr '=' ' ' | awk '{print \$2;}'; \
        $CLI \"show -display properties=serial_number /\" | grep serial_number | tr '=' ' ' | awk '{print \$2;}'; \
        $CLI \"show -display properties=composite_fw_version /\" | grep composite_fw_version | tr '=' ' ' | awk '{print \$2,\$3;}'; \
        $CLI \"show -display properties=primary_enclosure_id /vwc\" | grep \"fusion slice=-1\" > /dev/null;if [ \$? -eq 0 ];then echo CLAIMED; else echo UNCLAIMED;fi\`; \
        echo \$THE_INFO" >> ${TEMP_OUTPUT} &
        JOBS[$!]=$SWITCH
    else
        echo "`basename $0`: A switch was detected but is currently unavailable"
    fi
done

# Wait for jobs to finish
for JOB in ${!JOBS[*]} ; do
    wait $JOB
    if [ $? -ne 0 ] ; then
       echo "`basename $0`: JOB $JOB failed."
       RVAL=1
    fi
done

# Print switch info
cat $TEMP_OUTPUT | sort | sed 's/ /	/g'

rm $TEMP_OUTPUT 

exit $RVAL   
