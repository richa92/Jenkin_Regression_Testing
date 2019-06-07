#!/bin/bash


usage()
{
  echo "$0 - run RoboGalaxy test suite that will collect OV Support Dump, OV ciDebug logs, OA soap debug, OA show All, OA syslog, OA dump_debug, OA Support Dump, Network Logs, VCM log files."
  echo "Requirements: "
  echo "- ssh logins must be configured from RG_HOST to JUMP_STATION to OV_IP."
  echo "- ssh login must be configured from OV_IP to this RG_HOST."
  echo
  echo "Options: "
  echo "-h, --help"
  echo "      Output a small usage guide and exist successfully. No other output will be generated."
  echo "--oneview oneview-version"
  echo "      The version of OneView appliance to test."
  echo "--api api-version"
  echo "      The X-API-version header to use when executing the test suite."
  echo "--rgdir rgdir"
  echo "      The RoboGalaxy log directory name to use. Usually, a OneView build number (like 2.00.02-0219211) or a OneView upgrade path build numbers (like 1.20.01-0021397-1.20.05-0201918-2.00.03-0226313)."
  echo "--vc vc-version"
  echo "      The Virtual Connect version the test environment is using (e.g. 445)."
  echo "--enc enclosure-name"
  echo "      The enclosure name that test environment is using. This is just to easily identify the group of RG logs. Example: Austin2."
  echo "--testdir testdir"
  echo "      The directory name where the test suite resides. Example: Qos-200-US35763."
  echo "--rghost rghost"
  echo "      The RoboGalaxy VM hosting your test scripts. Please see requirements above..."
  echo "--rgscript rgscript-name"
  echo "      The filename of RG script to execute. This is usually a modified test suited for debugging requirements. Example: Mig-Qos-NoFcoe01-debugging-QXCR1001458836.txt"
  echo "--ovip oneview-ip"
  echo "      The OVA IP address."
  echo "--jmpstationip jump-station-ip"
  echo "      Jump station IP address. Please see requirements above..."
  echo "--oaip oa-ip"
  echo "      Onboard Administrator IP address."
  echo "--vcmip vcm-ip"
  echo "      Virtual Connect primary module IP address."
  echo "--gatewayip gateway-ip"
  echo "      Network gateway IP address."
  echo "--quix qxcr-id"
  echo "      Quix Id of the issue we are debugging. If there's none, you can use a dummy quix or any identifier."
  echo "--retry [True|False]"
  echo "      If you have a retry capability in your RG test script and will use it, you can specify True."
  echo "--email email-recipient"
  echo "      Comma-separated emails to receive the notifications."
}

#Default values
OV_VERSION="200"
API_VERSION="201"
RG_DIR="2.00.02-0219211"
VC_VERSION="445"
ENC=""
TEST_DIR=""
RG_HOST="15.186.8.60"
RG_SCRIPT=""
OV_IP=""
JUMP_STATION="15.178.211.147"
OA_IP=""
VCMCLI_TARGET_HOST=""
GATEWAY="15.186.0.1"
QUIX=""
RETRY="False"
EMAIL="jason.mas.pernito@hpe.com"

OPTS=`getopt -o h -l help,oneview:,api:,rgdir:,vc:,enc:,testdir:,rghost:,rgscript:,ovip:,jmpstationip:,oaip:,vcmip:,gatewayip:,quix:,retry:,email: -- "$@"`
if [ $? != 0 ]
then
  exit 1
fi

eval set -- "$OPTS"

