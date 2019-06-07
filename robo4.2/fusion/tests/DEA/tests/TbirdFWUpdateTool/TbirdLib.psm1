Import-Module "C:\Users\Administrator\git\fusion\tests\DEA\tests\TbirdFWUpdateTool\HPOneView.120.psm1"

[String]$script:MaxXAPIVersion         = "300"
[String]$script:logicalInterconnectGroupsUri = "/rest/logical-interconnect-groups"
[String]$script:sasLogicalInterconnectGroupsUri = "/rest/sas-logical-interconnect-groups"
[String]$script:enclosureGroupsUri           = "/rest/enclosure-groups"
[String]$script:logicalEnclosuresUri         = "/rest/logical-enclosures"
[String]$script:enclosuresUri                = "/rest/enclosures"
[String]$script:enclosuresTypeUri            = "/rest/enclosure-types/SY12000"
[String]$script:firmwareDriversUri           = "/rest/firmware-drivers"
[String]$script:ethNetworksUri               = "/rest/ethernet-networks"
[String]$script:fcNetworksUri                = "/rest/fc-networks"
		$script:applianceConnectedTo         = @{User = "None"; Appliance = "Not connected"}
        $script:HPOneViewAppliance           = $null
[String]$script:applMacAddresses             = "/rest/appliance/network-interfaces/mac-addresses"
[String]$script:applConfigUri                = "/rest/appliance/network-interfaces"
[String]$script:ilt                          = "/rest/interconnect-link-topologies?start=0&count=1"
[int]$script:lastWebResponse                 = $null
$script:defaultTimeout                       = New-TimeSpan -Minutes 20

#------------------------------------
#  Profile Management
#------------------------------------
$script:profilesUri                   = "/rest/server-profiles"
$script:profileListUri                = "/rest/server-profiles?start=0&count=250"
$script:profileIndexListUri           = "/rest/index/resources?sort=name:asc&category=server-profiles"
$script:profileAvailStorageSystemsUri = '/rest/server-profiles/available-storage-systems'

#Get the Interconnects
Function Get-InterconnectBaysDetails($enclosurename)
{
    $em = (Get-HPOVEnclosure $enclosureName).interconnectbays| select baynumber, interconnectModel
    $Bays = @{}
    foreach($e in $em){
        if($e.interconnectmodel){
            $Bays.add($e.bayNumber,$e.interconnectModel)
            } 
        }
return $Bays
}

#Get Interconnects bayset
Function Get-InterconnectBaySet($Bays)
{
    if($Bays.keys -contains "1" -or $Bays.keys -contains "4"){
        $BaySet = 1
    }
    elseif($Bays.keys -contains "2" -or $Bays.keys -contains "5"){
        $BaySet = 2
    }
    else{
        $BaySet = 3
    }
return $BaySet
}

#Get the redundant type
Function Get-RedundantType($Bays, $enclosurename)
{
    if ($enclosurename.count -gt 1){
        if( ($Bays.keys -contains "1" -and $Bays.keys -contains "4") -or ($Bays.keys -contains "2" -and $Bays.keys -contains "5") -or ($Bays.keys -contains "3" -and $Bays.keys -contains "6") ){
            $redundantType = "HighlyAvailable"
        }
        elseif($Bays.keys -contains "1" -or $Bays.keys -contains "2" -or $Bays.keys -contains "3"){
            $redundantType = "NonRedundantASide"
        }
        else{
        $redundantType = "NonRedundantBSide"
        }
    }
    else{
        if( ($Bays.keys -contains "1" -and $Bays.keys -contains "4") -or ($Bays.keys -contains "2" -and $Bays.keys -contains "5") -or ($Bays.keys -contains "3" -and $Bays.keys -contains "6") ){
            $redundantType = "Redundant"
        }
        elseif($Bays.keys -contains "1" -or $Bays.keys -contains "2" -or $Bays.keys -contains "3"){
            $redundantType = "NonRedundantASide"
        }
        else{
        $redundantType = "NonRedundantBSide"
        }
    }
return $redundantType
}


function New-HPTBLogicalInterconnectGroup {

    # .ExternalHelp HPOneView.120.psm1-help.xml

    [CmdletBinding(DefaultParameterSetName = "Default")]
    param (
        [Parameter(Mandatory = $True,ParameterSetName = "Default",HelpMessage = "Please specify the Logical Interconnect Name", Position = 0)]
        [ValidateNotNullOrEmpty()]
        [Alias('name')]
        [String]$ligName,

        [Parameter(Mandatory = $True,ParameterSetName = "Default",HelpMessage = "Please specify the redundancyType, can be [HighlyAvailable], [NonRedundantASide], [NonRedundantBSide], [Redundant]", Position = 1)]
        [ValidateNotNullOrEmpty()]
        [Alias('redundanttype')]
        [String]$redundancyType,

        [Parameter(Mandatory = $False,ParameterSetName = "Default",HelpMessage = "Please specify the single or list of Enclosures ..", Position = 2)]
        [ValidateNotNullOrEmpty()]
        [string[]] $enclosureNames,
        
        [Parameter(Mandatory = $True,ValueFromPipeline = $true,ParameterSetName = "Default",HelpMessage = "Please specify the Interconnect Modules in Hashtable format for all Interconnect Bays: ", Position = 3)]
        [ValidateNotNullOrEmpty()]
        [Alias('interconnectbaydetails')]
        [Hashtable]$Bays,
        # @{3 = "HP VC SE 40Gb F8 Module";6 = "HP VC SE 40Gb F8 Module"}
                
        [Parameter(Mandatory = $False,ParameterSetName = "Default",HelpMessage = "Enable IGMP Snooping", Position = 4)]
		[Alias("IGMPSnoop")]
        [bool]$enableIgmpSnooping = $False,
		
		[Parameter(Mandatory = $False,ParameterSetName = "Default",HelpMessage = "IGMP Idle Timeout Interval (1-3600 [sec])", Position = 5)]
        [ValidateRange(1,3600)]
		[Alias('IGMPIdle')]
	    [int]$igmpIdleTimeoutInterval = 260,
		
		[Parameter(Mandatory = $False,ParameterSetName = "Default",HelpMessage = "Enable Fast MAC Cache Failover", Position = 6)]
		[Alias('FastMAC')]
	    [bool]$enableFastMacCacheFailover = $True,
		
		[Parameter(Mandatory = $False,ParameterSetName = "Default",HelpMessage = "Fast MAC Cache Failover Interval (1-30 [sec])", Position = 7)]
        [ValidateRange(1,30)]
		[Alias('FastMACRefresh')]
    	[int]$macRefreshInterval = 5,
		
		[Parameter(Mandatory = $False,ParameterSetName = "Default",HelpMessage = "Enable Network Loop Protection on the Downlink Ports)", Position = 8)]
		[Alias('LoopProtect')]
	    [bool]$enableNetworkLoopProtection = $True,

		[Parameter(Mandatory = $False,ParameterSetName = "Default",HelpMessage = "Enable Network Pause Flood Protection on the Downlink Ports)", Position = 9)]
		[Alias('PauseProtect')]
	    [bool]$enablePauseFloodProtection = $True,
		
		[Parameter(Mandatory = $False,ParameterSetName = "Default",HelpMessage = "Enable SNMP Settings", Position = 10)]
        [Alias('snmpValues')]
	    [hashtable]$SNMP = $null,

        [Parameter(Mandatory = $True,ParameterSetName = "Default",HelpMessage = "Enable SNMP Settings", Position = 11)]
        [Alias('interconnectBaySet')]
	    [String]$iConnectBaySet,

        [Parameter(Mandatory = $True,ParameterSetName = "Import",HelpMessage = "Specify JSON source file to create Logical Interconnect Group")]
        [ValidateScript({split-path $_ | Test-Path})]
        [Alias('i')]
	    [object]$Import

    )

    Begin {
        
        #Check to make sure the user is authenticated
        If (!$global:cimgmtSessionId){
            $errorRecord = New-ErrorRecord HPOneview.Appliance.AuthSessionException NoAuthSession AuthenticationError $($MyInvocation.InvocationName.ToString().ToUpper()) -Message "No valid session ID found.  Please use Connect-HPOVMgmt to connect and authenticate to an appliance." #-verbose
            $PSCmdlet.ThrowTerminatingError($errorRecord)

	    }
        
    }
	
	Process{

        If ($Import){
            
            Write-Log -LogPath $CompletePath -LineValue "Reading input file"

            try {

                #Open input file, join so we can vlidate if the JSON format is correct.
                $lig = [string]::Join("", (gc $import -ErrorAction Stop)) | convertfrom-json -ErrorAction Stop
                $lig | write-debug

                Write-Log -LogPath $CompletePath -LineValue "Sending request"
                $task = Send-HPOVRequest $logicalInterconnectGroupsUri POST $lig

            }
            
            #If there was a problem with the input file (format, not syntax) throw error
            catch [System.ArgumentException] {

                $errorRecord = New-ErrorRecord InvalidOperationException InvalidArgumentValue InvalidArgument 'Import' -TargetType "PSObject" -Message "JSON Input File is invalid.  Please check the contents and try again." #-verbose
                $PSCmdLet.ThrowTerminatingError($errorRecord)
            }

        }

        Else {
             #In case of more than one enclosure need to initilize indexes
             $iConnectModuleindexes = @()
             for($count=1; $count -le $enclosureNames.count; $count++){
                $iConnectModuleindexes += $count
                }
              
		    $lig = @{
                name                    = $ligName;
	            state                   = "Active";
	            status                  = $null; 
	            uplinkSets              = @();
                enclosureType           = "SY12000";
	            interconnectMapTemplate = @{interconnectMapEntryTemplates = @()};
	            ethernetSettings = @{
                    #type                        = "EthernetInterconnectSettingsV3";
                    type                        = "EthernetInterconnectSettingsV201";
                    enableIgmpSnooping          = $enableIgmpSnooping;
                    igmpIdleTimeoutInterval     = $igmpIdleTimeoutInterval; 
                    enableFastMacCacheFailover  = $enableFastMacCacheFailover;
                    macRefreshInterval          = $macRefreshInterval;
                    enableNetworkLoopProtection = $enableNetworkLoopProtection;
                    enablePauseFloodProtection  = $enablePauseFloodProtection;

                };
			    snmpConfiguration       = $snmp;
	            stackingMode            = "Enclosure";
                type                    = "logical-interconnect-groupV300";
                interconnectBaySet      = $iConnectBaySet;
                redundancyType          = $redundancyType;
                enclosureIndexes        = $iConnectModuleindexes
                
	        }
        
        
            #Make sure the snmpConfiguration type property is set, as the caller might not know about this.
            if ($lig.snmpConfiguration) { $lig.snmpConfiguration.type = "snmp-configuration" }
		
             $Secondary = @{ }

		    #check for any duplicate keys
		    $duplicates = $Bays.keys | where { $Secondary.ContainsKey($_) }
		    if ($duplicates) {
		        foreach ($item in $duplicates) {
		                $Secondary.Remove($item)
		        }
		    }

		    #join the two hash tables
		    $NewBays = $Bays+$Secondary 
		    Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Bay configuration: $($NewBays | Sort-Object Key -Descending | Out-String)"
 		
		   
            #Incase of more than one enclosure, we need to repeat interconnectMapTable
            foreach ($index in $iConnectModuleindexes){
            #for($index = 2;$index -gt 0; $index=$index-1){
                   $Bays = Get-InterconnectBaysDetails $enclosurenames[$index-1]
                   #Loop through hashtable
                   forEach($bay in $Bays.GetEnumerator()){#|Sort-Object Name){
                          $ret = Get-Inteconnect $bay
                          $lig.interconnectMapTemplate.interconnectMapEntryTemplates += @{
                          enclosureIndex = $index;
		    	          logicalDownlinkUri = $null;
	                      permittedInterconnectTypeUri = $ret.uri;
				          logicalLocation = @{locationEntries = @(@{relativeValue = $bay.name; type = "Bay"}, @{relativeValue = $index; type = "Enclosure"})}}
                          }
                   }

            Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] LIG: $($lig | out-string)"

	        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Sending request to create $Name..."

		    
            $task = Send-HPOVRequest $script:logicalInterconnectGroupsUri POST $lig
            
        }

	}

    End {

        $task

    }
}

Function Get-Inteconnect{
# Get the inteconnect on the basis of different interconnects
[CmdletBinding()]
Param(
[parameter(Position = 0, Mandatory = $true)]
        $bay
        # @{3 = "HP VC SE 40Gb F8 Module"}
        )
                            
		  	switch ($bay.value) {
			        "FlexFabric" {            
			            #Get VC FlexFabric interconnect-type URI
                        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Found VC FF in bay $($bay.name | out-string)"
			            $ret = Get-HPOVInterconnectType -partNumber "571956-B21"
			        }
			        "Flex10" {
			            #Get VC Flex-10 interconnect-type URI
                        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Found VC F10 in bay $($bay.name | out-string)"
			            $ret = Get-HPOVInterconnectType -partNumber "455880-B21"
			        }
			        "Flex1010D" {
			            #Get VC Flex-10/10D interconnect-type URI
                        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Found VC F1010D in bay $($bay.name | out-string)"
			            $ret = Get-HPOVInterconnectType -partNumber "638526-B21"
			        }
			        "Flex2040f8" {
			            #Get VC Flex-10/10D interconnect-type URI
                        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Found VC Flex2040f8 in bay $($bay.name | out-string)"
			            $ret = Get-HPOVInterconnectType -partNumber "691367-B21"
			        }
			        "VCFC20" {
			            #Get VC Flex-10/10D interconnect-type URI
                        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Found VC FC 20-port in bay $($bay.name | out-string)"
			            $ret = Get-HPOVInterconnectType -partNumber "572018-B21"
			        }
			        "VCFC24" {
			            #Get VC Flex-10/10D interconnect-type URI
                        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Found VC FC 24-port in bay $($bay.name | out-string)"
			            $ret = Get-HPOVInterconnectType -partNumber "466482-B21"
			        }
			        "FEX" {
			            #Get Cisco Fabric Extender for HP BladeSystem interconnect-type URI
                        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Found Cisco Fabric Extender for HP BladeSystem in bay $($bay.name | out-string)"
			            $ret = Get-HPOVInterconnectType -partNumber "641146-B21"
			        }
                    "HP VC SE 40Gb F8 Module" {
                        #Get HP VC SE 40Gb F8 Module for HP BladeSystem interconnect-type URI                      
                         Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] HP VC SE 40Gb F8 Module for HP BladeSystem in bay $($bay.name | out-string)"
			             $ret = Get-HPOVInterconnectType -partNumber "794502-B21"
                    }
                    "VC SE 40Gb F8 Module" {
                        #Get HP VC SE 40Gb F8 Module for HP BladeSystem interconnect-type URI                      
                         Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] HP VC SE 40Gb F8 Module for HP BladeSystem in bay $($bay.name | out-string)"
			             $ret = Get-HPOVInterconnectType -partNumber "794502-B21"
                         #$ret = Get-HPOVInterconnectType -partNumber "779218-B21"
                    }
                    "HP Synergy Interconnect Link Module" {
                        #Get HP Synergy Interconnect Link Module for HP BladeSystem interconnect-type URI                      
                         Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Found HP Synergy Interconnect Link Module for HP BladeSystem in bay $($bay.name | out-string)"
			             $ret = Get-HPOVInterconnectType -partNumber "779218-B21"
                    }
                    "HP FlexFabric 40/40Gb Module" {
                    #Get HP FlexFabric 40/40Gb Module for HP BladeSystem interconnect-type URI                      
                         Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Found HP FlexFabric 40/40Gb Module for HP BladeSystem in bay $($bay.name | out-string)"
			             $ret = Get-HPOVInterconnectType -partNumber "779224-B21"
                    }
                    "Virtual Connect SE 40Gb F8 Module for Synergy" {
                    #Get Virtual Connect SE 40Gb F8 Module for Synergy for HP BladeSystem interconnect-type URI                      
                         Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Found Virtual Connect SE 40Gb F8 Module for Synergy for HP BladeSystem in bay $($bay.name | out-string)"
			             $ret = Get-HPOVInterconnectType -partNumber "779224-B21"
                    }
                    "Synergy 40Gb F8 Switch" {
                    #Get Synergy 40Gb F8 Switch for HP BladeSystem interconnect-type URI                      
                         Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Found Synergy 40Gb F8 Switch for HP BladeSystem in bay $($bay.name | out-string)"
			             $ret = Get-HPOVInterconnectType -partNumber "779224-B21"
                    }
                    "Synergy 20Gb Interconnect Link Module" {
                    #Get Synergy 20Gb Interconnect Link Module interconnect-type URI                      
                         Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Found Synergy 20Gb Interconnect Link Module for HP BladeSystem in bay $($bay.name | out-string)"
			             $ret = Get-HPOVInterconnectType -partNumber "779218-B21"
                    }
                    "Virtual Connect SE 16Gb FC Module" {
                    #Get Virtual Connect SE 16Gb FC Module interconnect-type URI                      
                         Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Found Virtual Connect SE 16Gb FC Module for HP BladeSystem in bay $($bay.name | out-string)"
			             $ret = Get-HPOVInterconnectType -partNumber "779227-B21"
                    }
				    default {
					    $ret = $null
				    }
				
                }
    return $ret
    }
function New-HPTBEnclosureGroup {
    
    # .ExternalHelp HPOneView.120.psm1-help.xml

    [CmdletBinding()]
    Param (
        [parameter(Position = 0, Mandatory = $true, HelpMessage = "Enter a name for the new enclosure group.")]
        [ValidateNotNullOrEmpty()]
        [alias('name')]
        [string]$egName = $Null,
         
        [parameter(Position = 1, Mandatory = $true, ValueFromPipeline = $true, ParameterSetName = "Default", HelpMessage = "Enter the Logical Interconnect Group uri.")]
        [ValidateNotNullOrEmpty()]
        #[alias('name')]
        [String[]]$ligUris,


        [parameter(Position = 2, Mandatory = $true, HelpMessage = "Enter IPV4 Address Mode.")]
        [ValidateNotNullOrEmpty()]
        [string]$ipAddressingMode = $Null,

        [parameter(Position = 3, Mandatory = $false)]
        [string]$interconnectBayMappingCount = 6,

        [parameter(Position = 4, Mandatory = $false)]
        [string]$configurationScript = $null,

        [parameter(Position = 5, Mandatory = $false)]
        [validateset('Enclosure')]
        [string]$stackingMode = "Enclosure",

        [parameter(Position = 6, Mandatory = $true)]
        [int]$enclosureCount = 1
    )

    Begin {

        #$PipelineInput = -not $PSBoundParameters.ContainsKey("logicalInterconnectGroup")

        if (-not($global:cimgmtSessionId)) {
        
            $errorRecord = New-ErrorRecord HPOneview.Appliance.AuthSessionException NoAuthSession AuthenticationError "New-HPOVEnclosureGroup" -Message "No valid session ID found.  Please use Connect-HPOVMgmt to connect and authenticate to an appliance." #-verbose
            $PSCmdlet.ThrowTerminatingError($errorRecord)

        }

    }


    Process {
            #Retrieve Logical Interconnect group details, such as bay mapping and populate bay and respective uri in hash table.
            [HashTable]$ligBayDetails = $null
            [System.Array]$interconnectBayMappings = $null;
            foreach ($liguri in $liguris){
                $ligname = (Send-HPOVRequest $liguri).name
                foreach($lig_details in $ligs){
                    if($lig_details.name -eq $ligName){
                        $imts = $lig_details.interconnectMapTemplate
                        foreach($imt in $imts){
                            if($imt.type -match "sas"){
                                $interconnectBayMappings += [PsCustomObject]@{
                                    interconnectBay = $imt.bay;
                                    logicalInterconnectGroupUri = $liguri;
                                    enclosureIndex = $imt.enclosure
                                    }
                             }
                             else{
                                $interconnectBayMappings += [PsCustomObject]@{
                                    interconnectBay = $imt.bay;
                                    logicalInterconnectGroupUri = $liguri;
                                    enclosureIndex = $imt.enclosure
                                    }

                            }
        }
    }
}
}
<#

            ForEach($ligUri in $ligUris){
            <#
				# determine type of interconnect
				foreach($lig_details in $ligs){
					if($lig_details.name -eq $lig){
						if($lig_details.type -match "sas"){
							$logicalInterconnectGroupsUri = $sasLogicalInterconnectGroupsUri
							}}}
              
                $buildingUri = $logicalInterconnectGroupsUri + "?filter=name=$lig"
                  
                $buildingUri = (Get-HPOVLogicalInterconnectGroup -name $lig).uri
                Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Lig uri using name: $($buildingUri)"
                
                $ligMember = (Send-HPOVRequest $buildingUri).members
                Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Lig member details: $($ligMember)"
                
                $ligUri = $ligMember.uri
  
                
                Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Lig uri: $($ligUri)"
                
                $interconnectBaySet = (Send-HPOVRequest $ligUri).interconnectBaySet
                Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Lig InterconnectBaySet: $($interconnectBaySet)"
                
                if (-not ($liguri -match "sas")){
                    $redundancyType = (Send-HPOVRequest $ligUri).redundancyType
                    Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Lig InterconnectBaySet: $($redundancyType)"
                    }
                if (($interconnectBaySet -eq 1 -or $interconnectBaySet -eq 2 -or $interconnectBaySet -eq 3) -and ($redundancyType -eq "HighlyAvailable" -or $redundancyType -eq "Redundant"))
                    {
                        $ligBayDetails += @{ $interconnectBaySet = $ligUri; ($interconnectBaySet + 3) = $ligUri;}
                    }
                elseif (($interconnectBaySet -eq 1 -or $interconnectBaySet -eq 2 -or $interconnectBaySet -eq 3) -and ($redundancyType -eq "NonRedundantASide"))
                    {
                        $ligBayDetails += @{ $interconnectBaySet = $ligUri;}
                    }
                elseif(($interconnectBaySet -eq 1 -or $interconnectBaySet -eq 2 -or $interconnectBaySet -eq 3) -and ($redundancyType -eq "NonRedundantBSide"))
                    {
                        $ligBayDetails += @{ ($interconnectBaySet + 3) = $ligUri;}
                    }
                else{
                        $ligBayDetails += @{ ($interconnectBaySet) = $ligUri;}
                     }
                
            }

            #Fill in missing bay locations from the input value if needed.
		    $Secondary = @{ 1 = $null; 2 = $null; 3 = $null; 4 = $null; 5 = $null; 6 = $null}
            
		    #check for any duplicate keys
            $duplicates = $ligBayDetails.keys | where { $Secondary.ContainsKey($_) }

		    if ($duplicates) {
		        foreach ($item in $duplicates) {
		                $Secondary.Remove($item)
		        }
		    }

		 #join the two hash tables
		 $ligDetails = $ligBayDetails+$Secondary 
 
		 Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Bay configuration: $($ligDetails | Sort-Object Key -Descending | Out-String)"
         
         #initialize interconnectBayMappings table
         [System.Array]$interconnectBayMappings = $null;
         foreach ($interconnectBay in $ligDetails.GetEnumerator()){
              if(!$($interconnectBay.Value)){
                    $interconnectBayMappings += [PsCustomObject]@{
                        interconnectBay = $($interconnectBay.Name);
                        logicalInterconnectGroupUri = $null;
                        }
              }
              else
              {
                $interconnectBayMappings += [PsCustomObject]@{
                    interconnectBay = $($interconnectBay.Name);
                    logicalInterconnectGroupUri = $($interconnectBay.Value);
                    }
              }
        }
                  #>
       
        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] interconnectBayMappings: $($interconnectBayMappings | Sort-Object Key -Descending | Out-String)"

        $eg = [PsCustomObject] @{
            #type = "EnclosureGroupV200";
            type = "EnclosureGroupV300";
            name = $egName;
            stackingMode = $stackingMode;
            configurationScript = $configurationScript;
            interconnectBayMappings = $interconnectBayMappings;
            interconnectBayMappingCount = $interconnectBayMappingCount
            ipAddressingMode = $ipAddressingMode
            enclosureCount = $enclosureCount
            enclosureTypeUri = $enclosuresTypeUri
        }

        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Enclosure Group object: $($eg | out-string)"

        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Creating $($name) Enclosure Group"
        $resp = New-HPOVResource $enclosureGroupsUri $eg
    }

    end {

        return $resp

    }

}
function New-HPTBLogicalEnclosure {
    
    # .ExternalHelp HPOneView.120.psm1-help.xml

    [CmdletBinding()]
    Param (
        [parameter(Position = 0, Mandatory = $true, HelpMessage = "Enter a name for the new logical enclosure name.")]
        [ValidateNotNullOrEmpty()]
        [string]$name,
         
        [parameter(Position = 1, Mandatory = $true, HelpMessage = "Enter the name of Enclosure Group to apply.")]
        [ValidateNotNullOrEmpty()]
        [alias('eGName')]
        [string]$enclGroupName,
        
        [parameter(Position = 2, Mandatory = $true, HelpMessage = "Enter the set of enclosure names that are linked")]
        [ValidateNotNullOrEmpty()]
        [string[]]$enclosureNames = @(),

        [parameter(Position = 3, Mandatory = $false, HelpMessage = "Enter the sppFileName of the firmware baseline to apply to interconnects")]
        [string]$sppFileName = $null,

        [parameter(Position = 4, Mandatory = $false)]
        [bool]$forceInstallFirmware = $false
    )

    Begin {


        if (-not($global:cimgmtSessionId)) {
        
            $errorRecord = New-ErrorRecord HPOneview.Appliance.AuthSessionException NoAuthSession AuthenticationError "New-HPOVEnclosureGroup" -Message "No valid session ID found.  Please use Connect-HPOVMgmt to connect and authenticate to an appliance." #-verbose
            $PSCmdlet.ThrowTerminatingError($errorRecord)

        }

    }


    Process {  

        #Get the Enclsoure uri using Enclosure Group name
        [string[]]$enclosureUris = $null
        <#
        Foreach($enclName in $enclosureNames){
            $buildingUri = $enclosuresUri + "?filter=name='$enclName'"
            Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Building Enclosure uri using name: $($buildingUri)"
                
            $enclosureMember = (Send-HPOVRequest $buildingUri).members
            Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Enclosure member details: $($enclosureMember)"
                
            $enclosureUris  += $enclosureMember.uri
            Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Enclosure uri: $($enclosureUris)"    
            }
        #>
        #Get the enclosure uri using InterconnectLinkTopplogies
        $enclosureUris = (Send-HPOVRequest $ilt).members.enclosureMembers.enclosureUri

        #Get the Enclsoure Group uri using Enclosure Group name
        $buildingUri = $enclosureGroupsUri + "?filter=name=$enclGroupName"
        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Enclosure Group uri using name: $($buildingUri)"
                
        $egMember = (Send-HPOVRequest $buildingUri).members
        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Enclosure Group member details: $($egMember)"
                
        $egUri = $egMember.uri
        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Enclosure Group uri: $($egUri)"
        
        #Get the Firmware drivers uri using firmware bundle name
        if($sppFileName){
            $buildingUri = $firmwareDriversUri + "?filter=name=$sppFileName"
            Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] building Firmware drivers using firmware build name: $($buildingUri)"
               
            $firmwareBaselineUri = ((Send-HPOVRequest $buildingUri).members).uri
            Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Firmware drivers ur: $($firmwareBaselineUri)"
            }    


        $le = [PsCustomObject] @{
            name = $name;
            enclosureUris = $enclosureUris
            enclosureGroupUri = $egUri
            firmwareBaselineUri = $firmwareBaselineUri
            forceInstallFirmware = $forceInstallFirmware
        }
        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Enclosure Group object: $($le | out-string)"

        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Creating $($name) Logical Enclosure"
        $resp = New-HPOVResource $logicalEnclosuresUri $le
    }

    end {

        return $resp

    }

}

