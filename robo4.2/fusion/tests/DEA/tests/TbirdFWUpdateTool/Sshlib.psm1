# Quick and untested copy of what you need:
 
# Import-Module ".\Posh-SSH"
Import-Module "C:\Users\Administrator\git\fusion\tests\DEA\tests\TbirdFWUpdateTool\Posh-SSH"
#Import-Module ".\Renci.Sshnet.dll"


[int]$port = 22
<# Library 
Synopsis: 
	connect to CIM using ssh, remove any existing trusted host.

Examples: 
	Connect-ssh -tbhost [TBhost] -user [username] -password [password] -timeout [100]
Parameters: 
	tbhost: Required: command to run on the appliance.
	username: Optional: default root.
	password: Optional: default hpvse1.
    timeout: Optional: default 100 seconds.
Dependencies: 
	
Notes: 
	
#> 

Function Connect-ssh{
param(
            [parameter(Mandatory = $true, HelpMessage = "Enter OV ip or fqdn host name -",Position=0)]
            [ValidateNotNullOrEmpty()]
            [string]$host, #"csitb10-ov.rsn.rdlabs.hpecorp.net" 
            [parameter(Mandatory = $false, HelpMessage = "Enter CIM username -",Position=1)]
            [string]$username = "root",
            [parameter(Mandatory = $false, HelpMessage = "Enter CIM password -",Position=2)]
            $Password="hpvse1",
            [parameter(Mandatory = $false, HelpMessage = "Enter timeout -",Position=3)]
            [int]$timeout=60)
Process{
    $password = ConvertTo-SecureString -String $password -AsPlainText -Force 
    $credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $username, $password
    
    #Remove host if it is already trusted
    $hostlists = (Get-SSHTrustedHost).SSHHOST
    foreach($list in $hostlists){
        if($list -eq $host){
            Remove-SSHTrustedHost -SSHHost $list
            }
        }
    
    # Create SSH Session
    $ssh = New-SSHSession -ComputerName $host -Credential $credential -ConnectionTimeout $timeout -AcceptKey  
}

End{
    Return $ssh
}

}
<# Library 
Synopsis: 
	ssh to the CIM, collect health status, run fru update, run fru update_em on standby EM and collect the health data.

Examples: 
    Invoke-fru -tbhost [TBhost] -fruFileName "hpeMgmtUtil_v2.6.13_20160226_internal.tar" -iLOusername "Administrator" -iLOpassword "XXXXX" -ilofwUpdate $true -enclType 2 -encLocation 2
Parameters: 
	tbhost: Required: command to run on the appliance.
	username: Optional: default root.
	password: Optional: default hpvse1.
    regx: Optional: default null.
    logFileName: Optional: default null.
    timeout: Optional: default 100.
    fruFileName: Required: FRU toll file name.
    iLoUserName: Required: server iLO user name.
    iLOPassword: Required:  server iLO password.
    enclType: Required: 1 for DP Enclosure and  2 for VP Enclosure
    enclLocation: Optional: 2, 2 for local and 1 for remote enclosure
    ilofwUpdate: Required: $true|$false, if we want to update iLO to debug provide $true otherwise $false.
Dependencies: 
	
Notes: 
	
#> 
Function Invoke-fru
{
param(
            [parameter(Mandatory = $true, HelpMessage = "Enter OV ip or fqdn host name -",Position=0)]
            [ValidateNotNullOrEmpty()]
            [string]$tbhost, #"csitb10-ov.rsn.rdlabs.hpecorp.net" 
            [parameter(Mandatory = $false, HelpMessage = "Enter CIM username -",Position=1)]
            [string]$username = "root",
            [parameter(Mandatory = $false, HelpMessage = "Enter CIM password -",Position=2)]
            $password = "hpvse1",
            [parameter(Mandatory = $false, HelpMessage = "Expected regular expressopn to perform action[.*Please enter 1 or 2:]",Position=3)]
            [Regex]$regx,
            [parameter(Mandatory = $false, HelpMessage = "Enter FRU tool log filename -",Position=4)]
            [string]$logFileName=$null,
            [parameter(Mandatory = $false, HelpMessage = "Enter FRU utilitty timeout -",Position=5)]
            [int]$timeout=100,
            [parameter(Mandatory = $true, HelpMessage = "FRU tool file name[hpeMgmtUtil_v2.6.....]",Position=6)]
            [string]$fruFileName,
            [parameter(Mandatory = $true, HelpMessage = "Target blade iLO username",Position=8)]
            [string]$iLOusername,
            [parameter(Mandatory = $true, HelpMessage = "Target blade iLO password",Position=9)]
            [string]$iLOpassword,
            [parameter(Mandatory = $true, HelpMessage = "Please enter enclosure type 1 or 2 [ 1. DP Enclosure; 2. VP Enclosure]",Position=10)]
            $enclType,
            [parameter(Mandatory = $false, HelpMessage = "Enclosre location [local = 2, remote = 1]",Position=11)]
            $encLocation = 2,
            [parameter(Mandatory = $true, HelpMessage = "Enter update iLO firmware True/False -")]
			$ilofwUpdate,
            [parameter(Mandatory = $false, HelpMessage = "Provide input to continue on error [True/False] -")]
			[bool]$halt = $false
            )
BEGIN {
    #Get ssh connection
    $ssh = Connect-ssh -Host $tbhost -UserName $username -Password $password
    # Get the log file if it has not been provided
    if(!$logFileName){
    $logFileName = Get-Date -Format s | foreach {$_ -replace ":", "."}
    $logFileName = $logFileName + ".log"
    }

    if(!$regx){
    $regx = [Regex]".*Please enter 1 or 2:"
    }

    # initialize multi action array
    $matrix = @((".*Please enter target blade iLO Username", $iLOusername),
        (".*Please enter target blade iLO Password",$iLOpassword),
        (".*Please enter 1 or 2 \[ 1\. DP Enclosure; 2\. VP Enclosure\]",$enclType),
        (".*==>Please enter 1 or 2:",$encLocation))
    }
PROCESS {

    #untar hpeMgmtUtil....tar
    Expand-file -ssh $ssh -FileName $fruFileName

    #update fru config.py to update iLO firmware update
    Update-file -ssh $ssh -ilofwUpdate $ilofwUpdate
    <#
    # Get the Inventory
    $commands = "cd /tmp/hpeMgmtUtil;python3.4 hpeMgmtUtilCli.py diags get_fru_inventory"
    $iLogFileName = "FruInventory_" + $logfileName
    $expectedRegex =  ".*POWER SUPPLIES.*#"
    Invoke-FruCommands -ssh $ssh -commands $commands  -logfileName $iLogFileName -encType $encLocation -regx $regx -timeout $timeout -expectedRegex $expectedRegex
    #>
    
    # Get the Health summary
    $commands = "cd /tmp/hpeMgmtUtil;python3.4 hpeMgmtUtilCli.py diags show_health_summary"
    $sLogFileName = "HealthSummary_" + $logfileName
    #$expectedRegex = ".*Health entities found.*#"
    $expectedStr = "Health entities found"
    #$expectedRegex = ".*\]#"
    #".*hpeMgmtUtil\]#"
    Invoke-FruCommands -ssh $ssh -commands $commands -logfileName $sLogFileName -encType $encLocation -regx $regx -timeout $timeout -expectedStr $expectedStr -halt $halt
    
    # Run FRU update_all
    $commands = "cd /tmp/hpeMgmtUtil;python3.4 hpeMgmtUtilCli.py fru update_all"
    $FRULogFileName = "FRUALL_" + $logfileName
    #$expectedRegex = ".*END OF FRUs UPDATE PROCESS.*#"
    $expectedStr = "END OF FRUs UPDATE PROCESS"
    $timeout = $timeout*5
    Invoke-FruCommands -ssh $ssh -commands $commands -logfileName $FRULogFileName -encType $encLocation -regx $regx -timeout $timeout -multiAction $matrix -expectedStr $expectedStr -halt $halt
    
    $versionDate = get-FRUVersionDate -fruFileName $fruFileName
    #hpeMgmtUtil_v2.6.15_20160324_internal.tar] => 20160324
    # Compare the version date to make sure to update EM fru explicitly
    if($versionDate -lt 20160324){
        # get the primary enclosure serial number
        $enclosureSN = get-EnclosureSN -ssh $ssh 
        # get the EM session
        $emSession = get-EMSession -ssh $ssh -encSerialNumber $enclosureSN
        # Get the floating EM IP
        $floatingEMIP = get-FloatingEMIP -ssh $ssh -encSerialNumber $enclosureSN
        # Reset the Active EM to swith EM from standby to active
        $activeEM = get-ActiveEM -ssh $ssh -emSession $emSession -emIP $floatingEMIP
        Reset-ActiveEM -ssh $ssh -emSession $emSession -emIP $floatingEMIP -activeEM $activeEM

        # Sleep for 60 seconds to activate standby EM
        Start-Sleep -s 120
        write-host "Sleeping for 120 seconds to make sure Standby EM becomes active"

        # update em_fru
        $ssh = Connect-ssh -Host $tbhost -UserName $username -Password $password
        # get the primary enclosure serial number
        $enclosureSN = get-EnclosureSN -ssh $ssh 
        # get the EM session
        $emSession = get-EMSession -ssh $ssh -encSerialNumber $enclosureSN
        # Get the floating EM IP
        $floatingEMIP = get-FloatingEMIP -ssh $ssh -encSerialNumber $enclosureSN
        # Reset the Active EM to swith EM from standby to active
        $activeEM = get-ActiveEM -ssh $ssh -emSession $emSession -emIP $floatingEMIP

        # initialize matrix for fru em_update
        $matrix = @((".*==>Please enter 1 or 2:",$encLocation),
         (".*==>Please enter 1 or 2:",$enclType),
        (".*==>Please enter 1 or 2:",1),#[ 1. Merge FRU; 2. Create Fresh FRU]
        #(".*1 Active EM   2. Standby EM     :",1),
        (".*==>Please enter 1 or 2:",1),#
        (".*Please enter EM number:",$activeEM))
    
        # Run fru em_update
        $commands = "cd /tmp/hpeMgmtUtil;python3.4 hpeMgmtUtilCli.py fru update_em"
        $FRULogFileName = "FRU_Em_Update_" + $logfileName
        #$expectedRegex = ".*Update Active EM bay FRU Success.*#"
        $expectedStr = "Update Active EM bay FRU Success"
        Invoke-FruCommands -ssh $ssh -commands $commands -logfileName $FRULogFileName -encType $encLocation -regx $regx -timeout $timeout -multiAction $matrix -expectedStr $expectedStr -halt $halt
   }
    # Get the Health summary again
    $commands = "cd /tmp/hpeMgmtUtil;python3.4 hpeMgmtUtilCli.py diags show_health_summary"
    $sLogFileName = "HealthSummary_After_" + $logfileName
    #$expectedRegex = ".*Health entities found.*#"
    $expectedStr = "Health entities found"
    Invoke-FruCommands -ssh $ssh -commands $commands -logfileName $sLogFileName -encType $encLocation -regx $regx -timeout $timeout -expectedStr $expectedStr -halt $halt
   
    }
END {
    Remove-SSHSession -SSHSession $ssh
    Remove-variable ssh
    }
}

