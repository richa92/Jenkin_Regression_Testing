Param([string]$dhcpserverip, [string]$username, [string]$password, [string]$EthernetInterface, [String]$TeamName, [string]$CreateRemove)

Function SetupNICTeam($dhcpserverip, $username, $password, $EthernetInterface, $TeamName, $CreateRemove)
{
    #Create a Remote session
    # Please Ensure that the user know in prior VLAN ID and Interface Name Associated with the VLAN ID
    # $EthernetInterface eg: "Ethernet1,Ethernet2" or "Ethernet*"
    $session = GenerateWindowsSession $dhcpserverip $username $password
    Write-Host($EthernetInterface)
    If($CreateRemove -eq "c")
    {
    $check_NicTeam=Invoke-Command -Session $session -ScriptBlock {Get-NetLbfoTeam}
    If([string]::IsNullOrEmpty($check_NicTeam))
    {
        Write-Host("Creating Nic Teaming..")
        $temp=Invoke-Command -Session $session -ScriptBlock {param($EthernetInterface,$TeamName) New-NetLbfoTeam -Name $TeamName -TeamMembers $EthernetInterface -TeamingMode LACP -Confirm:$false} -ArgumentList $EthernetInterface,$TeamName
        $check_NicTeam=Invoke-Command -Session $session -ScriptBlock {Get-NetLbfoTeam}
        Start-Sleep -s 10
        If($check_NicTeam.Name -eq $TeamName)
        {
            Write-Host("Nic Teaming Successfull")
            Write-Host("Teaming Mode is LACP")
        }
        Else
        {
            Write-Host("Nic Teaming Failed")
        }
    }
    Else
    {
        Write-Host("Nic Teaming Already Exists!!!")
    }
    # Remove the CimSession
    $PSComputerName=GetIPFromNICTeam($TeamName)
    DisconnectDHCP($session)
    return $PSComputerName
    }
    ElseIf($CreateRemove -eq "d")
    {
        DeleteNicTeam $session $TeamName
        DisconnectDHCP($session)
    }
    Else
    {
        Write-Host("Not Valid option c-create NIC Team or d-Delete NIC Team")
    }
}

Function GenerateWindowsSession($dhcpserverip, $username, $password)
{

    Write-Host($dhcpserverip)
    # we need to have dhcp module copy at dhcp server from \\jdata.us.rdlabs.hpecorp.net\Cosmos\Automation\Tools\Microsoft.DHCP.PowerShell.Admin.psm1
    # DHCP server should be enable to communicate with remote server

    #Enable automation vm to communicate with remote server
    #Enable-PSRemoting -Force
    #Set-Item "wsman:\localhost\client\trustedhosts" $dhcpserverip -concatenate -force

    $password = ConvertTo-SecureString $password -AsPlainText -Force
    $cred= New-Object System.Management.Automation.PSCredential ($username, $password )
    $session = New-PSSession -ComputerName $dhcpserverip -Credential $cred

    return $session
}


Function DisconnectDHCP($session)
{
    # remove powershell session
    Remove-PSSession $session
}

Function GetIPFromNICTeam($TeamName)
{
    write-Host("Querying IP Address of the NIC Team..")

    $Quey_Details=Invoke-Command -Session $session -ScriptBlock { param($TeamName)Get-NetIPConfiguration -InterfaceAlias $TeamName} -ArgumentList $TeamName
    $Query_IP=$Quey_Details.IPv4Address
    return $Query_IP.IPAddress
}

SetupNICTeam $dhcpserverip $username $password $EthernetInterface $TeamName $CreateRemove