function Update-HPTBResource {
    
    # .ExternalHelp HPOneView.120.psm1-help.xml

    [CmdletBinding()]
    Param (

         [parameter(Position = 0, Mandatory = $true, HelpMessage = "Enter the URI string of the resource type to be created")]
         [ValidateNotNullOrEmpty()]
         [string] $uri,

         [parameter(Position = 1, Mandatory = $true, HelpMessage = "Enter the resource object definition")]
         [ValidateNotNullOrEmpty()]
         [object] $resource
    
		 )

    Begin {

        if (-not($global:cimgmtSessionId)) {
        
            $errorRecord = New-ErrorRecord HPOneview.Appliance.AuthSessionException NoAuthSession AuthenticationError "Update-HPOVResource" -Message "No valid session ID found.  Please use Connect-HPOVMgmt to connect and authenticate to an appliance." #-verbose
            $PSCmdlet.ThrowTerminatingError($errorRecord)

        }

    }

    Process {

        Send-HPTBRequest $uri PATCH $resource

    }

}


function Remove-HPTBLogicalEnclosure {
    
    # .ExternalHelp HPOneView.120.psm1-help.xml

    [CmdLetBinding(DefaultParameterSetName = "default",SupportsShouldProcess = $True,ConfirmImpact = 'High')]
    Param (
        [parameter(Mandatory = $true, Position = 0, ValueFromPipeline = $true,ParameterSetName = "default", HelpMessage = "Specify the Logical Enclosure(s) to remove.")]
        [ValidateNotNullOrEmpty()]
        [Alias("uri")]
        [Alias("name")]
        $logicalEncl = $null,

	    [parameter(Mandatory = $false)] 
        [switch]$force
    )

    begin {

        if (-not($global:cimgmtSessionId)) {
        
            $errorRecord = New-ErrorRecord HPOneview.Appliance.AuthSessionException NoAuthSession AuthenticationError 'Remove-HPOVLogicalInterconnectGroup' -Message "No valid session ID found.  Please use Connect-HPOVMgmt to connect and authenticate to an appliance." #-verbose
            $PSCmdlet.ThrowTerminatingError($errorRecord)

        }
    }

    Process {

        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Processing $($logicalEncl.count) objects."

        foreach ($le in $logicalEncl) {

            $logicalEnclNameOrUri = $null;
            $logicalEnclDisplayName = $null;
            if ($le -is [String]) {

                Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] logicalEncl parameter type is String."
                $logicalEnclNameOrUri = $le
                $logicalEnclDisplayName = $le
            }
            elseif ($le -is [PSCustomObject] -and $li.category -ieq 'logical-enclsosures') {
                Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] logicalEncl parameter type is PsCustomObject and correct resource Category type."
                $logicalEnclNameOrUri = $le.uri;
                $logicalEnclDisplayName = $le.name;
            }
            else {
                Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] logicalEncl parameter type is invalid or correct resource Category type is wrong."
                $errorRecord = New-ErrorRecord InvalidOperationException InvalidArgumentValue InvalidArgument 'Remove-HPTBLogicalEnclosure' -Message "The logicalEncl parameter '$logicalEncl' is invalid.  Check the parameter value and try again." #-verbose

                #If more than 1 object is being processed, generate non-terminating error.
                if ($logicalEncl.count -gt 1) { $pscmdlet.WriteError($errorRecord) }

                #If only a single object, generate terminating error.
                else { $pscmdlet.ThrowTerminatingError($errorRecord) }

            }

            if (!$logicalEnclNameOrUri) {
                $errorRecord = New-ErrorRecord InvalidOperationException InvalidArgumentValue InvalidArgument 'Remove-HPTBLogicalEnclosure' -Message "The lig parameter '$logicalEncl' is invalid.  Check the parameter value and try again." #-verbose
                $pscmdlet.ThrowTerminatingError($errorRecord)
            }
            elseif ($pscmdlet.ShouldProcess($logicalEnclDisplayName,'Remove logical enclosure from appliance?')){   
            
                if ([bool]$force) { 
                    $task = Remove-HPOVResource -nameOrUri $logicalEnclNameOrUri -force }
                else { 
                    $task = Remove-HPOVResource -nameOrUri $logicalEnclNameOrUri }
                return $task
            }
        }
    }
}
function New-HPTBNetwork {

    # .ExternalHelp HPOneView.120.psm1-help.xml

    [CmdLetBinding(DefaultParameterSetName = "Ethernet")]
    Param (
        [parameter(Mandatory = $true, ParameterSetName = "FC",Position=0)]
        [parameter(Mandatory = $true, ParameterSetName = "Ethernet",Position=0)]
        [parameter(Mandatory = $true, ParameterSetName = "VLANIDRange",Position=0)]
        [string]$Name, 

        [parameter(Mandatory = $true, ParameterSetName = "FC",Position=1)]
        [parameter(Mandatory = $false, ParameterSetName = "Ethernet",Position=1)]
        [parameter(Mandatory = $false, ParameterSetName = "VLANIDRange",Position=1)]
        [ValidateSet("Ethernet", "FC", "FibreChannel", "Fibre Channel")]
        [string]$type = "Ethernet",
        
        [parameter(Mandatory = $true, ParameterSetName = "Ethernet",Position=2)] 
        [int32]$vlanId,

        [parameter(Mandatory = $true, ParameterSetName = "VLANIDRange",Position=1)]
        [string]$vlanRange,

        [parameter(Mandatory = $false, ParameterSetName = "Ethernet",Position=3)] 
        [parameter(Mandatory = $false, ParameterSetName = "VLANIDRange",Position=2)]
        [ValidateSet('Untagged','Tagged','Tunnel')]
        [string]$VLANType = "Tagged", 

        [parameter(Mandatory = $false, ParameterSetName = "VLANIDRange")]
        [parameter(Mandatory = $false, ParameterSetName = "Ethernet")]
        [ValidateSet("General", "Management", "VMMigration", "FaultTolerance")]
        [string]$purpose = "General", 

        [parameter(Mandatory = $false, ParameterSetName = "VLANIDRange")]
        [parameter(Mandatory = $false, ParameterSetName = "Ethernet")]
        [boolean]$smartLink = $true, 

        [parameter(Mandatory = $false, ParameterSetName = "VLANIDRange")]
        [parameter(Mandatory = $false, ParameterSetName = "Ethernet")]
        [boolean]$privateNetwork = $false, 

        [parameter(Mandatory = $false, ParameterSetName = "FC")]
        [ValidateSet("Auto", "Two_Gbps", "Four_Gbps", "Eight_Gbps", IgnoreCase = $false)]
        [string]$fcUplinkBandwidth = $Null, 

        [parameter(Mandatory = $false, ParameterSetName = "VLANIDRange")]
        [parameter(Mandatory = $false, ParameterSetName = "Ethernet")]
        [parameter(Mandatory = $false, ParameterSetName = "FC")]
        [validaterange(2,20000)]
        [int32]$typicalBandwidth = 2500, 
        
        [parameter(Mandatory = $false, ParameterSetName = "VLANIDRange")]
        [parameter(Mandatory = $false, ParameterSetName = "Ethernet")]
        [parameter(Mandatory = $false, ParameterSetName = "FC")]
        [validaterange(100,20000)]
        [int32]$maximumBandwidth = 10000, 

        [parameter(Mandatory = $false, ParameterSetName = "FC")]
        [int32]$linkStabilityTime = 30, 

        [parameter(Mandatory = $false, ParameterSetName = "FC")]
        [boolean]$autoLoginRedistribution = $False,

        [parameter(Mandatory = $false, ParameterSetName = "FC")]
        [ValidateSet("FabricAttach","FA", "DirectAttach","DA")]
        [string]$fabricType="FabricAttach",

        [parameter(Mandatory = $false, ParameterSetName = "FC", ValueFromPipeline = $True)]
        [ValidateNotNullOrEmpty()]
        [object]$managedSan=$Null,

        [parameter(Mandatory = $true, ParameterSetName = "importFile", HelpMessage = "Enter the full path and file name for the input file.")]
        [Alias("i", "import")]
        [string]$importFile
    )

    Begin {

        If (-not($global:cimgmtSessionId)) { 

            $errorRecord = New-ErrorRecord HPOneview.Appliance.AuthSessionException ResourceExists AuthenticationError $script:HPOneViewAppliance -Message "You are already logged into $Appliance. Please use Disconnect-HPOVMgmt to end your existing session, and then call Connect-HPOVMgmt again." #-verbose
            $PSCmdlet.ThrowTerminatingError($errorRecord)

        }

        if ($fcUplinkBandwidth) {

            Write-Warning "FcUplinkBandwidth parameter has been deprecated and is no longer used. Please specify the Uplink Bandwidth when creating the Uplink Set using New-HPOVUplinkSet -FcUplinkSpeed parameter."

        }
    }
     
    Process {

        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Resolved Parameter Set Name: $($PsCmdLet.ParameterSetName)"

        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Network Type Requested: $($type)"

        switch ($type) {

            "Ethernet" {

                if (-not $vlanRange) {

                    Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Creating '$name' Ethernet Network"

                    $network = [pscustomobject]@{
                    
                        #type                = "ethernet-networkV2"; 
                        type                = "ethernet-networkV3"; 
                        vlanId              = $vlanId; 
                        ethernetNetworkType = $VLANType; 
                        purpose             = $purpose; 
                        name                = $Name; 
                        smartLink           = $smartLink;
                        privateNetwork      = $privateNetwork

                    }

                }

                else {
                    
                    Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Creating bulk '$name' + '$vlanRange' Ethernet Networks"

                    $network = [pscustomobject]@{

                        type           = "bulk-ethernet-network"; 
                        vlanIdRange    = $vlanRange; 
                        purpose        = $purpose; 
                        namePrefix     = $Name; 
                        smartLink      = $smartLink; 
                        privateNetwork = $privateNetwork;
                        bandwidth      = @{
                            
                            typicalBandwidth = $typicalBandwidth;
                            maximumBandwidth = $maximumBandwidth
                            
                        }

                    }

                }

            }
            
            { @("FC","FibreChannel","Fibre Channel") -contains $_ } {

                Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Creating '$name' FC Network"

                #If maxbandiwdth value isn't specified, 10Gb is the default value, must change to 8Gb
                if ( $maximumBandwidth -eq 10000 ){$maximumBandwidth = 8000}

                #Get Managed SAN Fabric URI for Fabric Attach
                if ($managedSan) { 

                    if ($managedSan -is [PSCustomObject] -and $managedSan.category -eq 'fc-sans') { 
                    
                        $managedSanObject = $managedSan 
                        
                    }

                    elseif ($managedSan -is [PSCustomObject] -and -not ($managedSan.category -eq 'fc-sans')) { 
                    
                        $errorRecord = New-ErrorRecord HPOneView.NetworkResourceException InvalidManagedSanUri InvalidArgument 'managedSan' -Message "The Managed SAN object category provided '$($managedSan.category)' is not the the expected value of 'fc-sans'. Please verify the parameter value and try again." #-verbose
                        $PSCmdlet.ThrowTerminatingError($errorRecord)   
                        
                    }

                    elseif ($managedSan -is [String] -and $managedSan.StartsWith($script:fcManagedSansUri)) { 
                    
                        $managedSanObject = [pscustomobject]@{uri = $managedSan}
                        
                    }
                   
                    elseif ($managedSan -is [String] -and $managedSan.StartsWith('/rest/')) { 
                    
                        $errorRecord = New-ErrorRecord HPOneView.NetworkResourceException InvalidManagedSanUri InvalidArgument 'managedSan' -Message "The Managed SAN Uri provided '$managedSan' is incorrect.  Managed SAN URI must begin with '/rest/fc-sans/managed-sans'." #-verbose
                        $PSCmdlet.ThrowTerminatingError($errorRecord)                       
                    
                    }
                    
                    elseif ($managedSan -is [String]) {

						#Get ManagedSan object
                        Try { $managedSanObject = Get-HPOVManagedSan $managedSan }
						
						#If specified ManagedSan object does not exist, generate trappable error
						catch {
		
							$errorRecord = New-ErrorRecord HPOneView.NetworkResourceException InvalidManagedSanName InvalidArgument 'managedSan' -Message "The Managed SAN Name provided '$managedSan' was not found." #-verbose
							$PSCmdlet.ThrowTerminatingError($errorRecord)   

						}

                    }

                }

                else { $managedSanObject = [PSCustomObject]@{ uri = $Null }}

                $network = [pscustomobject]@{

                    type                    = "fc-networkV2"; 
                    name                    = $Name; 
                    linkStabilityTime       = $linkStabilityTime; 
                    autoLoginRedistribution = $autoLoginRedistribution; 
                    fabricType              = $FabricType; 
                    connectionTemplateUri   = $null;
                    managedSanUri           = $managedSanObject.uri
                
                }
                
            }

            default { Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Invalid type: $($type)" }
        }

        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Network Object:  $($network | fl | out-string)"

        If ($importFile) {

            try {

                $network = [string]::Join("", (gc $importfile -ErrorAction Stop)) | convertfrom-json -ErrorAction Stop

            }
            catch [System.Management.Automation.ItemNotFoundException] {

                $errorRecord = New-ErrorRecord System.Management.Automation.ItemNotFoundException InputFileNotFound ObjectNotFound 'New-HPOVNetwork' -Message "$importFile not found.  Please check the filename or path is valid and try again." #-verbose
                    
                #Generate Terminating Error
                $PSCmdlet.ThrowTerminatingError($errorRecord)

            }
            catch [System.ArgumentException] {

                $errorRecord = New-ErrorRecord System.ArgumentException InvalidJSON ParseError 'New-HPOVNetwork' -Message "JSON incorrect or invalid within '$importFile' input file." #-verbose
                    
                #Generate Terminating Error
                $PSCmdlet.ThrowTerminatingError($errorRecord)

            }

        }

    }

    end {

        $colStatus = $null
        $colStatus = @()

        foreach($net in $network) {

            if ($net.defaultTypicalBandwidth) { $typicalBandwidth = $net.defaultTypicalBandwidth }
            if ($net.defaultMaximumBandwidth) { $maximumBandwidth = $net.defaultMaximumBandwidth }
            if ($net.typicalBandwidth) { $typicalBandwidth = $net.typicalBandwidth }
            if ($net.maximumBandwidth) { $maximumBandwidth = $net.maximumBandwidth }

            switch ($net.type) {

                "ethernet-networkV3" {

                    Write-Host "Creating Ethernet Network" $net.name 

                    $netUri = $script:ethNetworksUri

                    $net = $net | select name, type, vlanId, smartLink, privateNetwork, purpose, ethernetNetworkType, connectionTemplateUri

                }
                "ethernet-networkV2" {

                    Write-Host "Creating Ethernet Network" $net.name 

                    $netUri = $script:ethNetworksUri

                    $net = $net | select name, type, vlanId, smartLink, privateNetwork, purpose, ethernetNetworkType, connectionTemplateUri

                }

                "fc-networkV2" {

                    Write-Host "Creating FC Network" $net.name

                    $netUri = $script:fcNetworksUri

                    $net = $net | select name, linkStabilityTime, autoLoginRedistribution, type, fabricType, managedSanUri, connectionTemplateUri 

                }

                "bulk-ethernet-network" {
                    
                    Write-Host "Creating bulk '$name' + '$vlanRange' Ethernet Networks"
                    $netUri = $script:ethNetworksUri + "/bulk"

                }
                
                #Should never get here.  If so, this is an internal error we need to fix.
                default {

                    $errorRecord = New-ErrorRecord System.ArgumentException InvalidNetworkType InvalidType 'New-HPOVNetwork' -Message "(INTERNAL ERROR) The Network Resource Type $($net.type) is invalid for '$($net.name)' network." #-verbose
                    
                    #Generate Terminating Error
                    $PSCmdlet.ThrowTerminatingError($errorRecord)

                }

            }

			if ($net.connectionTemplateUri) { $net.connectionTemplateUri = $Null }

            $objStatus = [pscustomobject]@{ Name = $net.Name; Status = $Null; Details = $Null }

            #Check if Network Type is Direct Attach and if ManagedFabric parameter is being called at the same time.
            if (($fabricType -eq "DirectAttach" -or $fabricType -eq "DA") -and $managedfabric) { 

                $objStatus.Details = "You specified a DirectAttach Fabric Type and passed the ManagedSan parameter.  The ManagedSan parameter is to be used for FabricAttach networks only."
               
            }

            else { $task = Send-HPOVRequest $netUri POST $net }

            if (-not ($task.Uri)) {

                $objStatus.Status = "Failed"
                
                #Do not want to overwrite the details value from the Fabric Type check above.
                if ($task) { $objStatus.Details = $task }

            }

            else { 
                
                #Wait for the network to be created
                $task = Wait-HPOVTaskComplete $task.Uri
                $objStatus.Status = $task.taskState
                $objStatus.Details = $task

            }

            $colStatus += $objStatus

            if($objStatus.details.associatedResource.resourceUri) {

                $net=Send-HPOVRequest $objStatus.details.associatedResource.resourceUri

                if ($net -and $net.connectionTemplateUri) {

                    $ctUri = $net.connectionTemplateUri

                    $ct = Send-HPOVRequest $ctUri

                    if ($ct -and $ct.bandwidth) {

                        if ($typicalBandwidth) { $ct.bandwidth.typicalBandwidth = $typicalBandwidth }

                        if ($maximumBandwidth) { $ct.bandwidth.maximumBandwidth = $maximumBandwidth }

                        Set-HPOVResource -resource $ct | Out-Null

                    }

                }

            }

        }

        if ($colStatus | ? { $_.Status -ne "Completed" }) { write-error "One or more networks failed the creation attempt!" }

        $colStatus
        
    }
}
Function WaitForTask($task, $timeOut){
    $timeCount =0   
    do{
    $timeCount += 1
    Start-Sleep -s 1
    }
    while($task.TaskState -eq "Running" -and $timeOut*60 -ge $timeCount)
}
function Checkpoint-TBirdEnclosureHealth{
Param (
        [parameter(Mandatory = $false)]
        [ValidateNotNullOrEmpty()]
        [string]$enclosureName,
        [parameter(Mandatory = $false)]
        [ValidateNotNullOrEmpty()]
        [string]$enclosureExpectedState,
        [parameter(Mandatory = $false)]
        [ValidateNotNullOrEmpty()]
        [string]$enclosureExpectedStatus,
        [parameter(Mandatory = $false)]
        [ValidateNotNullOrEmpty()]
        [bool]$haltTest=$false
        )

# Get the current state and status for the enclosure
Write-Host("Enclosure Health Check for- {0}" -f $enclosureName)
$enc= (Get-HPOVEnclosure $enclosureName| select name,state,status)
Write-Log -LogPath $CompletePath -LineValue $enc  | Sort-Object name | format-table -Property name,state,status -AutoSize

If ($enc.state -eq $enclosureExpectedState -And $enc.status -match $enclosureExpectedStatus){
    Write-Log -LogPath $CompletePath -LineValue("State and status for enclosure - {0} are as expected, current State - {1} and Status -{2}" -f $enclosureName,$enc.state,$enc.status)
}
else{
    if ($haltTest){
        Write-Host("HALTING TEST PARAMETER SET TO TRUE, EXITING EXECUTION WITH BELOW ERROR")
        throw "State and status for enclosure - {0} are not as expected, current State - {1} and Status -{2}" -f $enclosureName,$enc.state,$enc.status
        }
    else{
        Write-Error("State and status for enclosure - {0} are not as expected, current State - {1} and Status -{2}" -f $enclosureName,$enc.state,$enc.status)
        }
}
}
function Checkpoint-TBirdDeviceBayHealth{
Param (
        [parameter(Mandatory = $false)]
        [ValidateNotNullOrEmpty()]
        [string]$enclosureName,
        [parameter(Mandatory = $false)]
        [ValidateNotNullOrEmpty()]
        [string]$deviceBayExpectedState,
        [parameter(Mandatory = $false)]
        [ValidateNotNullOrEmpty()]
        [string]$deviceBayExpectedStatus,
        [parameter(Mandatory = $false)]
        [ValidateNotNullOrEmpty()]
        [bool]$haltTest=$false
        )

Write-Host("Device Health check for Enclosure - {0}" -f $enclosureName)
$enc= (Get-HPOVEnclosure $enclosureName| select name, deviceBays)
$bays=$enc.deviceBays | select bayNumber,devicePresence,deviceUri
#Write-host $bays  | Sort-Object bayNumber | format-table -Property bayNumber,devicePresence,deviceUri -AutoSize
foreach ($dBay in $bays) {
    if ($dBay.devicePresence -eq "Present") { 
        $device= Send-HPOVRequest $dBay.deviceUri
        Write-Log -LogPath $CompletePath -LineValue("server device bay name - {0}" -f $device.name)
        Write-Log -LogPath $CompletePath -LineValue("Expected state - {0}" -f $deviceBayExpectedState)
        Write-Log -LogPath $CompletePath -LineValue("Expected status - {0}" -f $deviceBayExpectedStatus)
        
        #check for device bay state
        If ($device.state -eq $deviceBayExpectedState){ 
            Write-Log -LogPath $CompletePath -LineValue("State for device bay - {0} is as expected, Current state - {1}" -f $device.name,$device.state)
        }
        else{ 
            if ($haltTest){
                Write-Host("HALTING TEST PARAMETER SET TO TRUE, EXITING EXECUTION WITH BELOW ERROR")
                throw "State for device bay - {0} is not as expected, Current state - {1}" -f $device.name,$device.state
            }
            else{
                Write-Error("State for device bay - {0} is not as expected, Current state - {1}" -f $device.name,$device.state)
                }
        }

        # check for device status
        If ($device.status -match $deviceBayExpectedStatus){
             Write-Log -LogPath $CompletePath -LineValue("status for device bay - {0} is as expected, Current state - {1}" -f $device.name,$device.status)
        }
        else{
            if ($haltTest){
                Write-Host("HALTING TEST PARAMETER SET TO TRUE, EXITING EXECUTION WITH BELOW ERROR")
                throw "status for device bay - {0} is not as expected, Current state - {1}" -f $device.name,$device.status
            }
            else{
                Write-Error("status for device bay - {0} is not as expected, Current state - {1}" -f $device.name,$device.status)
                }
        }
    }
    
}

}
function Checkpoint-TBirdInterconnectBayHealth{
Param (
        [parameter(Mandatory = $false)]
        [ValidateNotNullOrEmpty()]
        [string]$enclosureName,
        [parameter(Mandatory = $false)]
        [ValidateNotNullOrEmpty()]
        [string]$InterconnectBayExpectedState,
        [parameter(Mandatory = $false)]
        [ValidateNotNullOrEmpty()]
        [string]$InterconnectBayExpectedStatus,
        [parameter(Mandatory = $false)]
        [ValidateNotNullOrEmpty()]
        [string]$InterconnectBayExpectedPowerStatus,
        [parameter(Mandatory = $false)]
        [ValidateNotNullOrEmpty()]
        [bool]$haltTest=$false
        )

Write-Host("Interconnects bays for Enclosure Name - {0}" -f $enclosureName)
$enc= (Get-HPOVEnclosure $enclosureName| select name, interconnectBays)
$bays=$enc.interconnectBays | select bayNumber,interconnectUri,interconnectModel
#Write-host $bays  | Sort-Object bayNumber | format-table -Property bayNumber,interconnectUri,interconnectModel -AutoSize
foreach ($iBay in $bays) {
    if ($iBay.interconnectUri) { 
        $interconnect= Send-HPOVRequest $iBay.interconnectUri
        Write-Log -LogPath $CompletePath -LineValue("server Interconnect bay name - {0}" -f $interconnect.name)
        Write-Log -LogPath $CompletePath -LineValue("Expected state - {0}" -f $InterconnectBayExpectedState)
        Write-Log -LogPath $CompletePath -LineValue("Expected status - {0}" -f $InterconnectBayExpectedStatus)
        Write-Log -LogPath $CompletePath -LineValue("Expected status - {0}" -f $InterconnectBayExpectedPowerStatus)
        
        #check for interconnect bay state
        If ($interconnect.state -match $InterconnectBayExpectedState){ Write-Log -LogPath $CompletePath -LineValue("State for Interconnect bay - {0} is as expected, Current state - {1}" -f $interconnect.name,$interconnect.state)
        }
        else{
            if ($haltTest){
                Write-Host("HALTING TEST PARAMETER SET TO TRUE, EXITING EXECUTION WITH BELOW ERROR")
                throw "State for Interconnect bay - {0} is not as expected, Current state - {1}" -f $interconnect.name,$interconnect.state
            }
            else{
                Write-Error("State for Interconnect bay - {0} is not as expected, Current state - {1}" -f $interconnect.name,$interconnect.state)
                } 
        }

        # check for interconnect status
        If ($interconnect.status -match $InterconnectBayExpectedStatus){ Write-Log -LogPath $CompletePath -LineValue("status for interconnect bay - {0} is as expected, Current status - {1}" -f $interconnect.name,$interconnect.status)
        }
        else{
            if ($haltTest){
                Write-Host("HALT TEST PARAMETER SET TO TRUE, EXITING EXECUTION WITH BELOW ERROR")
                throw "status for interconnect bay - {0} is not as expected, Current status - {1}" -f $interconnect.name,$interconnect.status
            }
            else{
                Write-Error("status for interconnect bay - {0} is not as expected, Current status - {1}" -f $interconnect.name,$interconnect.status)
                } 
        }
        #powerStatus
        If ($interconnect.powerState -match $InterconnectBayExpectedPowerStatus){ Write-Log -LogPath $CompletePath -LineValue("Power status for interconnect bay - {0} is as expected, CUrrent Power State - {1}" -f $interconnect.name,$interconnect.powerState)
        }
        else{
            if ($haltTest){
                Write-Host("HALT TEST PARAMETER SET TO TRUE, EXITING EXECUTION WITH BELOW ERROR")
                throw "Power status for interconnect bay - {0} is not as expected, CUrrent Power State - {1}" -f $interconnect.name,$interconnect.powerState
            }
            else{
                Write-Error("Power status for interconnect bay - {0} is not as expected, CUrrent Power State - {1}" -f $interconnect.name,$interconnect.powerState)
                }  
        }
    }
    
}

}
function Checkpoint-TBirdFanBayHealth{
Param (
        [parameter(Mandatory = $false)]
        [ValidateNotNullOrEmpty()]
        [string]$enclosureName,
        [parameter(Mandatory = $false)]
        [ValidateNotNullOrEmpty()]
        [string]$FanBayExpectedStatus,
        [parameter(Mandatory = $false)]
        [ValidateNotNullOrEmpty()]
        [bool]$haltTest=$false
        )

Write-Host("Fan Health check for Enclosure - {0}" -f $enclosureName)
$enc= (Get-HPOVEnclosure $enclosureName| select fanBays)
$bays=$enc.fanBays | select bayNumber,devicePresence,status
#Write-host $bays | Sort-Object bayNumber | format-table -Property bayNumber,devicePresence,status -AutoSize
foreach ($fBay in $bays) {
    if ($fBay.devicePresence -eq "Present") { 
        Write-Log -LogPath $CompletePath -LineValue("server Fan present at bay - {0}" -f $fBay.bayNumber)
        Write-Log -LogPath $CompletePath -LineValue("Expected status - {0}" -f $FanBayExpectedStatus)

        # check for fan status
        If ($fBay.status -match $FanBayExpectedStatus){ Write-Log -LogPath $CompletePath -LineValue("status for fan bay at  - {0} is as expected, Current status - {1}" -f $fBay.bayNumber,$fBay.status)
        }
        else{
            if ($haltTest){
                Write-Host("HALT TEST PARAMETER SET TO TRUE, EXITING EXECUTION WITH BELOW ERROR")
                throw "status for fan bay - {0} is not as expected, Current status - {1}" -f $fBay.bayNumber,$fBay.status
            }
            else{
                Write-Error("status for fan bay - {0} is not as expected, Current status - {1}" -f $fBay.bayNumber,$fBay.status)
                }  
        }
    }
    
}

}
function Checkpoint-TBirdPowerBayHealth{
Param (
        [parameter(Mandatory = $false)]
        [ValidateNotNullOrEmpty()]
        [string]$enclosureName,
        [parameter(Mandatory = $false)]
        [ValidateNotNullOrEmpty()]
        [string]$powerBayExpectedStatus,
        [parameter(Mandatory = $false)]
        [ValidateNotNullOrEmpty()]
        [bool]$haltTest=$false
        )

Write-Host("Power Bay health check for Enclosure - {0}" -f $enclosureName)
$enc= (Get-HPOVEnclosure $enclosureName| select powerSupplyBays)
$bays=$enc.powerSupplyBays | select bayNumber,devicePresence,status
#Write-host $bays  | Sort-Object bayNumber | format-table -Property bayNumber,devicePresence,status -AutoSize
foreach ($pBay in $bays) {
    if ($pBay.devicePresence -eq "Present") { 
        Write-Log -LogPath $CompletePath -LineValue("server power present at bay - {0}" -f $pBay.bayNumber)
        Write-Log -LogPath $CompletePath -LineValue("Expected status - {0}" -f $powerBayExpectedStatus)

        # check for fan status
        If ($pBay.status -match $powerBayExpectedStatus){ Write-Log -LogPath $CompletePath -LineValue("status for power bay at  - {0} is as expected, Current status - {1}" -f $pBay.bayNumber,$pBay.status)
        }
        else{ 
            if ($haltTest){
                Write-Host("HALT TEST PARAMETER SET TO TRUE, EXITING EXECUTION WITH BELOW ERROR")
                throw "status for power bay - {0} is not as expected, Current status - {1}" -f $pBay.bayNumber,$pBay.status
            }
            else{
                Write-Error("status for power bay - {0} is not as expected, Current status - {1}" -f $pBay.bayNumber,$pBay.status)
                }  
        }
    }
    
}

}

function New-HPTBProfile {

    # .ExternalHelp HPOneView.120.psm1-help.xml

	[CmdLetBinding(DefaultParameterSetName = "Default")]
    Param (
        [parameter(Mandatory = $true,ParameterSetName = "Default", Position = 0)]
        [parameter(Mandatory = $true,ParameterSetName = "SANStorageAttach", Position = 0)]
		[ValidateNotNullOrEmpty()]
        [string]$name,

        [parameter(Mandatory = $false, valuefrompipeline = $True, ParameterSetName = "Default", Position = 1)]
        [parameter(Mandatory = $false, valuefrompipeline = $True, ParameterSetName = "SANStorageAttach", Position = 1)]
        [ValidateNotNullOrEmpty()]
        [object]$server = "unassigned",

        [parameter(Mandatory = $false,ParameterSetName = "Default", position = 2)] 
        [parameter(Mandatory = $false,ParameterSetName = "SANStorageAttach", position = 2)]
		[string]$description = $null,

        [parameter(Mandatory = $false,ParameterSetName = "Default", position = 3)]
        [parameter(Mandatory = $false,ParameterSetName = "SANStorageAttach", position = 3)]
		[ValidateNotNullOrEmpty()]
        [array]$connections = @(),

        [parameter(Mandatory = $false,ParameterSetName = "Default",position = 4)]
        [parameter(Mandatory = $false,ParameterSetName = "SANStorageAttach", position = 4)]
		[ValidateNotNullOrEmpty()]
		[Alias('eg')]
        [object]$enclosureGroup = $Null,

        [parameter(Mandatory = $false,ParameterSetName = "Default", position = 5)]
        [parameter(Mandatory = $false,ParameterSetName = "SANStorageAttach", position = 5)]
        [ValidateNotNullOrEmpty()]
		[Alias('sht')]
        [object]$serverHardwareType = $null,

        [parameter(Mandatory = $false,ParameterSetName = "Default")]
        [parameter(Mandatory = $false,ParameterSetName = "SANStorageAttach")]
        [ValidateNotNullOrEmpty()]
        [switch]$firmware,
	
        [parameter(Mandatory = $false,ParameterSetName = "Default")]
        [parameter(Mandatory = $false,ParameterSetName = "SANStorageAttach")]
        [ValidateNotNullOrEmpty()]
        [object]$baseline = $null,

        [parameter(Mandatory = $false,ParameterSetName = "Default")]
        [parameter(Mandatory = $false,ParameterSetName = "SANStorageAttach")]
        [switch]$forceInstallFirmware,
	
        [parameter(Mandatory = $false,ParameterSetName = "Default")]
        [parameter(Mandatory = $false,ParameterSetName = "SANStorageAttach")]
        [ValidateNotNullOrEmpty()]
        [switch]$bios = $false,

	    [parameter(Mandatory = $false,ParameterSetName = "Default")]
        [parameter(Mandatory = $false,ParameterSetName = "SANStorageAttach")]
        [ValidateNotNullOrEmpty()]
        [array]$biosSettings=@(),
        
        [parameter(Mandatory = $false,ParameterSetName = "Default")]
        [parameter(Mandatory = $false,ParameterSetName = "SANStorageAttach")]        
        [ValidateSet("UEFI","UEFIOptimized","BIOS", IgnoreCase = $False)]
        [string]$BootMode = "UEFI",

        [parameter(Mandatory = $false,ParameterSetName = "Default")]
        [parameter(Mandatory = $false,ParameterSetName = "SANStorageAttach")]        
        [ValidateSet("Auto","IPv4","IPv6","IPv4ThenIPv6","IPv6ThenIPv4", IgnoreCase = $False)]
        [string]$pxeBootPolicy = "Auto",

        [parameter(Mandatory = $false,ParameterSetName = "Default")]
        [parameter(Mandatory = $false,ParameterSetName = "SANStorageAttach")]
        [Alias('boot')]
        [switch]$manageBoot,

	    [parameter(Mandatory = $false,ParameterSetName = "Default")]
        [parameter(Mandatory = $false,ParameterSetName = "SANStorageAttach")]
        [array]$bootOrder = @(),

        [parameter(Mandatory = $false,ParameterSetName = "Default")]
        [parameter(Mandatory = $false,ParameterSetName = "SANStorageAttach")]
        [switch]$localstorage,

        [parameter(Mandatory = $false,ParameterSetName = "Default")]
        [parameter(Mandatory = $false,ParameterSetName = "SANStorageAttach")]
        [switch]$Initialize,

        [parameter(Mandatory = $false,ParameterSetName = "Default")]
        [parameter(Mandatory = $false,ParameterSetName = "SANStorageAttach")]        
        [switch]$Bootable,

        [parameter(Mandatory = $false, ParameterSetName = "Default")]
        [parameter(Mandatory = $false,ParameterSetName = "SANStorageAttach")]
        [ValidateSet("RAID1","RAID0","NONE", IgnoreCase=$true)]
        [string]$RaidLevel = $Null,

        [parameter(Mandatory = $True,ParameterSetName = "SANStorageAttach")]
        [switch]$SANStorage,

        [parameter(Mandatory = $true, ParameterSetName = "SANStorageAttach")]
        [ValidateSet('CitrixXen','AIX','IBMVIO','RHEL4','RHEL3','RHEL','RHEV','VMware','Win2k3','Win2k8','Win2k12','OpenVMS','Egenera','Exanet','Solaris9','Solaris10','Solaris11','ONTAP','OEL','HPUX11iv1','HPUX11iv2','HPUX11iv3','SUSE','SUSE9','Inform', IgnoreCase=$true)]
        [Alias('OS')]
        [string]$HostOStype = $Null,

        [parameter(Mandatory = $true, ParameterSetName = "SANStorageAttach")]
        [object]$StorageVolume = $Null,

        [parameter(Mandatory = $false, ParameterSetName = "SANStorageAttach")]
        [Alias('Even')]
        [switch]$EvenPathDisabled,

        [parameter(Mandatory = $false, ParameterSetName = "SANStorageAttach")]
        [Alias('Odd')]
        [switch]$OddPathDisabled,

        [parameter(Mandatory = $false, ParameterSetName = "Default")]
        [parameter(Mandatory = $false,ParameterSetName = "SANStorageAttach")]
        [ValidateSet("Bay","BayAndServer", IgnoreCase=$false)]
        [string]$Affinity = "Bay",
	
        [parameter(Mandatory = $false, ParameterSetName = "Default")]
        [parameter(Mandatory = $false,ParameterSetName = "SANStorageAttach")]
        [ValidateSet("Virtual", "Physical", "UserDefined", IgnoreCase=$true)]
        [string]$macAssignment = "Virtual",

        [parameter(Mandatory = $false,ParameterSetName = "Default")]
        [parameter(Mandatory = $false,ParameterSetName = "SANStorageAttach")]
        [ValidateSet("Virtual", "Physical", "'UserDefined", IgnoreCase=$true)]
        [string]$wwnAssignment = "Virtual",

        [parameter(Mandatory = $false,ParameterSetName = "Default")]
        [parameter(Mandatory = $false,ParameterSetName = "SANStorageAttach")]
        [ValidateSet("Virtual", "Physical", "UserDefined", IgnoreCase=$true)]
        [string]$snAssignment = "Virtual",

		[parameter(Mandatory = $false,ParameterSetName = "Default")]
        [parameter(Mandatory = $false,ParameterSetName = "SANStorageAttach")]
        [string]$serialnumber = $Null,

		[parameter(Mandatory = $false,ParameterSetName = "Default")]
        [parameter(Mandatory = $false,ParameterSetName = "SANStorageAttach")]
        [string]$uuid = $Null,

        [parameter(Mandatory = $false,ParameterSetName = "Default")]
        [parameter(Mandatory = $false,ParameterSetName = "SANStorageAttach")]
        [bool]$hideUnusedFlexNics = $True,

        [parameter(Mandatory = $true, ParameterSetName = "Import")]
        [switch]$Import,
        
        [parameter(Mandatory = $true, ParameterSetName = "Import", ValueFromPipeline = $true)]
        [alias("location","file")]
        [Object]$ProfileObj

    )
	
    Begin {

        if (-not($global:cimgmtSessionId)) {
        
            $errorRecord = New-ErrorRecord HPOneview.Appliance.AuthSessionException NoAuthSession AuthenticationError "New-HPOVProfile" -Message "No valid session ID found.  Please use Connect-HPOVMgmt to connect and authenticate to an appliance." #-verbose
            $PSCmdlet.ThrowTerminatingError($errorRecord)

        }

		if ($snAssignment -eq "UserDefined" -and (-not($serialnumber)) -and (-not($uuid))) {
		
			$errorRecord = New-ErrorRecord HPOneview.ServerProfileResourceException InvalidArgument InvalidArgument 'snAssignment' -Message "The -snAssignment paramter was set to 'UserDefined', however both -serialnumber and -uuid are Null.  You must specify a value for both parameters." #-verbose
            $PSCmdlet.ThrowTerminatingError($errorRecord)
		
		}
		elseif ($snAssignment -eq "UserDefined" -and $serialnumber -and (-not($uuid))) {
		
			$errorRecord = New-ErrorRecord HPOneview.ServerProfileResourceException InvalidArgument InvalidArgument 'uuid' -Message "The -snAssignment paramter was set to 'UserDefined', however -uuid is Null.  You must specify a value for both parameters." #-verbose
            $PSCmdlet.ThrowTerminatingError($errorRecord)

		}
		elseif ($snAssignment -eq "UserDefined" -and (-not($serialnumber)) -and $uuid) {
		
			$errorRecord = New-ErrorRecord HPOneview.ServerProfileResourceException InvalidArgument InvalidArgument 'serialnumber' -Message "The -snAssignment paramter was set to 'UserDefined', however -serialnumber is Null.  You must specify a value for both parameters." #-verbose
            $PSCmdlet.ThrowTerminatingError($errorRecord)
		
		}

        #New Server Resource Object
        $serverProfile = [pscustomobject]@{

            type                  = "ServerProfileV6"; 
            name                  = $name; 
            description           = $description; 
            affinity              = $Affinity;
            hideUnusedFlexNics    = [bool]$hideUnusedFlexNics ;
            bios                  = @{

                manageBios         = [bool]$bios;
                overriddenSettings = $biosSettings

            }; 
            firmware                 = [PSCustomObject]@{

                manageFirmware       = [bool]$firmware;
                firmwareBaselineUri  = [String]$baseline;
                forceInstallFirmware = [bool]$forceInstallFirmware
                 
            };
            boot           = [PSCustomObject]@{
            
                manageBoot = $manageBoot.IsPresent; 
                order      = $bootOrder
                
            };
            bootMode              = $null;
            localStorage          = $null
            serialNumberType      = $snAssignment; 
            macType               = $macAssignment;
            wwnType               = $wwnAssignment;
            connections           = $connections; 
			serialNumber          = $serialnumber;
            serverHardwareUri     = $null;
            serverHardwareTypeUri = $null;
            enclosureGroupUri     = $null;
            sanStorage            = $null;
			uuid                  = $uuid
        }

    }
	
	Process {

        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Bound PS Parameters: $($PSBoundParameters | out-string)"

        $uri = $script:profilesUri

        #Import Server Profile JSON to appliance
        if ($import) {

            if (($ProfileObj -is [System.String]) -and (Test-Path $ProfileObj)) {

                #Recieved file location
                Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Received JSON file as input $($ProfileObj)"
                $serverProfile = (get-content $ProfileObj) -join "`n" | convertfrom-json

				#Remove unique values with Select-Object
				$serverProfile = $serverProfile | Select-Object * -Exclude uri,created,modified,eTag

                Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Sending request"
                $resp = Send-HPOVRequest $script:profilesUri POST $serverProfile

            }

            #Input object could be the JSON object, which is type [System.String]
            elseif ($ProfileObj -is [System.String]) {

                Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Received JSON resource object as input $($ProfileObj | out-string)"
                $serverProfile = $ProfileObj -join "`n" | convertfrom-json

                Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Sending request"
                $resp = Send-HPOVRequest $script:profilesUri POST $serverProfile

            }

            #Input object is PsCustomObject of a Server Profile
            elseif ($ProfileObj -is [PsCustomObject]) {

                Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Received JSON PsCustomObject as input $($ProfileObj | out-string)"
                Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Sending request"
                $resp = Send-HPOVRequest $script:profilesUri POST $ProfileObj

            }

            #Inavlid input type for $ProfileObj and Generate Terminating Error
            else { 

                $errorRecord = New-ErrorRecord HPOneView.ServerProfileResourceException InvalidImportObject InvalidArgument 'New-HPOVPropfile' -Message "Invalid `$Import input object.  Please check the object you provided for ProfileObj parameter and try again" #-verbose
                $PSCmdlet.ThrowTerminatingError($errorRecord)
            
            }
        }

        #We are not going to import a Server Profile
        else {
		
		    # We are creating an unassigned server profile
	        if ($server -eq 'unassigned') {
			
                Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Creating an Unassigned Server Profile"
			
			    #Check to see if the serverHardwareType or enclosureGroup is null, and generate error(s) then break.
			    if (-not $serverHardwareType) {

                    $errorRecord = New-ErrorRecord HPOneView.ServerProfileResourceException InvalidServerHardwareTypeObject InvalidArgument 'New-HPOVPropfile' -Message "Server Hardware Type is missing.  Please provide a Server Hardware Type using the -sht parameter and try again." #-verbose
				    $PSCmdlet.ThrowTerminatingError($errorRecord)

			    }
			
			    #If the URI is passed as the Server Hardware Type, then set the serverHardwareTypeUri variable
			    If ($serverHardwareType -is [string]){

				    if ($serverHardwareType.StartsWith($script:serverHardwareTypesUri)){ 
                        
                        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] SHT URI Provided: $serverHardwareType" 

                        $serverProfile.serverHardwareTypeUri = $serverHardwareType
                        $serverHardwareType = Send-HPOVRequest $serverHardwareType
                        
                    }
				
				    #Otherwise, perform a lookup ofthe SHT based on the name
				    else {

                        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] SHT Name Provided: $serverHardwareType"

					    $serverHardwareType = Get-HPOVServerHardwareType -name $serverHardwareType

                        if ($serverHardwareType) {

					        $serverProfile.serverHardwareTypeUri = $serverHardwareType.uri
					        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] SHT URI: $serverHardwareTypeUri"
                        }

                        else {

                            $errorRecord = New-ErrorRecord HPOneView.ServerProfileResourceException InvalidServerHardwareTypeParameter InvalidArgument 'New-HPOVPropfile' -Message "" #-verbose
                            $PSCmdlet.ThrowTerminatingError($errorRecord)

                        }

				    }

			    }
			
			    #Else the SHT object is passed
			    else { 

                    Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] ServerHardwareType object provided"
                    Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] ServerHardwareType Name: $($serverHardwareType.name)"
                    Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] ServerHardwareType Uri: $($serverHardwareType.uri)"

                    $serverProfile.serverHardwareTypeUri = $serverHardwareType.uri
                    
                }
			
			    
                if (-not $enclosureGroup -and -not ($serverHardwareType.model -match "DL")) {
					    
                    $errorRecord = New-ErrorRecord HPOneView.ServerProfileResourceException InvalidEnclosureGroupObject InvalidArgument 'New-HPOVPropfile' -Message "Enclosure Group is missing.  Please provide an Enclosure Group using the -eg parameter and try again." #-verbose
				    $PSCmdlet.ThrowTerminatingError($errorRecord)

                }

                elseif ($enclosureGroup -is [string]){

				    #If the URI is passed as the Enclosure Group, then set the enclosureGroupUri variable
				    if ($enclosureGroup.StartsWith('/rest')){ $serverProfile.enclosureGroupUri = $enclosureGroup}

				    #Otherwise, perform a lookup ofthe Enclosure Group
				    else{

					    $enclosureGroup = Get-HPOVEnclosureGroup -name $enclosureGroup

                        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] EG URI: $enclosureGroupUri"					    
                        $serverProfile.enclosureGroupUri = $enclosureGroup.uri
					    
				    }

			    }
						
			    #Else the EG object is passed
			    elseif (($enclosureGroup -is [PSCustomObject]) -and ($enclosureGroup.category -eq "enclosure-groups")) { 

                    Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Enclosure Group object provided"
                    Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Enclosure Group Name: $($enclosureGroup.name)"
                    Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Enclosure Group Uri: $($enclosureGroup.uri)"

                    $serverProfile.enclosureGroupUri = $enclosureGroup.uri 

                }

                elseif (-not $enclosureGroup -and ($serverHardwareType.model -match "DL")) {

                    Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Server is a ProLiant DL model. Enclosure Group not required."

                }
                                
                else { 
                
                    #write-error "The Enclosure Group object was invalid." -Category SyntaxError -RecommendedAction "Specify a correct Enclosure Group name, URI or object." -CategorytargetName "New-HPOVProfile" 
                    $errorRecord = New-ErrorRecord HPOneView.ServerProfileResourceException InvalidEnclosureGroupObject InvalidArgument 'New-HPOVPropfile' -Message "Enclosure Group is invalid.  Please specify a correct Enclosure Group name, URI or object and try again." #-verbose

                    #Generate Terminating Error
				    $PSCmdlet.ThrowTerminatingError($errorRecord)
                    
                }

	        }
	
		    # Creating an assigned profile
		    else {
			
			    #Looking for the $server DTO to be string
			    if ($server -is [string]) {
				
				    #If the server URI is passed, look up the server object
				    if ($server.StartsWith($script:serversUri)) {

					    Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Server URI passed: $server"
					    [object]$server = Send-HPOVRequest $server

				    }
				
				    #Else the name is passed and need to look it up.
				    else{

					    [object]$server = Get-HPOVServer -name $server
                    
                        #An error should have been displayed if the server object wasn't found.
                        if (-not ($server)){ break }

				    }

			    }
			
			    Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Server Object: $($server | out-string)"

			    #Check to make sure the server NoProfileApplied is true
			    if (!$server.serverProfileUri) {

				    $serverProfile.serverHardwareUri = $server.uri
				    $serverProfile.serverHardwareTypeUri = $server.serverHardwareTypeUri
				    
                    #Handle Blade Server objects
                    if ($server.serverGroupUri) { $serverProfile.enclosureGroupUri = $server.serverGroupUri }

			    }
			    else {

                    $errorRecord = New-ErrorRecord HPOneView.ServerProfileResourceException ServerProfileAlreadyAssigned ResourceExists 'New-HPOVProfile' -Message "$((Send-HPOVRequest $server.serverProfileUri).name) already has a profile assigned, '$($serverProfile.name)'.  Please specify a different Server Hardware object." #-verbose
				    $pscmdlet.ThrowTerminatingError($errorRecord)

			    }

                #Get the SHT of the SH that we are going to assign.
                $serverHardwareType = Send-HPOVRequest $server.serverHardwareTypeUri

		    }

            #Handle DL Server Profiles by setting BL-specific properties to NULL
            if ($serverHardwareType.model -match "DL") {

                Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Server Hardware Type is a DL, setting 'macType', 'wwnType', 'serialNumberType', 'affinity' and 'hideUnusedFlexNics' to Null."

                $serverProfile.macType            = $Null
                $serverProfile.wwnType            = $Null
                $serverProfile.serialNumberType   = $Null
                $serverProfile.hideUnusedFlexNics = $Null
                $serverProfile.affinity           = $Null

            }

            #Handle Boot Order
            if (-not $PSBoundParameters["bootorder"] -and -not $PSBoundParameters["BootMode"] -and $ManageBoot -and $serverHardwareType.model -match "Gen8") {

                Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] No boot order provided.  Defaulting to ‘CD’,’Floppy’,’USB’,’HardDisk’,’PXE’"
                $serverProfile.boot.order = @(‘CD’,’Floppy’,’USB’,’HardDisk’,’PXE’)

            }
            elseif (-not ($PSBoundParameters["bootorder"]) -and -not ($PSBoundParameters["BootMode"]) -and $ManageBoot -and $serverHardwareType.model -match "Gen9") {`

                Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] No boot order provided.  Defaulting to ‘CD’,’USB’,’HardDisk’,’PXE’"
                $serverProfile.boot.order = @(‘CD’,’USB’,’HardDisk’,’PXE’)

            }
			elseif ($ManageBoot -and $serverHardwareType.model -match "Gen9" -and $bootOrder -contains "Floppy" -and $BootMode -match "EUFI") {

				$errorRecord = New-ErrorRecord HPOneView.ServerProfileResourceException InvalidBootOrderParameterValue InvalidArgument  'BootOrder' -Message "The -bootOrder parameter contains 'Floppy' which is an invalid boot option for a UEFI-based system." #-verbose
				$pscmdlet.ThrowTerminatingError($errorRecord)

			}

            #Check to make sure Server Hardware Type supports Firmware Management (OneView supported G7 blade would not support this feature)
            if ($serverHardwareType.model -match "Gen9") {
                
                Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Gen 9 Server, setting BooMode to: $($BootMode)"

                switch ($BootMode) {

                    "BIOS" {
                    
                        $serverProfile.bootMode = [PSCustomObject]@{
                            manageMode = $true;
                            mode       = $BootMode;
                        }
                    
                    }

                    { "UEFI","UEFIOptimized" -match $_ } {
                    
                        $serverProfile.bootMode = [PSCustomObject]@{
                            manageMode    = $true;
                            mode          = $BootMode;
                            pxeBootPolicy = $pxeBootPolicy
                        }

                        #Generate error stating that bootOrder parameter can only contain a single value when specifying UEFI or UEFIOptimized.
                        if ($bootOrder.length -gt 1) {

                            $errorRecord = New-ErrorRecord HPOneView.ServerProfileResourceException InvalidBootOrderParameterValue InvalidArgument  'BootOrder' -Message "The -bootOrder parameter contains more than 1 entry ($($bootOrder -join ",")).  Only a single value is allowed, and must either be 'HardDisk' or 'PXE'." #-verbose
				            $pscmdlet.ThrowTerminatingError($errorRecord)

                        }
                        
                        #Error if target server model is a DL Gen9 and trying to configure bootOrder
                        if ($serverHardwareType.model -match "DL" -and $serverHardwareType.model -match "Gen9" -and $bootOrder.length -gt 0) {
                        
                            $errorRecord = New-ErrorRecord HPOneView.ServerProfileResourceException BootOrderNotSupported InvalidArgument  '$bootOrder' -Message "The -bootOrder parameter canont be set when BootMode is set to either UEFI or UEFIOptimized.  Please set the -bootOrder value to '`$Null' and try again." #-verbose
				            $pscmdlet.ThrowTerminatingError($errorRecord)                        

                        }

                        #Set the default UEFI/UEFI Optimized BootOrder for Gen9 BL to 'HardDisk'
                        elseif (-not $PSBoundParameters["bootOrder"]) {

                            Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] BootOrder not specified, setting default 'HardDisk'."
                            [array]$serverProfile.boot.order = "HardDisk"

                        }

                        #Override for Gen9 UEFI
                        else { $serverProfile.boot.order = $bootorder }
                    
                    }

                }

            }

            if (-not ($BootMode -eq "BIOS") -and -not ($serverHardwareType.model -match "Gen9" -and $serverHardwareType.model -match "SY")) {

                $errorRecord = New-ErrorRecord HPOneView.ServerProfileResourceException BootModeNotSupported InvalidArgument  'New-HPOVProfile' -Message "The -bootMode parameter was provided and the Server Hardware model '$($serverHardwareType.model)' does not support this parameter.  Please verify the Server Hardware Type is at least an HP ProLiant BL Gen9." #-verbose
				$pscmdlet.ThrowTerminatingError($errorRecord)    

            }
            
			$BootableConnections = @()

            #Loop through connections to look for bootable settings and if -manageboot is omitted from $PSBoundParameters
            foreach ($connection in $serverProfile.connections) {
				
				if ($connection.boot.priority -ne "NotBootable") {

					Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Found bootable connection ID '$($connection.id)'"

					$BootableConnections += $connection.id

				}

			}

			if ((-not($manageBoot.IsPresent)) -and $BootableConnections.count -gt 0) {
				Write-Host "ManageBoot Type" + ($manageBoot.gettype().fullname)
				Write-Host "ManageBoot Present? " $manageBoot.IsPresent
				Write-Host "Bootable Connections: " $BootableConnections.count

				$errorRecord = New-ErrorRecord HPOneView.ServerProfileResourceException BootableConnectionsFound InvalidArgument 'manageBoot' -Message "Bootable Connections $($BootableConnections -join ",") were found, however the -manageBoot switch parameter was not provided.  Please correct your command syntax and try again." #-verbose
				$pscmdlet.ThrowTerminatingError($errorRecord)  

			} 

            #Check to make sure Server Hardware Type supports Firmware Management (OneView supported G7 blade would not support this feature)
            if ($firmware) {
                
                Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Firmware Baseline $($baseline)"

                if ($serverHardwareType.capabilities -match "firmwareUpdate" ) {

                    #Validating that the baseline value is a string type and that it is an SPP name.
		            if (($baseline -is [string]) -and (-not ($baseline.StartsWith('/rest'))) -and ($baseline -match ".iso")) {

                        try {

			                $baseline = Get-HPOVBaseline -isoFileName $baseline
			                $serverProfile.firmware.firmwareBaselineUri = $baseline.uri

                        }

                        catch {

                            Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Error caught when looking for Firmware Baseline."

                            $errorRecord = New-ErrorRecord HPOneView.ServerProfileResourceException InvalidBaselineResourceName ObjectNotFound  'Basline' -Message "The provided SPP Baseline '$($baseline)' was not found or an error occurred during lookup." #-verbose
				            $pscmdlet.ThrowTerminatingError($errorRecord)

                        }

		            }

                    #Validating that the baseline value is a string type and that it is an SPP name.
		            elseif (($baseline -is [string]) -and (-not ($baseline.StartsWith('/rest')))) {

                        try {

			                $baseline = Get-HPOVBaseline -SppName $baseline
			                $serverProfile.firmware.firmwareBaselineUri = $baseline.uri

                        }

                        catch {

                            Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Error caught when looking for Firmware Baseline."

                            $errorRecord = New-ErrorRecord HPOneView.ServerProfileResourceException InvalidBaselineResourceUri ObjectNotFound 'Basline' -Message "The provided SPP Baseline '$($baseline)' was not found or an error occurred during lookup." #-verbose
				            $pscmdlet.ThrowTerminatingError($errorRecord)

                        }

		            }
            
                    #Validating that the baseline value is a string type and that it is the Basline URI
		            elseif (($baseline -is [string]) -and ($baseline.StartsWith('/rest'))) {
			    
			            $baselineObj = Send-HPOVRequest $baseline

                        if ($baselineObj.category -eq "firmware-drivers") {
			            
                            Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Valid Firmware Baseline provided: $($baselineObj.baselineShortName)"
                            $serverProfile.firmware.firmwareBaselineUri = $baselineObj.uri 
                        
                        }
                        else {

                            $errorRecord = New-ErrorRecord HPOneView.ServerProfileResourceException InvalidBaselineResource ObjectNotFound 'Basline' -Message "The provided SPP Baseline URI '$($baseline)' is not valid or the correct resource category (expected 'firmware-drivers', received '$($baselineObj.category)'.  Please check the -baseline parameter value and try again." #-verbose
				            $pscmdlet.ThrowTerminatingError($errorRecord)

                        }

		            }

                    #Else we are expecting the SPP object that contains the URI.
                    elseif (($baseline) -and ($baseline -is [object])) {

                        $serverProfile.firmware.firmwareBaselineUri = $baseline.uri
                    
                    }

                }

                else {

                    $errorRecord = New-ErrorRecord HPOneView.ServerProfileResourceException ServerHardwareMgmtFeatureNotSupported NotImplemented 'New-HPOVProfile' -Message "`"$($serverHardwareType.name)`" Server Hardware Type does not support Firmware Management." #-verbose
				    $pscmdlet.ThrowTerminatingError($errorRecord)
                    
                }

            }

            #Check to make sure Server Hardware Type supports Bios Management (OneView supported G7 blade do not support this feature)
            if ($bios) {

				if ([bool]($bl460bios | Measure-Object).count) {

					$errorRecord = New-ErrorRecord HPOneView.ServerProfileResourceException BiosSettingsIsNull InvalidArgument 'biosSettings' -TargetType 'Array' -Message "BIOS parameter was set to TRUE, but no biosSettings were provided.  Either change -bios to `$False or provide valid bioSettings to set within the Server Profile." #-verbose
					$pscmdlet.ThrowTerminatingError($errorRecord)

				}

				else {
					
					if ($serverHardwareType.capabilities -match "ManageBIOS" ) { 

						#check for any duplicate keys
					    $biosFlag = $false
					    $hash = @{}
					    $biosSettings.id | % { $hash[$_] = $hash[$_] + 1 }

					    foreach ($biosItem in ($hash.GetEnumerator() | ? {$_.value -gt 1} | % {$_.key} )) {
					         
					        $errorRecord = New-ErrorRecord HPOneView.ServerProfileResourceException BiosSettingsNotUnique InvalidOperation 'New-HPOVProfile' -Message "'$(($serverHardwareType.biosSettings | where { $_.id -eq $biosItem }).name)' is being set more than once. Please check your BIOS Settings are unique.  This setting might be a dependency of another BIOS setting/option.  Please check your BIOS Settings are unique.  This setting might be a dependency of another BIOS setting/option." #-verbose
					        $pscmdlet.ThrowTerminatingError($errorRecord)

					    }

					}

					else { 

					    $errorRecord = New-ErrorRecord HPOneView.ServerProfileResourceException ServerHardwareMgmtFeatureNotSupported NotImplemented 'New-HPOVProfile' -Message "`"$($serverHardwareType.name)`" Server Hardware Type does not support BIOS Management." #-verbose
					    $pscmdlet.ThrowTerminatingError($errorRecord)                
					
					}

				}

           }

            #Set Local Storage Management and Check to make sure Server Hardware Type supports it (OneView supported G7 blade would not support this feature)
            if (($localstorage) -and ($serverHardwareType.capabilities -match "ManageLocalStorage" )) {
            
                 $serverProfile.localStorage = [PSCustomObject]@{ 
                     initialize         = [bool]$Initialize;
                     manageLocalStorage = [bool]$localstorage;
                     logicalDrives      = @(

                         @{ 

                             bootable  = [bool]$Bootable;
                             raidLevel = $RaidLevel.ToUpper() 

                         }

                     )

                 }
                 
            }
		    
            #StRM Support
            if ([bool]$SANStorage -and $serverHardwareType.model -match "BL") { 

                Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] SAN Storage being requested"
            
                Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Getting list of available storage systems"
                #Get list of available storage system targets and the associated Volumes based on the EG and SHT provided
                $availStorageSystems = (Send-HPOVRequest ($script:profileAvailStorageSystemsUri + "?enclosureGroupUri=$($serverProfile.enclosureGroupUri)&serverHardwareTypeUri=$($serverHardwareType.uri)")).members

                Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Available Storage Systems: $($availStorageSystems | fl | out-string)"

                #Error on no available storage systems
                if (-not ($availStorageSystems)) {

                    $errorRecord = New-ErrorRecord HPOneView.ServerProfileResourceException NoAvailableStorageSystems ObjectNotFound 'SANStorage' -Message "No available storage systems found for '$($serverHardwareType.name)' Server Hardware Type and '$((Send-HPOVRequest $serverProfile.enclosureGroupUri).name)' Enclosure Group.  Please verify an available Storage System exists, and has connectivity to the destination server or Enclosure Group." #-verbose
				    $pscmdlet.ThrowTerminatingError($errorRecord)  

                }
                
                $serverProfile.sanStorage = [pscustomobject]@{
                    hostOSType        = $script:profileSanManageOSType.($HostOsType);
                    manageSanStorage  = [bool]$SANStorage;
                    volumeAttachments = @()
                }
                
                #Copy the parameter array into a new object
                [Array]$volumesToAttach = $StorageVolume | % { $_ }
                
                Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Volumes to process $($volumesToAttach | fl | out-string)"
                
                $i = 0
                
                #Process volumes being passed
                foreach ($volume in $volumesToAttach) {  

                    #If the storage paths array is null, process connections to add mapping
                    if (-not ($volume.storagePaths)) {

                        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Storage Paths value is Null. Building connection mapping." #-Verbose

                        #Static Volume, must have volumeUri attribute present to be valid
                        if ($volume.volumeUri) {

                            Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Getting list of attachable volumes"

                            #Get list of attachable Volumes (i.e. they are not assigned private or are shareable volumes)
                            $attachableVolumes = (Send-HPOVRequest $script:attachableVolumesUri).members

                            #Get storage volume name for reporting purposes
                            $volumeName = (send-hpovrequest $volume.volumeUri).name

                            Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Processing Volume ID: $($volume.id)"
                            Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Looking to see if volume '$($volume.volumeUri) ($($volumeName))' is attachable"
                
                            #validate volume is attachable
                            $attachableVolFound = $attachableVolumes | ? { $_.uri -eq $volume.volumeUri }

                            #If it is available, continue processing
                            if ($attachableVolFound) {
                
                                Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] '$($attachableVolFound.uri) ($($attachableVolFound.name))' volume is attachable"
                
                                #validate the volume that is available, is also avialable to the server hardware type and enclosure group
                                $volumeToStorageSystem = $availStorageSystems | ? { $_.storageSystemUri -eq $attachableVolFound.storageSystemUri }
                
                                #If available, process the volume networks
                                if ($volumeToStorageSystem) { 
                                
                                    #Check to make sure profile connections exist.
                                    if ($serverProfile.connections -and $serverProfile.connections.functionType -contains "FibreChannel") {

                                        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Profile has connections"
                                    
                                        #loop through profile connections
                                        $found = 0

                                        foreach ($volConnection in $attachableVolFound.availableNetworks) {

                                            #Write-Log -LogPath $CompletePath -LineValue "Looking for $volConnection"
                                            $profileConnection = $serverProfile.connections | ? { $_.networkUri -eq $volConnection }

                                            if ($profileConnection) {

                                                #Keep track of the connections found for error reporting later
                                                $found++

                                                Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Mapping connection ID '$($profileConnection.id)' -> volume ID '$($volumesToAttach[$i].id)'"
                                            
                                                $volumesToAttach[$i].storagePaths += @(
                                                    [pscustomobject]@{
                                                        connectionId = $profileConnection.id;
                                                        isEnabled    = $True
                                                    }
                                                )

                                            }

                                        }

                                        if (-not ($found)) {

                                            $uri += "?force=true"

                                            #Generate non-terminating error and continue
                                            $errorRecord = New-ErrorRecord HPOneView.ServerProfileResourceException NoProfileConnectionsMapToVolume ObjectNotFound 'New-HPOVProfile' -Message "Unable to find a Profile Connection that will map to '$($volumeName)'. Creating server profile resource without Volume Connection Mapping."  #-verbose
                                            #$PSCmdlet.ThrowTerminatingError($errorRecord)
                                            $PSCmdlet.WriteError($errorRecord)

                                        }
                                    
                                    }

                                    #Else, generate an error that at least one FC connection must exist in the profile in order to attach volumes.
                                    else {

                                        $errorRecord = New-ErrorRecord HPOneView.ServerProfileResourceException NoProfileConnections ObjectNotFound 'New-HPOVProfile' -Message "The profile does not contain any Network Connections.  The Profile must contain at least 1 FC Connection to attach Storage Volumes.  Use the New-HPOVProfileConnection helper cmdlet to create 1 or more connections and try again."  #-verbose
                                        $PSCmdlet.ThrowTerminatingError($errorRecord)

                                    }
                
                                }
                
                                #If not, then error
                                elseif (-not($volumeToStorageSystem)) { 
                            
                                    $errorRecord = New-ErrorRecord InvalidOperationException StorageVolumeDoesNotExistOnStorageArray ObjectNotFound 'New-HPOVProfile' -Message "'$($volumeName)' Volume is not available on the '$($volumeToStorageSystem.storageSystemName)' storage system" #-verbose
                                    $PSCmdlet.ThrowTerminatingError($errorRecord)                      
                            
                                }
                
                            }
                
                            elseif (-not ($attachableVolFound)) { 
                        
                                $errorRecord = New-ErrorRecord InvalidOperationException StorageVolumeUnavailableForAttach ResourceUnavailable 'New-HPOVProfile' -Message "'$($volumeName)' Volume is not available to be attached to the profile. Please check the volume and try again."  #-verbose
                                $PSCmdlet.ThrowTerminatingError($errorRecord)

                            }

                        }

                        #Ephemeral volume support
                        elseif (-not ($volume.volumeUri) -and $volume.volumeStoragePoolUri -and $volume.volumeStorageSystemUri) {

                            Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] No volumeUri, ephemeral volume request."

                            #Check to make sure profile connections exist.
                            if ($serverProfile.connections -and $serverProfile.connections.functionType -contains "FibreChannel") {

                                Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Profile has connections"

                                #Process available storage system and available FC networks
                                $storageSystemVolCreate = $availStorageSystems | where { $_.storageSystemUri -eq $volume.volumeStorageSystemUri }

                                if ($storageSystemVolCreate) {
                                    
                                    #loop through profile connections
                                    $found = 0

                                    foreach ($storageSystemConnection in $storageSystemVolCreate.connections) {

                                        $profileConnection = $serverProfile.connections | ? { $_.networkUri -eq $storageSystemConnection }

                                        if ($profileConnection) {

                                            #Keep track of the connections found for error reporting later
                                            $found++
                                            Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Mapping connection ID '$($profileConnection.id)' -> volume ID '$($volumesToAttach[$i].id)'"
                                            
                                            $volumesToAttach[$i].storagePaths += @(
                                                
                                                [pscustomobject]@{
                                                
                                                    connectionId      = $profileConnection.id;
                                                    isEnabled         = $True;
                                                    storageTargetType =  "Auto"

                                                }
                                            
                                            )

                                        }

                                    }

                                    if (!$found) {
                                    
                                        $uri += "?force=true"

                                        #Generate non-terminating error and continue
                                        $errorRecord = New-ErrorRecord HPOneView.ServerProfileResourceException NoProfileConnectionsMapToVolume ObjectNotFound 'New-HPOVProfile' -Message "Unable to find a Profile Connection that will map to '$($volumeName)'. Creating server profile resource without Volume Connection Mapping."  #-verbose
                                        #$PSCmdlet.ThrowTerminatingError($errorRecord)
                                        $PSCmdlet.WriteError($errorRecord)

                                
                                    }

                                }

                                else {

                                    $errorRecord = New-ErrorRecord HPOneView.ServerProfileResourceException StorageSystemNotFound ObjectNotFound 'New-HPOVProfile' -Message "The provided Storage System URI '$($volume.volumeStorageSystemUri)' for the ephemeral volume '$($volume.name)' was not found as an available storage system."  #-verbose
                                    $PSCmdlet.ThrowTerminatingError($errorRecord)

                                }
                                    
                            }

                            #Else, generate an error that at least one FC connection must exist in the profile in order to attach volumes.
                            else {

                                $errorRecord = New-ErrorRecord HPOneView.ServerProfileResourceException NoProfileConnections ObjectNotFound 'New-HPOVProfile' -Message "The profile does not contain any Network Connections.  The Profile must contain at least 1 FC Connection to attach Storage Volumes.  Use the New-HPOVProfileConnection helper cmdlet to create 1 or more connections and try again."  #-verbose
                                $PSCmdlet.ThrowTerminatingError($errorRecord)

                            }

                        }
 
                    }
                    
                    $i++
                }

                $serverProfile.sanStorage.volumeAttachments = $volumesToAttach
                
                #Check to see if user passed -EvenPathDisable and/or -OddPathDisable parameter switches
                if ($EvenPathDisabled.IsPresent -or $OddPathDisabled.IsPresent) {
                    
                    if ($EvenPathDisabledd.IsPresent) { Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Disable Even Path: $([bool]$EvenPathDisable)" }
                    if ($OddPathDisable.IsPresent) { Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Disable Odd Path: $([bool]$OddPathDisable)" }

                    #Keep track of Volume Array index
                    $v = 0
                    foreach ($vol in $serverProfile.sanStorage.volumeAttachments) {
                        
                        #Keep track of Volume Path Array index
                        $p = 0
                        foreach ($path in $vol.storagePaths) {

                            if ([bool]$OddPathDisabled -and [bool]($path.connectionID % 2)) { $isEnabled = $false }
                            elseif ([bool]$EvenPathDisabled -and [bool]!($path.connectionID % 2)) { $isEnabled = $false }
                            else { $isEnabled = $true }

                            Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Setting Connection ID '$($path.connectionID)' path enabled:  $($isEnabled)"

                            $serverProfile.sanStorage.volumeAttachments[$v].storagePaths[$p].isEnabled = $isEnabled
                            $p++
                        }

                        $v++

                    }
                    
                }

            }

		    Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Profile: $($serverProfile | out-string)"
	        $resp = Send-HPOVRequest $uri POST $serverProfile

	    }

    }

    End {

        return $resp
        
    }
}


function New-TBirdServerProfile_old{
Param (
        [parameter(Mandatory = $false)]
        [ValidateNotNullOrEmpty()]
        [string]$enclosureName,
        [parameter(Mandatory = $false)]
        [ValidateNotNullOrEmpty()]
        [string]$sppFileName
                
        )

Write-Host("Create Server Profiles for Enclosure - {0}" -f $enclosureName)
$enc= (Get-HPOVEnclosure $enclosureName| select name, deviceBays)
$bays=$enc.deviceBays | select bayNumber,devicePresence,deviceUri
#Write-Output $bays  | Sort-Object bayNumber | format-table -Property bayNumber,devicePresence,deviceUri -AutoSize
$sppTasks = @()
foreach ($dBay in $bays) {
    if ($dBay.devicePresence -eq "Present") { 
        $device= Send-HPOVRequest $dBay.deviceUri
        Write-Host("server device bay name - {0}" -f $device.name)
        if ($device.powerState -ne "Off") {
            Write-Host "Server" $device.name "is" $device.powerState ".  Powering it off..."
            $task = Set-HPOVServerPower -serverUri $device.uri -powerState "Off" -powerControl "PressAndHold"
            Write-Host $task.name $task.taskStatus
            $task = Wait-HPOVTaskComplete -taskUri $task.uri
        }

        #create profile
        if ($device.state -eq "NoProfileApplied") { 
            $profileName = "Profile-" + $device.name
            Write-Host "Creating" $profileName "for server" $device.name
            <#
            # Add netrwork for this server
            $net = Get-HPOVNetwork $ethNetworks
            $con = New-HPOVProfileConnection -id 1 -type Ethernet -network $net
            $conList = @($con)
            #>
            $task = New-HPTBProfile -name $profileName -server $device
            Write-Log -LogPath $CompletePath -LineValue $task
            Write-Host $task.name $task.taskStatus
            $task = Wait-HPOVTaskComplete -taskUri $task.uri

            $profile = Send-HPOVRequest $task.associatedResource.resourceUri
            # ADVANCED SERVER SETTINGS
            # First view the capabilities of the server hardware for this profile
            $serverType = Send-HPOVRequest $profile.serverHardwareTypeUri
            # Now update the firmware of the profile.  
            if ($sppFileName) {
                #$fw = Get-HPOVSppFile $sppFileName
                 $fw = Get-HPOVBaseLine -isoFileName $sppFileName
                #$fw = (Get-HPOVBaseline).name
                # Now select the firmware SPP in the server profile
                
                $profile.firmware.manageFirmware = $true
                $profile.firmware.firmwareBaselineUri = $fw.uri
                $profile.firmware.forceInstallFirmware = $true
                $profile.firmware.firmwareInstallType = "FirmwareOnlyOfflineMode"
                $task = Set-HPOVResource $profile
                $sppTasks += $task.uri
            }
        }
    }
}
#return the list of task to caller
if($sppTasks){
    return ,$sppTasks
    }
#wait for tasks to be completed
#if ($sppFileName) {
#$task=Get-HPOVTask -ResourceCategory server-profiles | Wait-HPOVTaskComplete -timeout (New-TimeSpan -Minutes 60)
#Power On the devices
#foreach ($dBay in $bays) {
#    if ($dBay.devicePresence -eq "Present"){
#        Write-Host "device at bay " $dbay.bayNumber "Powering it On..."
#        $task = Set-HPOVServerPower -serverUri $dbay.deviceUri -powerState "On" -powerControl "MomentaryPress"
#        }
#    }
#}
}


Function Update-TBirdFW{
   <#
    .SYNOPSIS 
      Update the TBird Enclosure component firmware ( During LE cration provide firmware baseline with force option) with specified SSP bundle in in runner file

    .Description
      Update the TBird Enclosure component firmware ( During LE cration provide firmware baseline with force option) with specified SSP bundle in in runner file

    .EXAMPLE
     #Update-TBirdFW -ligs $ligs -enclosureNames "0000A66101" -enclGroupName $enclGroupName -path $sppPath -haltTest $false

     .EXAMPLE
     #Update-TBirdFW -ligs $ligs -enclosureNames "0000A66101,0000A66102" -enclGroupName $enclGroupName -path $sppPath -haltTest $false
     
     This cmdlet will import and use the HPOneView public library 
  #>
    Param(
             [parameter(Mandatory = $true, HelpMessage = "Enter the lig details -",Position=0)]
             [ValidateNotNullOrEmpty()]
             $ligs,

             [parameter(Mandatory = $true, HelpMessage = "Please enter the Enclosure names (seperated by ',') -",Position=1)]
             [ValidateNotNullOrEmpty()]
             [string[]] $enclosureNames,

             [parameter(Mandatory = $true, HelpMessage = "Please enter the Enclosure Group name -",Position=2)]
             [string] $enclGroupName,

             [parameter(Mandatory = $true, HelpMessage = "Enter the SPP File path -",Position=5)]
             [ValidateNotNullOrEmpty()]
             [string] $path,

             [parameter(Mandatory = $true, HelpMessage = "Enter the halttest condition, True will discontinue where False will continue the run as per expected health check states-",Position=6)]
             [ValidateNotNullOrEmpty()]
             [boolean]$haltTest = $False,
             [parameter(Mandatory = $false, HelpMessage = "Enter the True\False for force Firmware installation-")]
             [boolean]$forceInstallFirmware = $true,
             [parameter(Mandatory = $true, HelpMessage = "Enter the LE Name-")]
             [String]$leName


    )
    
    $SNMP = @{readCommunity = "MyTr@p1"; enabled=$True; systemContact = "Network Admin"; snmpAccess = @("192.168.1.2/32","10.1.1.0/24");trapDestinations = @(@{trapDestination="myhost.local";communityString="MyTr@p2";trapFormat="SNMPv1";trapSeverities=@("Critical", "Major", "Minor", "Warning", "Normal", "Info", "Unknown");fcTrapCategories=@("PortStatus", "Other")})}
    $upsName = "TB_Uplink_" + $netName

    #Input for Enclosure Group
    $ipAddressingMode = "DHCP"

    #firmware details
    #get the fileName of spp iso
    $sppIsoFileName = $path.Substring($path.LastIndexOf('\')+1) #"SPPGen9Snap5.2015_0814.22.iso"

    #get the name as appliance store SPPGen9Snap5.2015_0814.22.iso => SPPGen9Snap5_2015_0814_22.iso
    $newSppIsoFileName = $sppIsoFileName -replace "(\d)\.(\d)", '$1_$2'
       
    #HEALTH CHECK FOR THE ENCLOSURE  
    ForEach ($encl in $enclosureNames) {
        Checkpoint-TBirdEnclosureHealth -enclosureName $encl -enclosureExpectedState "Monitored" -enclosureExpectedStatus "(?i)Warning|OK" -haltTest $haltTest
        Checkpoint-TBirdDeviceBayHealth -enclosureName $encl -deviceBayExpectedState "Monitored" -deviceBayExpectedStatus "(?i)Warning|OK" -haltTest $haltTest
        Checkpoint-TBirdInterconnectBayHealth -enclosureName $encl -InterconnectBayExpectedState "Monitored" -InterconnectBayExpectedStatus "(?i)Warning|OK" -InterconnectBayExpectedPowerStatus "(?i)On|Off" -haltTest $haltTest

        Checkpoint-TBirdFanBayHealth -enclosureName $encl -FanBayExpectedStatus "(?i)Warning|OK" -haltTest $haltTest
        Checkpoint-TBirdPowerBayHealth -enclosureName $encl -powerBayExpectedStatus "(?i)Warning|OK" -haltTest $haltTest
    }
    
    ####Add sppfile
    $firmwareBaselineName = Add-LatestSpp $path $newSppIsoFileName
      
   #Create Lig
   New-lig $ligs

    #Create Eg
    New-eg -ligs $ligs -enclGroupName $enclGroupName
    
    #Create Le
    $buildingUri = $enclosureGroupsUri + "?filter=name=$enclGroupName" 
    $enclGroupName = (Send-HPOVRequest (Send-HPOVRequest $buildingUri).members.uri).name
    #Exit the program if EG not found  
	if(-Not $enclGroupName){ throw "EG [$enclGroupName] not found"}

    Write-Host "############## Creating Le $leName"
    Write-Log -LogPath $CompletePath -LineValue "############## Creating Le $leName"
    
    $letask = New-HPTBLogicalEnclosure $leName -enclGroupName $enclGroupName $enclosureNames $firmwareBaselineName $forceInstallFirmware
    Write-Host "waiting on LE creation"
    Write-Log -LogPath $CompletePath -LineValue "waiting on LE cration"
    wait-for-task -task_uri $letask.uri -timeout 7200
  
    #power on the devices on successful LE creation
    $buildingUri = $logicalEnclosuresUri + "?filter=name=$leName"
    $OVLeName = (Send-HPOVRequest (Send-HPOVRequest $buildingUri).members.uri).name
    
    if($leName -eq $OVLeName){
        start-servers -enclosureNames $enclosureNames -timeout 600
        
        #HEALTH CHECK FOR THE ENCLOSURE
        ForEach ($encl in $enclosureNames) {
            Checkpoint-TBirdEnclosureHealth -enclosureName $encl -enclosureExpectedState "Configured" -enclosureExpectedStatus "(?i)Warning|OK" -haltTest $haltTest
            Checkpoint-TBirdDeviceBayHealth -enclosureName $encl -deviceBayExpectedState "NoProfileApplied" -deviceBayExpectedStatus "(?i)Warning|OK" -haltTest $haltTest
            Checkpoint-TBirdInterconnectBayHealth -enclosureName $encl -InterconnectBayExpectedState "(?i)Configured|Monitored" -InterconnectBayExpectedStatus "(?i)Warning|OK" -InterconnectBayExpectedPowerStatus "(?i)On|Off" -haltTest $haltTest
            Checkpoint-TBirdFanBayHealth -enclosureName $encl -FanBayExpectedStatus "(?i)Warning|OK" -haltTest $haltTest 
            Checkpoint-TBirdPowerBayHealth -enclosureName $encl -powerBayExpectedStatus "(?i)Warning|OK" -haltTest $haltTest
        }
    }
    
}

Function Update-TBirdBBFW{
   <#
    .SYNOPSIS 
      Update firmware using BigBang SharedInfrastructureAndServerProfiles on EM, Interconnect and servers with specified SSP bundle

    .Description
      Update firmware using BigBang SharedInfrastructureAndServerProfiles on EM, Interconnect and servers with specified SSP bundle

    .EXAMPLE
    Update-TBirdBBFW -ligs $ligs -enclosureNames "0000A66101" -enclGroupName $enclGroupName -path $sppPath -haltTest $false

    .EXAMPLE
     Update-TBirdBBFW -ligs $ligs -enclosureNames "0000A66101, 0000A66102" -enclGroupName $enclGroupName -path $sppPath -haltTest $false
     
     This cmdlet will import and use the HPOneView public library 
  #>
    Param(
             [parameter(Mandatory = $true, HelpMessage = "Enter the lig details -",Position=0)]
             [ValidateNotNullOrEmpty()]
             $ligs,

             [parameter(Mandatory = $true, HelpMessage = "Please enter the Enclosure names (seperated by ',') -",Position=1)]
             [ValidateNotNullOrEmpty()]
             [string[]] $enclosureNames,

             [parameter(Mandatory = $true, HelpMessage = "Please enter the Enclosure Group name -",Position=2)]
             [string] $enclGroupName,

             [parameter(Mandatory = $true, HelpMessage = "Enter the SPP File path -",Position=5)]
             [ValidateNotNullOrEmpty()]
             [string] $path,

             [parameter(Mandatory = $true, HelpMessage = "Enter the halttest condition, True will discontinue where False will continue the run as per expected health check states-",Position=6)]
             [ValidateNotNullOrEmpty()]
             [boolean]$haltTest = $False,

             [parameter(Mandatory = $false, HelpMessage = "Enter the True\False for force Firmware installation-")]
             [boolean]$forceInstallFirmware = $true,
             [parameter(Mandatory = $false, HelpMessage = "Enter the Logical Interconnect Activation Mode[Orchestrated or Parallel]-")]
             # $logicalinterconnectActivationMode = "Orchestrated",
             $logicalinterconnectActivationMode = "Parallel",   

             [parameter(Mandatory = $true, HelpMessage = "Enter the LE Name-")]
             [String]$leName
    )


    $SNMP = @{readCommunity = "MyTr@p1"; enabled=$True; systemContact = "Network Admin"; snmpAccess = @("192.168.1.2/32","10.1.1.0/24");trapDestinations = @(@{trapDestination="myhost.local";communityString="MyTr@p2";trapFormat="SNMPv1";trapSeverities=@("Critical", "Major", "Minor", "Warning", "Normal", "Info", "Unknown");fcTrapCategories=@("PortStatus", "Other")})}
    $upsName = "TB_Uplink_" + $netName

    #Input for Enclosure Group
    #$ligList = @($ligName)
    $ipAddressingMode = "DHCP"

    #firmware details
    #get the fileName of spp iso
    $sppIsoFileName = $path.Substring($path.LastIndexOf('\')+1) #"SPPGen9Snap5.2015_0814.22.iso"

    #get the name as appliance store SPPGen9Snap5.2015_0814.22.iso => SPPGen9Snap5_2015_0814_22.iso
    $newSppIsoFileName = $sppIsoFileName -replace "(\d)\.(\d)", '$1_$2'
            

    #HEALTH CHECK FOR THE ENCLOSURE  
    ForEach ($encl in $enclosureNames) {
        Checkpoint-TBirdEnclosureHealth -enclosureName $encl -enclosureExpectedState "Monitored" -enclosureExpectedStatus "(?i)Warning|OK" -haltTest $haltTest
        Checkpoint-TBirdDeviceBayHealth -enclosureName $encl -deviceBayExpectedState "Monitored" -deviceBayExpectedStatus "(?i)Warning|OK" -haltTest $haltTest
        Checkpoint-TBirdInterconnectBayHealth -enclosureName $encl -InterconnectBayExpectedState "Monitored" -InterconnectBayExpectedStatus "(?i)Warning|OK" -InterconnectBayExpectedPowerStatus "(?i)On|Off" -haltTest $haltTest

        Checkpoint-TBirdFanBayHealth -enclosureName $encl -FanBayExpectedStatus "(?i)Warning|OK" -haltTest $haltTest
        Checkpoint-TBirdPowerBayHealth -enclosureName $encl -powerBayExpectedStatus "(?i)Warning|OK" -haltTest $haltTest
    }
    
    ####Add sppfile
    $firmwareBaselineName =Add-LatestSpp $path $newSppIsoFileName
    
    #Create Lig
    New-lig $ligs 

    #Create Eg
    New-eg -ligs $ligs -enclGroupName $enclGroupName
   
    #Create Le
    $buildingUri = $enclosureGroupsUri + "?filter=name=$enclGroupName" 
    $enclGroupName = (Send-HPOVRequest (Send-HPOVRequest $buildingUri).members.uri).name
    #Exit the program if EG not found  
	if(-Not $enclGroupName){ throw "EG [$enclGroupName] not found"}
	
    Write-Host "############## Creating Le $leName"
    $letask = New-HPTBLogicalEnclosure -name $leName -enclGroupName $enclGroupName -enclosureNames $enclosureNames
    Write-Host "waiting on LE cration"
    Write-Log -LogPath $CompletePath -LineValue "waiting on LE creation"
    wait-for-task -task_uri $letask.uri -timeout 7200
    
    stop-servers -enclosureNames $enclosureNames -timeout 600
    New-TBirdServerProfile -enclosureName $enclosureNames
    # BigBang Firmware update
    Write-Host "Initiating Big Bang Update SharedInfrastructureAndServerProfiles"
    $task =Update-HPTBLogicalEnclosureFirmwareUpdate -name $leName -sppFileName $firmwareBaselineName -firmwareUpdateOn "SharedInfrastructureAndServerProfiles" -forceInstallFirmware $forceInstallFirmware -logicalinterconnectActivationMode $logicalinterconnectActivationMode

    Write-Host "waiting on Big Bang firmware Update [SharedInfrastructureAndServerProfiles]"
    wait-for-task -task_uri $task.uri -timeout 7200 

    #power on the devices on successful LE creation
    $buildingUri = $logicalEnclosuresUri + "?filter=name=$leName"
    $OVLeName = (Send-HPOVRequest (Send-HPOVRequest $buildingUri).members.uri).name
    
    if($leName -eq $OVLeName){
        #HEALTH CHECK FOR THE ENCLOSURE
        ForEach ($encl in $enclosureNames) {
            Checkpoint-TBirdEnclosureHealth -enclosureName $encl -enclosureExpectedState "Configured" -enclosureExpectedStatus "(?i)Warning|OK" -haltTest $haltTest
            Checkpoint-TBirdDeviceBayHealth -enclosureName $encl -deviceBayExpectedState "ProfileApplied" -deviceBayExpectedStatus "(?i)Warning|OK" -haltTest $haltTest
            Checkpoint-TBirdInterconnectBayHealth -enclosureName $encl -InterconnectBayExpectedState "(?i)Configured|Monitored" -InterconnectBayExpectedStatus "(?i)Warning|OK" -InterconnectBayExpectedPowerStatus "(?i)On|Off" -haltTest $haltTest
            Checkpoint-TBirdFanBayHealth -enclosureName $encl -FanBayExpectedStatus "(?i)Warning|OK" -haltTest $haltTest  
            Checkpoint-TBirdPowerBayHealth -enclosureName $encl -powerBayExpectedStatus "(?i)Warning|OK" -haltTest $haltTest
        }
    }
        
}

Function Update-TBirdBBFW-Options{
   <#
    .SYNOPSIS 
      BigBang firmware Update with different choices, profileFirmare, [EnclosureOnly] | [SharedInfrastructureOnly] using specified SSP bundle

    .Description
      BigBang firmware Update with different choices, profileFirmare, [EnclosureOnly] | [SharedInfrastructureOnly] using specified SSP bundle

    .EXAMPLE
    Update-TBirdBBFW-Options -ligs $ligs -enclosureNames "0000A66101" -path $sppPath -haltTest $false -profileFirmware $false -bigBangFirmwareoption "EnclosureOnly"

    .EXAMPLE
    Update-TBirdBBFW-Options -ligs $ligs -enclosureNames "0000A66101" -path $sppPath -haltTest $false -profileFirmware $true -bigBangFirmwareoption "SharedInfrastructureOnly"

    .EXAMPLE
    Update-TBirdBBFW-Options -ligs $ligs -enclosureNames "0000A66101" -path $sppPath -haltTest $false -profileFirmware $false -bigBangFirmwareoption "SharedInfrastructureOnly"

    .EXAMPLE
    Update-TBirdBBFW-Options -ligs $ligs -enclosureNames "0000A66101" -path $sppPath -haltTest $false -profileFirmware $true -bigBangFirmwareoption "EnclosureOnly"
        
     
    This cmdlet will import and use the HPOneView public library 
  #>
    Param(
             [parameter(Mandatory = $true, HelpMessage = "Enter the lig details -",Position=0)]
             [ValidateNotNullOrEmpty()]
             $ligs,

             [parameter(Mandatory = $true, HelpMessage = "Please enter the Enclosure names (seperated by ',') -",Position=1)]
             [ValidateNotNullOrEmpty()]
             [string[]] $enclosureNames,
			
			[parameter(Mandatory = $true, HelpMessage = "Please enter the Enclosure Group name -",Position=2)]
            [string] $enclGroupName,
			
             [parameter(Mandatory = $true, HelpMessage = "Enter the SPP File path -",Position=5)]
             [ValidateNotNullOrEmpty()]
             [string] $path,

             [parameter(Mandatory = $true, HelpMessage = "Enter the halttest condition, True will discontinue where False will continue the run as per expected health check states-",Position=6)]
             [ValidateNotNullOrEmpty()]
             [boolean]$haltTest = $False,

             [parameter(Mandatory = $true, HelpMessage = "Enter the True\False for Profile Firmware update-")]
             [boolean]$profileFirmware,
             [parameter(Mandatory = $true, HelpMessage = "Enter the BigBang option for Firmware update [EnclosureOnly] | [SharedInfrastructureOnly] | [SharedInfrastructureAndServerProfiles] -")]
             $bigBangFirmwareoption,
             [parameter(Mandatory = $false, HelpMessage = "Enter the True\False for force Firmware installation-")]
             [boolean]$forceInstallFirmware = $true,
             [parameter(Mandatory = $false, HelpMessage = "Enter the Logical Interconnect Activation Mode[Orchestrated or Parallel]-")]
             [String]$logicalinterconnectActivationMode = "Orchestrated",
             [parameter(Mandatory = $true, HelpMessage = "Enter the LE Name-")]
             [String]$leName

    )


    $SNMP = @{readCommunity = "MyTr@p1"; enabled=$True; systemContact = "Network Admin"; snmpAccess = @("192.168.1.2/32","10.1.1.0/24");trapDestinations = @(@{trapDestination="myhost.local";communityString="MyTr@p2";trapFormat="SNMPv1";trapSeverities=@("Critical", "Major", "Minor", "Warning", "Normal", "Info", "Unknown");fcTrapCategories=@("PortStatus", "Other")})}
    $upsName = "TB_Uplink_" + $netName

    $ipAddressingMode = "DHCP"

    #firmware details
    #get the fileName of spp iso
    $sppIsoFileName = $path.Substring($path.LastIndexOf('\')+1) #"SPPGen9Snap5.2015_0814.22.iso"

    #get the name as appliance store SPPGen9Snap5.2015_0814.22.iso => SPPGen9Snap5_2015_0814_22.iso
    $newSppIsoFileName = $sppIsoFileName -replace "(\d)\.(\d)", '$1_$2'
      
    #HEALTH CHECK FOR THE ENCLOSURE  
    ForEach ($encl in $enclosureNames) {
        Checkpoint-TBirdEnclosureHealth -enclosureName $encl -enclosureExpectedState "Monitored" -enclosureExpectedStatus "(?i)Warning|OK" -haltTest $haltTest
        Checkpoint-TBirdDeviceBayHealth -enclosureName $encl -deviceBayExpectedState "Monitored" -deviceBayExpectedStatus "(?i)Warning|OK" -haltTest $haltTest
        Checkpoint-TBirdInterconnectBayHealth -enclosureName $encl -InterconnectBayExpectedState "Monitored" -InterconnectBayExpectedStatus "(?i)Warning|OK" -InterconnectBayExpectedPowerStatus "(?i)On|Off" -haltTest $haltTest

        Checkpoint-TBirdFanBayHealth -enclosureName $encl -FanBayExpectedStatus "(?i)Warning|OK" -haltTest $haltTest
        Checkpoint-TBirdPowerBayHealth -enclosureName $encl -powerBayExpectedStatus "(?i)Warning|OK" -haltTest $haltTest
    }
    
    ####Add sppfile
    #upload spp if either profile or bigbang firmware updated selected to update
    if($profileFirmware -ne $false -or $bigBangFirmwareoption -ne $false){ 
        $firmwareBaselineName = Add-LatestSpp $path $newSppIsoFileName
        }
      
    #Create Lig
    New-lig -ligs $ligs
 
    #Create Eg
    New-eg -ligs $ligs -enclGroupName $enclGroupName
    	
    #Create Le
    $buildingUri = $enclosureGroupsUri + "?filter=name=$enclGroupName" 
    $enclGroupName = (Send-HPOVRequest (Send-HPOVRequest $buildingUri).members.uri).name
    #Exit the program if EG not found  
	if(-Not $enclGroupName){ throw "EG [$enclGroupName] not found"}
	
    Write-Host "############## Creating Le $leName"
    Write-Log -LogPath $CompletePath -LineValue "############## Creating Le $leName"
    $letask = New-HPTBLogicalEnclosure $leName -enclGroupName $enclGroupName $enclosureNames

    Write-Host "waiting on LE creation"
    
    wait-for-task -task_uri $letask.uri -timeout 3600
    
    #Verify LE exist and proceed with add profiles and update firmwar
    $buildingUri = $logicalEnclosuresUri + "?filter=name=$leName"
    $OVleName = (Send-HPOVRequest (Send-HPOVRequest $buildingUri).members.uri).name
    
    if($leName -eq $OVLeName){
        stop-servers -enclosureNames $enclosureNames -timeout 600
        New-TBirdServerProfile -enclosureName $enclosureNames
        if($profileFirmware){
               Update-ServerFirmware -enclosureName $enclosureNames -sppFileName $firmwareBaselineName -forceInstallFirmware $forceInstallFirmware
               #power on the devices
               start-servers -enclosureNames $enclosureNames -timeout 600
                }
        else{
            Write-Warning "Skipping server firmware update as instructed by user."
        }

        # BigBang Firmware update
        if($bigBangFirmwareoption){
            Write-Host "Initiating Big Bang Update [$bigBangFirmwareoption]"
            $task =Update-HPTBLogicalEnclosureFirmwareUpdate -name $leName -sppFileName $firmwareBaselineName -firmwareUpdateOn $bigBangFirmwareoption -forceInstallFirmware $forceInstallFirmware -logicalinterconnectActivationMode $logicalinterconnectActivationMode
            Write-Host "waiting on Big Bang firmware Update [$bigBangFirmwareoption]"
            wait-for-task -task_uri $task.uri -timeout 7200 
            }
        else{
            Write-warning "Skipping BigBang update as instructed by user."
        }

        
 
        #HEALTH CHECK FOR THE ENCLOSURE
        ForEach ($encl in $enclosureNames) {
            Checkpoint-TBirdEnclosureHealth -enclosureName $encl -enclosureExpectedState "Configured" -enclosureExpectedStatus "(?i)Warning|OK" -haltTest $haltTest
            Checkpoint-TBirdDeviceBayHealth -enclosureName $encl -deviceBayExpectedState "ProfileApplied" -deviceBayExpectedStatus "(?i)Warning|OK" -haltTest $haltTest
            Checkpoint-TBirdInterconnectBayHealth -enclosureName $encl -InterconnectBayExpectedState "(?i)Configured|Monitored" -InterconnectBayExpectedStatus "(?i)Warning|OK" -InterconnectBayExpectedPowerStatus "(?i)On|Off" -haltTest $haltTest
            Checkpoint-TBirdFanBayHealth -enclosureName $encl -FanBayExpectedStatus "(?i)Warning|OK" -haltTest $haltTest  
            Checkpoint-TBirdPowerBayHealth -enclosureName $encl -powerBayExpectedStatus "(?i)Warning|OK" -haltTest $haltTest
        }
    }
}

Function New-lig{
        param([parameter(Mandatory = $true, HelpMessage = "Enter the lig details -",Position=0)]
             [ValidateNotNullOrEmpty()]
             $ligs)
    Process{
        $ligTasks = @()
        foreach($lig in $ligs){
            $name = $lig["name"]
            Write-Host ""
            Write-Host "############## Creating Lig $name"
            Write-Log -LogPath $CompletePath -LineValue "############## Creating Lig $name"
	        if($lig["redundanttype"]){
    
                $ligTasks += New-HPTBLIG -name $lig["name"] -redundanttype $lig["redundanttype"] -interconnectBaySet $lig["interconnectBaySet"] -interconnectMapTemplate $lig["interconnectMapTemplate"] -enclosureIndexes $lig["enclosureIndexes"] -interconnectType $lig["type"]
            }
            else{
                $ligTasks += New-HPTBLIG -name $lig["name"] -interconnectBaySet $lig["interconnectBaySet"] -interconnectMapTemplate $lig["interconnectMapTemplate"] -enclosureIndexes $lig["enclosureIndexes"] -interconnectType $lig["type"]
            }
    }

    #Wait for Lig task
        foreach($ligTask in $ligTasks){
            wait-for-task -task_uri $ligTask.uri -timeout 300
        }
    }
}

Function New-eg{
    param([parameter(Mandatory = $true, HelpMessage = "Enter the lig details -",Position=0)]
          $ligs,
          [parameter(Mandatory = $true, HelpMessage = "Enter the enclosure Group name -",Position=1)]
          $enclGroupName)
    Process{
        # Get the LIG name
        $ligNames = @()
		$ligUris = @()
        foreach($lig in $ligs){
            $name = $lig["name"]
            if($lig["type"] -match "sas"){
                $buildingUri = $sasLogicalInterconnectGroupsUri + "?filter=name=$name"
            }
            else{
                $buildingUri = $logicalInterconnectGroupsUri + "?filter=name=$name"
            }
		$ligUri = (Send-HPOVRequest $buildingUri).members.uri
        $ligName = (Send-HPOVRequest (Send-HPOVRequest $buildingUri).members.uri).name
        
        #Exit the program if LIG not found
        if(-Not $ligname){ throw "LIG [$ligname] not found"}
        else{
			$ligNames += $ligName
			$ligUris += $ligUri
			}
	    }
        Write-Host ""
        Write-Host "############## Creating eg $enclGroupName"
        Write-Log -LogPath $CompletePath -LineValue "############## Creating eg $enclGroupName"
        $egtask = New-HPTBEnclosureGroup $enclGroupName -ligUris $ligUris $ipAddressingMode -enclosureCount $enclosureNames.Count

    #Wait for Eg task
    $task = Get-HPOVTask -ResourceCategory enclosure-groups -Count 1 | Wait-HPOVTaskComplete
    }
}
 
function Set-HPTBApplianceNetworkConfig {

    # .ExternalHelp HPOneView.120.psm1-help.xml
       
    [CmdletBinding(DefaultParameterSetName="primary")]
	Param (
        
		[parameter(Position = 0, mandatory=$true, ParameterSetName="secondary")]
        [ValidateScript({$_ -ne "eth0"})]
		[string]$device,

        [parameter(Position = 1, mandatory=$true, ParameterSetName="secondary")]
        [ValidateSet("Management", "Deployment")]
		[string]$interfaceName,

		[parameter(Position = 0,mandatory=$false, ParameterSetName="primary")]
        [parameter(Position = 2,mandatory=$true, ParameterSetName="secondary")]
		[string]$hostname = $null,

		[parameter(Position = 1,mandatory=$false, ParameterSetName="primary")]
        [parameter(Position = 3,mandatory=$false, ParameterSetName="secondary")]
		[string]$ipv4Type = $null,

		[parameter(Position = 2,mandatory=$false, ParameterSetName="primary")]
        [parameter(Position = 4,mandatory=$false, ParameterSetName="secondary")]
		[string]$ipv4Addr = $null,

        [parameter(Position = 3,mandatory=$false, ParameterSetName="primary")]
        [parameter(Position = 5,mandatory=$false, ParameterSetName="secondary")]
		[string]$ipv4Node1 = $null,

        [parameter(Position = 4,mandatory=$false, ParameterSetName="primary")]
        [parameter(Position = 6,mandatory=$false, ParameterSetName="secondary")]
		[string]$ipv4Node2 = $null,

		[parameter(Position = 5,mandatory=$false, ParameterSetName="primary")]
        [parameter(Position = 7,mandatory=$false, ParameterSetName="secondary")]
		[string]$ipv4Subnet = $null,

		[parameter(Position = 6,mandatory=$false, ParameterSetName="primary")]
        [parameter(Position = 8,mandatory=$false, ParameterSetName="secondary")]
		[string]$ipv4Gateway = $null,

		[parameter(Position = 7,mandatory=$false, ParameterSetName="primary")]
        [parameter(Position = 9,mandatory=$false, ParameterSetName="secondary")]
		[string]$ipv6Type = $null,

		[parameter(Position = 8,mandatory=$false, ParameterSetName="primary")]
        [parameter(Position = 10,mandatory=$false, ParameterSetName="secondary")]
		[string]$ipv6Addr = $null,

		[parameter(Position = 9,mandatory=$false, ParameterSetName="primary")]
        [parameter(Position = 11,mandatory=$false, ParameterSetName="secondary")]
		[string]$ipv6Subnet = $null,

		[parameter(Position = 10,mandatory=$false, ParameterSetName="primary")]
        [parameter(Position = 12,mandatory=$false, ParameterSetName="secondary")]
		[string]$ipv6Gateway = $null,

		[parameter(mandatory=$false, ParameterSetName="primary")]
        [parameter(mandatory=$false, ParameterSetName="secondary")]
        [alias('overrideDhcpDns')]
		[switch]$overrideIpv4DhcpDns,

		[parameter(mandatory=$false, ParameterSetName="primary")]
        [parameter(mandatory=$false, ParameterSetName="secondary")]
		[switch]$overrideIpv6DhcpDns,

		[parameter(Position = 11,mandatory=$false, ParameterSetName="primary")]
        [parameter(Position = 13,mandatory=$false, ParameterSetName="secondary")]
		[string]$domainName = $null,

		[parameter(Position = 12,mandatory=$false, ParameterSetName="primary")]
        [parameter(Position = 14,mandatory=$false, ParameterSetName="secondary")]
		[array]$searchDomains = @(),

		[parameter(Position = 13,mandatory=$false, ParameterSetName="primary")]
        [parameter(Position = 15,mandatory=$false, ParameterSetName="secondary")]
        [alias('nameServers')]
		[array]$ipV4nameServers = @(),

		[parameter(Position = 14,mandatory=$false, ParameterSetName="primary")]
        [parameter(Position = 16,mandatory=$false, ParameterSetName="secondary")]
		[array]$ipV6nameServers = @(),

		[parameter(Position = 15,mandatory=$false, ParameterSetName="primary")]
        [parameter(Position = 17,mandatory=$false, ParameterSetName="secondary")]
        [array]$ntpServers = @(),

        [parameter(mandatory=$true, ParameterSetName="importFile", HelpMessage="Enter the full path and file name for the input file.")]
        [alias("i", "import")]
        [ValidateScript({Test-Path $_})]
        $importFile
    ) 

    Begin { }
    
    Process { 

        # Get the current config (to get ETag & ensure we don't overwrite anything):
        $currentConfig = Get-HPOVApplianceNetworkConfig
    
        if ($currentConfig.etag)  {$etag = $currentConfig.etag }
    
        Switch ($PsCmdlet.ParameterSetName) {
    
            "secondary" {
            [int]$i=0
            $deviceIndex = $NULL
            $configured = $false
            #If($currentConfig.applianceNetworks.Count -gt 1){
                For($i -eq 0; $i -le ($currentConfig.applianceNetworks.Count - 1); $i++)
                    {
                     if($currentConfig.applianceNetworks[$i].device -eq $device){
                        $deviceIndex = $i; $configured=$true; break
                        }
                    }
                #}
            
            if (-not($configured)) {
                $freeMacs = Send-HPOVRequest $script:applMacAddresses
                if($freeMacs.members | ? {$_.device -eq $device}){
                    $macAddr = ($freeMacs.members | ? {$_.device -eq $device}).macAddress
                    # Update any non-null values that were passed-in:
                    $secondaryNet = New-Object System.Object
                    $secondaryNet | Add-Member -NotePropertyName device -NotePropertyValue $device
                    $secondaryNet | Add-Member -NotePropertyName macAddress -NotePropertyValue $macAddr
                    if ($hostname)     { $secondaryNet | Add-Member -NotePropertyName hostname -NotePropertyValue $hostname }
                    if ($ipv4Type)     { $secondaryNet | Add-Member -NotePropertyName ipv4Type -NotePropertyValue $ipv4Type.ToUpper()
                                         # If setting DHCP, clear any existing IP address:
                                         if ($ipv4Type -ieq "DHCP") {$secondaryNet | Add-Member -NotePropertyName app1Ipv4Addr -NotePropertyValue $null;
                                                                    $secondaryNet | Add-Member -NotePropertyName app2Ipv4Addr -NotePropertyValue $null }
                                       }
                    if ($ipv4Addr)     { $secondaryNet | Add-Member -NotePropertyName virtIpv4Addr -NotePropertyValue $ipv4Addr }
                    if ($ipv4Node1)    { $secondaryNet | Add-Member -NotePropertyName app1Ipv4Addr -NotePropertyValue $ipv4Node1 }
                    if ($ipv4Node2)    { $secondaryNet | Add-Member -NotePropertyName app2Ipv4Addr -NotePropertyValue $ipv4Node2 }
                    if ($ipv4Subnet)   { $secondaryNet | Add-Member -NotePropertyName ipv4Subnet -NotePropertyValue $ipv4Subnet }
                    if ($ipv4Gateway)  { $secondaryNet | Add-Member -NotePropertyName ipv4Gateway -NotePropertyValue $ipv4Gateway }
                    if ($ipv6Type)     { $secondaryNet | Add-Member -NotePropertyName ipv6Type -NotePropertyValue $ipv6Type.ToUpper() 
                                         # If setting DHCP, clear any existing IP address:
                                         if ($ipv6Type -ieq "DHCP") { $secondaryNet | Add-Member -NotePropertyName app1Ipv6Addr = $null }
                                       }
                    if ($ipv6Addr)     { $secondaryNet | Add-Member -NotePropertyName app1Ipv6Addr -NotePropertyValue $ipv6Addr }
                    if ($ipv6Subnet)   { $secondaryNet | Add-Member -NotePropertyName ipv6Subnet -NotePropertyValue $ipv6Subnet }
                    if ($ipv6Gateway)  { $secondaryNet | Add-Member -NotePropertyName ipv6Gateway -NotePropertyValue $ipv6Gateway }
                    if ($overrideDhcpDns){ $secondaryNet | Add-Member -NotePropertyName overrideDhcpDnsServers -NotePropertyValue $overrideDhcpDns }
                    if ($domainName)   { $secondaryNet | Add-Member -NotePropertyName domainName -NotePropertyValue $domainName }
                    if ($searchDomains){ $secondaryNet | Add-Member -NotePropertyName searchDomains -NotePropertyValue $searchDomains }
                    if ($nameServers)  { $secondaryNet | Add-Member -NotePropertyName nameServers -NotePropertyValue $nameServers }

                    if ($ntpServers) { $currentConfig.time.ntpServers = $ntpServers }

                    # Hard code the following settings, for now:
                    $secondaryNet | Add-Member -NotePropertyName allowTransientValidationErrors -NotePropertyValue "false" # "true" or "false"
                    $secondaryNet | Add-Member -NotePropertyName confOneNode -NotePropertyValue "true"  # Always "true", for now
                    $secondaryNet | Add-Member -NotePropertyName activeNode -NotePropertyValue "1"      # Always "1", for now
                    $currentConfig.applianceNetworks += $secondaryNet                    
                    }
                else{
                    #$errMessage = $device + " does not exist on the appliance."
                    #Throw $errMessage
                    $errorRecord = New-ErrorRecord InvalidOperationException UnknownNetworkInterface ObjectNotFound 'Set-HPOVApplianceNetworkConfig' -Message $device + " does not exist on the appliance." #-verbose
                    $pscmdlet.ThrowTerminatingError($errorRecord)
                    
                    }
                }

            }
    
            "primary" {
                [int]$i=0
                $deviceIndex = $NULL
                For($i -eq 0; $i -le ($currentConfig.applianceNetworks.Count - 1); $i++)
                    {
                     if($currentConfig.applianceNetworks[$i].interfaceName -eq "Appliance"){
                        
                        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Found interface: $($currentConfig.applianceNetworks[$i].interfaceName)"
                        $deviceIndex = $i
                        $configured=$true
                        
                        #break out of for loop
                        break
                        }
                    }
                }
            "importFile" {
                try {
                    $importConfig = [string]::Join("", (gc $importfile -ErrorAction Stop))
                    $importConfig = $importConfig -replace "\s","" | convertfrom-json -ErrorAction Stop
                    $freeMacs = Send-HPOVRequest $script:applMacAddresses
    
                    [int]$i=0
                    For($i -eq 0; $i -le ($importConfig.applianceNetworks.Count - 1); $i++)
                        {
                        if ($importConfig.applianceNetworks[$i].ipv4Gateway -eq "127.0.0.1"){
                            $importConfig.applianceNetworks[$i].ipv4Gateway = ""
                            }
                        if ($importConfig.applianceNetworks[$i].nameServers -is "String"){
                            $importConfig.applianceNetworks[$i].nameServers = @()
                            }
                        if ($importConfig.applianceNetworks[$i].searchDomains -is "String"){
                            $importConfig.applianceNetworks[$i].searchDomains = @()
                            }
                        if (-not($importConfig.applianceNetworks[$i].macAddress)) {
                            $macAddr = ($currentConfig.applianceNetworks | ? {$_.device -eq $importConfig.applianceNetworks[$i].device}).macAddress
                            if(-not($macAddr)) {
                                $macAddr = ($freeMacs.members | ? {$_.device -eq $importConfig.applianceNetworks[$i].device}).macAddress
                                }
                            if(-not($macAddr)){
                                $errorRecord = New-ErrorRecord InvalidOperationException ApplianceNICResourceNotFound ObjectNotFound 'Get-HPOVStorageSystem' -Message ($importConfig.applianceNetworks[$i].device + "does not exist on the appliance.") #-verbose
                                #$errMessage = $importConfig.applianceNetworks[$i].device + "does not exist on the appliance."
                                #Throw $errMessage
                                $PsCmdlet.ThrowTerminatingError($errorRecord)
                                }
                            $importConfig.applianceNetworks[$i] | Add-Member -NotePropertyName macAddress -NotePropertyValue $macAddr
    
                            }
                        }
                    #zero the $currentConfig.applianceNetworks array so we can send it all new values
                    $currentConfig.applianceNetworks = @()
                    $currentConfig.applianceNetworks = $importConfig.applianceNetworks
                    }
                catch [System.Management.Automation.ItemNotFoundException] {
    
                    $errorRecord = New-ErrorRecord System.Management.Automation.ItemNotFoundException ImportFileNotFound ObjectNotFound 'Set-HPOVApplianceNetworkConfig' -Message "$importFile not found!" #-verbose
                    $pscmdlet.ThrowTerminatingError($errorRecord)
    
                }
    
                catch [System.ArgumentException] {
    
                    $errorRecord = New-ErrorRecord System.ArgumentException InvalidJSON ParseErrror 'Set-HPOVApplianceNetworkConfig' -Message "Input JSON format incorrect!" #-verbose
                    $pscmdlet.ThrowTerminatingError($errorRecord)    

                }

            }

        }

        if($configured){
                # Update any non-null values that were passed-in:
                
                if ($hostname)        { $currentConfig.applianceNetworks[$deviceIndex].hostname =     $hostname }
                if ($ipv4Type)        { $currentConfig.applianceNetworks[$deviceIndex].ipv4Type =     $ipv4Type.ToUpper()
                    
                    # If setting DHCP, clear any existing IP address:
                    if ($ipv4Type -ieq "DHCP") { 
                        $currentConfig.applianceNetworks[$deviceIndex].app1Ipv4Addr = $null;
                        $currentConfig.applianceNetworks[$deviceIndex].app2Ipv4Addr = $null

                        # If $overrideIPv4DhcpDns is true, set it, if not make sure it is fale
                        if ($overrideIpv4DhcpDns) { $currentConfig.applianceNetworks[$deviceIndex].overrideIpv4DhcpDnsServers = [bool]$overrideIpv4DhcpDns }
                        else { $currentConfig.applianceNetworks[$deviceIndex].overrideIpv4DhcpDnsServers = $false }

                    }

                    elseif ($ipv4Type -ieq "STATIC") {
                        #Make sure override.. is false if STATIC ip addresses are in use.
                        $currentConfig.applianceNetworks[$deviceIndex].overrideIpv4DhcpDnsServers = $false 
                    }
                }


                if ($ipv4Addr)        { $currentConfig.applianceNetworks[$deviceIndex].virtIpv4Addr = $ipv4Addr }
                if ($ipv4Node1)       { $currentConfig.applianceNetworks[$deviceIndex].app1Ipv4Addr = $ipv4Node1 }
                if ($ipv4Node2)       { $currentConfig.applianceNetworks[$deviceIndex].app2Ipv4Addr = $ipv4Node2 }
                if ($ipv4Subnet)      { $currentConfig.applianceNetworks[$deviceIndex].ipv4Subnet =   $ipv4Subnet }
                if ($ipv4Gateway)     { $currentConfig.applianceNetworks[$deviceIndex].ipv4Gateway =  $ipv4Gateway }
                if ($ipv6Type)        { $currentConfig.applianceNetworks[$deviceIndex].ipv6Type =     $ipv6Type.ToUpper() 
                                          
                    # If setting DHCP, clear any existing IP address:
                    if ($ipv6Type -ieq "DHCP") { $currentConfig.applianceNetworks[$deviceIndex].app1Ipv6Addr = $null }

                }
                if ($ipv6Addr)        { $currentConfig.applianceNetworks[$deviceIndex].app1Ipv6Addr = $ipv6Addr }
                if ($ipv6Subnet)      { $currentConfig.applianceNetworks[$deviceIndex].ipv6Subnet =   $ipv6Subnet }
                if ($ipv6Gateway)     { $currentConfig.applianceNetworks[$deviceIndex].ipv6Gateway =  $ipv6Gateway }
                #if ($overrideIpv4DhcpDns) { $currentConfig.applianceNetworks[$deviceIndex].overrideIpv4DhcpDnsServers = [bool]$overrideIpv4DhcpDns }
                if ($overrideIpv6DhcpDns) { $currentConfig.applianceNetworks[$deviceIndex].overrideIpv6DhcpDnsServers = [bool]$overrideIpv6DhcpDns }
                if ($domainName)      { $currentConfig.applianceNetworks[$deviceIndex].domainName =   $domainName }
                if ($searchDomains)   { $currentConfig.applianceNetworks[$deviceIndex].searchDomains =$searchDomains }
                if ($ipV4nameServers)     { $currentConfig.applianceNetworks[$deviceIndex].ipv4NameServers =  $ipV4nameServers }
                if ($ipV6nameServers)     { $currentConfig.applianceNetworks[$deviceIndex].ipv6NameServers =  $ipV6nameServers }
    
                if ($ntpServers) { $currentConfig.time.ntpServers = $ntpServers }
    
                # Hard code the following settings, for now:
                $currentConfig.applianceNetworks[$deviceIndex].confOneNode = "true"  # Always "true", for now
                $currentConfig.applianceNetworks[$deviceIndex].activeNode = "1"      # Always "1", for now
            }
        
        if ($etag) { $currentConfig | Add-Member -type NoteProperty -name etag -value $etag }

    }

    end {

        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Configuration to be applied: $($currentConfig | out-string)"

        #Remove MAC Address value or DHCP setting will break
        if ($currentConfig.macAddress) { $currentConfig.macAddress = $Null }

        # This is an asynchronous method, so get the returned Task object
        $task = Send-HPOVRequest $applConfigUri POST $currentConfig
       
       
        #Take a peak at the task before moving on
        try { $taskStatus = Send-HPOVRequest $task.uri }
        catch [HPOneView.Appliance.NetworkConnectionException]{
        
            #The appliance is no longer reachable.  Let's 
			$errorRecord = New-ErrorRecord HPOneview.Appliance.NetworkConnectionException ApplianceUnreachable ConnectionError 'Set-HPOVApplianceNetworkConfig' -Message "Unable to reconnect to the appliance.  Please check to make sure there are no IP Address conflicts or your set the IP Address and Subnet Mask correctly." #-verbose
            $PsCmdlet.ThrowTerminatingError($errorRecord)         

        }
        
        if ($ipv4Type -eq "static") {
                      
            #Start a new stopwatch object
            
            $sw = [diagnostics.stopwatch]::StartNew()
            do{
            
                #Check to make sure we connect to a OneView appliance
                try{ $resp = Invoke-WebRequest -uri "http://$ipv4Addr" -UseBasicParsing}
                catch{
                    [System.Exception] 
                    #go for another try
                    }
                start-sleep -seconds 5
                }until(($sw.elapsed -ge $script:defaultTimeout) -or ($resp.Content -match "OneView") )

            #Check to make sure we connect to a OneView appliance
            $resp = Invoke-WebRequest -uri "http://$ipv4Addr" -UseBasicParsing
            #If successful, update current POSH session
            if ($resp.Content -match "OneView") { 
           

                Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Updating session appliance variables with new appliance address: $ipv4Addr"
                $Script:PromptApplianceHostname        = $ipv4Addr
                $script:HPOneViewAppliance             = $ipv4Addr
                #$global:cimgmtSessionId.appliance     = $ipv4Addr
                $script:applianceConnectedTo.appliance = $ipv4Addr
                $global:cimgmtSessionId                = $null

            }
            else {

                #Unable to connect to new appliance address or connection failed.  Need to generate error here.
				$errorRecord = New-ErrorRecord HPOneview.Appliance.NetworkConnectionException ApplianceUnreachable ConnectionError 'Set-HPOVApplianceNetworkConfig' -Message "Unable to reconnect to the appliance.  Please check to make sure there are no IP Address conflicts or your set the IP Address and Subnet Mask correctly." #-verbose
                $PsCmdlet.ThrowTerminatingError($errorRecord)    

            }
        }
           

    }

}

Function Set-HPTBFirstTimeSetup{
Param(
             [parameter(Mandatory = $true, HelpMessage = "Enter Tbird dhcp ip -",Position=0)]
             [ValidateNotNullOrEmpty()]
             [string] $DhcpIpAddress,

             [parameter(Mandatory = $true, HelpMessage = "Enter Tbird new static ip -",Position=1)]
             [ValidateNotNullOrEmpty()]
             [string] $NewStaticIp,

             [parameter(Mandatory = $true, HelpMessage = "Enter Tbird new password -",Position=2)]
             [ValidateNotNullOrEmpty()]
             [string] $NewTbirdPassword,
             
             [parameter(Mandatory = $true, HelpMessage = "Enter Tbird FQDN host name -",Position=3)]
             [ValidateNotNullOrEmpty()]
             [string] $HostName,

             [parameter(Mandatory = $true, HelpMessage = "Enter Tbird Maintenance node 1 IP -",Position=4)]
             [ValidateNotNullOrEmpty()]
             [string] $TbirdMaintenanceNode1,

             [parameter(Mandatory = $true, HelpMessage = "Enter Tbird Maintenance node 2 IP -",Position=5)]
             [ValidateNotNullOrEmpty()]
             [string] $TbirdMaintenanceNode2,

             [parameter(Mandatory = $true, HelpMessage = "Enter Tbird Subment mask IP-",Position=6)]
             [ValidateNotNullOrEmpty()]
             [string] $SubnetMask,
                          
             [parameter(Mandatory = $true, HelpMessage = "Enter Tbird Gateway IP -",Position=7)]
             [ValidateNotNullOrEmpty()]
             [string] $GatewayIP,

             [parameter(Mandatory = $true, HelpMessage = "Enter Tbird Domain name -",Position=8)]
             [ValidateNotNullOrEmpty()]
             [string] $DomainName,

             [parameter(Mandatory = $true, HelpMessage = "Enter Tbird Domain IPV4 name servers -",Position=9)]
             [ValidateNotNullOrEmpty()]
             [string[]]$IpV4NameServers

			 )
  
$params = @{
        hostname        = $HostName ;
        ipv4Type        = "STATIC";
        ipv4Addr        = $NewStaticIp;
        ipv4Node1       = $TbirdMaintenanceNode1;
        ipv4Node2       = $TbirdMaintenanceNode2;
        ipv4Subnet      = $SubnetMask;
        ipv4Gateway     = $GatewayIP;
        ipv6Type        = "UNCONFIGURE";
        ipv6Addr        = "";
        ipv6Subnet      = "";
        ipv6Gateway     = "";
        domainName      = $DomainName; `
        searchDomains   = "";
        ipV4nameServers = $IpV4NameServers;
        ipV6nameServers = @();
        ntpServers      = ""
    }  

    # Accept the EULA
    Write-Host "Accepting EULA..."
    if (Get-HPOVEulaStatus -appliance $DhcpIpAddress) {

        Write-Log -LogPath $CompletePath -LineValue "Accepting EULA..."

        $ret = Set-HPOVEulaStatus -supportAccess "yes" -appliance $DhcpIpAddress

    }

    
    # For initial setup, connect first using "default" Administrator credentials:
    Write-Host "Setting initial password"
    Try { Connect-HPOVMgmt -appliance $DhcpIpAddress -user "Administrator" -password "admin" }
    catch [HPOneView.Appliance.PasswordChangeRequired] {

        Write-Log -LogPath $CompletePath -LineValue "Set initial password"
        Set-HPOVInitialPassword -userName "Administrator" -oldPassword "admin" -newPassword $NewTbirdPassword
    
    }
    
    Write-Log -LogPath $CompletePath -LineValue "Reconnect with new password"
    
    Connect-HPOVMgmt -appliance $DhcpIpAddress -user Administrator -password $NewTbirdPassword
    
       
    #Configure applince network
    Write-Host "Setting appliance networking configuration"
    Write-Log -LogPath $CompletePath -LineValue "Set appliance networking configuration"
    $task = Set-HPTBApplianceNetworkConfig @params #-import $global:fts_config
    
    #Verify if sessionid is not available
    if (-not($Global:cimgmtSessionId)) { Connect-HPOVMgmt -appliance $NewStaticIp -user Administrator -password $NewTbirdPassword }

    Write-Log -LogPath $CompletePath -LineValue "Completed appliance networking configuration"
}

Function Start-Log{
  <#
  .SYNOPSIS
    Creates log file
  .DESCRIPTION
    Creates log file with path and name that is passed. Checks if log file exists, and if it does deletes it and creates a new one.
    Once created, writes initial logging data
  .PARAMETER LogPath
    Mandatory. Path of where log is to be created. Example: C:\Windows\Temp
  .PARAMETER LogName
    Mandatory. Name of log file to be created. Example: Test_Script.log
      
  .PARAMETER ScriptVersion
    Mandatory. Version of the running script which will be written in the log. Example: 1.5
  .INPUTS
    Parameters above
  .OUTPUTS
    Log file created
  .EXAMPLE
    Log-Start -LogPath "C:\Windows\Temp" -LogName "Test_Script.log" -ScriptVersion "1.5"
  #>
    
  [CmdletBinding()]
  
  Param ([Parameter(Mandatory=$true)][string]$LogPath, [Parameter(Mandatory=$true)][string]$LogName, [Parameter(Mandatory=$true)][string]$ScriptVersion)
  
  Process{
    $sFullPath = $LogPath + "\" + $LogName
    
    #Check if file exists and delete if it does
    If((Test-Path -Path $sFullPath)){
      Remove-Item -Path $sFullPath -Force
    }
    
    #Create file and start logging
    New-Item -Path $LogPath -Value "*****" -Name $LogName -ItemType File
    
    Add-Content -Path $sFullPath -Value "***************************************************************************************************"
    Add-Content -Path $sFullPath -Value "Started processing at [$([DateTime]::Now)]."
    Add-Content -Path $sFullPath -Value "***************************************************************************************************"
    Add-Content -Path $sFullPath -Value ""
    Add-Content -Path $sFullPath -Value "Running script version [$ScriptVersion]."
    Add-Content -Path $sFullPath -Value ""
    Add-Content -Path $sFullPath -Value "***************************************************************************************************"
    Add-Content -Path $sFullPath -Value ""
  
    #Write to screen for debug mode
    Write-Debug "***************************************************************************************************"
    Write-Debug "Started processing at [$([DateTime]::Now)]."
    Write-Debug "***************************************************************************************************"
    Write-Debug ""
    Write-Debug "Running script version [$ScriptVersion]."
    Write-Debug ""
    Write-Debug "***************************************************************************************************"
    Write-Debug ""
  }
}

Function Add-LatestSpp{
        Param(
             [parameter(Mandatory = $true, HelpMessage = "Enter the spp path -",Position=0)]
             [ValidateNotNullOrEmpty()]
             [string] $path,

             [parameter(Mandatory = $true, HelpMessage = "Please enter the new Spp Iso File Name -",Position=1)]
             [ValidateNotNullOrEmpty()]
             [string[]] $newSppIsoFileName)

    Write-Host "Upload SppFile, if it is not already uploaded"
    Write-Log -LogPath $CompletePath -LineValue "Upload SppFile, if it is not already uploaded"
    #throws exception in case there is no spp bundle
    try{
        $res = Get-HPOVSppFile
        }
    catch [system.exception] {
        Write-Log -LogPath $CompletePath -LineValue "No firmware bundle has been uploaded"
        $res = $null
        }

    #We are uploading the firmware if there is no bundle or the specified name does not exist in appliance
    if($res -eq $null -or !($res.isoFileName -contains $newSppIsoFileName)){
        # Remove spp
        if($res){
            Write-Host "Removing spp to avoid storage size issue and name conflict"
            # if more than one spp available
            foreach($r in $res){
                $task = Remove-HPOVResource $r.uri
                }
            }
        $sppTask=Add-HPOVBaseline -sppFile $path
        #Wait for spp task
        $task = Wait-HPOVTaskComplete $sppTask.uri -timeout (New-TimeSpan -Minutes 10)
        }
    else{
        Write-Log -LogPath $CompletePath -LineValue "Provided spp name $sppIsoFileName is allready uploaded to appliance"
    }

    #Get the firmware baseline Name
     $firmwareBaselineName = (Get-HPOVBaseline).isoFilename
     if(-Not $firmwareBaselineName){ 
        Throw "Firmware baseline not found, please update the firmware and then proceed with firmware update."}
     else {
        return $firmwareBaselineName
        }

    }

function Update-HPTBLogicalEnclosureFirmwareUpdate {
    
    # .ExternalHelp HPOneView.120.psm1-help.xml
    # Update-HPTBLogicalEnclosureFirmwareUpdate -name "LEName" -sppFileName "sppFileName" -firmwareUpdateOn "SharedInfrastructureAndServerProfiles" -forceInstallFirmware $true
    [CmdletBinding()]
    Param (
        [parameter(Position = 0, Mandatory = $true, HelpMessage = "Enter logical enclosure name.")]
        [ValidateNotNullOrEmpty()]
        [string]$name,

        [parameter(Position = 1, Mandatory = $true, HelpMessage = "Enter the sppFileName of the firmware baseline to apply")]
        [string]$sppFileName = $null,

        [parameter(Position = 2, Mandatory = $true, HelpMessage = "Enter the device to update firmware [EnclosureOnly], [SharedInfrastructureOnly] and [SharedInfrastructureAndServerProfiles]")]
        [ValidateNotNullOrEmpty()]
        [string]$firmwareUpdateOn = "SharedInfrastructureAndServerProfiles",

        [parameter(Position = 3, Mandatory = $false, HelpMessage = "Enter true/false, true indicates that the user has chosen to update unmanaged interconnects where false indicates otherwise")]
        [bool]$unmanagedInterconnects = $False,

        [parameter(Position = 4, Mandatory = $false, HelpMessage = "Enter true/false, true indicates that the user has chosen to force install firmware where false indicates otherwise")]
        [bool]$forceInstallFirmware = $true,

        [parameter(Position = 5, Mandatory = $true, HelpMessage = "Logical interconnect activation mode [Orchestrated] or [Parallel]")]
        [string]$logicalinterconnectActivationMode = "Parallel",

        [parameter(Position = 6, Mandatory = $false, HelpMessage = "Validate If LI Firmware Update Is Non Disruptive[True or False]")]
        [bool]$isNonDisruptiveFU = $False
    )

    Begin {


        if (-not($global:cimgmtSessionId)) {
        
            $errorRecord = New-ErrorRecord HPOneview.Appliance.AuthSessionException NoAuthSession AuthenticationError "New-HPOVEnclosureGroup" -Message "No valid session ID found.  Please use Connect-HPOVMgmt to connect and authenticate to an appliance." #-verbose
            $PSCmdlet.ThrowTerminatingError($errorRecord)

        }

    }


    Process {  

        #Get the Logical Enclsoure uri using Logical Enclosure name
        [string]$leUri = $null
        $buildingUri = $logicalEnclosuresUri + "?filter=name='$name'"
        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Building Logical Enclosure uri using name: $($buildingUri)"
                
        $logicalEnclosureMember = (Send-HPOVRequest $buildingUri).members
        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Logical Enclosure member details: $($logicalEnclosureMember)"
                
        $leUri  += $logicalEnclosureMember.uri
        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Logical Enclosure uri: $($logicalEnclosureUri)"    
            
        
        #Get the Firmware drivers uri using firmware bundle name
        if($sppFileName){
            $buildingUri = $firmwareDriversUri + "?filter=name=$sppFileName"
            Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] building Firmware drivers using firmware build name: $($buildingUri)"
               
            $firmwareBaselineUri = ((Send-HPOVRequest $buildingUri).members).uri
            Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Firmware drivers ur: $($firmwareBaselineUri)"
            }    
        else{
        msg = "Failed to continue Big Bang Firmware update,SPP details has not been provided."
        Write-Host msg
        Write-Error -Message msg -ErrorAction Stop
        } 
        
        $le = @( @{
                op = "replace";
                path =  "/firmware";
                value = @{
                firmwareBaselineUri = $firmwareBaselineUri;
                forceInstallFirmware = $forceInstallFirmware;
                firmwareUpdateOn = $firmwareUpdateOn;
                logicalInterconnectUpdateMode = $logicalinterconnectActivationMode;
                updateFirmwareOnUnmanagedInterconnect = $unmanagedInterconnects;
                validateIfLIFirmwareUpdateIsNonDisruptive = $isNonDisruptiveFU               
                }
            })
       
       
       
        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Logical Enclosure Firmware Update object: $($lefu | out-string)"

        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Updating $($name) Logical Enclosure Firmware on $firmwareUpdateOn device"
        $resp = Update-HPTBResource $leUri $le
    }

    end {

        return $resp

    }

}

