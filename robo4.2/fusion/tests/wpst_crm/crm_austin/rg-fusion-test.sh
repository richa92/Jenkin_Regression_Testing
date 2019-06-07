#!/bin/bash
# Automated script runner
# Expected arguments:
#   $1 - X-API-version
#   $2 - OneView version
#   $3 - OneView build (e.g.: pass1, rc1, etc.)
#   $4 - VC version
#   $5 - OneView appliance IP address
#   $6 - Enclosure key as per defined in your credential file (e.g. Austin4)
#   $7 - Optional: intended for runmode (e.g.: --runmode ExitOnFailure --runmode SkipTeardownOnExit) and/or vcDomainConfigOVBug (aka QXCR1001433023. Example: -vvcDomainConfigOVBug:True)
#
# Usage: rg-fusion-test.sh <x-api-version> <oneview version> <oneview build> <vc version> <oneview IP> <credential name>
#
# Example: rg-fusion-test.sh 120 200 pass51 441 15.186.28.193 Austin4

API_VERSION=$1
OV_VERSION=$2
OV_PASS_BUILD=$3
VC_VERSION=$4
OV_IP=$5
ENCLOSURE=$6
EXTRA_OPTION="$7"

RGLOGS_DIR="/var/www/html/rg_logs/api${API_VERSION}/ov${OV_VERSION}/${OV_PASS_BUILD}/vc${VC_VERSION}"
TEST_RECIPIENT="nirmaltej.jaldu@hpe.com,amal-ghosh.av@hpe.com"
RGTEST_VMIP="$(ifconfig | grep -A 1 'eth0' | tail -1 | cut -d ':' -f 2 | cut -d ' ' -f 1)"
TEST_DIRS="\
1kVlans-200-regression \
All-120 \
Common \
DualHop-200-US35754 \
Gen9-200-US35750 \
LLDPtlv-200-US39378 \
Qos-200-US35763 \
SRIOV-200-US36453 \
Limitations \
Conflicts-When-Migrating-with-Existing-LIGs \
PSD \
"

if [ $OV_VERSION -ge 300 ]
then
    ovexclude="--exclude BelowOV300OROV120OROV200-API200OROnlyOV200OROnlyOV120"
elif [ $OV_VERSION -eq 200 ]
then
    ovexclude="--exclude OV120OROV300OROnlyOV120"
elif [ $OV_VERSION -eq 120 ]
then
    ovexclude="--exclude OV200OROV300OROV200-API120OROnlyOV200"
fi

if [ $VC_VERSION -ge 445 ]
then
    vcexclude="--exclude BelowVC430ORBelowVC445ORVC43X"
    if [ $OV_VERSION -ge 300 ];then vcexclude="${vcexclude}ORVC445-BelowOV300";fi
elif [ $VC_VERSION -ge 440 ]
then
    vcexclude="--exclude BelowVC430ORVC43XORVC445"
elif [ $VC_VERSION -ge 430 ]
then
    vcexclude="--exclude BelowVC430ORVC445"
fi

if [ $API_VERSION -ne $OV_VERSION ]
then
    # Note: We need to add something like this when OV3.0 comes and API bug remained
    bug_in_api="-vBUG_IN_API:True"
fi

if [ $API_VERSION -ge 201 ]
then
    apiexclude="--exclude OV200-API120ORAPI120ORVC445-API120"
    if [ $VC_VERSION -ge 445 ];then apiexclude="${apiexclude}ORBelowVC445-API200";fi
elif [ $API_VERSION -eq 200 ]
then
    apiexclude="--exclude OV200-API120ORAPI120ORVC445-API120"
    if [ $OV_VERSION -eq 300 ]
    then
	apiexclude="${apiexclude}OROV300-API201"
    fi
    if [ $VC_VERSION -ge 445 ];then apiexclude="${apiexclude}ORBelowVC445-API200";fi
