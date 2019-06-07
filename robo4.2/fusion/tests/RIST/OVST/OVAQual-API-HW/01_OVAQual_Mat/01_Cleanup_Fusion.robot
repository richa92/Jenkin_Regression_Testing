*** Settings ***
Documentation      Tests to Cleanup OA and ilo
Resource           ../resource.txt
Test Teardown                   Pause And Send EMail on Failure

*** Test Cases ***

Cleanup-OA
    [Documentation]   Cleanup OA VC Mode and Restart OA
    [TAGS]    Cleanup  CleanupOA
    # Power Off All Blades, Clear VC Mode and Restart oa
    :For    ${oa}    In     @{cleanup_oa}
    \    Log    Powering off all blades  console=True
    \    ${status} =   Power off all blades   ${oa}
    \    Log  ${status}
    \    Log   Clearing VC Mode  console=True
    \    ${clear_status} =    Clear Oa Vc Mode    ${oa}
    \    Log   ${clear_status}
    \    Log    Restarting ${oa['hostname']} OA  console=True
    \    ${restart_status}=   Restart Oa    ${oa}
    \    Log  ${restart_status}
    \    Ping OA IP    ${oa['hostname']}

Cleanup-ilo
    [Documentation]   Cleanup ilo by removing sso certificates
    [TAGS]    Cleanup  Cleanupilo
    :FOR    ${ilo}    IN    @{cleanup_ilo}
    \  ${status}=  Run Keyword And Continue On Failure  remove all sso certificates blade   ${ilo}
    \  Run Keyword If   '${status}'=='True'   Log  SSO Certificate successfully deleted in ${ilo['ilo']}  console=yes
    \  Run Keyword If   '${status}'=='False'  Log  SSO Certificate is not present in ${ilo['ilo']}  console=yes

*** Keywords ***

Ping OA IP
    [Documentation]   Ping OA ip
    [arguments]     ${ip}
    ${output} =    Run    ping ${ip} -4 -n 1
    Should Contain    ${output}    time
    Log    OA is up and pinging    console=yes
