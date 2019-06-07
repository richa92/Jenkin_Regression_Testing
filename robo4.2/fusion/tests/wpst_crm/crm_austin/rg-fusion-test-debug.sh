#!/bin/bash

#Requirements:
#  - ssh logins must be configured from RG_HOST to JUMP_STATION to OV_IP
#  - ssh login must be configured from OV_IP to this RG_HOST

#Global variables must be setup here first
OV_VERSION="200"
API_VERSION="201"
RG_DIR="2.00.02-0219211-2.00.03-0226313"
VC_VERSION="445"
ENC="Austin2"
TEST_DIR="All-120"
RG_HOST="15.186.8.60"
RG_SCRIPT="3.1.1.4-enetVlan-debugging-QXCR1001458836.txt"
OV_IP="15.186.21.204"
JUMP_STATION="15.178.211.147"
OA_IP="15.186.2.79"
VCMCLI_TARGET_HOST="15.186.20.255"
GATEWAY="15.186.0.1"
QUIX="QXCR1001458836-${ENC}"
LOCAL_CI_DEBUG_DIR="/automation/fusion-2.00.03/tests/wpst_crm/crm_austin/${TEST_DIR}/${QUIX}"
BUG_IN_API="False"

if [ ${OV_VERSION} != ${API_VERSION} ];then BUG_IN_API="True";fi

pybot -d /var/www/html/rg_logs/api${API_VERSION}/ov${OV_VERSION}/${RG_DIR}/vc${VC_VERSION}/${ENC}/${TEST_DIR}/${RG_SCRIPT} -t 1* --runmode ExitOnFailure -vOV_IP:${OV_IP} -vX-API-version:${API_VERSION} -vBUG_IN_API:${BUG_IN_API} ${RG_SCRIPT}
echo "Please manually collect OA showAll, OA dump_debug and OA Support Dump" | mail -s "${ENC} Tests Complete, get OA dump_debug and supportdump" -r "jason.mas.pernito@hpe.com" jason.mas.pernito@hpe.com

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


echo "Please see collected OV Support Dump, OV ciDebug logs, OA soap debug, OA show All, OA syslog, OA dump_debug, OA Support Dump, Network Logs, VCM log files" | mail -s "${ENC} Tests Complete, inspect collected logs" -r "jason.mas.pernito@hpe.com" jason.mas.pernito@hpe.com

