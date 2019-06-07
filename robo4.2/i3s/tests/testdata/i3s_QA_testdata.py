"""
Module:  i3S QA Shared Variables
Purpose: Shared variables for the Automation QA Team
"""

__author__  = "i3S Automation QA"
__version__ = "0.1"

GENERAL = {
        "fusion_IP"             :    '15.212.164.206',
        "DEFAULT_USER"          :    'Administrator',
        "DEFAULT_PASSWORD"      :    'admin123',
        "SELENIUM_SPEED"        :    '0.0',
        "BROWSER"               :    'Firefox',
}

VCENTER =    { 
        "VSPHERE_IP"            :   "16.84.192.161",
        "VSPHERE_USERNAME"      :    "ImgMgmt",
        "VSPHERE_PASSWORD"      :    "HP!nv3nt",
        }

#
#  Expose Dictionary Keys/Values as Variables
#              
              
locals().update(GENERAL)
locals().update(VCENTER)
