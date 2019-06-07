Param([string]$dhcpserverip, [string]$username, [string]$password)

Function MonitorStoragePath($dhcpserverip, $username, $password)
{
    #Create a Remote session
    $session = GenerateWindowsSession $dhcpserverip $username $password

    Write-Host("Monitoring the storagePath")
    Start-Sleep -s 10
    $out= Invoke-Command -Session $session -ScriptBlock{mpclaim.exe -s -d}
    $out1 = $out | out-string
    If($out1.Contains("Disk 0"))
    {
         $append = "0"
    }
    $out2= Invoke-Command -Session $session -ScriptBlock{param($append)mpclaim.exe -s -d $append} -ArgumentList $append
    $out2 = $out2 | out-string
    If($out2)
    {
       Write-Host($out2)
    }
    If($out1.Contains("Disk 1"))
    {
        $append = "1"
        $out3= Invoke-Command -Session $session -ScriptBlock{param($append)mpclaim.exe -s -d $append} -ArgumentList $append
        $out3 = $out3 | out-string
        Write-Host($out3)
    }
    DisconnectWindowsSession $session
}

Function GenerateWindowsSession($dhcpserverip, $username, $password)
{
    # we need to have dhcp module copy at dhcp server from \\jdata.us.rdlabs.hpecorp.net\Cosmos\Automation\Tools\Microsoft.DHCP.PowerShell.Admin.psm1
    # DHCP server should be enable to communicate with remote server

    #Enable automation vm to communicate with remote server
    #Invoke-Command -Session $session -ScriptBlock {Enable-PSRemoting -Force}
    #Invoke-Command -Session $session -ScriptBlock {Set-Item "wsman:\localhost\client\trustedhosts" $dhcpserverip -concatenate -force}
    #Set-Item "wsman:\localhost\client\trustedhosts" $dhcpserverip -concatenate -force

    $password = ConvertTo-SecureString $password -AsPlainText -Force
    $cred= New-Object System.Management.Automation.PSCredential ($username, $password)
    $session = New-PSSession -ComputerName $dhcpserverip -Credential $cred

    #Write-Host $session
    return $session
}

Function DisconnectWindowsSession($session)
{
        # remove powershell session
        Remove-PSSession $session
}

MonitorStoragePath $dhcpserverip $username $password