<# Library 
Synopsis: 
	ssh to the CIM, collect remote enclosure health status, run fru update on remote enclosure, run fru update_em on standby EM of remote enclosure and collect the health data remote enclosure.

Examples: 
    Invoke-Remotefru -tbhost [TBhost] -fruFileName "hpeMgmtUtil_v2.6.13_20160226_internal.tar" -iLOusername "Administrator" -iLOpassword "XXXXX" -ilofwUpdate $true -enclType 2 -encLocation 1
Parameters: 
	tbhost: Required: command to run on the appliance.
	username: Optional: default root.
	password: Optional: default hpvse1.
    regx: Optional: default null.
    logFileName: Optional: default null.
    timeout: Optional: default 100.
    fruFileName: Required: FRU toll file name.
    iLoUserName: Required: server iLO user name.
    iLOPassword: Required:  server iLO password.
    enclType: Required: 1 for DP Enclosure and  2 for VP Enclosure
    enclLocation: Optional: 1, 2 for local and 1 for remote enclosure
    ilofwUpdate: Required: $true|$false, if we want to update iLO to debug provide $true otherwise $false.
Dependencies: 
	
Notes: 
	
#>  
Function Invoke-Remotefru
{
param(
            [parameter(Mandatory = $true, HelpMessage = "Enter OV ip or fqdn host name -",Position=0)]
            [ValidateNotNullOrEmpty()]
            [string]$tbhost, #"csitb10-ov.rsn.rdlabs.hpecorp.net" 
            [parameter(Mandatory = $false, HelpMessage = "Enter CIM username -",Position=1)]
            [string]$username = "root",
            [parameter(Mandatory = $false, HelpMessage = "Enter CIM password -",Position=2)]
            $password = "hpvse1",
            [parameter(Mandatory = $true, HelpMessage = "Enclosure sn\name -",Position=3)]
            $enclosureSN,
            [parameter(Mandatory = $false, HelpMessage = "Expected regular expressopn to perform action[.*Please enter 1 or 2:]",Position=4)]
            [Regex]$regx,
            [parameter(Mandatory = $false, HelpMessage = "Enter FRU tool log filename -",Position=5)]
            [string]$logFileName=$null,
            [parameter(Mandatory = $false, HelpMessage = "Enter FRU utilitty timeout -",Position=6)]
            [int]$timeout=100,
            [parameter(Mandatory = $true, HelpMessage = "FRU tool file name[hpeMgmtUtil_v2.6.....]",Position=7)]
            $fruFileName,
            [parameter(Mandatory = $true, HelpMessage = "Target blade iLO username",Position=8)]
            [string]$iLOusername,
            [parameter(Mandatory = $true, HelpMessage = "Target blade iLO password",Position=9)]
            [string]$iLOpassword,
            [parameter(Mandatory = $true, HelpMessage = "Please enter enclosure type 1 or 2 [ 1. DP Enclosure; 2. VP Enclosure]",Position=10)]
            $enclType=2,
            [parameter(Mandatory = $false, HelpMessage = "Enclosre location [local = 2, remote = 1]",Position=11)]
            $encLocation = 1,
            [parameter(Mandatory = $true, HelpMessage = "Enter update iLO firmware True/False -")]
			$ilofwUpdate,
            [parameter(Mandatory = $false, HelpMessage = "Provide input to continue on error [True/False] -")]
			[bool]$halt = $false
            )
BEGIN {
   
    #Get ssh connection
    $ssh = Connect-ssh -Host $tbhost -UserName $username -Password $password
    # Get the log file if it has not been provided
    if(!$logFileName){
    $logFileName = Get-Date -Format s | foreach {$_ -replace ":", "."}
    $logFileName = $enclosureSN + $logFileName + ".log"
    }

    if(!$regx){
    $regx = [Regex]".*Please enter 1 or 2:"
    }

    # initialize multi action array
    <#
    $matrix = @((".*Please enter target blade iLO Username", $iLOusername),
        (".*Please enter target blade iLO Password",$iLOpassword),
        (".*Please enter 1 or 2 \[ 1\. DP Enclosure; 2\. VP Enclosure\]",$enclType),
        (".*==>Please enter 1 or 2:",$encLocation))
    #>
    $enclosureIP = get-EnclosureIP -ssh $ssh -encSerialNumber $enclosureSN
    $remoteEnclPassword = get-EnclosurePassword -ssh $ssh -encSerialNumber $enclosureSN
    $base_matrix = @((".*==>Please enter 1 or 2:",$encLocation),
        (".*Please enter remote EM I.P address:",$enclosureIP),
        (".*Please enter network interface:","bond0"),
        (".*Enter the password :",$remoteEnclPassword),
        (".*Enter the enclosure serial number you wish to interact with:",$enclosureSN))
    }
PROCESS {

    #untar hpeMgmtUtil....tar
    Expand-file -ssh $ssh -FileName $fruFileName

    #update fru config.py to update iLO firmware update
    Update-file -ssh $ssh -ilofwUpdate $ilofwUpdate
    <#
    # Get the Remote Inventory
    $commands = "cd /tmp/hpeMgmtUtil;python3.4 hpeMgmtUtilCli.py diags get_fru_inventory"
    $iLogFileName = "FruInventory_Remote_" + $logfileName
    $expectedRegex =  ".*POWER SUPPLIES.*#"
    Invoke-FruCommands -ssh $ssh -commands $commands  -logfileName $iLogFileName -encType $encLocation -regx $regx -timeout $timeout -multiAction $base_matrix -expectedRegex $expectedRegex
    #>
	
    # Get the Remote Enclosure Health summary
    $commands = "cd /tmp/hpeMgmtUtil;python3.4 hpeMgmtUtilCli.py diags show_health_summary"
    $sLogFileName = "HealthSummary_Remote_" + $logfileName
    #$expectedRegex = ".*Health entities found.*#"
    $expectedStr = "Health entities found"
    Invoke-FruCommands -ssh $ssh -commands $commands -logfileName $sLogFileName -encType $encLocation -regx $regx -timeout $timeout -multiAction $base_matrix -expectedStr $expectedStr -halt $halt

    # Run Remote FRU update_all
    $fru_all_base_matrix = @((".*Please enter target blade iLO Username", $iLOusername),
        (".*Please enter target blade iLO Password",$iLOpassword),
        (".*Please enter 1 or 2 \[ 1\. DP Enclosure; 2\. VP Enclosure\]",$enclType))

    $fru_all_matrix = $fru_all_base_matrix + $base_matrix
    $commands = "cd /tmp/hpeMgmtUtil;python3.4 hpeMgmtUtilCli.py fru update_all"
    $FRULogFileName = "FRUALL_Remote_" + $logfileName
    #$expectedRegex = ".*END OF FRUs UPDATE PROCESS.*#"
    $expectedStr = "END OF FRUs UPDATE PROCESS"
    $timeout = $timeout*5
    Invoke-FruCommands -ssh $ssh -commands $commands -logfileName $FRULogFileName -encType $encLocation -regx $regx -timeout $timeout -multiAction $fru_all_matrix -expectedStr $expectedStr -halt $halt
    
    $versionDate = get-FRUVersionDate -fruFileName $fruFileName
    #hpeMgmtUtil_v2.6.15_20160324_internal.tar] => 20160324
    # Compare the version date to make sure to update EM fru explicitly
    if($versionDate -lt 20160324){
    # get the EM session
    $emSession = get-EMSession -ssh $ssh -encSerialNumber $enclosureSN
    # Get the floating EM IP
    $floatingEMIP = get-FloatingEMIP -ssh $ssh -encSerialNumber $enclosureSN
    # Reset the Active EM to swith EM from standby to active
    $activeEM = get-ActiveEM -ssh $ssh -emSession $emSession -emIP $floatingEMIP
    Reset-ActiveEM -ssh $ssh -emSession $emSession -emIP $floatingEMIP -activeEM $activeEM

    # Sleep for 60 seconds to activate standby EM
    Start-Sleep -s 120
    write-host "Sleeping for 120 seconds to make sure Standby EM becomes active"

    # update em_fru
    $ssh = Connect-ssh -Host $tbhost -UserName $username -Password $password
    # get the EM session
    $emSession = get-EMSession -ssh $ssh -encSerialNumber $enclosureSN
    # Get the floating EM IP
    $floatingEMIP = get-FloatingEMIP -ssh $ssh -encSerialNumber $enclosureSN
    # Reset the Active EM to swith EM from standby to active
    $activeEM = get-ActiveEM -ssh $ssh -emSession $emSession -emIP $floatingEMIP
    
    # initialize matrix for fru em_update
    $em_matrix = @((".*==>Please enter 1 or 2:",$encLocation),
         (".*==>Please enter 1 or 2:",$enclType),
        (".*==>Please enter 1 or 2:",1),
        (".*Please enter EM number:",$activeEM),
        (".*Please enter remote EM I.P address:",$enclosureIP),
        (".*Please enter network interface:","bond0"),
        (".*Enter the password :",$remoteEnclPassword),
        (".*Enter the enclosure serial number you wish to interact with:",$enclosureSN))
  
    # Run Remote fru em_update
    $commands = "cd /tmp/hpeMgmtUtil;python3.4 hpeMgmtUtilCli.py fru update_em"
    $FRULogFileName = "FRU_Em_Update_Remote_" + $logfileName
    #$expectedRegex = ".*Update Active EM bay FRU Success.*#"
    $expectedStr = "Update Active EM bay FRU Success"
    Invoke-FruCommands -ssh $ssh -commands $commands -logfileName $FRULogFileName -encType $encLocation -regx $regx -timeout $timeout -multiAction $em_matrix -expectedStr $expectedStr -halt $halt
    }

    # Get the Remote Enclosure Health summary
    $commands = "cd /tmp/hpeMgmtUtil;python3.4 hpeMgmtUtilCli.py diags show_health_summary"
    $sLogFileName = "HealthSummary_After_Remote_" + $logfileName
    #$expectedRegex = ".*Health entities found.*#"
    $expectedStr = "Health entities found"
    Invoke-FruCommands -ssh $ssh -commands $commands -logfileName $sLogFileName -encType $encLocation -regx $regx -timeout $timeout -multiAction $base_matrix -expectedStr $expectedStr -halt $halt

    }
END {
    Remove-SSHSession -SSHSession $ssh
    Remove-variable ssh
    }
}