elif [ $API_VERSION -eq 120 ]
then
    apiexclude="--exclude API200"
    if [ $VC_VERSION -ge 445 ]
    then
        apiexclude="${apiexclude}ORVC445-API200ORBelowVC445-API200"
    else
        apiexclude="${apiexclude}ORVC445-API120"
    fi

    if [ $OV_VERSION -ge 300 ]
    then
        apiexclude="${apiexclude}OROV200-API200OROV300-API201"
    elif [ $OV_VERSION -eq 200 ]
    then
        apiexclude="${apiexclude}OROV200-API200"
    elif [ $OV_VERSION -eq 120 ]
    then
        apiexclude="${apiexclude}OROV200-API200"
    fi
fi

for testdir in $TEST_DIRS
do
    cd ${testdir}
    startDateTime=$(date +%Y%m%d-%H%M%S)
    pybot ${EXTRA_OPTION} -l ${RGLOGS_DIR}/${ENCLOSURE}/${testdir}/log-${startDateTime}.html -r ${RGLOGS_DIR}/${ENCLOSURE}/${testdir}/report-${startDateTime}.html --output ${RGLOGS_DIR}/${ENCLOSURE}/${testdir}/output-${startDateTime}.xml -vX-API-version:${API_VERSION} ${bug_in_api} -vOV_IP:${OV_IP} -i $ENCLOSURE $ovexclude $vcexclude $apiexclude .
    if [ -e "${RGLOGS_DIR}/${ENCLOSURE}/${testdir}/log-${startDateTime}.html" ]
    then
        (
        echo "<html>";
        echo "<h1>RoboGalaxy Automated Test Results Available</h1>";
        echo "<h4>OneView Build: <span style=\"background-color:#FFFF00\">${OV_PASS_BUILD}</span></h4>";
        echo "<table border=\"1\">";
        echo "<tr><td><b>X-API Version</b></td><td><b>OneView Version</b></td><td><b>VC Version</b></td><td><b>Enclosure Name</b></td><td><b>Test Dir</b></td><td><b>Links to RG files</b></td></tr>";
        echo "<tr><td bgcolor=\"#FFFF00\">${API_VERSION}</td><td bgcolor=\"#FFFF00\">${OV_VERSION}</td><td bgcolor=\"#FFFF00\">${VC_VERSION}</td><td bgcolor=\"#FFFF00\">${ENCLOSURE}</td><td bgcolor=\"#FFFF00\">${testdir}</td><td bgcolor=\"#FFFF00\"><a href=\"http://${RGTEST_VMIP}/rg_logs/api${API_VERSION}/ov${OV_VERSION}/${OV_PASS_BUILD}/vc${VC_VERSION}/${ENCLOSURE}/${testdir}/log-${startDateTime}.html\">log-${startDateTime}.html</a><br><a href=\"http://${RGTEST_VMIP}/rg_logs/api${API_VERSION}/ov${OV_VERSION}/${OV_PASS_BUILD}/vc${VC_VERSION}/${ENCLOSURE}/${testdir}/report-${startDateTime}.html\">report-${startDateTime}.html</a><br><a href=\"http://${RGTEST_VMIP}/rg_logs/api${API_VERSION}/ov${OV_VERSION}/${OV_PASS_BUILD}/vc${VC_VERSION}/${ENCLOSURE}/${testdir}/output-${startDateTime}.xml\">output-${startDateTime}.xml</a></td>";
        ) | mail -s "$(echo -e "RG Automated Test Result: [${OV_PASS_BUILD}][api${API_VERSION}][ov${OV_VERSION}][vc${VC_VERSION}][${ENCLOSURE}][${testdir}]\nContent-Type: text/html\nMIME-Version: 1.0\nContent-Disposition: inline")" -r "meadowsp@hpe.com" ${TEST_RECIPIENT}
    fi
    cd -
done

echo "just sayin'..." | mail -s "${ENCLOSURE} Tests Complete" -r ${TEST_RECIPIENT}

