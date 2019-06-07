#
##
###
####  Script used to build Daisy resources.
####  Can specify build to test and robot file to execute
####  This script will copy the results files to a folder named "Pass_Build_##_Results"
####  This script will Push Results to Rally (Make sure Test Folder and Test Set are correct)
####  This script invokes the listener for performance metrics
###
##
#

param([string]$build,
      [string]$robot,
      [switch]$help=$false
)

$DEBUG = $false

$IP = "16.114.208.62"
$DATA = "data_variables_ftc_CGW.py"

$LISTENER = "..\..\..\..\Tools\performance\listener.py"
$PERFORMANCEFILES = ("dbfile.txt", "keywordresults.txt", "logstash.txt", "log_message.txt")

$PUSHDATA2RALLY = ("..\..\..\..\Scripts\PushData2Rally.py", "\Python27\Scripts\PushData2Rally.py")
$GoodPushData2Rally = $False
$MINPUSHLINES = 313
foreach ($path in $PUSHDATA2RALLY) {
	write-host "`nVerify $path as valid PushData2Rally script."
	if (Test-Path $path) {
		$lines =(Get-Content $path).Length
		if ($lines -ge $MINPUSHLINES) {
			$GoodPushData2Rally = $True
			$PUSHDATA2RALLY = $path
			write-host "Path verified`n"
			break
		} else {
			write-host "Path found but line count incorrect. Expecting at least: $MINPUSHLINES, file contained: $lines."
		}
	} else {
		write-host "Path not found."
	}
}

IF (! $GoodPushData2Rally) {
	write-host "`nUnable to find valid PushData2Rally.p" -ForegroundColor Red
	$yorn = read-host "Do you wish to continue anyway? y or n"
	if ($yorn -eq 'n') {
		write-host "OK, will Exit by request."
		exit
	}
} else {
	write-host "`nWill use: $PUSHDATA2RALLY`n"
}

$TESTFOLDER = "1039"
$TESTSET = "240"

if ($help) {
	write-host "`n.\Execute_Pybot.ps1 -build build_number -robot robot_file"
	write-host "`nFor example:"
	write-host "`t.\Execute_Pybot.ps1 -build 49 -robot 03_OVF2458_0005_Create_EGs.robot`n"
	exit
}

#remove the performance files.  Some tests not tagged thus the performance files would be residual from a previous tests and not valid
write-host "`nRemoving any residual performance files."
foreach ($performanceFile in $PERFORMANCEFILES) {
	if (test-path $performanceFile) {
		write-host "Removing $performanceFile"
		rm $performanceFile
	}
}

# Determine build number and create results folder
if ([string]::IsNullOrEmpty($build)) {
	$passbuild = read-host "`nTesting Pass Build?"
} else {
	$passbuild = $build
}
$passbuild = "Pass_Build_$($passbuild)_Results"

# Determine robot file to execute
if ([string]::IsNullOrEmpty($robot)) {
	$robotFiles = Get-Childitem *.robot | sort-object

	write-host "`n`nIndex`tRobot File" -ForegroundColor magenta

	$index = 0

	$foreground_colors = ("yellow", "cyan")

	foreach ($robot_ in $robotFiles) {
		$color = $index % 2
		write-host "$index	 $($robot_.Name)" -Foregroundcolor $foreground_colors[$color]
		if ($color -eq 1) { write-host }
		$index++
	}

	$max_index = $index -1
	while($true) {
		$index = [int](read-host "`nWhich Index to you wish to execute? (0 - $($max_index))")
		write-host "Selected $index $max_index"
		if (($index -ge 0) -and ($index -le $max_index)) { break }
	}

	$robot = $robotFiles[$index].Name
	$base = $robotFiles[$index].BaseName
} else {
	$base = $robot.replace(".robot","")
}

write-host "`nWill execute: pybot --listener $($LISTENER)`n`t-v APPLIANCE_IP:$($IP) -V $($DATA)`n`t-o $($base)_output.xml -l $($base)_log.html -r $($base)_report.html`n`t$($robot)`n"

if ($GoodPushData2Rally) {	
	write-host "`nWill push to rally TestFolder: $($TESTFOLDER) and TestSet: $($TESTSET).`n"
}

write-host "Note:  If this is a new deploy, you must manually change the OV Administrator and SSH root passwords as defined in the data file." -Foregroundcolor yellow
write-host "(in time we should automate/enable those tasks)`n`n" -Foregroundcolor yellow
$ok = read-host "Continue: y or n?" 

if ($ok -ne "y") {
	write-host "OK, will Exit by request."
	exit
}

# Now create the folder for results.  Not need to create earlier as nothing was executed.
if (-not (test-path "$($passbuild)")) {
	write-host "`nCreating folder $($passbuild)"
	mkdir "$($passbuild)"
}

if (! $DEBUG) {
	write-host "`nHere we go." -ForegroundColor Green
	pybot --listener $LISTENER -v APPLIANCE_IP:$IP -V $DATA -o "$($base)_output.xml" -l "$($base)_log.html" -r "$($base)_report.html" $robot


	if ($GoodPushData2Rally) {	
		write-host "`nPush Results to Rally" -ForegroundColor Green
		python $PUSHDATA2RALLY -u 'fvt.tester@hpe.com' -p 'Insight812345' -w  'OneView' -pr 'FVT' -tf $TESTFOLDER -ts $TESTSET -ty "Regression" "$($base)_output.xml"
	} else {
		write-host "`nDid NOT Push Results to Rally, no viable PushData2Rally.py found." -ForegroundColor Yellow
	}
}

write-host "`nMove results and performance files" -ForegroundColor Green
$movefiles = $PERFORMANCEFILES + ("$($base)_output.xml", "$($base)_log.html", "$($base)_report.html") 

foreach ($movefile in $movefiles) {
	if (test-path $movefile) {
		if ($movefile.EndsWith('.txt')) {
			write-host "mv $movefile $($passbuild)\\$($base)_$($movefile)"
			mv $movefile "$($passbuild)\\$($base)_$($movefile)" -Force
		} else {
			write-host "mv $movefile $($passbuild)\\$($movefile)"
			mv $movefile "$($passbuild)\\$($movefile)" -Force
		}
	}
}

write-host "`n`n"

