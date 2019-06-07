*** Settings ***
Documentation   Test suite for creating RAID init profiles for Plexxi DLs.
...             This script is meant to help save time by discovering all server hardware
...             added to a OV appliance and creating a server profile with local storage
...             options that will create a RAID array on the brand new equipment. Thus,
...             it is really only intended to be used once per rig.  However, it might
...             also be useful later to wipe local OS installs.
...             You can pass in the number of drives and RAID level as variables.
...
...             Note: Creates and applies profiles, but does not remove them in case issues
...             are hit.
...
...                 Script Usage:
...
...                 - pybot -v OV_IP:<ip\fqdn> create_raid_profiles.robot
...                 - pybot -v OV_IP:<ip\fqdn> -v DRIVES 2 -v RAID_LEVEL RAID1 create_raid_profiles.robot


Library         FusionLibrary
Library         Collections
Library         create_raid_profiles_data.py

Resource        ../../../../Resources/api/fusion_api_resource.txt

Suite Setup     Login

*** Variables ***
${OV_IP}        ${None}
&{OV_CRED}      userName=Administrator      password=hpvse123
${DRIVES}       2
${RAID_LEVEL}   RAID1
*** Keywords ***
Login
    [Documentation]     Prepares the testing environment by logging to the appliances
    ${r}    ${s}=    Fusion Api Login Appliance  ${OV_IP}  ${OV_CRED}
    Run Keyword If  ${r['status_code']} is not 200    Fail      Unable to login

*** Test Cases ***
Create server profiles to manage local storage
    [Tags]    profiles
    [Documentation]     Creates SP (for all found hardware that does not have a profile) to init RAID
    ${resps} =       create list
    ${servers} =     fusion api get server hardware
    :FOR   ${s}   IN   @{servers['members']}
    \      Run Keyword If   '${s['serverProfileUri']}' != '${None}'    Continue for loop
    \      ${profile} =    mk_profile    name=${s['serialNumber']}   serverHardwareUri=${s['uri']}    drives=${DRIVES}    raidLevel=${RAID_LEVEL}
    \      ${resp} =       fusion api create server profile     body=${profile}    param=?force=ignoreServerHealth
    \      Append to list    ${resps}    ${resp}
    \      Wait for Task2    ${resps}    timeout=800   interval=10