while true ; do
case "$1" in
  -h | --help) usage; break;;
  --oneview) OV_VERSION="$2"; shift 2;;
  --api) API_VERSION="$2"; shift 2;;
  --rgdir) RG_DIR="$2"; shift 2;;
  --vc) VC_VERSION="$2"; shift 2;;
  --enc) ENC="$2"; shift 2;;
  --testdir) TEST_DIR="$2"; shift 2;;
  --rghost) RG_HOST="$2"; shift 2;;
  --rgscript) RG_SCRIPT="$2"; shift 2;;
  --ovip) OV_IP="$2"; shift 2;;
  --jmpstationip) JUMP_STATION="$2"; shift 2;;
  --oaip) OA_IP="$2"; shift 2;;
  --vcmip) VCMCLI_TARGET_HOST="$2"; shift 2;;
  --gatewayip) GATEWAY="$2"; shift 2;;
  --quix) QUIX="$2"; shift 2;;
  --retry) RETRY="$2"; shift 2;;
  --email) EMAIL="$2"; shift 2;;
  --) shift; break;;
esac
done

if [ ${ENC} = "" ];then echo "--enc was not specified.";exit 1; fi
if [ ${TEST_DIR} = "" ];then echo "--testdir was not specified.";exit 1; fi
if [ ${RG_SCRIPT} = "" ];then echo "--rgscript was not specified.";exit 1; fi
if [ ${OV_IP} = "" ];then echo "--ovip was not specified.";exit 1; fi
if [ ${OA_IP} = "" ];then echo "--oaip was not specified.";exit 1; fi
if [ ${VCMCLI_TARGET_HOST} = "" ];then echo "--vcmip was not specified.";exit 1; fi
if [ ${QUIX} = "" ];then echo "--quix was not specified.";exit 1; fi

QUIX="${QUIX}-${ENC}"
LOCAL_CI_DEBUG_DIR="/automation/fusion-2.00.03/tests/wpst_crm/crm_austin/${TEST_DIR}/${QUIX}"
BUG_IN_API="False"

if [ ${OV_VERSION} != ${API_VERSION} ];then BUG_IN_API="True";fi

pybot -d /var/www/html/rg_logs/api${API_VERSION}/ov${OV_VERSION}/${RG_DIR}/vc${VC_VERSION}/${ENC}/${TEST_DIR}/${RG_SCRIPT} -t 1* --runmode ExitOnFailure -vOV_IP:${OV_IP} -vX-API-version:${API_VERSION} -vBUG_IN_API:${BUG_IN_API} ${RG_SCRIPT}
echo "Please manually collect OA show all, OA dump_debug and OA supportdump" | mail -s "${ENC} Tests Complete, get OA dump_debug and supportdump" -r "jason.mas.pernito@hpe.com" ${EMAIL}

mkdir -p ${QUIX}
ssh ${JUMP_STATION} "ssh ${OV_IP} \"route -n\"" > ${QUIX}/route-n.txt
ssh ${JUMP_STATION} "ssh ${OV_IP} \"ping -c20 ${OA_IP}\"" > ${QUIX}/ping-oa.txt
ssh ${JUMP_STATION} "ssh ${OV_IP} \"traceroute ${OA_IP}\"" > ${QUIX}/traceroute-oa.txt
ssh ${JUMP_STATION} "ssh ${OV_IP} \"arp -n\"" > ${QUIX}/arp-n.txt
ssh ${JUMP_STATION} "ssh ${OV_IP} \"ping -c20 ${VCMCLI_TARGET_HOST}\"" > ${QUIX}/ping-vcm.txt
ssh ${JUMP_STATION} "ssh ${OV_IP} \"traceroute ${VCMCLI_TARGET_HOST}\"" > ${QUIX}/traceroute-vcm.txt
ssh ${JUMP_STATION} "ssh ${OV_IP} \"arp -n\"" > ${QUIX}/arp-n2.txt
ssh ${JUMP_STATION} "ssh ${OV_IP} \"route -n\"" > ${QUIX}/route-n2.txt
ssh ${JUMP_STATION} "ssh ${OV_IP} \"ping -c20 ${GATEWAY}\"" > ${QUIX}/ping-gateway.txt
ssh ${JUMP_STATION} "ssh ${OV_IP} \"arp -n\"" > ${QUIX}/arp-n3.txt
ssh ${JUMP_STATION} "ssh ${OV_IP} \"ping -c20 ${OA_IP}\"" > ${QUIX}/ping-oa2.txt
ssh ${JUMP_STATION} "ssh ${OV_IP} \"traceroute ${OA_IP}\"" > ${QUIX}/traceroute2.txt
ssh ${JUMP_STATION} "ssh ${OV_IP} \"arp -n\"" > ${QUIX}/arp-n4.txt
ssh ${JUMP_STATION} "ssh ${OV_IP} \"ping -c20 ${VCMCLI_TARGET_HOST}\"" > ${QUIX}/ping-vcm2.txt
ssh ${JUMP_STATION} "ssh ${OV_IP} \"traceroute ${VCMCLI_TARGET_HOST}\"" > ${QUIX}/traceroute-vcm2.txt
ssh ${JUMP_STATION} "ssh ${OV_IP} \"arp -n\"" > ${QUIX}/arp-n5.txt

