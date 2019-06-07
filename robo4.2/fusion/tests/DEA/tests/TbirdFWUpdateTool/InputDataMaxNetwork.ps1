
$script:ovIP = "16.114.216.224"             
$script:ovUser = "Administrator"
$script:ovPass = "wpsthpvse1"  

$script:spppath = "E:\Downloads\SPPgen9snap6.2016_0607.115.iso"
$Global:ligs = @(@{name = "Potahs_lig_1";
                   interconnectMapTemplate =@(@{bay = 3; enclosure =1; type ="Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23";enclosureindex = 1; PN = "794502-B23"},
                            @{bay = 6; enclosure =1; type ="Synergy 20Gb Interconnect Link Module";enclosureindex = 1; PN = "779218-B21"},
                            @{bay = 3; enclosure =2; type ="Synergy 20Gb Interconnect Link Module";enclosureindex = 2; PN = "779218-B21"},
                            @{bay = 6; enclosure =2; type ="Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23";enclosureindex = 2; PN = "794502-B23"},
                            @{bay = 3; enclosure =3; type ="Synergy 20Gb Interconnect Link Module";enclosureindex = 3; PN = "779218-B21"},
                            @{bay = 6; enclosure =3; type ="Synergy 20Gb Interconnect Link Module";enclosureindex = 3; PN = "779218-B21"});
                    enclosureIndexes =@(1,2,3);
                    redundanttype = "HighlyAvailable";
                    interconnectBaySet =3;
                    type = "logical-interconnect-groupV300"},
                @{name = "Potahs_lig_2";
                   interconnectMapTemplate =@(@{bay = 2; enclosure =1; type ="Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23";enclosureindex = 1; PN = "794502-B23"},
                            @{bay = 5; enclosure =1; type ="Synergy 20Gb Interconnect Link Module";enclosureindex = 1; PN = "779218-B21"},
                            @{bay = 2; enclosure =2; type ="Synergy 20Gb Interconnect Link Module";enclosureindex = 2; PN = "779218-B21"},
                            @{bay = 5; enclosure =2; type ="Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23";enclosureindex = 2; PN = "794502-B23"},
                            @{bay = 2; enclosure =3; type ="Synergy 20Gb Interconnect Link Module";enclosureindex = 3; PN = "779218-B21"},
                            @{bay = 5; enclosure =3; type ="Synergy 20Gb Interconnect Link Module";enclosureindex = 3; PN = "779218-B21"});
                    enclosureIndexes =@(1,2,3);
                    redundanttype = "HighlyAvailable";
                    interconnectBaySet =2;
                    type = "logical-interconnect-groupV300"})


# Example for Natasha
<#
@{name = "lig_1";
                   interconnectMapTemplate =@(@{bay = 1; enclosure =1; type ="HPE Synergy 12Gb SAS Connection Module";enclosureindex = 1; PN = "755985-B21"} );
                    enclosureIndexes =@(1);
                    interconnectBaySet =1;
                    type = "sas-logical-interconnect-group"}
#>

$script:runTRU = $True
$script:TRU_FileName = "tru-2.0.6.21.zip"
$script:TRU_RecipeFileName = "RecipeGARFS18.rcp"

$script:runHPIPU = $False
$script:HPIP_FileName = "hpip-update1.0.zip"
$script:isopath = "http://10.0.0.5/Cosmos/Builds/T-bird/GARFS18/Step06_HPIP_2.50_Build_88/HPIP250.2016_0524.88.iso"

$script:runFRU = $False
$script:FRU_FileName = "hpeMgmtUtil_v2.7.3_20160603_internal.tar" #FRU utitlity name
$script:frulocal = $True # Update as $False if want to skip the FRU update for local enclosure
$script:fruRemoteFrameNames = @() # Provide all remote frame as a list @("frame1","frame2") "CN754406X3", "CN7544023R"
$script:ilofwupdate = $False
$script:iLOusername = "Administrator"
$script:iLOpassword = "hpvse123"
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
$script:runFWU = $False #FWU, BBFWU, BBFWU-O, $False
$script:haltTest = $false
$script:forceInstallFirmware = $True
$script:profileFirmware = $False #only applicable with BBFWU-O
$script:bigBangFirmwareoption = $false  #only applicable with BBFWU-O, BigBang firmware Update with different choices, profileFirmare, [EnclosureOnly] | [SharedInfrastructureOnly]

$Global:leName =  "TB_LogicalEnclosure"
$Global:egName =  "TB_EnclGroup"
$Global:Path = Get-Location
$Global:LogFileName = Get-Date -Format s | foreach {$_ -replace ":", "."}
$Global:ConsoleFName = "Console_" + $LogFileName + ".html"
$Global:LogFileName ="GFU_" + $LogFileName + ".log"
$Global:CompletePath = $Path.path+"\"+$LogFileName
$Global:CompleteConsolePath = $Path.path+"\"+$ConsoleFName
