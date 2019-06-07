#!/bin/bash
#
#(C) Copyright 2016-2018 Hewlett Packard Enterprise Development LP
#
# Script to decrypt support dump
#

echo "************************************"
echo Utility to decrypt support dump 3.0
echo "************************************"


# Set Decryption-Util.jar in the classpath
echo Classpath: $CLASSPATH
currentDir=$(pwd)
echo Current Dir : $currentDir
dir_to_replace="abaf-common/src/main/java/decryptionUtility"
decrypt_util_dir="${currentDir/support-dump/$dir_to_replace}"

export CLASSPATH=$CLASSPATH:$decrypt_util_dir/Decryption-Util.jar:$CLASSPATH
#CLASSPATH=$CLASSPATH:${PWD}/Decryption-Util.jar
#export CLASSPATH
echo CLASSPATH: ${CLASSPATH}

if [ "$#" != 1 ]
then
    echo -e "$0: missing support dump file operand\n\n"
    echo "Valid command: $0 absolute-path-of-support-dump-file"
    exit 1
fi

if [ ! -f "$1" ]
then
    echo "File with name $1 was not found. Please provide valid support dump file."
    exit 1
fi

echo $1
# execute java command to decrypt support dump

#java com.hp.ci.mgmt.supportdump.util.EncryptionUtil ${supportDumpPath} ${privateKeyPath}

while :;do echo -n .;sleep 0.5;done & # create a progress bar of . character and run in background
trap "kill $!" EXIT  #Die with parent if we die prematurely
echo
echo "Going to run Decryptutil"
echo $JAVA_HOME
if [ -n "$JAVA_HOME" ]; then
    $JAVA_HOME/bin/java com.hp.ci.mgmt.supportdump.util.DecryptionUtil $1;
else
    java com.hp.ci.mgmt.supportdump.util.DecryptionUtil $1;
fi

kill $! && trap " " EXIT #Kill the loop and unset the trap or else the pid might get reassigned and we might end up killing a completely different process





