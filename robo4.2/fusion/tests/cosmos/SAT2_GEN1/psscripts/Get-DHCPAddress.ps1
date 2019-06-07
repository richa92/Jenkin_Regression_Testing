Param([string]$mac, [string]$dhcpserverip, [string]$username, [string]$password, [string]$scope)

Function GetIPFromDHCP($mac, $dhcpserverip, $username, $password, $scope)
{
    #  Connect to DHCP server
    $session = ConnectDHCP $dhcpserverip $username $password
    #  Replace mac : to  - as db will return 'AC:16:2D:B9:23:B8' and dhcp retruns as ac-16-2d-b9-23-b8'
    $mac = $mac -replace ":", "-"
    $mac = $mac.ToLower()

    $leaseobj = Invoke-Command -Session $session -ScriptBlock {param($scope, $mac) Get-DHCPServerv4Lease -ScopeID $scope -ClientId $mac} -ArgumentList $scope, $mac
    $ipaddress = $leaseobj.IPAddress
    # Remove the CimSession
    DisconnectDHCP($session)
    return $ipaddress
}

Function ConnectDHCP($dhcpserverip, $username, $passwd)
{
    #  Add DHCP cmdlets in PS
    #  Add-WindowsFeature -Name DHCP
    #  DHCP server should be enable to communicate with remote server
    #  Enable automation vm to communicate with remote server
    #  Enable-PSRemoting -Force
    #  Set-Item "wsman:\localhost\client\trustedhosts" $dhcpserverip -concatenate -force
    $password = ConvertTo-SecureString $passwd -AsPlainText -Force
    $cred= New-Object System.Management.Automation.PSCredential ($username, $password )
    $session = New-PSSession -ComputerName $dhcpserverip -Credential $cred
    return $session
}

Function DisconnectDHCP($session)
{
    #  remove powershell session
    Remove-PSSession $session
}

GetIPFromDHCP $mac $dhcpserverip $username $password $scope