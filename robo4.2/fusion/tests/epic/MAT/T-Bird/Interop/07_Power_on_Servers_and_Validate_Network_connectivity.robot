*** Settings ***
Documentation
...     This Test Suite uses Server Administrator credentials to Power on Servers and network connectivity using MeatGrinder tool
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      SERVER
Resource                        ./resource_tbird.txt
Suite Setup                     MAT Suite Setup     ${admin_credentials}
Suite Teardown                  MAT Suite Teardown
Variables                       ./data_variables_tbird.py

*** Test Cases ***

Power on Servers and Validate Network Connectivity
    [Tags]  MeatGrinderStress
    [Documentation]  Power on Servers and network connectivity using MeatGrinder tool
    Power on Servers in Profiles   ${server_profiles}
    #Power on Servers in Profiles   ${server_profiles_from_spt}
    Sleep  5m
    Run  powershell Enable-PSRemoting -Force
    Run  powershell Set-Item wsman:\\localhost\\client\\trustedhosts * -Force
    Run  powershell Restart-Service WinRM
    : For  ${ip}  in  @{win_name}
    \   ${username} =  set variable  ${stress_tool['username']}
    \   ${password} =  set Variable  ${stress_tool['password']}
    \   ${driverpath} =  set variable  ${stress_tool['DriverName']}
    \   ${filename} =  set variable  ${stress_tool['filename']}
    \   ${dest_path} =  set variable  ${stress_tool['dest']}
    \   ${source} =  set variable  ${stress_tool['source']}
    \   ${target} =  set variable  ${stress_tool['target']}
    \   ${hostname} =  set variable  ${ip['name']}
    \   ${sharedDrive} =  set variable  ${ip['shared_drive']}
    \   ${sharedFolder} =  set variable  ${ip['shared_folder']}
    \   ${host} =  set variable  \\\\${ip['name']}
    \   ${dest} =  set variable  ${host}${dest_path}
    \   ${move_etd}=  Run  powershell $Username = '${username}'; $Password = '${password}'; $pass = ConvertTo-SecureString -AsPlainText $Password -Force; $Cred = New-Object System.Management.Automation.PSCredential -ArgumentList $Username,$pass; Invoke-Command -ComputerName ${hostname} -ScriptBlock { Move-Item C:\\Program\\" \\"Files\\ETD\\" \\"x86-64\\" \\"Windows\\" \\"Meatgrinder\\" \\"4.410 C:\\Users\\Administrator\\Desktop\\ETD -force } -credential $Cred
    \   ${copy_ini}=  Run  powershell $Username = '${username}'; $Password = '${password}'; $DriverName = '${driverpath}'; $HostName = '${host}'; $dest = '${dest}'; $source = '${source}'; $target = '${target}'; $Pswd = ConvertTo-SecureString -String $Password -AsPlaintext -Force; $credentials = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $UserName,$Pswd; New-PSDrive -Persist -Name $DriverName -PSProvider FileSystem -Root $dest -credential $credentials; copy-item $source -destination $target ; net use /delete * /y
    \   ${stress}=  Run  powershell $Username = '${username}'; $Password = '${password}'; $pass = ConvertTo-SecureString -AsPlainText $Password -Force; $Cred = New-Object System.Management.Automation.PSCredential -ArgumentList $Username,$pass ; $session = New-PsSession -ComputerName ${hostname} -Credential $Cred ; Invoke-Command -Session $session -ScriptBlock {net stop workstation /y ; net start workstation; $Username = '${username}'; $Password = '${password}'; $pass = ConvertTo-SecureString -AsPlainText $Password -Force; $Cred = New-Object System.Management.Automation.PSCredential -ArgumentList $Username,$pass; net use /delete * /y ; New-PSDrive ${driverpath} -PSProvider FileSystem -Root \\\\${sharedDrive}\\${sharedFolder} -Persist -Credential $Cred ; net use ; powershell -command ${stress_tool['etdpath']} -start -nodrivers -ini=${stress_tool['inipath']} } -asJob
    \   Log  ${stress}  console=yes
    \   ${State}=  Get Regexp Matches  ${stress}  Running
    \   ${Job}=  Get Regexp Matches  ${stress}  Job1
    \   Run Keyword If  "${State}" == "[]" and "${Job}" == "[]"  Run Keyword And Continue on Failure  FAIL  MG is not running

Ping Server Open SSH Connection And Verify Disk
    [Tags]     LinuxPing
    [Documentation]      Ping the server, open the SSH connection and check number of disks present
    : For  ${ip}  in  @{rhel_name}
    \  ${hostname} =  set variable  ${ip['name']}
    \  ${username} =  set variable  ${ip['username']}
    \  ${password} =  set variable  ${ip['password']}
    \  ${RC}   ${output} =   Run and return RC and Output    ping -n 4 ${hostname}
    \  ${gotTask}     ${response} =    Run Keyword and Ignore Error  Should be equal     ${RC}   ${0}    \n${output}
    \  Run Keyword If  '${gotTask}'=='FAIL'  Run Keyword And Continue on Failure  Fail  Server with IP- ${hostname} is unreachable . Output is ${response}
    \  ...  ELSE  Log  Server with IP- ${hostname} is pingable  console=yes
    \  ${status}   ${resp}=    Run Keyword And Ignore Error    Open Connection    ${hostname}
    \  Run Keyword If  '${status}'=='FAIL'   Run Keyword And Continue on Failure  Fail    Failed to Open SSH Connection for server
    \  ${newstatus}    ${resp}=    Run Keyword And Ignore Error    Login    ${username}     ${password}
    \  ${stdout}=   Execute command      lsblk | grep sd
    \  Log      ${stdout}     console= True
    \  Close All Connections
