#**************Script to configure Windows Servers using the HA file created for the setup*****************
# To Configure the Teams with LACP mode and to specify the LBA , use .\win_bond_config.ps1  -HA_filepath C:\Temp\HA_ipaddr.conf -Servername VCUQQQ000B -MODE LACP -LBA HyperVPort
#To Configure Teams as LACP , without any LBA specification (create Lacp teams with its default settings) , use .\win_bond_config.ps1 -HA_filepath C:\Temp\HA_ipaddr.conf -Servername VCUQQQ000B -MODE LACP
# To Configure Teams as Non-LACP and to specify the LBA , use .\win_bond_config.ps1 -HA_filepath C:\Temp\HA_ipaddr.conf -Servername VCUQQQ000B -LBA HyperVPort
# To Configure Teams as Non-LACP , without any LBA specification (create Non-Lacp teams with its default settings) , use .\win_bond_config.ps1 -HA_filepath C:\Temp\HA_ipaddr.conf -Servername VCUQQQ000B
####################**************************************************************###############################
param
(
    [string]$HA_filepath,
    [string]$Servername,
    [string]$MODE,
    [string]$LBA
)
$Load_Balancing_Algorithms = "Dynamic", "HyperVPort", "TransportPorts"
if ($LBA -ne "")
{
    for ($i=0; $i -ilt ($Load_Balancing_Algorithms.Count); $i++)
    {
        if ($LBA -eq $Load_Balancing_Algorithms[$i])
        {
            $Load_Balancing_Algorithm = $LBA
            Write-host "Load_Balancing_Algorithm is",  $Load_Balancing_Algorithm
        }
    }
    if ($Load_Balancing_Algorithm -eq $Null)
    {
        $Load_Balancing_Algorithm = "Dynamic"
        Write-host "The specified LBA is invalid so team is going to create with ",  $Load_Balancing_Algorithm
    }
}
else
{
    $Load_Balancing_Algorithm = "Dynamic"
    Write-host "Load_Balancing_Algorithm ",  $Load_Balancing_Algorithm
}
$content=select-string -path $HA_filepath -pattern $servername
if (($content -eq $Null) -or ($Servername.Length -ne 10 ))
{
    Write-host "Invalid HA file or Server Name"
    exit
}
else
{

    $mac_reg = "([0-9A-F]{2}[:]){5}([0-9A-F]{2})"
    $ip_reg = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    $vlan_reg= "[0-9X]{1,4}(.)(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
    $IP=@()
    $VLAN=@()
    $vlan_IP=@()
    $team_mac=@()
    $macaddress =@()
    $team_mac1=@()
    $team_mac2=@()
    $gateway=@()
    $j=0

    for ($i=0; $i -ilt ($content.Count); $i++)
    {
        # Filetering the MAC address*****************************************************
        [regex]::matches($content[$i], $mac_reg) | % {$team_mac += $_.value}
        $x=$team_mac.getvalue(0)
        $y=$team_mac.getvalue(1)
        $z=$x + "+" + $y
        $macaddress = $macaddress + $z
        $team_mac=@()
        $x=0
        $y=0
        $z=0
        #*********************************************************************************
        # Filetering the IP, VLAN and Gateway address*****************************************************
        [regex]::matches($content[$i], $vlan_reg) | % {$vlan_IP += $_.value}  # match the vlan and IP infromation from Server HA extracted content
        $VLAN_SPLIT= $vlan_IP[$i].Split(" ",2)
        $a = $VLAN_SPLIT.GetValue(0)
        $VLAN = $VLAN + $a  # Vlan Information
        $b = $VLAN_SPLIT.GetValue(1)
        $IP = $IP + $b # IP Information
        $y=$IP.GetValue($i)
        $g=$y.Split(".")
        $g=$g[0..2] -join '.'
        $gateway= $gateway +$g #  Gateway Information for the specific IP
        $VLAN_SPLIT=@()
    }

    #Team Interface creation**********************************************************
    $team_macaddress = $macaddress |select -Unique
    $team_macaddress = $team_macaddress.Split(" ")
    For ($i=0; $i -ilt ($team_macaddress.Count); $i++)
    {
        $team_macaddress_split = $team_macaddress[$i].Split("+",2)
        $Team_mac1 = $team_macaddress_split.getvalue(0)
        $Team_mac2 = $team_macaddress_split.getvalue(1)
        $Team_mac1 = $Team_mac1 -replace ':','-'
        $Team_mac2 = $Team_mac2 -replace ':','-'
        $team1_interface1=Get-NetAdapter | where {$_.MacAddress -eq $Team_mac1}
        $team1_interface2=Get-NetAdapter | where {$_.MacAddress -eq $Team_mac2}
        $interface1 = $team1_interface1.ifAlias
        $interface2 = $team1_interface2.ifAlias

        If ($MODE -eq "LACP")
        {
            Write-host "Creating Team in LACP mode"
            write-host New-NetLbfoTeam -Name "Team$i" -TeamMembers $interface1, $interface2  -TeamingMode LACP -LoadBalancingAlgorithm $Load_Balancing_Algorithm -Confirm: $false
            New-NetLbfoTeam -Name "Team$i" -TeamMembers $interface1, $interface2  -TeamingMode LACP  -LoadBalancingAlgorithm $Load_Balancing_Algorithm  -Confirm: $false

        }
        Else
        {
            Write-host "Creating Team in Non-LACP mode"
            write-host New-NetLbfoTeam -Name "Team$i" -TeamMembers $interface1, $interface2 -LoadBalancingAlgorithm $Load_Balancing_Algorithm -Confirm: $false
            New-NetLbfoTeam -Name "Team$i" -TeamMembers $interface1, $interface2 -LoadBalancingAlgorithm $Load_Balancing_Algorithm -Confirm: $false
        }
    }
    #********************************************************************************** 
    #Vlan interface ceration and IP mapping********************************************************************************
    for ($i=0; $i -ilt ($content.Count); $i++)
    {
        $vlan_value=0
        $ip_value=0
        $gateway_value=0
        $team_number = [array]::indexof($team_macaddress,$macaddress.getvalue($i))
        $vlan_value=($VLAN.getvalue($i))
        $ip_value=($IP.getvalue($i))
        $gateway_value=($gateway.GetValue($i))
        $Default_gateway=$gateway_value+".1"

        If ($vlan_value -ne "X")
        {
            write-host Add-NetLbfoTeamNIC Team$team_number $vlan_value -Confirm: $false
            Add-NetLbfoTeamNIC Team$team_number $vlan_value -Confirm: $false
            Start-Sleep -s 30   #30 sec Sleep to let the interface to add to the Team.
            $vlanInterfaceAlias="Team$team_number - VLAN $vlan_value"
            Write-host $vlanInterfaceAlias
            start-sleep 5  #5 Sec Sleep for interface to be available for IP assignment.
            write-host New-NetIPAddress -InterfaceAlias "$vlanInterfaceAlias" -AddressFamily IPv4 -IPAddress $ip_value -DefaultGateway $Default_gateway -PrefixLength 24
            New-NetIPAddress -InterfaceAlias "$vlanInterfaceAlias" -AddressFamily IPv4 -IPAddress $ip_value -DefaultGateway $Default_gateway -PrefixLength 24
        }
        Else
        {
            write-host New-NetIPAddress -InterfaceAlias Team$team_number  -AddressFamily IPv4 -IPAddress $ip_value -DefaultGateway $Default_gateway -PrefixLength 24
            New-NetIPAddress -InterfaceAlias Team$team_number  -AddressFamily IPv4 -IPAddress $ip_value -DefaultGateway $Default_gateway -PrefixLength 24
        }
    }
}