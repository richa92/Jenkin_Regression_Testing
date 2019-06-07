# This script runs IO traffic to/from mapped LUNs in the Windows OS using diskspd tool.
# Script needs to be copied and run from $Test_Path = "C:\Users\Administrator\Desktop7\Diskspd\
# which also contains the Diskspd tool.
# Script will stress your computer CPU and storage, be sure that no critical workload is running.


# verfying the wwn range
Get-Volume | Select-Object -Property DriveLetter,Size | ForEach-Object -Process {$_.Size = ($_.Size)/1024.0/1024.0/1024.0;$_} | Format-Table -Autosize