Function Write-Log{
  <#
  .SYNOPSIS
    Writes to a log file
  .DESCRIPTION
    Appends a new line to the end of the specified log file
  
  .PARAMETER LogPath
    Mandatory. Full path of the log file you want to write to. Example: C:\Windows\Temp\Test_Script.log
  
  .PARAMETER LineValue
    Mandatory. The string that you want to write to the log
      
  .INPUTS
    Parameters above
  .OUTPUTS
    None
  .EXAMPLE
    Write-Log -LogPath "C:\Windows\Temp\Test_Script.log" -LineValue "This is a new line which I am appending to the end of the log file."
  #>
  
  [CmdletBinding()]
  
  Param ([Parameter(Mandatory=$true)][string]$LogPath, $LineValue="None")
  
  Process{
    Add-Content -Path $LogPath -Value $LineValue
  
    #Write to screen for debug mode
    Write-Debug $LineValue
  }
}



Function get-console{
#------------------------------------------------------------------------------
# This script grabs text from the console buffer and outputs to the pipeline
# lines of HTML that represent it.
#
# Usage: get-bufferhtml [args]
#
# Where args are:
#
# -last n       - how many lines back from current line to grab
#                 default is (effectively) everything
# -all          - grab all lines in console, overrides -last
# -trim         - trims blank space from the right of each line
#                 this is ok unless you have lots of text with
#                 varying background colours
# -font s       - optional css font name. default is nothing which
#                 means the browser will use whatever is default for a
#                 <pre> tag. "Courier New" is quite a good alternative
# -fontsize s   - optional css font size, eg "9pt" or "80%"
# -style s      - optional addition css, eg "overflow:hidden"
# -palette p    - choose a colour palette, one of:
#                 "powershell" normal for a PowerShell window (ie with
#                              strange colours for darkmagenta and darkyellow
#                 "standard"   normal ansi colours as used by a standard
#                              cmd.exe session
#                 "print"      like powershell, but with colours handy
#                              for printing where you want to save ink.
#
# The output is one large wrapped <pre> tag to keep whitespace intact.
#

param(
  [int]$last = 50000,             
  [switch]$all,                   
  [switch]$trim,                  
  [string]$font=$null,            
  [string]$fontsize=$null,        
  [string]$style="",              
  [string]$palette="powershell"   
  )
$ui = $host.ui.rawui
[int]$start = 0
if ($all) { 
  [int]$end = $ui.BufferSize.Height  
  [int]$start = 0
}
else { 
  [int]$end = ($ui.CursorPosition.Y - 1)
  [int]$start = $end - $last
  if ($start -le 0) { $start = 0 }
}
$height = $end - $start
if ($height -le 0) {
  write-warning "There must be one or more lines to get"
  return
}
$width = $ui.BufferSize.Width
$dims = 0,$start,($width-1),($end-1)
$rect = new-object Management.Automation.Host.Rectangle -argumentList $dims
$cells = $ui.GetBufferContents($rect)

# set default colours
$fg = $ui.ForegroundColor; $bg = $ui.BackgroundColor
$defaultfg = $fg; $defaultbg = $bg

# character translations
# wordpress weirdness means I do special stuff for < and \
$cmap = @{
    [char]"<" = "<span>&lt;</span>"
    [char]"\" = "&#x5c;"
    [char]">" = "&gt;"
    [char]"'" = "&#39;"
    [char]"`"" = "&#34;"
    [char]"&" = "&amp;"
}

# console colour mapping
# the powershell console has some odd colour choices, 
# marked with a 6-char hex codes below
$palettes = @{}
$palettes.powershell = @{
    "Black"       ="#000"
    "DarkBlue"    ="#008"
    "DarkGreen"   ="#080"
    "DarkCyan"    ="#088"
    "DarkRed"     ="#800"
    "DarkMagenta" ="#012456"
    "DarkYellow"  ="#eeedf0"
    "Gray"        ="#ccc"
    "DarkGray"    ="#888"
    "Blue"        ="#00f"
    "Green"       ="#0f0"
    "Cyan"        ="#0ff"
    "Red"         ="#f00"
    "Magenta"     ="#f0f"
    "Yellow"      ="#ff0"
    "White"       ="#fff"
  }
# now a variation for the standard console (used by cmd.exe) based
# on ansi colours
$palettes.standard = ($palettes.powershell).Clone()
$palettes.standard.DarkMagenta = "#808"
$palettes.standard.DarkYellow = "#880"

# this is a weird one... takes the normal powershell one and
# inverts a few colours so normal ps1 output would save ink when
# printed (eg from a web page).
$palettes.print = ($palettes.powershell).Clone()
$palettes.print.DarkMagenta = "#eee"
$palettes.print.DarkYellow = "#000"
$palettes.print.Yellow = "#440"
$palettes.print.Black = "#fff"
$palettes.print.White = "#000"

$comap = $palettes[$palette]

# inner function to translate a console colour to an html/css one
function c2h{return $comap[[string]$args[0]]}
$f=""
if ($font) { $f += " font-family: `"$font`";" }
if ($fontsize) { $f += " font-size: $fontsize;" }
$line  = "<pre style='color: $(c2h $fg); background-color: $(c2h $bg);$f $style'>" 
for ([int]$row=0; $row -lt $height; $row++ ) {
  for ([int]$col=0; $col -lt $width; $col++ ) {
    $cell = $cells[$row,$col]
    # do we need to change colours?
    $cfg = [string]$cell.ForegroundColor
    $cbg = [string]$cell.BackgroundColor
    if ($fg -ne $cfg -or $bg -ne $cbg) {
      if ($fg -ne $defaultfg -or $bg -ne $defaultbg) { 
        $line += "</span>" # remove any specialisation
        $fg = $defaultfg; $bg = $defaultbg;
      }
      if ($cfg -ne $defaultfg -or $cbg -ne $defaultbg) { 
        # start a new colour span
        $line += "<span style='color: $(c2h $cfg); background-color: $(c2h $cbg)'>" 
      }
      $fg = $cfg
      $bg = $cbg
    }
    $ch = $cell.Character
    $ch2 = $cmap[$ch]; if ($ch2) { $ch = $ch2 }
    $line += $ch
  }
  if ($trim) { $line = $Line.TrimEnd() }
  $line
  $line=""
}
if ($fg -ne $defaultfg -or $bg -ne $defaultbg) { "</span>" } # close off any specialisation of colour
"</pre>"
}

Function wait-for-task{
    Param ([parameter(Mandatory = $true, HelpMessage = "Enter the task uri-",Position=0)]
           [ValidateNotNullOrEmpty()]
           [string]$task_uri,

           [parameter(Mandatory = $false, HelpMessage = "Enter the default timeout in seconds-",Position=1)]
           $timeout=600)
    
    Process { 
    $seconds=0
    $name = (Send-HPOVRequest $task_uri).name
    $taskName = (Send-HPOVRequest $task_uri).associatedResource.resourceName 
        do{
            Write-Log -LogPath $CompletePath -LineValue $task_uri
            start-sleep -s 1
            $seconds += 1
            if($seconds%30 -eq 0){
                write-host "." -NoNewline
                }
            
            $percentComplete = (Send-HPOVRequest $task_uri).percentComplete 
            Write-Log -LogPath $CompletePath -LineValue $percentComplete
            $taskState = (Send-HPOVRequest $task_uri).taskState
            
            if($seconds -gt $timeout){
                Write-host "Default timeout meet, exiting wait-for-task for [$name]"
                break}
    }while($percentComplete -lt 100)
    
    #Verify task state
    if($taskState -eq "Completed")
        {write-host "$taskName [$name] completed successfully"}
    else{write-warning "$taskName [$name] failed to complete successfully, taskState appeared as [$taskState]"}
    }
}

function New-HPTBLIG {

    # .ExternalHelp HPOneView.120.psm1-help.xml

    [CmdletBinding(DefaultParameterSetName = "Default")]
    param (
        [Parameter(Mandatory = $True,ParameterSetName = "Default",HelpMessage = "Please specify the Logical Interconnect Name", Position = 0)]
        [ValidateNotNullOrEmpty()]
        [Alias('name')]
        [String]$ligName,

        [Parameter(Mandatory = $False,ParameterSetName = "Default",HelpMessage = "Please specify the redundancyType, can be [HighlyAvailable], [NonRedundantASide], [NonRedundantBSide], [Redundant]", Position = 1)]
        [ValidateNotNullOrEmpty()]
        [Alias('redundanttype')]
        [String]$redundancyType,
        
        [Parameter(Mandatory = $True,ParameterSetName = "Default",HelpMessage = "InterconnectMapTemplate", Position = 2)]
        $interconnectMapTemplate,
        
        [Parameter(Mandatory = $True,ParameterSetName = "Default",HelpMessage = "Enclosure index", Position = 3)]
        $enclosureIndexes,

        [Parameter(Mandatory = $False,ParameterSetName = "Default",HelpMessage = "Enable IGMP Snooping", Position = 4)]
		[Alias("IGMPSnoop")]
        [bool]$enableIgmpSnooping = $False,
		
		[Parameter(Mandatory = $False,ParameterSetName = "Default",HelpMessage = "IGMP Idle Timeout Interval (1-3600 [sec])", Position = 5)]
        [ValidateRange(1,3600)]
		[Alias('IGMPIdle')]
	    [int]$igmpIdleTimeoutInterval = 260,
		
		[Parameter(Mandatory = $False,ParameterSetName = "Default",HelpMessage = "Enable Fast MAC Cache Failover", Position = 6)]
		[Alias('FastMAC')]
	    [bool]$enableFastMacCacheFailover = $True,
		
		[Parameter(Mandatory = $False,ParameterSetName = "Default",HelpMessage = "Fast MAC Cache Failover Interval (1-30 [sec])", Position = 7)]
        [ValidateRange(1,30)]
		[Alias('FastMACRefresh')]
    	[int]$macRefreshInterval = 5,
		
		[Parameter(Mandatory = $False,ParameterSetName = "Default",HelpMessage = "Enable Network Loop Protection on the Downlink Ports)", Position = 8)]
		[Alias('LoopProtect')]
	    [bool]$enableNetworkLoopProtection = $True,

		[Parameter(Mandatory = $False,ParameterSetName = "Default",HelpMessage = "Enable Network Pause Flood Protection on the Downlink Ports)", Position = 9)]
		[Alias('PauseProtect')]
	    [bool]$enablePauseFloodProtection = $True,
		
		[Parameter(Mandatory = $False,ParameterSetName = "Default",HelpMessage = "Enable SNMP Settings", Position = 10)]
        [Alias('snmpValues')]
	    [hashtable]$SNMP = $null,

        [Parameter(Mandatory = $True,ParameterSetName = "Default",HelpMessage = "provide Interconnect bay set number", Position = 11)]
        [Alias('interconnectBaySet')]
	    [String]$iConnectBaySet,

        [Parameter(Mandatory = $True,ParameterSetName = "Default",HelpMessage = "provide Interconnect type[logical-interconnect-groupV300, sas-logical-interconnect-group]", Position = 12)]
	    [String]$interconnectType,

        [Parameter(Mandatory = $True,ParameterSetName = "Import",HelpMessage = "Specify JSON source file to create Logical Interconnect Group")]
        [ValidateScript({split-path $_ | Test-Path})]
        [Alias('i')]
	    [object]$Import
        

    )

    Begin {
        
        #Check to make sure the user is authenticated
        If (!$global:cimgmtSessionId){
            $errorRecord = New-ErrorRecord HPOneview.Appliance.AuthSessionException NoAuthSession AuthenticationError $($MyInvocation.InvocationName.ToString().ToUpper()) -Message "No valid session ID found.  Please use Connect-HPOVMgmt to connect and authenticate to an appliance." #-verbose
            $PSCmdlet.ThrowTerminatingError($errorRecord)

	    }
    }
	
	Process{

        If ($Import){
            
            Write-Log -LogPath $CompletePath -LineValue "Reading input file"

            try {

                #Open input file, join so we can vlidate if the JSON format is correct.
                $lig = [string]::Join("", (gc $import -ErrorAction Stop)) | convertfrom-json -ErrorAction Stop
                $lig | write-debug

                Write-Log -LogPath $CompletePath -LineValue "Sending request"
                $task = Send-HPOVRequest $logicalInterconnectGroupsUri POST $lig

            }
            
            #If there was a problem with the input file (format, not syntax) throw error
            catch [System.ArgumentException] {

                $errorRecord = New-ErrorRecord InvalidOperationException InvalidArgumentValue InvalidArgument 'Import' -TargetType "PSObject" -Message "JSON Input File is invalid.  Please check the contents and try again." #-verbose
                $PSCmdLet.ThrowTerminatingError($errorRecord)
            }

        }

		 Else {
            if($redundancyType){
              
		        $lig = @{
                    name                    = $ligName;
	                state                   = "Active";
	                status                  = $null; 
    	            uplinkSets              = @();




                    enclosureType           = "SY12000";
    	            interconnectMapTemplate = @{interconnectMapEntryTemplates = @()};
	                ethernetSettings = @{
                        #type                        = "EthernetInterconnectSettingsV300";
                        type                        = "EthernetInterconnectSettingsV201";
                        enableIgmpSnooping          = $enableIgmpSnooping;
                        igmpIdleTimeoutInterval     = $igmpIdleTimeoutInterval; 
                        enableFastMacCacheFailover  = $enableFastMacCacheFailover;
                        macRefreshInterval          = $macRefreshInterval;
                        enableNetworkLoopProtection = $enableNetworkLoopProtection;
                        enablePauseFloodProtection  = $enablePauseFloodProtection;

                    };

	    		    snmpConfiguration       = $snmp;
	                stackingMode            = "Enclosure";
                    type                    = $interconnectType;
                    interconnectBaySet      = $iConnectBaySet;
                    redundancyType          = $redundancyType;
                    enclosureIndexes        = $enclosureIndexes
	                }
            }
            else{
            $lig = @{
                    name                    = $ligName;
	                state                   = "Active";
	                status                  = $null; 
                    enclosureType           = "SY12000";
    	            interconnectMapTemplate = @{interconnectMapEntryTemplates = @()} 		    
                    type                    = $interconnectType;
                    interconnectBaySet      = $iConnectBaySet;
                    enclosureIndexes        = $enclosureIndexes
	                }
            }


        
        
            #Make sure the snmpConfiguration type property is set, as the caller might not know about this.
            if ($lig.snmpConfiguration) { $lig.snmpConfiguration.type = "snmp-configuration" }
		
            foreach($imt in $interconnectMapTemplate){
                          if($imt["type"] -match "SAS"){
                            $ret = Get-HPOVSASInterconnectType -partNumber $imt["PN"]
                            $lig.interconnectMapTemplate.interconnectMapEntryTemplates += @{
                            enclosureIndex =  $imt["enclosureindex"];
	                        permittedInterconnectTypeUri = $ret.uri;
                            logicalLocation = @{locationEntries = @(@{relativeValue = $imt["bay"]; type = "Bay"}, @{relativeValue = $imt["enclosureindex"]; type = "Enclosure"})}}
                            }
                          else{
                            $ret = Get-HPOVInterconnectType -partNumber $imt["PN"]
                            $lig.interconnectMapTemplate.interconnectMapEntryTemplates += @{
                            enclosureIndex =  $imt["enclosureindex"];
                            logicalDownlinkUri = $null;      
	                        permittedInterconnectTypeUri = $ret.uri;
                            logicalLocation = @{locationEntries = @(@{relativeValue = $imt["bay"]; type = "Bay"}, @{relativeValue = $imt["enclosureindex"]; type = "Enclosure"})}}
                            
                          }
                          
                }      
				
            Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] LIG: $($lig | out-string)"
	        Write-Log -LogPath $CompletePath -LineValue "[$($MyInvocation.InvocationName.ToString().ToUpper())] Sending request to create $Name..."
            if($imt["type"] -match "SAS"){
                $task = Send-HPOVRequest $script:sasLogicalInterconnectGroupsUri POST $lig
                }
            else{
  
            $task = Send-HPOVRequest $script:logicalInterconnectGroupsUri POST $lig        
			}

		}
	}
    End {

        $task
}
}

Function Start-servers{
param(
        [parameter(Mandatory = $true, HelpMessage = "Please enter the list Enclosure names) -")]
        [ValidateNotNullOrEmpty()]
        [string[]] $enclosureNames,

        [parameter(Mandatory = $false, HelpMessage = "Enter the default timeout in seconds-")]
         $timeout=600

        )
process{
    $tasks = @()
    forEach($encName in $enclosureNames){
        $enc= (Get-HPOVEnclosure $encName| select name, deviceBays)
        $bays=$enc.deviceBays | select bayNumber,devicePresence,deviceUri,bayPowerState

        foreach ($dbay in $bays) {
            if($dbay.deviceUri -match "/rest/server-hardware"){
                $powerState = (Send-HPOVRequest $dbay.deviceUri).powerstate
                if ($dbay.devicePresence -eq "Present" -and $powerState -ne "On" ){
                    Write-Host "device at bay " $dbay.bayNumber "Powering it On..."
                    $tasks += Set-HPOVServerPower -serverUri $dbay.deviceUri -powerState "On" -powerControl "MomentaryPress"
                    }
            }
        }
        }
    if($tasks){
    Write-host "Waiting on server Power on"
     foreach($task in $tasks){
        #$state = Wait-HPOVTaskComplete $task.uri -timeout (New-TimeSpan -Minutes 10)
        wait-for-task -task_uri $task.uri -timeout $timeout
        }
    }
  }
} 

Function Stop-servers{
param(
        [parameter(Mandatory = $true, HelpMessage = "Please enter the list Enclosure names) -")]
        [ValidateNotNullOrEmpty()]
        [string[]] $enclosureNames,

        [parameter(Mandatory = $false, HelpMessage = "Enter the default timeout in seconds-")]
         $timeout=600)
process{
         #power off servers
    $tasks = @()
    forEach($encName in $enclosureNames){
        $enc= (Get-HPOVEnclosure $encName| select name, deviceBays)
        $bays=$enc.deviceBays | select bayNumber,devicePresence,deviceUri,bayPowerState
        
        foreach ($dBay in $bays) {
            if($dbay.deviceUri -match "/rest/server-hardware"){
                $powerState = (Send-HPOVRequest $dbay.deviceUri).powerstate
                if ($dBay.devicePresence -eq "Present" -and $powerState -ne "Off" ){
                    $device= Send-HPOVRequest $dBay.deviceUri
                    if ($device.powerState -ne "Off") {
                        Write-Host "Server" $device.name "is" $device.powerState ".  Powering it off..."
                        $tasks += Set-HPOVServerPower -serverUri $device.uri -powerState "Off" -powerControl "PressAndHold"
			            }
                    }
		}
}}
#Wait for power off to be completed
if($tasks){
    Write-host "Waiting for servers to be powered off"
    foreach($task in $tasks){
	    wait-for-task -task_uri $task.uri -timeout $timeout
	}
}
}
}

function New-TBirdServerProfile{
Param (
        [parameter(Mandatory = $false)]
        [ValidateNotNullOrEmpty()]
        [string[]]$enclosureNames,
        [parameter(Mandatory = $false, HelpMessage = "Enter the default timeout in seconds-")]
        $timeout=600                
        )
$Tasks = @()
ForEach($enclosureName in $enclosureNames){
    Write-Host("Create Server Profiles for Enclosure - {0}" -f $enclosureName)
    $enc= (Get-HPOVEnclosure $enclosureName| select name, deviceBays)
    $bays=$enc.deviceBays | select bayNumber,devicePresence,deviceUri

    foreach ($dBay in $bays) {
        if ($dBay.devicePresence -eq "Present") {
            if($dbay.deviceUri -match "/rest/server-hardware"){
             $device= Send-HPOVRequest $dBay.deviceUri
            
                #create profile
                if ($device.state -eq "NoProfileApplied" -and $device.uri -match "server-hardware") { 
                    $profileName = "Profile-" + $device.name
                    Write-Host "Creating" $profileName "for server" $device.name
                    $task = New-HPTBProfile -name $profileName -server $device
                    Write-Log -LogPath $CompletePath -LineValue $task
                    $Tasks +=$task
                    }
            }
            }
          }
        }
#Wait for power off to be completed
Write-host "Waiting for profiles to be created"
 foreach($task in $Tasks){
	wait-for-task -task_uri $task.uri -timeout $timeout
	}
}

Function Update-ServerFirmware{
Param (
        [parameter(Mandatory = $false)]
        [ValidateNotNullOrEmpty()]
        [string[]]$enclosureNames,
        [parameter(Mandatory = $false)]
        [ValidateNotNullOrEmpty()]
        [string]$sppFileName,
        [parameter(Mandatory = $false, HelpMessage = "Enter the default timeout in seconds-")]
        $timeout=3600,
        [parameter(Mandatory = $false, HelpMessage = "Enter the True\False for force Firmware installation-")]
        [boolean]$forceInstallFirmware = $true)
process{
		$Tasks = @()
		ForEach($enclosureName in $enclosureNames){
		Write-Host("Apply firmware baseline to servers for Enclosure - {0}" -f $enclosureName)
		$enc= (Get-HPOVEnclosure $enclosureName| select name, deviceBays)
		$bays=$enc.deviceBays | select bayNumber,devicePresence,deviceUri

			foreach ($dBay in $bays) {
				if ($dBay.devicePresence -eq "Present") { 
					$device= Send-HPOVRequest $dBay.deviceUri
					if ($device.state -eq "ProfileApplied") { 
                        $profile = Send-HPOVRequest $device.serverProfileUri
						$serverType = Send-HPOVRequest $profile.serverHardwareTypeUri
                        $fw = Get-HPOVBaseLine -isoFileName $sppFileName
                        $profile.firmware.manageFirmware = $true
                        $profile.firmware.firmwareBaselineUri = $fw.uri
                        $profile.firmware.forceInstallFirmware = $forceInstallFirmware
                        $profile.firmware.firmwareInstallType = "FirmwareOnlyOfflineMode"
                        $task = Set-HPOVResource $profile
                        Write-Log -LogPath $CompletePath -LineValue $task
                        $Tasks += $task
                       }
                }
        }
    }
#Wait for power off to be completed
Write-host "Waiting for firmware baseline applied to servers"
 foreach($task in $Tasks){
	wait-for-task -task_uri $task.uri -timeout $timeout
	}

}
}