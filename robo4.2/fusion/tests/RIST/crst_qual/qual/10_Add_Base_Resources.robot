*** Settings ***
Documentation    Add Base Resources to OneView: Licenses, SPP, Users, Networks, Storage, etc.
Resource                ../resource.txt

Variables                       ../Common.py
Variables                       ../${DATA_FILE}

Suite Setup                     QUAL Suite Setup    ${ADMIN_CREDENTIALS}
Suite Teardown                  QUAL Suite Teardown

*** Test Cases ***
Add License
    [Documentation]    Add License to OneView
    [Tags]    10    LICENSE
    ${licenses} =     Get Variable Value    ${LICENSES}
    Run Keyword If    ${licenses} is not ${null}    Add Licenses from variable    ${licenses}

Download Latest iso
    [Tags]   10    GET_FW_BUNDLE
    Download Latest File From Web Folder    ${WEB_URL}    ${WEB_USERNAME}    ${WEB_PASSWORD}

Upload Firmware Bundle
    [Tags]    10    UPLOAD_FWBUNDLE
    [Documentation]    Uploads already obtained Firmware Bungle to OneView
    Upload SPP Bundle    ${SPP_LOCALPATH}

Firmware Bundle Should Match
    [Tags]    10    FWBUNDLE_MATCH
    ${fw_bundles} =     Get Firmware Bundle    ${EMPTY}

    Length Should Be    ${fw_bundles['members']}    1    msg=There should only be 1 uploaded bundle
    ${fw_bundle} =    Get From List    ${fw_bundles['members']}    0

    Should Match    ${fw_bundle['bundleType']}    SPP    msg=Bundle type should be SPP

#   OS Lenght on 5.0 not reporting the same as on 4.20.  Per Matt Kenney, just make sure bundle was uploaded
#   and it is ok to skip post upload validations.
#
#   In re: to #1 – this is likely to change periodically.  The intent is just to make sure that the SPP upload works,
#   I think the validation post successful upload can be fairly minimal.  If it helps to just reduce checks of SPP returns I’m all for it.
#
#   Matt
#    ${supported_os_list_length} =    Get Length    ${fw_bundle['supportedOSList']}
#    ${fwComponents_length} =    Get Length    ${fw_bundle['fwComponents']}
#
#    # not a very accurate test thus should determine exactly what to verify
#    Run Keyword If    ${supported_os_list_length} < 50    Fail    There should be at least 50 Supported OS
#    Run Keyword If    ${fwComponents_length} < 500    Fail    There should be at least 500 FW components

Add Users
    [Tags]      10    USERS
    [Documentation]     Add users to OneView (roles - Infrastructure administrator, Full, Server administrator, Network administrator, Backup administrator, Read only and Storage administrator)
    ${users} =    Get Variable Value    ${USERS}
    Run Keyword If  ${users} is not ${null}     Add Users from variable async  ${users}

Add San Manager
    [Tags]      10    SM
    [Documentation]     Add SAN Manager to OneView
    ${san_managers} =    Get Variable Value    ${SAN_MANAGERS}
    Run Keyword If  ${san_managers} is not ${null}     Add San Managers Async    ${san_managers}

Add Ethernet Networks
    [Tags]      10    E_NW
    [Documentation]     Add Ethernet Networks to OneView
    ${ethernet_networks} =    Get Variable Value    ${ETHERNET_NETWORKS}
    Run Keyword If  ${ethernet_networks} is not ${null}     Add Ethernet Networks from variable async  ${ethernet_networks}

Add Bulk Ethernet Networks
    [Tags]      10    BE_NW
    [Documentation]     Add Bulk Ethernet Networks to OneView
    ${bulk_ethernet_networks} =    Get Variable Value    ${BULK_ETHERNET_NETWORKS}
    Run Keyword If  ${bulk_ethernet_networks} is not ${null}     Create Bulk Ethernet Networks  ${bulk_ethernet_networks}

Add FC networks
    [Tags]    10    FC_NW
    [Documentation]        Add FC Networks to OneView
    ${fc_networks} =    Get Variable Value    ${FC_NETWORKDS}
    Run Keyword If  ${fc_networks} is not ${null}    Add FC Networks from variable async    ${fc_networks}

Add iSCSI Networks
    [Tags]      10    ISCSI_NW
    [Documentation]     Add iSCSI Networks to OneView
    ${iscsi_networks} =    Get Variable Value    ${ISCSI_NETWORKDS}
    Run Keyword If  ${iscsi_networks} is not ${null}     Add Ethernet Networks from variable async  ${iscsi_networks}

Add Network Sets
    [Tags]      10    NW_SETS
    [Documentation]     Add Network Sets to OneView
    ${network_sets} =    Get Variable Value    ${NETWORK_SETS}
    Run Keyword If  ${network_sets} is not ${null}   Add Networks Sets from variable async  ${networksets}    ${True}

*** Keywords ***
Upload SPP bundle
    [Documentation]    Read SPP bundle from a given path on mapped folder and upload it into OV
    [Arguments]     ${spp_path}
    @{spps_name} =  OperatingSystem.List Directory  ${spp_path}  *.iso  absolute
    :FOR    ${spp_name}  IN  @{spps_name}
    \  Upload Firmware Bundle By Curl    fw_absolute_path=${spp_name}    VERBOSE=True
    Log    Finished uploading ${spp_name} bundle    console=${CONSOLE}

