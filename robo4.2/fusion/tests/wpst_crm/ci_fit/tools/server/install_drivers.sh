#!/bin/bash

KVER=`uname -r | sed 's/BOOT//' | sed 's/default//'`

RPM="/bin/rpm"
RPMBUILD="/usr/bin/rpmbuild"
PKG_PATH=/usr/src/redhat

##### main #####
                                                                                
if [ $# -eq 1 ]
then
	SRC_RPM=$1
else
        echo "usage: $0 </path/to/driver SRC RPM>"
        exit 1
fi

BUILD_LOG="$SRC_RPM"_"build.log"
if [ -f $BUILD_LOG ]; then
	rm -f $BUILD_LOG
fi

if ! ls $SRC_RPM > /dev/null 2>&1
then
	echo "Error: Could not find $SRC_RPM driver source rpm."
	exit 1
fi

echo "Installing $SRC_RPM source rpm..." | tee -a $BUILD_LOG 
${RPM} -ivh $SRC_RPM | tee -a $BUILD_LOG

if [ $? -ne 0 ]
then
	echo "Error: Failed to install $SRC_RPM source rpm"
	exit 1
fi

SPEC_FILE=`${RPM} -qpl $SRC_RPM | grep spec` > /dev/null 2>&1
echo "Building binary rpm..." | tee -a $BUILD_LOG
${RPMBUILD} -bb $PKG_PATH/SPECS/$SPEC_FILE --define "KVER $KVER" | tee -a $BUILD_LOG

if [ $? -ne 0 ]
then
	echo "Error: RPM build failed for $SRC_RPM" 
	exit 1
fi

echo "Installing binary rpm..." | tee -a $BUILD_LOG
KMOD=(`cat $BUILD_LOG | grep "Wrote" | awk 'BEGIN{FS=" "} {print $NF}'`)
${RPM} -ivh $KMOD --nodeps | tee -a $BUILD_LOG


