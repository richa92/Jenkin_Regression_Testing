*** Keywords ***

Get Connection by Boot Priority
    [Documentation]  Given a list of SP Connections, find the connection with the specified boot priority
    [Arguments]  ${connections}  ${bootPriority}
    :FOR  ${conn}  IN  @{connections}
    \   Return From Keyword If  '${conn['boot']['priority']}' == '${bootPriority}'  ${conn}
    [Return]  ${None}

Get SAN Storage System WWNs
    [Documentation]  Given a list of storage system ports, return a list for the given VSAN and protocal type
    [Arguments]  ${ssys_ports}  ${vsan}  ${protocol}
    @{ret}=  Create List
    :FOR  ${port}  IN  @{ssys_ports}
    \   Continue For Loop If  '${port['actualSanName']}' != '${vsan}' or '${port['protocolType']}' != '${protocol}'
    \   ${wwn}=  Normalize WWN  ${port['address']}
    \   Append To List  ${ret}  ${wwn}
    [Return]  @{ret}

Normalize WWN
    [Documentation]  Given a WWN string, normalize it to be all uppercase and remove all ':' separators
    [Arguments]  ${wwn}
    ${ret}=  Remove String  ${wwn}  :
    ${ret}=  Convert To Uppercase  ${ret}
    [Return]  ${ret}

WWNs Should Be Equal
    [Documentation]  compare 2 WWNs after normalizing them
    [Arguments]  ${wwn1}  ${wwn2}
    ${nwwn1}=  Normalize WWN  ${wwn1}
    ${nwwn2}=  Normalize WWN  ${wwn2}
    Should Be Equal  ${nwwn1}  ${nwwn2}

Verify Against Storage System
    [Documentation]  Given a Server Profile, verify that the settings match the storage system
    [Arguments]  ${sp}  ${ptarget1}  ${ptarget2}  ${starget1}  ${starget2}
    # Collect values from the storage system
    ${ssys}=  Get Resource  ${sp['sanStorage']['volumeAttachments'][0]['volumeStorageSystemUri']}
    ${ssys_primary_WWNs}=  Get SAN Storage System WWNs  ${ssys['ports']}  ${FC_NETWORK_A_VSAN}  FC
    Length Should Be  ${ssys_primary_WWNs}  2
    ${ssys_secondary_WWNS}=  Get SAN Storage System WWNs  ${ssys['ports']}  ${FC_NETWORK_B_VSAN}  FC
    Length Should Be  ${ssys_secondary_WWNs}  2

    # Verify that the Server Profile primary targets reference WWNs associated with the storage system's primary connections
    ${ptarget_wwn1}=  Normalize WWN  ${ptarget1['arrayWwpn']}
    ${ptarget_wwn2}=  Normalize WWN  ${ptarget2['arrayWwpn']}
    Should Not Be Equal  ${ptarget_wwn1}  ${ptarget_wwn2}
    List Should Contain Value  ${ssys_primary_WWNs}  ${ptarget_wwn1}
    List Should Contain Value  ${ssys_primary_WWNs}  ${ptarget_wwn1}

    # Verify that the Server Profile secondary targets reference WWNs associated with the storage system's secondary connections
    ${starget_wwn1}=  Normalize WWN  ${starget1['arrayWwpn']}
    ${starget_wwn2}=  Normalize WWN  ${starget2['arrayWwpn']}
    Should Not Be Equal  ${starget_wwn1}  ${starget_wwn2}
    List Should Contain Value  ${ssys_secondary_WWNs}  ${starget_wwn1}
    List Should Contain Value  ${ssys_secondary_WWNs}  ${starget_wwn1}

Normalize RIS FC LUN
    [Documentation]  RIS FC Luns don't follow the normal convention, convert it
    [Arguments]  ${ris_lun}
    # There is a complex algorithm to convert the LUN in DesiredBootDevices to integer.  Since we should always be
    # creating LUN 1 with this server profile assume that LUN is 1 but do a sanity check vs. implementing the real
    # algorithm.  If this fails we'll need to invest the time to implement the real algorithm at
    # http://www.t10.org/ftp/t10/document.06/06-003r1.pdf
    Should Be Equal  ${ris_lun}  1000000000000
    [Return]  1