<# Library 
Synopsis: 
	get the SSHShellStream using existing ssh connection of the CIM, run command if expected condition meet.

Examples: 
    Invoke-FruCommands -ssh [ssh] -commands "python3.4 /tmp/hpeMgmtUtil/hpeMgmtUtilCli.py diags show_health_summary" -encType [1|2] -logFileName [LogFileName] -timeout [100]
Parameters: 
	ssh: Required: ssh connection.
	commands: Required: "python3.4 /tmp/hpeMgmtUtil/hpeMgmtUtilCli.py diags show_health_summary".
    enclType: Required: 1 for DP Enclosure and  2 for VP Enclosure.
    regx: Optional: default null.
    logFileName: Optional: default null.
    timeout: Optional: default 100.
    multiAction:Optional: $false
    expectedRegex:Optional: expected regex string
Dependencies: 
	
Notes: 
	
#>  

Function Invoke-FruCommands{
param(      [parameter(Mandatory = $true, HelpMessage = "SSH session", Position=0)]
            $ssh,
			[parameter(Mandatory = $true, HelpMessage = "Enter commands to be run on CIM [python3.4 hpeMgmtUtilCli.py diags show_health_summary ....] -", Position=1)]
            [string]$commands = "python3.4 /tmp/hpeMgmtUtil/hpeMgmtUtilCli.py diags show_health_summary",
            [parameter(Mandatory = $false, HelpMessage = "Regular expression to be expected [Remote = 1, Local = 2]",Position=2)]
            [string]$encType = 2,
            [parameter(Mandatory = $false, HelpMessage = "Provide Enclosure type[.*Please enter 1 or 2:]",Position=3)]
            [Regex]$regx,
            [parameter(Mandatory = $true, HelpMessage = "Enter FRU tool log filename -",Position=4)]
            [string]$logFileName,
            [parameter(Mandatory = $false, HelpMessage = "Enter FRU utilitty timeout -",Position=5)]
            [int]$timeout=10,
            [parameter(Mandatory = $false, HelpMessage = "Multi action data if we need any -",Position=6)]
            $multiAction,
            [parameter(Mandatory = $false, HelpMessage = "Expected result string  -",Position=7)]
            $expectedStr,
            [parameter(Mandatory = $false, HelpMessage = "Privide input to continue on error [True/False] -")]
            [bool]$halt = $false
            )
Begin{
    $SSHStream = New-SSHShellStream -Index $ssh.SessionId
    #wait for SSH command prompt
    $prompt = wait-ForCommandPrompt -SSHStream $SSHStream -stringToMatch "]#" -timeout 60
    
    }
Process{
    Write-Host "Running command [$commands]"
    

    if($multiAction){
        $ret = Invoke-SSHStreamExpectAction -ShellStream $SSHStream -Command $commands -Action $multiAction[0][1] -ExpectRegex $multiAction[0][0] -TimeOut 10
        Write-Verbose -Message "Executing command $($Commands)."
        for($index=1; $index -lt $multiAction.count; $index++){
             $found = $SSHStream.Expect([Regex]$multiAction[$index][0], (New-TimeSpan -Seconds 10))
                
            if ($found -ne $null){
                Write-Verbose -Message "Expected String: $($multiAction[$index][0]), action: $($multiAction[$index][1])."
                $action = $multiAction[$index][1]
                $SSHStream.WriteLine($action)    
            }
            else {
                Write-Verbose -Message 'Expect timeout without achiving a match.'
            }
        }
        } 
    else{
        $ret = Invoke-SSHStreamExpectAction -ShellStream $SSHStream -Command $commands -Action $encType -ExpectRegex $regx -TimeOut 10
        }   
    

    #$found = $SSHStream.Expect([Regex]$expectedRegex, (New-TimeSpan -Seconds $TimeOut))
    $msg = "waiting on " + $expectedStr
    Write-host "Waiting for  $expectedStr, Check the [$LogFileName] for latest update"
    $result = wait-ForCommandPrompt -SSHStream $SSHStream -stringToMatch $expectedStr -timeout $timeout -msg $msg -enclSerialName $action -logFileName $LogFileName
    #remove unnecessary symbols before writing to file.
    
   <#
   write-host "Waiting for command prompt"
    do{
        $result = $result + $SSHStream.read()
         start-sleep -s 1; 
         $sec +=1; 
         write-host -NoNewline "."
         if($sec -gt $timeout)
            {   write-verbose $result
                throw "Waited $timeout seconds, ssh root prompt not found"}
     }while(!($result -match $expectedStr))
     #>
    #$result = $SSHStream.read()
   # $result | Set-Content -Encoding UTF8 $LogFileName
    #$result|Out-File $LogFileName

    # check for different fail scenario if any such scenario meet exit the current run
    if($result -match "Traceback" -and $halt -eq $false ){
        Write-Error "FRU failed while running commands [$commands] , refer [$logfileName] file, provide fix and re run fru update" 
        }
    elseif($result -match "Traceback" -and $halt -eq $True ){
        throw "FRU failed while running commands [$commands] , refer [$logfileName] file, provide fix and re run fru update" 
        }

    elseif ($result -match "Exception" -or $result -match "Unknown" -or $result -match "Failed" -or $result -match "Error" -or $result -match "Warning" -or $result -match "SN=0000000000" -or $result -match "PN=          " -or $result -match "Unable to login" -and $halt -eq $false) {
        write-warning "Problem encountered while running commands [$commands] , refer [$logfileName] file, provide fix and re run fru update"    
		} 
    elseif ($result -match "Exception" -or $result -match "Unknown" -or $result -match "Failed" -or $result -match "Error" -or $result -match "Warning" -or $result -match "SN=0000000000" -or $result -match "PN=          " -or $result -match "Unable to login" -and $halt -eq $true) {
        throw "Problem encountered while running commands [$commands] , refer [$logfileName] file, provide fix and re run fru update"    
		} 
    else {
		Write-Host "Log collected and stored, refer [$logfileName] file for more details" 
    }
    }
End{
    Remove-variable SSHStream
    }
}

