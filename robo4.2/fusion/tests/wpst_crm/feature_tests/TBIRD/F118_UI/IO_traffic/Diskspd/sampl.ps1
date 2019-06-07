# This script runs IO traffic to/from mapped LUNs in the Windows OS using diskspd tool.
# Script needs to be copied and run from $Test_Path = "C:\Users\Administrator\Desktop7\Diskspd\
# which also contains the Diskspd tool.
# Script will stress your computer CPU and storage, be sure that no critical workload is running.


# Scanning LUNs and making it ready for use
Write-Host "list disk execution"
"rescan"|diskpart *> $null
Start-Sleep -s 5
$lisdisk = "list disk"|diskpart
Write-Host $listdisk
