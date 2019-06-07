#!/bin/bash

#
# Script to decrypt support dump
#

echo Utility to decrypt support dump

# Set EncryptionUtil-0.0.1-SNAPSHOT.jar in the classpath
echo Classpath: $CLASSPATH
echo Current Dir: ${PWD}
CLASSPATH=$CLASSPATH:${PWD}/EncryptionUtil-0.0.1-SNAPSHOT.jar
export CLASSPATH
echo CLASSPATH: ${CLASSPATH}

if [ "$1" != "-f" ]
then
	echo "Invalid option. Valid command: decrypt-support-dump -f absolute-path-of-support-dump-file -k absolute-path-of-private-key-file"
    exit 1
fi

if [ -f "$2" ]
then
    echo "Valid support dump file found"
else
    echo "Support dump file was not found."
    exit 1
fi

if [ "$3" != "-k" ]
then
	echo "Invalid option. Valid command: decrypt-support-dump -f absolute-path-of-support-dump-file -k absolute-path-of-private-key-file"
	exit 1
fi

if [ -f "$4" ]
then
    echo "Valid private key file found."
else
    echo "Private key file was not found."
	exit 1
fi

# execute java command to decrypt support dump

#java com.hp.ci.mgmt.supportdump.util.EncryptionUtil ${supportDumpPath} ${privateKeyPath}
java com.hp.ci.mgmt.supportdump.util.EncryptionUtil $2 $4
