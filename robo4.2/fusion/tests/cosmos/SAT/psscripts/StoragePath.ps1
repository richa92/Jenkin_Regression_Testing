Param([string]$dhcpserverip, [string]$username, [string]$password, [string]$expectedPath)

Function MonitorStoragePath($dhcpserverip, $username, $password, $expectedPath)
{
    #Create a Remote session
    $session = GenerateWindowsSession $dhcpserverip $username $password

    Write-Host("Monitoring the storagePath")
    Start-Sleep -s 10
    $out= Invoke-Command -Session $session -ScriptBlock{mpclaim.exe -s -d}
    $out = $out | out-string
    If($out.Contains("Disk 2"))
    {
         $append = "2"
    }
    $out1= Invoke-Command -Session $session -ScriptBlock{param($append)mpclaim.exe -s -d $append} -ArgumentList $append
    $out1 = $out1 | out-string
    $expected = "Disk2: {0} Paths" -f $expectedPath
    Write-Host($expected)
    If($out1.Contains($expected))
    {
       Write-Host("Contains {0} Paths" -f $expectedPath)
       If($out1.Contains("Active/Optimized"))
       {
            Write-Host("Paths are Active")
       }
       Else
       {
            Write-Host("Paths Not Active")
        }
    }
    Else
    {
         Write-Host("Does not Contains {0} Paths" -f $expectedPath)
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

MonitorStoragePath $dhcpserverip $username $password $expectedPath