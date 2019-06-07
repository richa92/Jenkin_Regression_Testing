Param([string]$dhcpserverip, [string]$username, [string]$password)

Function MACVerification($dhcpserverip, $username, $password)
{
    #Create a Remote session
    $session = GenerateWindowsSession $dhcpserverip $username $password

    Write-Host("MAC Verification")
    $out= Invoke-Command -Session $session -ScriptBlock{Get-NetAdapter | sort -Property name | select MacAddress}
    $out1 = $out | out-string
    return  $out1
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

MACVerification $dhcpserverip $username $password