<# Library 
Synopsis: 
	process fru file name and return the version.

Examples: 
    get-FRUVersionDate -frufileName $frufileName
    
Parameters: 
	$frufileName : FRU File Name
    
Dependencies: 
	
Notes: 
	
#>
Function get-FRUVersionDate{
param(
        [parameter(Mandatory = $true, HelpMessage = "FRU utility file name [hpeMgmtUtil_v2.6.15_20160324_internal.tar]", Position=0)]
        $fruFileName)
    $str = $fruFileName.replace("hpeMgmtUtil_v", "")
    $startIndex = $str.IndexOf("_")
    $si = $startIndex+1
    $endIndex = $str.IndexOf("_", $si)
    $versionDate = [int]($str.subString($si, $endIndex - $si))
    
    #$ver = [int]($str.Substring(0,$str.IndexOf("_"))).Replace(".","")
    #if(!($a.StartsWith("26"))){
    #    $ver = $ver + "0"
    #    }
    return $versionDate
}

Function wait-ForCommandPrompt{
    param(
        [parameter(Mandatory = $true, HelpMessage = "FRU utility file name [hpeMgmtUtil_v2.6.15_20160324_internal.tar]", Position=0)]
        $SSHStream,
        [parameter(Mandatory = $true, HelpMessage = "Provide string to be expected", Position=1)]
        [string]$stringToMatch,
        [parameter(Mandatory = $true, HelpMessage = "Enter FRU utilitty timeout -",Position=2)]
        [int]$timeout,
        [parameter(Mandatory = $false, HelpMessage = "Enter FRU utilitty timeout -",Position=3)]
        [string]$msg = "Waiting on prompt",
        [parameter(Mandatory = $false, HelpMessage = "Enter the enclosure serial number you wish to interact with -",Position=4)]
        [string]$enclSerialName,
        [parameter(Mandatory = $false, HelpMessage = "Enter the Log File Name -",Position=5)]
        [string]$logFileName

        )
    write-verbose $msg
    $result = ""
    do{
       [String]$temp = $SSHStream.read()
        
         start-sleep -s 10; 
         $sec +=10; 
         write-verbose "."
         if($temp -match "Traceback"){
            return $result + $temp
            }
         if($temp -match "Enter the enclosure serial number you wish to interact with"){
            write-verbose "Expecting enclosure serial numaber to interact"
            $SSHStream.WriteLine($enclSerialName)
            write-verbose "provided [$enclSerialName]"
            }
         elseif($sec -gt $timeout)
            {
                write-verbose $result
                Write-Error "Waited $timeout seconds, not found $stringToMatch"
                return $result
                }
        $result = $result + $temp
        if($LogFileName){
            $result | Set-Content -Encoding UTF8 $LogFileName
               }
     }while(!($result -match $stringToMatch))
     return $result
    }

<# Library 
Synopsis: 
	connect to CIM and unzip or untar files.

Examples: 
    Expand-file -ssh [ssh] -fileName [FileName] -timeout [100]
Parameters: 
	ssh: Required: ssh connection.
    fileNmae: Required: zip or tar failename
    timeout: Optional: default 100.
    
Dependencies: 
	
Notes: 
	
#> 
Function Expand-file{
param(
        [parameter(Mandatory = $true, HelpMessage = "ssh session to communicate with", Position=0)]
        $ssh,
        [parameter(Mandatory = $true, HelpMessage = "Enter zip/tar file name",Position=1)]
        [String]$FileName,
        [parameter(Mandatory = $false, HelpMessage = "Enter timeout -",Position=4)]
        [int]$timeout=60
    )
process{
    # make sure "hpeMgmtUtil_v2.6.0_20151119_internal.tar " file exist before running untar commands
    $ret = Invoke-SSHCommand -SSHSession $ssh -Command "ls /tmp" -TimeOut $timeout
    if($ret.output -contains $fileName){
        if($fileName -match ".tar"){
			Write-Host "untar [$FileName]"
	        # untar .tar file
    	    $ret = Invoke-SSHCommand -SSHSession $ssh -Command "cd /tmp;tar -xvf $FileName" -TimeOut $timeout

        	# look for .py file to run fru commands
        	$ret = Invoke-SSHCommand -SSHSession $ssh -Command "cd /tmp/hpeMgmtUtil;ls" -TimeOut $timeout
        	if ($ret.output -contains "hpeMgmtUtilCli.py"){
            	Write-Host "Python file hpeMgmtUtilCli.py found to run different FRU commands"
            	}
         	else{
            	 throw "hpeMgmtUtilCli.py not found, check the unzip folder."
            	}
            
         }
		 elseif($fileName -match ".zip"){
		 	Write-Host "unzip [$fileName]"
		 	$ret = Invoke-SSHCommand -SSHSession $ssh -Command "cd /tmp;unzip -o $FileName" -TimeOut $timeout
			$DirectoryName = $fileName -replace ".zip", ""
			$ret = Invoke-SSHCommand -SSHSession $ssh -Command "cd /tmp/$DirectoryName;ls" -TimeOut $timeout
        	if ($ret.output -contains "tbrUtility.py"){
            	Write-Host "Python file tbrUtility.py found to run TRU"
            	}
            Elseif ($ret.output -contains "HPIPUpdate.py"){
            	Write-Host "Python file HPIPUpdate.py found to run HPIP Firmware Update"
            	}
         	else{
            	 throw "Utility .py not found, check the unzip folder."
            	}
		 }
		 }
    else{
        throw "Please upload [$FileName] file to CIM before running commands"
        }
    }
}

