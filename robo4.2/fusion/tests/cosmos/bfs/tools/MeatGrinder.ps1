Param([string]$ip, [string]$targetip, [string]$username, [string]$password, [string]$sharedFolder)

Function MeatGrinder($ip, $targetip, $username, $password, $sharedFolder)
{
    #Create a Remote session
    $session = GenerateWindowsSession $ip $username $password
    MGRun  $session $targetip $sharedFolder
    DisconnectWindowsSession $session
}

Function GenerateWindowsSession($ip, $username, $password)
{
    # we need to have dhcp module copy at dhcp server from \\jdata.us.rdlabs.hpecorp.net\Cosmos\Automation\Tools\Microsoft.DHCP.PowerShell.Admin.psm1
    # DHCP server should be enable to communicate with remote server

    #Enable automation vm to communicate with remote server
    #Invoke-Command -Session $session -ScriptBlock {Enable-PSRemoting -Force}
    #Invoke-Command -Session $session -ScriptBlock {Set-Item "wsman:\localhost\client\trustedhosts" $dhcpserverip -concatenate -force}
    #Set-Item "wsman:\localhost\client\trustedhosts" $ip -concatenate -force

    $password = ConvertTo-SecureString $password -AsPlainText -Force
    $cred= New-Object System.Management.Automation.PSCredential ($username, $password)
    $session = New-PSSession -ComputerName $ip -Credential $cred

    #Write-Host $session
    return $session
}

Function DisconnectWindowsSession($session)
{
        # remove powershell session
        Remove-PSSession $session
}

Function MGRun($session, $targetip, $sharedFolder)
{
    Write-Host("Testing MG Run")
    ${file_exist}=  Invoke-Command -Session $session -ScriptBlock{Test-Path C:\\Users\\Administrator\\Desktop\\ETD\\etdntmg.exe}
    Write-Output("MG executable file is present")
    If($file_exist -ne $True){
           Move-Item "C:\Program Files\ETD x86-64 Windows Meatgrinder 5.110" "C:\\Users\\Administrator\\Desktop\\ETD"
    }
    ${restart_workstation}=  Invoke-Command -Session $session -ScriptBlock {net stop workstation /y ; net start workstation}
    Write-Output ${restart_workstation}
    ${MG_run}=  Invoke-Command -Session $session -ScriptBlock {$Username = 'Administrator'; $Password = 'Cosmos123'; $pass = ConvertTo-SecureString -AsPlainText $Password -Force; $Cred = New-Object System.Management.Automation.PSCredential -ArgumentList $Username,$pass; net use /delete * /y; New-PSDrive "X" -PSProvider FileSystem -Root \\\\$targetip\\$sharedFolder -Persist -Credential $Cred; net use ; powershell -command C:\\Users\\Administrator\\Desktop\\ETD\\etdntmg.exe -start -nodrivers -timeout=200 -ini="C:\\Users\\Administrator\\Desktop\\ETD\\default1.ini"}
    Write-Output ${MG_run}
    return ${MG_run}
}

MeatGrinder $ip $targetip $username $password $sharedFolder
