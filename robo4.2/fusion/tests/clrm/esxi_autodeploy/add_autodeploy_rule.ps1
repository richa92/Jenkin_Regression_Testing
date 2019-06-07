# Script adds a autodeploy rule to vcenter. It also adds the esxi depot image. Requires a profile to be created and available
# Example
#./Add_autodeploy_rule.ps1 10.1.47.13 Administrator@vsphere.local Welcome123# HPE-ESXi-6.7.0-OS-Release-Gen9plus-670.10.2.0.35 ESXI_67_C7k_G9 Z:\Sushil\auto_deploy\HPE-ESXi-6.7.0-OS-Release-Gen9plus-670.10.2.0.35-8169922.zip Deploy_DC SP-EB1301-BOTTOM-bay-9 VCGBUWO01Q
param (
    [string]$vcenter = "",
    [string]$username = "",
    [string]$password = "",
    [string]$image_name = "",
    [string]$profile_name = "",
    [string]$sw_depot = "",
    [string]$DC_name = "",
    [string]$rule_name = "",
    [string]$serial_num = ""
      )

Set-PowerCLIConfiguration -Scope User -ParticipateInCEIP $False -Confirm:$False
Set-PowerCLIConfiguration -InvalidCertificateAction ignore -Confirm:$False

Connect-VIServer $vcenter -User $username -Password $password

Add-EsxSoftwareDepot $sw_depot

New-DeployRule -Name $rule_name -Item $image_name,$profile_name,$DC_name -Pattern serial=$serial_num

add-deployrule $rule_name

Disconnect-VIServer -Confirm:$False