<# Library 
Synopsis: 
	connect to CIM and updates config_data.py to update iLO firmware during fru update.

Examples: 
    Update-file -ssh [ssh] -ilofwUpdate [True\False] -timeout [100]
Parameters: 
	ssh: Required: ssh connection.
    iLofwUpdate: Required: True|False
    timeout: Optional: default 100.
    
Dependencies: 
	
Notes: 
	
#> 
Function Update-file{
param(
        [parameter(Mandatory = $true, HelpMessage = "ssh session to communicate with", Position=0)]
        $ssh,
        [parameter(Mandatory = $true, HelpMessage = "ilo firmware update True\False",Position=1)]
        $ilofwUpdate,
        [parameter(Mandatory = $false, HelpMessage = "Enter FRU utilitty timeout -",Position=2)]
        [int]$timeout=10
        )
    if($ilofwUpdate){
        Write-Verbose "Updating FRU hpeMgmtUtil/config_data.py FLASH_ILO_FIRMWARE = False -> FLASH_ILO_FIRMWARE = True"
        $command = "cd /tmp/hpeMgmtUtil; sed -i -- 's/FLASH_ILO_FIRMWARE = False/FLASH_ILO_FIRMWARE = True/g' `"config_data.py`""

        $ret = Invoke-SSHCommand -SSHSession $ssh -Command $command -TimeOut $timeout

        if($ret.ExitStatus -eq "0"){
            Write-Verbose "Updated FRU hpeMgmtUtil/config_data.py FLASH_ILO_FIRMWARE = False -> FLASH_ILO_FIRMWARE = True"
            }
        else{
            Write-Warning "Failed to update hpeMgmtUtil/config_data FLASH_ILO_FIRMWARE = False -> FLASH_ILO_FIRMWARE = True"
            }
        }
    else{
         Write-Verbose "Skiping iLO firmware update using FRU"   

        }
    }

<# Library 
Synopsis: 
	connect to CIM and get the primary enclosure name.

Examples: 
    get-EnclosureSN -ssh [ssh] -commands [commands] -timeout [100]
Parameters: 
	ssh: Required: ssh connection.
    commands: optional: "/ci/bin/tbird/appliance-hal.sh list-enclosures"
    timeout: Optional: default 100.
    
Dependencies: 
	
Notes: 
	
#> 

Function get-EnclosureSN{
param(
    [parameter(Mandatory = $true, HelpMessage = "ssh session to communicate with", Position=0)]
    $ssh,
    [parameter(Mandatory = $false, HelpMessage = "command to be run",Position=1)]
    [string]$commands,
    [parameter(Mandatory = $false, HelpMessage = "Enter FRU utilitty timeout -",Position=4)]
    [int]$timeout=60
            
)

process{
    $commands ="lldpcli sho ne"
    $res = Invoke-SSHCommand -SSHSession $ssh -Command $commands -TimeOut $timeout
    $activeEMWithDetials = $res.output

    $commands ="/ci/bin/tbird/appliance-hal.sh list-enclosures"
    $res = Invoke-SSHCommand -SSHSession $ssh -Command $commands -TimeOut $timeout
    $enclosures = $res.output

    foreach($enclosure in $enclosures){
            if($activeEMWithDetials -match $enclosure){
                $primaryEnclosure = $enclosure
                break
            }
    }
    if($primaryEnclosure)
    {
        return $enclosure
    }
    else{
        throw "unable to get the primary enclosure Please check verify [$commands] in cim"
    }
}

}

<# Library 
Synopsis: 
	connect to CIM and get the primary enclosure password.

Examples: 
    get-EnclosurePassword -ssh [ssh] -encSerialNumber [encSerialNumber] -timeout [100]
Parameters: 
	ssh: Required: ssh connection.
    encSerialNumber: Required: "encSerialNumber"
    timeout: Optional: default 100.
    
Dependencies: 
	
Notes: 
	
#> 

Function get-EnclosurePassword{
param(
    [parameter(Mandatory = $true, HelpMessage = "ssh session to communicate with", Position=0)]
    $ssh,
    [parameter(Mandatory = $true, HelpMessage = "Provide enclosure serial number\name", Position=1)]
    [string]$encSerialNumber,
    [parameter(Mandatory = $false, HelpMessage = "Enter FRU utilitty timeout -",Position=2)]
    [int]$timeout=60
)

process{
    # Get the EM session
    $commands = "/ci/bin/tbird/appliance-hal.sh get-enclosure-credentials -s $encSerialNumber -o p"
    $res = Invoke-SSHCommand -SSHSession $ssh -Command $commands -TimeOut $timeout
    $password = $res.output
    if($password){
        return $password
    }
    else{
        throw "unable to get the password Please verify [$commands] in cim"
    }

}
}
<# Library 
Synopsis: 
	connect to CIM and get the enclosure ip by specifying enclosure serial number.

Examples: 
    get-EnclosureIP -ssh [ssh] -encSerialNumber [encSerialNumber] -timeout [100]
Parameters: 
	ssh: Required: ssh connection.
    encSerialNumber: Required: "encSerialNumber"
    timeout: Optional: default 100.
    
Dependencies: 
	
Notes: 
	
#> 
Function get-EnclosureIP{
param(
    [parameter(Mandatory = $true, HelpMessage = "ssh session to communicate with", Position=0)]
    $ssh,
    [parameter(Mandatory = $true, HelpMessage = "Provide enclosure serial number\name", Position=1)]
    [string]$encSerialNumber,
    [parameter(Mandatory = $false, HelpMessage = "Enter FRU utilitty timeout -",Position=2)]
    [int]$timeout=60
)

process{
    # Get the EM session
    $commands = "/ci/bin/tbird/appliance-hal.sh get-enclosure-credentials -s $encSerialNumber -o i"
    $res = Invoke-SSHCommand -SSHSession $ssh -Command $commands -TimeOut $timeout
    $enclosureIP = $res.output
    if($enclosureIP){
        return $enclosureIP
    }
    else{
        throw "unable to get the Enclosure IP Please verify [$commands] in cim"
    }

}
}
<# Library 
Synopsis: 
	connect to CIM and get the EM session.

Examples: 
    get-EMSession -ssh [ssh] -encSerialNumber [encSerialNumber] -timeout [100]
Parameters: 
	ssh: Required: ssh connection.
    encSerialNumber: Required: "encSerialNumber"
    timeout: Optional: default 100.
    
Dependencies: 
	
Notes: 
	
#> 
Function get-EMSession{
param(
    [parameter(Mandatory = $true, HelpMessage = "ssh session to communicate with", Position=0)]
    $ssh,
    [parameter(Mandatory = $true, HelpMessage = "Provide enclosure serial number\name", Position=1)]
    [string]$encSerialNumber,
    [parameter(Mandatory = $false, HelpMessage = "Enter FRU utilitty timeout -",Position=2)]
    [int]$timeout=60
)

process{
    # Get the EM session
    $commands = "/ci/bin/tbird/appliance-hal.sh get-enclosure-credentials -s $encSerialNumber -o t"
    $res = Invoke-SSHCommand -SSHSession $ssh -Command $commands -TimeOut $timeout
    $session = $res.output
    if($session){
        return $session
    }
    else{
        throw "unable to get the em session Please verify [$commands] in cim"
    }

}
}

<# Library 
Synopsis: 
	connect to CIM and get the EM floating IP.

Examples: 
    get-FloatingEMIP -ssh [ssh] -encSerialNumber [encSerialNumber] -timeout [100]
Parameters: 
	ssh: Required: ssh connection.
    encSerialNumber: Required: "encSerialNumber"
    timeout: Optional: default 100.
    
Dependencies: 
	
Notes: 
	
#>

Function get-FloatingEMIP{
param(
    [parameter(Mandatory = $true, HelpMessage = "ssh session to communicate with", Position=0)]
    $ssh,
    [parameter(Mandatory = $true, HelpMessage = "Provide enclosure serial number\name", Position=1)]
    [string]$encSerialNumber,
    [parameter(Mandatory = $false, HelpMessage = "Enter FRU utilitty timeout -",Position=2)]
    [int]$timeout=60
)

process{
    # Get the floating ipv6 ip of EM
    $commands = "/ci/bin/tbird/appliance-hal.sh get-enclosure-credentials -s $encSerialNumber -o i"
    $res = Invoke-SSHCommand -SSHSession $ssh -Command $commands -TimeOut $timeout
    $floatingEMIP = $res.output
    if($floatingEMIP){
        return $floatingEMIP
    }
    else{
        throw "unable to get the floating EM IP, Please verify [$comands] in cim"
    }

}
}

<# Library 
Synopsis: 
	connect to CIM and reset the active EM so that stand by EM becomes Active.

Examples: 
    Reset-ActiveEM -ssh [ssh] -emSession [emSession] -emIP [emIP] -timeout [100]
Parameters: 
	ssh: Required: ssh connection.
    emSession: Required: "emSession"
    emIP: Required: "emIP"
    timeout: Optional: default 100.
    
Dependencies: 
	
Notes: 
	
#>
Function Reset-ActiveEM{
param(
    [parameter(Mandatory = $true, HelpMessage = "ssh session to communicate with", Position=0)]
    $ssh,
    [parameter(Mandatory = $true, HelpMessage = "Provide EM session", Position=1)]
    [string]$emSession,
    [parameter(Mandatory = $true, HelpMessage = "Provide floating EM ip", Position=2)]
    [string]$emIP,
    [parameter(Mandatory = $false, HelpMessage = "Enter FRU utilitty timeout -",Position=3)]
    [int]$timeout=60,
    [parameter(Mandatory = $true, HelpMessage = "Active EM bay -",Position=4)]
    $activeEM

)

process{
    # Get the EM session
   
    if($activeEM -eq 1){
        $commands = "curl -g -x `"`" -k -v -X POST -H 'x-auth-token:$emSession' -d '{`"Action`":`"Reset`"}' https://$emIP%bond0/rest/v1/EnclosureManager/1"
        
    }
    else{
        $commands = "curl -g -x `"`" -k -v -X POST -H 'x-auth-token:$emSession' -d '{`"Action`":`"Reset`"}' https://$emIP%bond0/rest/v1/EnclosureManager/2"
        
    }

    $res = Invoke-SSHCommand -SSHSession $ssh -Command $commands -TimeOut $timeout

    if($res.output -match "Reset"){
        write-host "[$commands] successfully accepted"
        }
    else{
        throw "unable to reset the EM, Please verify [$commands] in CIM"
    }
}
}
<# Library 
Synopsis: 
	connect to CIM and get the Active EM.

