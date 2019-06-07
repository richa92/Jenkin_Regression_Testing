Import-Module "C:\Users\Administrator\git\fusion\tests\DEA\tests\TbirdFWUpdateTool\InputData.ps1" -Force
Import-Module "C:\Users\Administrator\git\fusion\tests\DEA\tests\TbirdFWUpdateTool\TbirdLib.psm1" -Force

$ScriptStart = (Get-Date)
$inputData = $args[0]

    if($inputData){
        Import-Module C:\Users\Administrator\git\fusion\tests\DEA\tests\TbirdFWUpdateTool\inputData -Force
        Write-Host "$inputData loaded as input file"
        }
    else{
        $inputData = "InputData.ps1"
        Import-Module C:\Users\Administrator\git\fusion\tests\DEA\tests\TbirdFWUpdateTool\$inputData -Force
        Write-Host "$inputData loaded as input file"
        }


$ScriptStart = (Get-Date)
# First connect to the HP OneView appliance.
if (-not $global:cimgmtSessionId) { Connect-HPOVMgmt $ovIP $ovUser $ovPass }

#Get the Enclosure
$enclosureNames = (Get-HPOVEnclosure).name

stop-servers -enclosureNames $enclosureNames -timeout 600


forEach($encName in $enclosureNames){
    $enc= (Get-HPOVEnclosure $encName| select name, deviceBays)
    $bays=$enc.deviceBays | select bayNumber,devicePresence,deviceUri,bayPowerState
   
    
    $list_profiles = $enc.deviceBays | select profileUri, devicePresence, bayPowerState
    Foreach ($profile in $list_profiles){
        if($profile.profileUri){
            $task_name = (Send-HPOVRequest $profile.profileUri).name
            Write-Host "Remove Profiles [$task_name]"
            $profileTask = Remove-HPOVProfile $profile.profileUri -Force -Confirm:$false
            }
        }
}
#wait for profile deletion
if($profileTask){
    $task = Get-HPOVTask -ResourceCategory server-profiles -Count 1| Wait-HPOVTaskComplete -timeout (New-TimeSpan -Minutes 10)
    }
# after profile deleting going directly for LE deletion fails, adding 10 seconds to avoid LE deletion failure
Write-Host "Sleeping for 10 seconds"
start-sleep -s 10

#Remove Le 
Write-Host "Delete Logical Enclosure [$leName]"
$leTask = Remove-HPTBLogicalEnclosure $leName -Force -Confirm:$false
#Wait for Le task
if($leTask){
    wait-for-task -task_uri $leTask.uri -timeout 600
    }
#$task = Get-HPOVTask -ResourceCategory logical-enclosures -Count 1| Wait-HPOVTaskComplete
Write-Host "Sleeping for 10 seconds"
start-sleep -s 10

#Remove Eg
Write-Host "Delete Enclosure Group $egName"
$egtask = Remove-HPOVEnclosureGroup -name $egName -Confirm:$false

#Wait for Eg deletion
$task = Get-HPOVTask -ResourceCategory enclosure-groups -Count 1| Wait-HPOVTaskComplete
Write-Host "Sleeping for 10 seconds"
start-sleep -s 10


#Remove Lig
foreach($lig in $ligs){
        $name = $lig["name"]
        Write-Host "Delete Lig $name"
        $ligtask = Remove-HPOVLogicalInterconnectGroup -name $name -Confirm:$false
        }
get-console > Log_TearDown.html

#Get the End time
$ScriptEnd = (Get-Date)

#Get the difference
$RunTime = New-Timespan -Start $ScriptStart -End $ScriptEnd

Write-host""
Write-host “Elapsed Time: $RunTime”



