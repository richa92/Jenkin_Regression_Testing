Import-Module "C:\Users\Administrator\git\fusion\tests\DEA\tests\TbirdFWUpdateTool\InputData.ps1" -Force
Import-Module "C:\Users\Administrator\git\fusion\tests\DEA\tests\TbirdFWUpdateTool\TbirdLib.psm1" -Force
Import-Module "C:\Users\Administrator\git\fusion\tests\DEA\tests\TbirdFWUpdateTool\SshLib.psm1" -Force

#Unblock DLL file blocked by Windows

Unblock-File C:\Users\Administrator\git\fusion\tests\DEA\tests\TbirdFWUpdateTool\Posh-SSH\poshssh.dll
Unblock-File C:\Users\Administrator\git\fusion\tests\DEA\tests\TbirdFWUpdateTool\Posh-SSH\Assembly\Renci.SshNet.dll
Unblock-File C:\Users\Administrator\git\fusion\tests\DEA\tests\TbirdFWUpdateTool\Posh-SSH\Assembly\Ionic.Zlib.dll

$inputData = $args[0]

    if($inputData){
        Import-Module C:\Users\Administrator\git\fusion\tests\DEA\tests\TbirdFWUpdateTool\$inputData -Force
        Write-Host "$inputData loaded as input file"
        }
    else{
        $inputData = "InputData.ps1"
        Import-Module C:\Users\Administrator\git\fusion\tests\DEA\tests\TbirdFWUpdateTool\$inputData -Force
        Write-Host "$inputData loaded as input file"
        }

Function GFU{
    param(
        [Parameter(Mandatory = $True,ParameterSetName = "Default",HelpMessage = "Provide input to run TRU[ True or False ]", Position = 0)]
        [bool]$tru,
        [Parameter(Mandatory = $True,ParameterSetName = "Default",HelpMessage = "Provide input to run FRU[ True or False ]", Position = 1)]
        [bool]$fru,
        [Parameter(Mandatory = $True,ParameterSetName = "Default",HelpMessage = "Provide input to run TRU[ FWU or BBFW or BBFW-O]", Position = 2)]
        [String]$fwu,
        [Parameter(Mandatory = $True,ParameterSetName = "Default",HelpMessage = "Provide input to run HPIP firmware update", Position = 3)]
        [String]$runHPIPU,
        [Parameter(Mandatory = $True,ParameterSetName = "Default",HelpMessage = "Provide input to run efuse frames", Position = 4)]
        [String]$efuseFrames)
        

Start-Log -LogPath $Path -LogName $LogFileName -ScriptVersion "1.9"

# First connect to the HP OneView appliance.
if (-not $global:cimgmtSessionId) { Connect-HPOVMgmt $ovIP $ovUser $ovPass }
#Call to update Firmware for a TBIRD

#Get the Enclosure
$script:enclosureNames = (Get-HPOVEnclosure).name

if($tru -eq $True){
    Send-filesToCIM -tbhost $ovIP -fileName $TRU_FileName -sourcePath $Path
    Invoke-tru -tbhost $ovIP -fileName $TRU_FileName -ovusername $ovUser -ovpassword $ovPass -recipefileName $TRU_RecipeFileName
    }
if($fru -eq $true){
    ###FRU enclType should be 2 for VP enclosure
    Send-filesToCIM -tbhost $ovIP -fileName $FRU_FileName -sourcePath $Path 
    if($frulocal -eq $true){
        Invoke-fru -tbhost $ovIP -fruFileName $FRU_FileName -iLOusername $iLOusername -iLOpassword $iLOpassword -ilofwUpdate $ilofwUpdate -enclType 2 -halt $fru_halt -timeout $fruTimeOut
        }
    foreach($frame in $fruRemoteFrameNames){
        Invoke-Remotefru -tbhost $ovIP -enclosureSN $frame -fruFileName $FRU_FileName -iLOusername $iLOusername -iLOpassword $iLOpassword -ilofwUpdate $ilofwUpdate -enclType 2 -halt $fru_halt -timeout $fruTimeOut
        }

    }
###Update firmware
if($fwu -eq "FWU"){
    ### Updates firmware on EM, Interconnect and server during LE creation
    Update-TBirdFW -ligs $ligs -enclosureNames $enclosureNames -enclGroupName $egName -path $sppPath -haltTest $haltTest -forceInstallFirmware $forceInstallFirmware -leName $leName
    }

elseif($fwu -eq "BBFWU"){
    #BigBang firmware Update
    ###Updates firmware on EM, Interconnect and server using BigBang SharedInfrastructureAndServerProfiles
    Update-TBirdBBFW -ligs $ligs -enclosureNames $enclosureNames -enclGroupName $egName -path $sppPath -haltTest $haltTest -forceInstallFirmware $forceInstallFirmware -leName $leName
    }
elseif($fwu -eq "BBFWU-O"){
    #BigBang firmware Update with different choices, profileFirmare, [EnclosureOnly] | [SharedInfrastructureOnly]
    Update-TBirdBBFW-Options -ligs $ligs -enclosureNames $enclosureNames -enclGroupName $egName -path $sppPath -haltTest $haltTest -profileFirmware $profileFirmware -bigBangFirmwareoption $bigBangFirmwareoption -forceInstallFirmware $forceInstallFirmware -leName $leName
    }

if($tru -eq $True){
    Send-filesToCIM -tbhost $ovIP -fileName $TRU_FileName -sourcePath $Path
    Invoke-tru -tbhost $ovIP -fileName $TRU_FileName -ovusername $ovUser -ovpassword $ovPass -recipefileName $TRU_RecipeFileName
    }

if($runHPIPU -eq $True){
    Send-filesToCIM -tbhost $ovIP -fileName $HPIP_FileName -sourcePath $Path
    Invoke-hpip -tbhost $ovIP -fileName $HPIP_FileName -ovusername $ovUser -ovpassword $ovPass -isopath $isopath
    }
if($efuseFrames -eq $True){
    Send-filesToCIM -tbhost $ovIP -fileName $efuse_FileName -sourcePath $Path
    Invoke-efuse -tbhost $ovIP
    }
#Get the console content and sotre into file for future reference
get-console > $CompleteConsolePath

}

# Get the current time
$ScriptStart = (Get-Date)

#run GFU script 
gfu -tru $runTRU -fru $runFRU -fwu $runFWU -runHPIPU $runHPIPU -efuseFrames $efuseFrames

#Get the End time
$ScriptEnd = (Get-Date)

#Get the difference
$RunTime = New-Timespan -Start $ScriptStart -End $ScriptEnd

Write-host""
Write-host “Elapsed Time: $RunTime”
