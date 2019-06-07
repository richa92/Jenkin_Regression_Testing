# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
"""
    Settings page
"""


from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.business_logic.base import FusionUIBaseElements
from FusionLibrary.ui.business_logic.settings_elements import FusionSettingsPage


def navigate():
    s2l = ui_lib.get_s2l()
    if not s2l._is_element_present(FusionSettingsPage.ID_PAGE_LABEL):
        s2l.click_element(FusionUIBaseElements.ID_MAIN_MENU_CONTROL)
        s2l.wait_until_page_contains_element(FusionUIBaseElements.ID_MENU_LINK_USERS_AND_GROUPS)
        s2l.click_element(FusionUIBaseElements.ID_MENU_LINK_SETTINGS)
        s2l.wait_until_page_contains_element(FusionSettingsPage.ID_PAGE_LABEL)


def add_data_centers(datacenterName, *params):
    raise NotImplementedError


def edit_data_center(datacenterName, *params):
    raise NotImplementedError


def remove_data_center(self, datacenterName):
    raise NotImplementedError


def select_data_center(self, datacenterName):
    raise NotImplementedError