Examples: 
    get-ActiveEM -ssh [ssh] -emSession [emSession] -emIP [emIP] -timeout [100]
Parameters: 
	ssh: Required: ssh connection.
    emSession: Required: "emSession"
    emIP: Required: "emIP"
    timeout: Optional: default 100.
    
Dependencies: 
	
Notes: 
	
#>
Function get-ActiveEM{
param(
    [parameter(Mandatory = $true, HelpMessage = "ssh session to communicate with", Position=0)]
    $ssh,
    [parameter(Mandatory = $true, HelpMessage = "Provide EM session", Position=1)]
    [string]$emSession,
    [parameter(Mandatory = $true, HelpMessage = "Provide floating EM ip", Position=2)]
    [string]$emIP,
    [parameter(Mandatory = $false, HelpMessage = "Enter FRU utilitty timeout -",Position=3)]
    [int]$timeout=60
)

process{
    # Get the EM session
    $commands = "curl -g -k -sS -H 'x-auth-token:$emSession'  https://$emIP%bond0/rest/v1/EnclosureManager/1 | python -mjson.tool | grep Role"
    $res = Invoke-SSHCommand -SSHSession $ssh -Command $commands -TimeOut $timeout
    $emRole = $res.output
    if($emRole -match "Active"){
        return 1
    }
    else{
         return 2
        
    }
}
}
<# Library 
Synopsis: 
	ssh to the appliance and run the command to get firmware version of all components.

Examples: 
	Invoke-tru -tbhost [tbhost] -user [username] -password [password] -fileName [tru file name] -logfileName [logfileName] -recipeFIleNmae [recipeFilename]
Parameters: 
	tbhost: Required: CIM IP.
	user: Optional: default root.
	password: Optional: default hpvse1.
    ovusername: Required: OV user name
    ovpassword: Required: OV password
    fileName: Required : default tru utility filename
    logfileName: Required : default log filename to store logs
    recipeFIleNmae: Required : default recipefileName 
	timeout: Optional : 3600
Dependencies: 
	
Notes: 
	
#> 
Function Invoke-tru
{
param(
            [parameter(Mandatory = $true, HelpMessage = "Enter OV ip or fqdn host name -",Position=0)]
            [ValidateNotNullOrEmpty()]
            [string]$tbhost, 
            [parameter(Mandatory = $false, HelpMessage = "Enter CIM username -",Position=1)]
            [string]$username = "root",
            [parameter(Mandatory = $false, HelpMessage = "Enter CIM password -",Position=2)]
            $password = "hpvse1",
			[parameter(Mandatory = $true, HelpMessage = "Enter OneView username -",Position=3)]
            [string]$ovusername,
            [parameter(Mandatory = $true, HelpMessage = "Enter OneView password -",Position=4)]
            $ovpassword,
            [parameter(Mandatory = $true, HelpMessage = "Enter TRU tool filename -",Position=5)]
            [string]$fileName,
			#[parameter(Mandatory = $true, HelpMessage = "Enter TRU tool file path -",Position=6)]
            #$sourcePath,
            [parameter(Mandatory = $false, HelpMessage = "Enter TRU utilitty log filename -",Position=7)]
            [string]$logfileName=$null,
            [parameter(Mandatory = $true, HelpMessage = "Enter TRU recipe filename [RecipeGARFSX.rcp] -",Position=8)]
            [string]$recipefileName,
            [parameter(Mandatory = $false, HelpMessage = "Enter TRU utilitty timeout -",Position=9)]
            [int]$timeout=3600 
            )
BEGIN {
   
    $ssh = Connect-ssh -Host $tbhost -UserName $username -Password $password
	$DirectoryName = $fileName -replace ".zip", ""
    
    $commands = "cd /tmp/$DirectoryName; python3.4 tbrUtility.py -d -ou $ovusername -op $ovpassword -e recipes/$recipefileName"
    # Get the log file if it has not been provided
    if(!$logfileName){
        $logfileName = Get-Date -Format s | foreach {$_ -replace ":", "."}
        $LogFileName = "TRU_" + $LogFileName + ".log"
        }

    # Get the sshstream
    $SSHStream = New-SSHShellStream -Index $ssh.SessionId
    }
PROCESS {
	#unzip the utility file
	Expand-file -ssh $ssh -FileName $fileName
   
    
    $ret = Invoke-SSHCommand -SSHSession $ssh -Command $commands -TimeOut $timeout 
    $ret.output|Out-File $LogFileName
    if($ret.ExitStatus -eq 0){
        Write-Host "TRU tool ran successfully and stored in [$logFileName]"
        }
    else{
        Write-warning "TRU tool run was not sucessful, refer [$logFileName] file for more detials"}
    
    }
END {
    Remove-SSHSession -SSHSession $ssh
    Remove-variable ssh
    }
}

<# Library 
Synopsis: 
	ssh to the appliance and run the command to update HPIP firmware version of all blade.

Examples: 
	Invoke-hpip -tbhost [tbhost] -user [username] -password [password] -fileName [tru file name] -logfileName [logfileName] -recipeFIleNmae [recipeFilename] -isopath [isopath]
