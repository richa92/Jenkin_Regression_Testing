
$script:ovIP = "10.16.25.254"             
$script:ovUser = "Administrator"
$script:ovPass = "Tbird123"  

#$script:spppath = "C:\SPP\SPP2017070.2017_0608.153.iso"       # \\eml.us.rdlabs.hpecorp.net\DEA\Hardware Firmware Software\SPP\SPPGen10Snap1FF\SPP2017070.2017_0608.153.iso
$script:spppath = "C:\SPP\SPPGen10Snap1FF.2017_0622.20.iso"

$Global:ligs = @(@{name = "lig_1";
                   interconnectMapTemplate =@(@{bay = 3; enclosure =1; type ="Virtual Connect SE 40Gb F8 Module for Synergy";enclosureindex = 1; PN = "794502-B23"}
                   #         @{bay = 6; enclosure =1; type ="Synergy 20Gb Interconnect Link Module";enclosureindex = 1; PN = "779218-B21"},
                   #         @{bay = 3; enclosure =2; type ="Synergy 20Gb Interconnect Link Module";enclosureindex = 2; PN = "779218-B21"},
                   #         @{bay = 6; enclosure =2; type ="Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23";enclosureindex = 2; PN = "794502-B23"}
                   );
                    #enclosureIndexes =@(1,2);
                    enclosureIndexes =@(1);
                    redundanttype = "NonRedundantASide";   # HighlyAvailable
                    interconnectBaySet =3;
                    type = "logical-interconnect-groupV300"})

# Example for Natasha
<#
@{name = "lig_1";
                   interconnectMapTemplate =@(@{bay = 1; enclosure =1; type ="HPE Synergy 12Gb SAS Connection Module";enclosureindex = 1; PN = "755985-B21"} );
                    enclosureIndexes =@(1);
                    interconnectBaySet =1;
                    type = "sas-logical-interconnect-group"}
#>

$script:runTRU = $False
$script:TRU_FileName = "tru-2.0.6.15.zip"
$script:TRU_RecipeFileName = "RecipeGARFS15.rcp"

$script:runHPIPU = $False
$script:HPIP_FileName = "tru-2.0.6.10.zip"
$script:HPIP_RecipeFileName = "RecipeGARFS14.rcp"
$script:isopath = "http://10.0.0.5/Cosmos/Builds/T-bird/GARFS16/Step06_HPIP250.2016_0506.83.iso"

$script:runFRU = $False
$script:FRU_FileName = "hpeMgmtUtil_v2.7.0_20160513_internal.tar" #FRU utitlity name
$script:frulocal = $True
$script:fruRemoteFrameNames = @("CN75460705") # Provide all remote frame as a list @("frame1","frame2")
$script:ilofwupdate = $True
$script:iLOusername = "Administrator"
$script:iLOpassword = "Tbird123"
$script:fru_halt = $false
$script:fruTimeOut = 2000 # timeout in seconds

$script:efuseFrames = $False
$script:efuse_FileName = "em_cim_cli.py"
<#
FWU     =>	Update Infrastructure (EM, ICM and servers) firmware, it provides firmware baseline while creating LE.
BBFWU   =>	BigBang firmware update, it also updates the firmware but first it creates LE without firmware baseline, 
            creates server profile without firmware baseline and then triggers firmware update for SharedInfrastructureAndServerProfiles.
BBFWU-O =>	BigBang firmware update with different options, here we have option to skip firmware update for servers, EM and Interconnects.
#>
#$script:runFWU = $false #FWU, BBFWU, BBFWU-O, $False
#$script:runFWU = $True #FWU, BBFWU, BBFWU-O, $False
$script:runFWU = "FWU" #FWU, BBFWU, BBFWU-O, $False
$script:haltTest = $false
$script:forceInstallFirmware = $True
$script:profileFirmware = $True #only applicable with BBFWU-O
$script:bigBangFirmwareoption = "SharedInfrastructureOnly"  #only applicable with BBFWU-O, BigBang firmware Update with different choices, profileFirmare, [EnclosureOnly] | [SharedInfrastructureOnly]

$Global:leName =  "TB_LogicalEnclosure"
$Global:egName =  "TB_EnclGroup"
$Global:Path = Get-Location
$Global:LogFileName = Get-Date -Format s | foreach {$_ -replace ":", "."}
$Global:ConsoleFName = "Console_" + $LogFileName + ".html"
$Global:LogFileName ="GFU_" + $LogFileName + ".log"
$Global:CompletePath = $Path.path+"\"+$LogFileName
$Global:CompleteConsolePath = $Path.path+"\"+$ConsoleFName
