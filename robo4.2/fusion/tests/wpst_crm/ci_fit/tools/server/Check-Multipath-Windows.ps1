####################################
# This script to check multipath in windows servers
#
# USAGE: .\check-Multipath-windows.ps1
####################################

$array = @()
$a = mpclaim -s -d
$words = ([regex]::matches($a, "Disk\d+", "IgnoreCase") | %{$_.value})
Write-host "Selected MPIO Disks :" $words -Separator ' '
Foreach ($i in $words)
{
    $words1 = ([regex]::matches($i, "\d+", "IgnoreCase") | %{$_.value})
    Write-host "Selected MPIO Disk Number is :" $words1 -Separator ' '
    $b = mpclaim -s -d $words1
    $match_out1 = ([regex]::matches($b, "MPIO\s$i\:\s+\d+\d+\s+Paths", "IgnoreCase") | %{$_.value})
    Write-Output $match_out1
    $match_out3 = $match_out1 -match '\w+\s\w+\:\s(.*)\s.*'
    Write-Output $match_out3
    Write-Output $Matches[1]
    $array += $Matches[1]

}
$x = 0
$array | Foreach {$x += $_}
$x
Write-host "Total Number of Paths available in the blade is : " $x -Separator ''