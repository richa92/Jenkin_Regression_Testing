Param([string]$ovIP, [string]$ovUser, [string]$ovPass, [string]$spp)
Import-Module ".\HPOneView.120.psm1"

if (-not $global:cimgmtSessionId) { Connect-HPOVMgmt $ovIP $ovUser $ovPass } 

$sppTask=Remove-HPOVResource 	/rest/firmware-drivers/$spp
#Wait for spp task
$task = Wait-HPOVTaskComplete $sppTask.uri -timeout (New-TimeSpan -Minutes 15) 
