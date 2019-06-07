# Script removes autodeploy rule by given name from the vcenter
# Example:
# ./Remove_autodeploy_rule.ps1 10.1.47.13 Administrator@vsphere.local Welcome123# SP-EB1301-BOTTOM-bay-9
param (
    [string]$vcenter = "",
    [string]$username = "",
    [string]$password = "",
    [string]$rule_name = ""
      )

Set-PowerCLIConfiguration -Scope User -ParticipateInCEIP $False -Confirm:$False
Set-PowerCLIConfiguration -InvalidCertificateAction ignore -Confirm:$False

Connect-VIServer $vcenter -User $username -Password $password

Get-DeployRule $rule_name | Remove-DeployRule -Delete

Disconnect-VIServer -Confirm:$False