Parameters: 
	tbhost: Required: CIM IP.
	user: Optional: default root.
	password: Optional: default hpvse1.
    ovusername: Required: OV user name
    ovpassword: Required: OV password
    fileName: Required : default tru utility filename
    logfileName: Required : default log filename to store logs
    recipeFIleNmae: Required : default recipefileName 
	timeout: Optional : 3600
    isopath: hpip iso image path
Dependencies: 
	
Notes: 
	
#> 
Function Invoke-hpip
{
param(
            [parameter(Mandatory = $true, HelpMessage = "Enter OV ip or fqdn host name -",Position=0)]
            [ValidateNotNullOrEmpty()]
            [string]$tbhost, 
            [parameter(Mandatory = $false, HelpMessage = "Enter CIM username -",Position=1)]
            [string]$username = "root",
            [parameter(Mandatory = $false, HelpMessage = "Enter CIM password -",Position=2)]
            $password = "hpvse1",
			[parameter(Mandatory = $true, HelpMessage = "Enter OneView username -",Position=3)]
            [string]$ovusername,
            [parameter(Mandatory = $true, HelpMessage = "Enter OneView password -",Position=4)]
            $ovpassword,
            [parameter(Mandatory = $true, HelpMessage = "Enter HPIPUpdate tool filename -",Position=5)]
            [string]$fileName,
            [parameter(Mandatory = $false, HelpMessage = "Enter HPIPUpdate utilitty log filename -",Position=6)]
            [string]$logfileName=$null,
            [parameter(Mandatory = $false, HelpMessage = "Enter HPIPUpdate utilitty timeout -",Position=7)]
            [int]$timeout=3600,
            [parameter(Mandatory = $true, HelpMessage = "Enter HPIP iso image path -")]
            $isopath
            )
BEGIN {
   
    $ssh = Connect-ssh -Host $tbhost -UserName $username -Password $password
	$DirectoryName = $fileName -replace ".zip", ""
    
    #$commands = "cd /tmp/$DirectoryName; python3.4 HPIPUpdate.py -d -ou $ovusername -op $ovpassword -e recipes/$recipefileName -i $isopath"
    $commands = "cd /tmp/$DirectoryName; python3.4 HPIPUpdate.py -d -ou $ovusername -op $ovpassword -i $isopath -e"
    
    # Get the log file if it has not been provided
    if(!$logfileName){
        $logfileName = Get-Date -Format s | foreach {$_ -replace ":", "."}
        $LogFileName = "HPIPUpdate" + $LogFileName + ".log"
        }

    # Get the sshstream
    $SSHStream = New-SSHShellStream -Index $ssh.SessionId
    }
PROCESS {
	#unzip the utility file
	Expand-file -ssh $ssh -FileName $fileName
   
    
    $ret = Invoke-SSHCommand -SSHSession $ssh -Command $commands -TimeOut $timeout 
    $ret.output|Out-File $LogFileName
    if($ret.ExitStatus -eq 0){
        Write-Host "HPIP update ran successfully and stored in [$logFileName]"
        }
    else{
        Write-warning "HPIP update run was not sucessful, refer [$logFileName] file for more detials"}
    
    }
END {
    Remove-SSHSession -SSHSession $ssh
    Remove-variable ssh
    }
}

<# Library 
Synopsis: 
	ssh to the appliance and run the command to efuse all devices in frame.

Examples: 
	Invoke-efuse -tbhost [tbhost] -user [username] -password [password]
Parameters: 
	tbhost: Required: CIM IP.
	user: Optional: default root.
	password: Optional: default hpvse1.
   
Dependencies: 
	
Notes: 
	
#> 
Function Invoke-efuse
{
param(
            [parameter(Mandatory = $true, HelpMessage = "Enter OV ip or fqdn host name -",Position=0)]
            [ValidateNotNullOrEmpty()]
            [string]$tbhost, 
            [parameter(Mandatory = $false, HelpMessage = "Enter CIM username -",Position=1)]
            [string]$username = "root",
            [parameter(Mandatory = $false, HelpMessage = "Enter CIM password -",Position=2)]
            $password = "hpvse1",
            [parameter(Mandatory = $false, HelpMessage = "Enter HPIPUpdate utilitty log filename -",Position=6)]
            [string]$logfileName=$null,
            [parameter(Mandatory = $false, HelpMessage = "Enter HPIPUpdate utilitty timeout -",Position=7)]
            [int]$timeout=60
            )
BEGIN {
   
    $ssh = Connect-ssh -Host $tbhost -UserName $username -Password $password
	           
    # Get the log file if it has not been provided
    if(!$logfileName){
        $timeStamp = Get-Date -Format s | foreach {$_ -replace ":", "."}
        $LogFileName = "EFUSE" + $timeStamp + ".log"
        }

    Write-Host "Refer Log file $LogFileName for Efuse details"

    # Get the sshstream
    $SSHStream = New-SSHShellStream -Index $ssh.SessionId
    $expectedResponse = "HTTP/1.1 202 Accepted"
    }
PROCESS {
	# Make sure em_cim_cli.py available to run efuse commands
	$ret = Invoke-SSHCommand -SSHSession $ssh -Command "cd /tmp;ls" -TimeOut $timeout
    if ($ret.output -contains "em_cim_cli.py"){
       	Write-Host "Python file em_cim_cli.py found to run Efuse"
        Write-Log -LogPath $logFileName -LineValue "Python file em_cim_cli.py found to run Efuse"
       	}
    else{
        Write-Log -LogPath $logFileName -LineValue "em_cim_cli.py not found, check the /tmp folder."
       	 throw "em_cim_cli.py not found, check the /tmp folder."
       	}
   
    # Get the primary Enclosure serial number
    $primaryEnclSN = get-EnclosureSN -ssh $ssh
    Write-Verbose "Primary enclosure:  $primaryEnclSN"
    Write-Log -LogPath $logFileName -LineValue "Primary enclosure:  $primaryEnclSN"


    $commands ="/ci/bin/tbird/appliance-hal.sh list-enclosures"
    $res = Invoke-SSHCommand -SSHSession $ssh -Command $commands -TimeOut $timeout
    $enclosures = $res.output
    
    # Create new array and move the primary enclosure at the end
    Write-Verbose "List enclosures: $enclosures"
    Write-Log -LogPath $logFileName -LineValue "List enclosures: $enclosures"
    $encs = New-Object System.Collections.ArrayList
    foreach($enclosure in $enclosures){
        $temp = $encs.add($enclosure)
        }
    $temp = $encs.Remove($primaryEnclSN)
    $temp = $encs.add($primaryEnclSN)

    Write-Verbose "List enclosures: $encs"
    Write-Log -LogPath $logFileName -LineValue "List enclosures: $encs"
    foreach($enclosure in $encs){
        Write-Host "Initiating Efuse on $enclosure frame"
        Write-Log -LogPath $logFileName -LineValue "Initiating Efuse on $enclosure frame"
        $commands = "cd /tmp; python em_cim_cli.py"
        start-sleep -s 20;
        Write-Verbose "Runnging command [$commands]"
        Write-Log -LogPath $logFileName -LineValue "Runnging command [$commands]"
        $SSHStream.WriteLine($commands)
        start-sleep -s 10;
        [String]$stream = $SSHStream.read()

            # Verify em_cim_cli.py command prompt available to run efuse commands
            Write-verbose $stream
            Write-Log -LogPath $logFileName -LineValue $stream
            if($stream.contains("[CLI]#")){

                $command = "efuse fan 1"
                Efuse -SSHStream $SSHStream -command $command -expectedResponse $expectedResponse -enclosure $enclosure -logFileName $logfileName

                # Efuse Fan
                for ($i=2; $i -lt 11; $i++){
                    $command = "efuse fan $i"
                    Efuse -SSHStream $SSHStream -command $command -expectedResponse $expectedResponse -enclosure $enclosure -logFileName $logfileName

                }
                # Efuse PS
                for ($i=1; $i -lt 7; $i++){
                    $command = "efuse ps $i"
                    Efuse -SSHStream $SSHStream -command $command -expectedResponse $expectedResponse -enclosure $enclosure -logFileName $logfileName

                }
                # Efuse blade
                for ($i=1; $i -lt 13; $i++){
                    $command = "efuse blade $i"
                    Efuse -SSHStream $SSHStream -command $command -expectedResponse $expectedResponse -enclosure $enclosure -logFileName $logfileName
                }
                # Efuse interconnect
                for ($i=1; $i -lt 7; $i++){
                    $command = "efuse interconnect $i"
                    Efuse -SSHStream $SSHStream -command $command -expectedResponse $expectedResponse -enclosure $enclosure -logFileName $logfileName
                }

                # Efuse frontpanel
                    $command = "efuse frontpanel 1"
                    Efuse -SSHStream $SSHStream -command $command -expectedResponse $expectedResponse -enclosure $enclosure -logFileName $logfileName

                # Efuse CIM
                for ($i=1; $i -lt 3; $i++){
                    $command = "efuse cim $i"
                    Efuse -SSHStream $SSHStream -command $command -expectedResponse $expectedResponse -enclosure $enclosure -logFileName $logfileName
                }
                
                # Exit from CLI command prompt
                start-sleep -s 1
                $SSHStream.WriteLine("exit")
                start-sleep -s 2;
                [String]$stream = $SSHStream.read()
                Write-verbose $stream
                Write-Log -LogPath $logFileName -LineValue $stream
                if ($stream -match "HTTP/1.1 200 OK"){
                        write-host "Exiting from Efuse CLI"
                        Write-Log -LogPath $logFileName -LineValue "Exiting from Efuse CLI"
                    }    
                else{
                     Write-Log -LogPath $logFileName -LineValue "Failed to Exiting from Efuse CLI"
                     write-error "Failed to exit from Efuse CLI"
                    }

            }
           

        }

    }
END {
    Remove-SSHSession -SSHSession $ssh
    Remove-variable ssh
    }
}

