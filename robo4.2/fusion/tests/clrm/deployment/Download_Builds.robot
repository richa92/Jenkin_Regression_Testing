*** Settings ***
Documentation    Download latest build
Suite Setup      Set Log Level   Trace

Library          i3SLibrary
Library          OperatingSystem
Library          BuiltIn
Library          Collections
Library          String


*** Variables ***
${PROXY}            http://16.167.28.210:8080/
${BUILD_URL}        http://ci-artifacts02.vse.rdlabs.hpecorp.net/Fusion/rel/4.10/DDImage/
${DESTN}            e:/shares/builds/
${F_TYPE}           ova
${LATEST}           ${None}
${PASS_BUILD}       ${None}
${BUILD_RETAIN_NUM}  ${None}


*** Test Cases ***
Download Build From Fusion File Server
    [Documentation]  Download build from a url
    [Tags]      download
    ${r}=   Download File By Type     ${BUILD_URL}  ${DESTN}    ${F_TYPE}   ${LATEST}   ${PASS_BUILD}   ${PROXY}
    Should Not Be Empty     ${r}    Error: Unable to download the build.
    Log     ${r} has been successfully download.

Cleanup Older Builds
    [Documentation]  Remove older builds
    [Tags]      cleanup
    ${file_list}=   List Files In Directory     ${DESTN}    pattern=*.${F_TYPE}
    Log  \n"Builds in the Directory: ${file_list}"     console=True
    Sort And Remove Older Builds    ${file_list}


*** Keywords ***

Sort And Remove Older Builds
    [Documentation]  sort the builds to daily and pass groups and delete older builds if count exceeding retain number
    [Arguments]  ${builds}

    #sort the builds
    ${pass_builds}=     create list
    ${daily_builds}=    create list
    :For  ${build}  IN  @{builds}
    \   run keyword if  "PASS" in "${build}"
    \   ...     Append to List     ${pass_builds}   ${build}
    \   ...     ELSE    Append to List     ${daily_builds}   ${build}

    #Delete Older builds
    Run keyword if  ${PASS_BUILD} == ${True}   Run Keywords    Log     \n"Cleanup of older pass builds"     console=True
    ...     AND     Delete builds  ${pass_builds}
    ...     ELSE    Run Keywords    Log     \n"Cleanup of older daily builds"     console=True
    ...             AND     Delete builds   ${daily_builds}

Delete builds
    [Documentation]  Delete builds if the build count exceeds the retain number
    [Arguments]    ${build_list}

    ${build_count}=    Get Length      ${build_list}
    Log     \n"Number of builds available : ${build_count}"     console=True
    Log     \n"Number of builds to retain : ${BUILD_RETAIN_NUM}"     console=True

    run keyword and return if   ${build_count} <= ${BUILD_RETAIN_NUM}    Log   \n"Directory has the required minimum number of builds, cleanup will not run"     console=True

    Log     \n"Removing older builds"      console=True
    Sort List   ${build_list}
    ${delete_count}=   Evaluate    ${build_count}-${BUILD_RETAIN_NUM}
    Log     \n"Number of builds to remove: ${delete_count}"      console=True
    ${builds_to_delete}=    Get Slice From List     ${build_list}     start=0     end=${delete_count}
    Log     \n"Deletion list:\n ${builds_to_delete}"      console=True

    :For  ${build}  IN   @{builds_to_delete}
    \   Log   \n"Deleting build: ${DESTN}${/}${build}"      console=True
    \   Remove File     ${DESTN}${/}${build}
