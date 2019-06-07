Param([string]$dhcpserverip, [string]$username, [string]$password, [string]$SetupMPIO= "True")

Function SetupMPIO($dhcpserverip, $username, $password)
{
    #Create a Remote session
    $session = GenerateWindowsSession $dhcpserverip $username $password

    If($SetupMPIO -eq $True)
    {
    $checkFeatureStatus = InstallWindowsMIPOFeature $session $dhcpserverip
    If($checkFeatureStatus.State -eq "Enabled")
    {
        Write-Host("Multi-Path IO is already Setup.. Adding the Hardware...3PARdataVV")
        $session = GenerateWindowsSession $dhcpserverip $username $password
        $mpclaim_list1=Invoke-Command -Session $session -ScriptBlock {mpclaim.exe -E}
        $mpclaim_list2=$mpclaim_list1 | select-string -pattern "3PARdataVV"
        $mpclaim_list3=$mpclaim_list2 | out-string
        If($mpclaim_list3.contains("NO"))
        {
            Invoke-Command -Session $session -ScriptBlock {mpclaim.exe -r -i -d "3PARdataVV"}
            DisconnectWindowsSession $session
            Write-Host("Rebooting the Host to add the Hardware device")
            start-sleep -s 350
        }
        else
        {
            Write-Host("3PARDataVV Hardware Already Added")
        }
    }
    else
    {
         Write-Host("Multi-Path IO Feature Could not be enabled")
    }
    }
    DisconnectWindowsSession $newsession
}

Function InstallWindowsMIPOFeature($session, $dhcpserverip)
{
    $checkFeatureInstallStatus= Invoke-Command -Session $session -ScriptBlock {Get-WindowsOptionalFeature -Online -FeatureName MultiPathIO}
    If($checkFeatureInstallStatus.State -eq "Disabled")
    {
        Write-Host("Enabling Feature : Multi Path IO...")
        Invoke-Command -Session $session -ScriptBlock {Enable-WindowsOptionalFeature -NoRestart -Online -FeatureName "MultiPathIO"}
        Invoke-Command -Session $session -ScriptBlock {param($dhcpserverip)Restart-Computer -ComputerName $dhcpserverip -Force} -ArgumentList $dhcpserverip
        Write-Host("Rebooting the Host for Feature to take effect")
        Start-Sleep -s 450
        $session = GenerateWindowsSession $dhcpserverip $username $password
        $checkFeatureInstallStatus=Invoke-Command -Session $session -ScriptBlock {Get-WindowsOptionalFeature -Online -FeatureName "MultiPathIO"}
        return $checkFeatureInstallStatus
     }
     elseif($checkFeatureInstallStatus.State -eq "EnablePending")
     {
        Write-Host("Enable Feature Pending: Multi Path IO...")
        Invoke-Command -Session $session -ScriptBlock {param($dhcpserverip)Restart-Computer -ComputerName $dhcpserverip -Force} -ArgumentList $dhcpserverip
        Write-Host("Rebooting the Host for Feature to take effect")
        Start-Sleep -s 260
        $session = GenerateWindowsSession $dhcpserverip $username $password
        $checkFeatureInstallStatus=Invoke-Command -Session $session -ScriptBlock {Get-WindowsOptionalFeature -Online -FeatureName "MultiPathIO"}
        return $checkFeatureInstallStatus
     }
    else
    {
        Write-Host("Multi Path IO Already Installed")
        $checkFeatureInstallStatus= Invoke-Command -Session $session -ScriptBlock {Get-WindowsOptionalFeature -Online -FeatureName "MultiPathIO"}
        return $checkFeatureInstallStatus
    }
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

SetupMPIO $dhcpserverip $username $password $SetupMPIO $expectedPath
