#!/bin/bash

DATAFILE=$1

#main
targetFile=$(basename "$DATAFILE" | /bin/sed -e "s/^data-/save-/")
targetDir=$(dirname "$DATAFILE")

if [ -e $DATAFILE ]
then
  echo -n "Promoting data file ${DATAFILE} to ${targetDir}/${targetFile}..."
  cp "$DATAFILE" "${targetDir}/${targetFile}"
  if [ $? != 0 ];then echo "Failed to copy $DATAFILE to ${targetDir}/${targetFile}";exit 1; fi
  git add "${targetDir}/${targetFile}"
  if [ $? != 0 ];then echo "Failed to git add ${targetDir}/${targetFile}";exit 1; fi
  echo "[DONE]"
fi