Function EFUSE{
param(
    [parameter(Mandatory = $true, HelpMessage = "Enter OV ip or fqdn host name -",Position=0)]
    [ValidateNotNullOrEmpty()]
    $SSHStream,
    [parameter(Mandatory = $true, HelpMessage = "Enter efuse command [efuse fan 1] -",Position=1)]
    [ValidateNotNullOrEmpty()]
    $command,
    [parameter(Mandatory = $true, HelpMessage = "Enter expected response -",Position=2)]
    [ValidateNotNullOrEmpty()]
    $expectedResponse,
    [parameter(Mandatory = $true, HelpMessage = "Enter enclosure name -",Position=3)]
    [ValidateNotNullOrEmpty()]
    $enclosure,
    [parameter(Mandatory = $False, HelpMessage = "Timeout",Position=4)]
    $timeout = 5,
    [parameter(Mandatory = $True, HelpMessage = "Timeout",Position=5)]
    $logFileName
    
    )
process{
       $sec = 0
       # send the command to ssh stream
       $SSHStream.WriteLine($command)
       start-sleep -s $timeout;
       
       # read the ssh stream
       [String]$stream = $SSHStream.read()
       Write-Verbose "SshStream : $stream"
       Write-Log -LogPath $logFileName -LineValue "SshStream : $stream"
       if ($stream -match "Enter the enclosure you wish to interact with:"){
                    $SSHStream.WriteLine($enclosure)
                    start-sleep -s $timeout;
                    [String]$stream = $SSHStream.read()
           }
              
       if($stream -match $expectedResponse){
            write-host "Efuse command [$command] accepted"
            Write-Log -LogPath $logFileName -LineValue "Efuse command [$command] accepted"
            }
        else{
            Write-Log -LogPath $logFileName -LineValue "Efuse command [$command] not accepted"
            write-error "Efuse command [$command] not accepted"
            }         
}

}
<# Library 
Synopsis: 
	ssh to the appliance and run the command to get firmware version of all components.

Examples: 
	runTRUTool -cichost [cichost] -user [username] -password [password] - sshlibpath [library path] -command [Sets of command]
Parameters: 
	ccichost: Required: command to run on the appliance.
	user: Optional: default root.
	password: Optional: default hpvse1.
	command: Optional: default is "cd /tmp/tru-2.0.0.0; python3.4 tbrUtility.py -d"
Dependencies: 
	
Notes: 
	
#> 
Function Copy-filesFromCIM{
param(
            [parameter(Mandatory = $true, HelpMessage = "Enter OV ip or fqdn host name -",Position=0)]
            [ValidateNotNullOrEmpty()]
            [string]$tbhost, #"csitb10-ov.rsn.rdlabs.hpecorp.net" 
            [parameter(Mandatory = $false, HelpMessage = "Enter CIM username -",Position=1)]
            [string]$user = "root",
            [parameter(Mandatory = $false, HelpMessage = "Enter CIM password -",Position=2)]
            [string]$password = "hpvse1",
            [parameter(Mandatory = $false, HelpMessage = "Enter filename to be uploaded",Position=3)]
			[string]$fileName = "get_info.xml",
			[parameter(Mandatory = $false, HelpMessage = "Enter source path to copy file from -",Position=4)]
			$sourcePath = "/tmp",
            [parameter(Mandatory = $false, HelpMessage = "Enter destination path copy file to -",Position=5)]
			[string]$destFolder = "C:\Users\Administrator\git\epic"
            )
$password = ConvertTo-SecureString -String $password -AsPlainText -Force 
$credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $username, $password
$Session = New-SFTPSession -ComputerName $tbhost -Credential $Credentials 
if($fileName){
    Get-SFTPFile -SFTPSession $Session -RemoteFile "$sourcePath" -LocalPath "$destFolder"}
else{
    Get-SCPFolder -ComputerName $tbhost -Credential $Credentials -LocalFolder $destFolder -RemoteFolder $sourcePath
    }
}


<# Library 
Synopsis: 
	sendfile to CIM

Examples:
	Send-filesToCIM -tbhost [tbhost] -user [username] -password [password] -fileName [fileName] -sourcePath [sourcePath] -destFolder [destFolder]
                    
Parameters: 
	ccichost: Required: command to run on the appliance.
	user: Optional: default root.
	password: Optional: default hpvse1.
	fileName: Required:  default " fileName to be copied"
    sourcePath: Required:  default is "sourcepath of file"
    destFolder: Required:  default is "destination folder"
	
Dependencies: 
		
Notes: 

	
#> 
function Send-filesToCIM
{ param(
            [parameter(Mandatory = $true, HelpMessage = "Enter OV ip or fqdn host name -",Position=0)]
            [ValidateNotNullOrEmpty()]
            [string]$tbhost, #"csitb10-ov.rsn.rdlabs.hpecorp.net" 
            [parameter(Mandatory = $false, HelpMessage = "Enter CIM username -",Position=1)]
            [string]$user = "root",
            [parameter(Mandatory = $false, HelpMessage = "Enter CIM password -",Position=2)]
            [string]$password = "hpvse1",
            [parameter(Mandatory = $true, HelpMessage = "Enter filename to be uploaded",Position=3)]
			[string]$fileName,
			[parameter(Mandatory = $true, HelpMessage = "Enter source path to copy file from -",Position=4)]
			$sourcePath,
            [parameter(Mandatory = $false, HelpMessage = "Enter destination path copy file to -",Position=5)]
			[string]$destFolder = "/tmp"
            )
	if (!$sourcePath)
	{
		$sourcePath = $path
	}
	$ConnInfo = New-Object Renci.SshNet.PasswordConnectionInfo($tbhost, $port, $user, $password)
	$SftpClient = New-Object Renci.SshNet.SftpClient($ConnInfo)
	try {
		$SftpClient.Connect()
		Write-Host "Connected to host [$tbhost] using SSH client"
		$SftpClient.ChangeDirectory($destFolder)
		Write-Host "Change Directory to $destFolder"
		# Get the path
		$fname = "$sourcePath\$fileName"
		$SftpClient.UploadFile([System.IO.File]::OpenRead($fname), $fileName)
		Write-Host "File [$fileName] uploaded successfully at [$destFolder] directory of remote server [$tbhost]"
		
	}
	catch {
		[string]$e = $_.Exception.ToString()
		Write-Host ("function UploadFile Exception: " + $_.Exception.ToString())
		
	}
	
	finally
    {
        # Disconnect, clean up
		$SftpClient.Disconnect()
		#$SftpClient.Dispose()
    }
}