#Copy OV ciDebug logs
ssh ${JUMP_STATION} "ssh ${OV_IP} \"scp /ci/logs/ciDebug.* ${RG_HOST}:${LOCAL_CI_DEBUG_DIR}\""

#Get OA soap debug logs
wget -O ${QUIX}/RECV.log.0 --no-check-certificate https://${OA_IP}/RECV.log.0
wget -O ${QUIX}/RECV.log.1 --no-check-certificate https://${OA_IP}/RECV.log.1
wget -O ${QUIX}/SENT.log.0 --no-check-certificate https://${OA_IP}/SENT.log.0
wget -O ${QUIX}/SENT.log.1 --no-check-certificate https://${OA_IP}/SENT.log.1

#Get VCM log files
scp -o StrictHostKeyChecking=no root@${VCMCLI_TARGET_HOST}:/tmp/tracelog.txt ${QUIX}/tracelog.txt
scp -o StrictHostKeyChecking=no root@${VCMCLI_TARGET_HOST}:/var/log/messages ${QUIX}/varlog
ssh -o StrictHostKeyChecking=no root@${VCMCLI_TARGET_HOST} "/usr/local/vcmsupport/bin/traceallthreads vcmd" > ${QUIX}/vcmd_threads
ssh -o StrictHostKeyChecking=no root@${VCMCLI_TARGET_HOST} "/usr/bin/free" > ${QUIX}/memory
ssh -o StrictHostKeyChecking=no root@${VCMCLI_TARGET_HOST} "du /tmp -h" > ${QUIX}/tmp
ssh -o StrictHostKeyChecking=no root@${VCMCLI_TARGET_HOST} "/usr/local/vcm/bin/priv_debug_dump"
scp -o StrictHostKeyChecking=no root@${VCMCLI_TARGET_HOST}:/upload/vc_dump_debug_info  ${QUIX}/vc_dump_debug_info

#Get OV Support dump
pybot -d /var/www/html/rg_logs/api${API_VERSION}/ov${OV_VERSION}/${RG_DIR}/vc${VC_VERSION}/${ENC}/${TEST_DIR}/${RG_SCRIPT} -t 2* -vOV_IP:${OV_IP} -vX-API-version:${API_VERSION} -vBUG_IN_API:${BUG_IN_API} ${RG_SCRIPT}

#Retry test case if applicable
if [ ${RETRY} = "True" ]
then
  pybot -d /var/www/html/rg_logs/api${API_VERSION}/ov${OV_VERSION}/${RG_DIR}/vc${VC_VERSION}/${ENC}/${TEST_DIR}/${RG_SCRIPT} -t 3* -vOV_IP:${OV_IP} -vX-API-version:${API_VERSION} -vBUG_IN_API:${BUG_IN_API} ${RG_SCRIPT}
fi

echo "Please see collected OV Support Dump, OV ciDebug logs, OA soap debug, OA show All, OA syslog, OA dump_debug, OA Support Dump, Network Logs, VCM log files" | mail -s "${ENC} Tests Complete, inspect collected logs" -r "jason.mas.pernito@hpe.com" ${EMAIL}

