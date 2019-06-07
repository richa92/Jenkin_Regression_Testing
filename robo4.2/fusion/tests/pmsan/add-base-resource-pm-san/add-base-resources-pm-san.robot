*** Settings ***
Documentation   AddBaseResources C7000 for PM SAN
...             - First time setup
...             - Add networks, LIG, EG, and enclosures
...             - Add storage systems and edit the storage pools to managed
...             = USAGE =
...             | pybot | -v  APPLIANCE_IP:<IP> | -v DATA_FILE:data/preCheckIn-1200.py | .\csat-pm-san-profiles.robot |
...             = Variables =
...             | APPLIANCE_IP | Required; IP address of the OneView appliance to use |
...             | DATA_FILE  | The data file to use for test run.  Contains variable definitions that may vary from system to system. |

Resource        ../../../Resources/api/fusion_api_resource.txt

Variables       ${DATA_FILE}

*** Test Cases ***
ABR C7000 Initialize the Variables
    Set Log Level                   TRACE
    log variables

ABR C7000 FTS, Add Licenses
#    First Time Setup                password=${APPLIANCE_ADMIN_PASSWORD}
    Fusion Api Login Appliance      ${APPLIANCE_IP}     ${ADMIN_CREDENTIALS}
    Add Licenses from variable      ${LICENSES}

ABR C7000 Add the Base Resources
    Add Users from variable                 ${USERS}
    ${RESPLIST} =  Add San Managers Async   ${SAN_MANAGERS}
    Wait for task2                          ${RESPLIST}  timeout=120  interval=10
    Add Ethernet Networks from variable     ${ETHERNET_NETWORKS}
    Add FC Networks from variable           ${FC_NETWORKS}
    Add LIG from list                       ${LIGS}
    Add Enclosure Group from list           ${ENC_GROUPS}
    Add Enclosures from variable            ${ENCLOSURES}

ABR C7000 Add and Edit the Storage Systems
    ${RESPLIST} =  Add Storage Systems Async  ${STORAGE_SYSTEMS}
    wait for task2  ${RESPLIST}  timeout=300  interval=10

    ${RESPLIST} =  Edit Storage Systems Async  ${STORAGE_SYSTEMS}
    wait for task2  ${RESPLIST}  timeout=300  interval=10

ABR C7000 Edit the Storage Pools to Managed
    ${resplist} =  Edit Storage Pools Async  ${STORAGE_POOLS}
    wait for task2  ${RESPLIST}  timeout=300  interval=10

Logout
    [Documentation]  Log out OneView
    Fusion Api Logout Appliance

