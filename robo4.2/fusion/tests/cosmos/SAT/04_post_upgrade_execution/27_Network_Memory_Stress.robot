*** Settings ** *
Documentation
...     This Test Suite uses AD server Group User credentials for configuring NIC teaming, multipath, network and memory Tests.
...     Test Data is defined in Python Data Variable file.
...     TAGS:    CONFIG-NIC-IO
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup    ${ad_server_credentials}
Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
...                             AND  Regression Test Teardown

*** Test Cases ***
Power On Windows server Profiles And Wait For Post State
    [Tags]    SP-ON  T-BIRD  C7000
    [Documentation]    Power On Server Profile And Wait For Post State
    Power On Server Profile And Wait For POST State    ${win_os_servers}

Check And Configure NIC Teaming In Windows
    [Tags]    NIC  T-BIRD  C7000
    [Documentation]    Create NIC Teaming in Windows
    [Timeout]    15min   Timeout Test Issue after trying for 15 mins
    : FOR  ${win_os_server}  IN   @{win_os_servers}
    \    Run Keyword And Continue On Failure    Check And Configure NIC Teaming In Windows    ${win_os_server}   c     Teaming1     Ethernet*

Install MPIO Feature, Windows Server Should Be Pinging, FCoE Disk Should Exist and Active - C7000
    [Tags]    OSIP  C7000
    [Documentation]     Windows Server Should Be Pinging, FCoE Disk Should Exist and paths should be Active
    : FOR  ${win_os_server}  IN   @{win_os_servers}
    \    Run Keyword And Continue On Failure   Install MPIO Feature And Windows Server Should Be Pinging     ${win_os_server}
    \    Run Keyword And Continue On Failure   Windows Server Should Be Pinging And Volume Should Be Active    ${win_os_server}   02

Install MPIO Feature, Windows Server Should Be Pinging, FC Disk Should Exist and Active - Tbird
    [Tags]    OSIP-TB  T-BIRD
    [Documentation]     Windows Server Should Be Pinging and FC Disk Should Exist and paths should be Active
    : FOR  ${win_os_server}  IN   @{win_os_servers}
    \    Run Keyword And Continue On Failure   Install MPIO Feature And Windows Server Should Be Pinging     ${win_os_server}
    \    Run Keyword And Continue On Failure   Windows Server Should Be Pinging And Volume Should Be Active    ${win_os_server}   04

Network And Memory Stress Using MeatGrinder
    [Tags]    MeatGrinderStress  T-BIRD  C7000
    [Documentation]    Network Connectivity And Memory Stress Using MeatGrinder
    ${win_os_1}=    Get IP From Server Profile   ${win_os_servers[0]}
    ${win_os_2}=    Get IP From Server Profile   ${win_os_servers[1]}
    Enable PSRemaoting And Set Trustedhosts
    : For  ${ip}  in  @{win_name}
    \   ${username} =  set variable  ${stress_tool['username']}
    \   ${password} =  set Variable  ${stress_tool['password']}
    \   ${driverpath} =  set variable  ${stress_tool['DriverName']}
    \   ${filename} =  set variable  ${stress_tool['filename']}
    \   ${dest_path} =  set variable  ${stress_tool['dest']}
    \   ${source} =  set variable  ${stress_tool['source']}
    \   ${target} =  set variable  ${stress_tool['target']}
    \   ${hostname} =  set variable  ${win_os_1[0]}
    \   ${sharedDrive} =  set variable  ${win_os_2[0]}
    \   ${sharedFolder} =  set variable  ${ip['shared_folder']}
    \   ${host} =  set variable  \\\\${win_os_1[0]}
    \   ${dest} =  set variable  ${host}${dest_path}
    \   ${move_etd}=  Run  powershell $Username = '${username}'; $Password = '${password}'; $pass = ConvertTo-SecureString -AsPlainText $Password -Force; $Cred = New-Object System.Management.Automation.PSCredential -ArgumentList $Username,$pass; Invoke-Command -ComputerName ${hostname} -ScriptBlock { Move-Item C:\\Program\\" \\"Files\\ETD\\" \\"x86-64\\" \\"Windows\\" \\"Meatgrinder\\" \\"4.410 C:\\Users\\Administrator\\Desktop\\ETD -force } -credential $Cred
    \   ${copy_ini}=  Run  powershell $Username = '${username}'; $Password = '${password}'; $DriverName = '${driverpath}'; $HostName = '${host}'; $dest = '${dest}'; $source = '${source}'; $target = '${target}'; $Pswd = ConvertTo-SecureString -String $Password -AsPlaintext -Force; $credentials = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $UserName,$Pswd; New-PSDrive -Persist -Name $DriverName -PSProvider FileSystem -Root $dest -credential $credentials; copy-item $source -destination $target ; net use /delete * /y
    \   ${stress}=  Run  powershell $Username = '${username}'; $Password = '${password}'; $pass = ConvertTo-SecureString -AsPlainText $Password -Force; $Cred = New-Object System.Management.Automation.PSCredential -ArgumentList $Username,$pass ; $session = New-PsSession -ComputerName ${hostname} -Credential $Cred ; Invoke-Command -Session $session -ScriptBlock {net stop workstation /y ; net start workstation; $Username = '${username}'; $Password = '${password}'; $pass = ConvertTo-SecureString -AsPlainText $Password -Force; $Cred = New-Object System.Management.Automation.PSCredential -ArgumentList $Username,$pass; net use /delete * /y ; New-PSDrive ${driverpath} -PSProvider FileSystem -Root \\\\${sharedDrive}\\${sharedFolder} -Persist -Credential $Cred ; net use ; powershell -command ${stress_tool['etdpath']} -start -nodrivers -ini=${stress_tool['inipath']} } -asJob
    \   Log  ${stress}  console=yes
    \   ${State}=  Get Regexp Matches  ${stress}  Running
    \   ${Job}=  Get Regexp Matches  ${stress}  Job1
    \   Run Keyword If  "${State}" == "[]" and "${Job}" == "[]"  Run Keyword And Continue on Failure  FAIL  MeatGrinder is not running