"""
OvsLibrary OneView Supportibility UI Keywords.

"""

from FusionLibrary.ui.business_logic.base import ScreenShotType
from tests.ovs.OvsLibrary import ovs_fixme


class OVSUIKeywords(object):
    """
    Class for OVS fixme Keyword
    """
    __metaclass__ = ScreenShotType

    def fusion_ui_update_fixmebin(self, *app_obj):
        """Keyword to update fixme.bin
        To Update fixmebin file using upgrade framework
        Example: In Robot file
        tests.ovs.OvsLibrary.Fusion Ui Update Fixmebin    @{TestData.update_appliance}
        """
        return ovs_fixme.update_appliance(app_obj)
