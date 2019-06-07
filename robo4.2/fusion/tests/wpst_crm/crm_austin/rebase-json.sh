#!/bin/bash
# Rebase json (golden) files from one OneView and/or API Versions to another.

PATH=$1
SOURCE_OV_VERSION=$2
SOURCE_API_VERSION=$3
TARGET_OV_VERSION=$4
TARGET_API_VERSION=$5
FORCE=$6

if [ ${SOURCE_OV_VERSION} -eq ${SOURCE_API_VERSION} ]
then
  FILES=$(/bin/find ${PATH} -name save-*-api${SOURCE_API_VERSION}.json)
else
  FILES=$(/bin/find ${PATH} -name save-*-api${SOURCE_API_VERSION}-ov${SOURCE_OV_VERSION}.json)
fi

function copyJsonFile(){
  srcJson="$1"
  destJson="$2"

  echo "Copying ${srcJson} to ${destJson}"
  /bin/cp "${srcJson}" "${destJson}"
  /usr/bin/git add "${destJson}"
}

#main
for srcJsonFile in ${FILES}
do
  if [ ${TARGET_API_VERSION} -eq ${TARGET_OV_VERSION} ]
  then
    if [ ${SOURCE_OV_VERSION} -eq ${SOURCE_API_VERSION} ]
    then
      targetFile=$(echo "$srcJsonFile" | /bin/sed -e "s/api${SOURCE_API_VERSION}\.json/api${TARGET_API_VERSION}\.json/")
    else
      targetFile=$(echo "$srcJsonFile" | /bin/sed -e "s/api${SOURCE_API_VERSION}-ov${SOURCE_OV_VERSION}\.json/api${TARGET_API_VERSION}\.json/")
    fi
  else
    if [ ${SOURCE_OV_VERSION} -eq ${SOURCE_API_VERSION} ]
    then
      targetFile=$(echo "$srcJsonFile" | /bin/sed -e "s/api${SOURCE_API_VERSION}\.json/api${TARGET_API_VERSION}-ov${TARGET_OV_VERSION}\.json/")
    else
      targetFile=$(echo "$srcJsonFile" | /bin/sed -e "s/api${SOURCE_API_VERSION}-ov${SOURCE_OV_VERSION}\.json/api${TARGET_API_VERSION}-ov${TARGET_OV_VERSION}\.json/")
    fi
  fi
  if [ -e ${targetFile} ]
  then
    if [ "$FORCE" = "force" ]
    then
      copyJsonFile "${srcJsonFile}" "${targetFile}"
    else
      echo "No rebasing occurred for ${srcJsonFile}. Target file exists!"
    fi
  else
    copyJsonFile "${srcJsonFile}" "${targetFile}" 
  fi
done

