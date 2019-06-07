# This script runs IO traffic to/from mapped LUNs in the Windows OS using diskspd tool.
# Script needs to be copied and run from $Test_Path = "C:\Users\Administrator\Desktop7\Diskspd\
# which also contains the Diskspd tool.
# Script will stress your computer CPU and storage, be sure that no critical workload is running.


# Scanning LUNs and making it ready for use
"rescan"|diskpart *> $null
Start-Sleep -s 5
Get-Disk -FriendlyName *3PARdata*| ? IsOffline | Set-Disk -IsOffline:$false -erroraction 'silentlycontinue'
Get-Disk -FriendlyName *3PARdata*| ? IsReadOnly | Set-Disk -IsReadOnly:$false -erroraction 'silentlycontinue'
Start-Sleep -s 5

$diskcmd1 = Get-Disk -FriendlyName *3PARdata* | Get-Partition | select DriveLetter
$diskcmd2 = Get-Disk -FriendlyName *3PARdata* | select Number
foreach($out in $diskcmd1)
{
$letter = $out.DriveLetter
if($letter -eq "D")
{
$val = 1
break
}
}
if($val -ne 1)
{
foreach($disk in $diskcmd2)
{
$diskID = $disk.Number
Initialize-Disk $diskID
New-Partition -DiskNumber $diskID -DriveLetter D -UseMaximumSize
Format-Volume -FileSystem NTFS -DriveLetter D -Confirm:$false
break
}
}

# Clear screen
Clear

# Disk to test
$Disk = “D:”
$Test_Path = "C:\Users\Administrator\Desktop7\Diskspd\"

# Use 1 thread / core
#$Thread = “-t”+(Get-WmiObject win32_processor).NumberofCores
$Thread = “-t6”

# Change this time in seconds for each run
$Time = “-d60”

# Outstanding IOs
# Should be 2 times the number of disks in the RAID
# Between  8 and 16 is generally fine
$OutstandingIO = “-o16”

$Capacity = 1

$CapacityParameter = “-c”+$Capacity+”G”

# Check Disk exits
# Disk preparation
# Delete testfile.dat if it exists
# Add the headers to the output file
If (Test-Path D:)
	{
		$output_file = “$(get-date -f MM-dd-yyyy-hhmm)_output.txt”
#		Clear-Content $output_file
		“Drive D: exists!”
		$IsDir = test-path -path “$Disk\TestDiskSpd”
		if ($IsDir -like “False”)
			{
				new-item -itemtype directory -path “$Disk\TestDiskSpd\”
			}
		$Cleaning = test-path -path “$Disk\TestDiskSpd\testfile.dat”

		if ($Cleaning -eq “True”)
			{
#				“Removing current testfile.dat from drive”

				remove-item $Disk\TestDiskSpd\testfile.dat
			}
	}
else
	{
		Write-Host "Drive D: Not found mapped!"
		exit
	}

# Number of tests
$NumberOfTests = 1

# Begin Test
# We will run the tests with 8K blocks
(8) | % { 
		$BlockParameter = (“-b”+$_+”K”)
		$Blocks = (“Blocks “+$_+”K”)

		# We will do Read tests
		$WriteParameter = “-w”+0
		$IO = “Read”
		# We will do random IO tests
		$AccessParameter = “-“+“r”
		$type = “Random”
		#Print command and output file
		“.\diskspd.exe $CapacityPArameter $Time $AccessParameter $WriteParameter $Thread $OutstandingIO $BlockParameter -h -L $Disk\TestDiskSpd\testfile.dat”
		“Test Output file is :$output_file”
		
		write-host “Starting IO Test”
		(1) | % {

					# The test itself (finally !!)
	
					$result = .\diskspd.exe $CapacityParameter $Time $AccessParameter $WriteParameter $Thread $OutstandingIO $BlockParameter -h -L $Disk\TestDiskSpd\testfile.dat

					# Now we will break the very verbose output of DiskSpd in a single line with the most important values

					foreach ($line in $result) {
												if ($line -like “total:*”) 
												{ $total=$line; break }
												}
					foreach ($line in $result) {
												if ($line -like “avg.*”) 
												{ $avg=$line; break } 
												}
					foreach ($line in $result) {
												if ($line -like “actual*”) 
												{ $actual=$line; break } 
												}
					$testtime = $actual.Split(“:”)[1].Trim()
					$mbps = $total.Split(“|”)[2].Trim()
					$iops = $total.Split(“|”)[3].Trim()
					$latency = $total.Split(“|”)[4].Trim()
					$cpu = $avg.Split(“|”)[1].Trim()

					# We output the values to the text file
					“.\diskspd.exe $CapacityPArameter $Time $AccessParameter $WriteParameter $Thread $OutstandingIO $BlockParameter -h -L $Disk\TestDiskSpd\testfile.dat”  >> ./$output_file
					“Test $Disk, $IO, $type, $Blocks, $iops iops, $mbps MB/sec, $testtime, $latency ms”  >> ./$output_file

					# We output a verbose format on screen
					“Test  $Disk, $IO, $type, $Blocks, $iops iops, $mbps MB/sec, $testtime, $latency ms, $cpu CPU”
				}
		}




