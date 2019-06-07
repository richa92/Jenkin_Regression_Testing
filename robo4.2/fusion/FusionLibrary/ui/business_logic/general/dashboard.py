"""
    Dashboard
"""

from FusionLibrary.ui.business_logic.base import TakeScreenShotWhenReturnFalseDeco, FusionUIBase
from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.business_logic.general.dashboard_elements import GeneralDashboardElements, AddDashboardPanelElements, RemoveDashboardPanelElements
from RoboGalaxyLibrary.utilitylib import logging as logger


class AddDashboardPanel(object):

    @classmethod
    def click_add_dashboard_panel(cls, timeout=5, fail_if_false=True):
        logger.debug("click add Dashboard")
        ui_lib.wait_for_element_and_click(GeneralDashboardElements.ID_BUTTON_DASHBOARD_ACTION, timeout, fail_if_false)
        ui_lib.wait_for_element_and_click(GeneralDashboardElements.ID_SELECT_ADD_DASHBOARD_ACTIONS, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_dashboard_panel_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait for  Add Dashboard Panel dialog shown ")
        ui_lib.wait_for_element_visible(AddDashboardPanelElements.ID_DIALOG_ADD_DASHBOARD_PANEL, timeout, fail_if_false)

    @classmethod
    def select_panel(cls, panel, timeout=5, fail_if_false=True):
        logger.debug("select panel [%s]" % panel)
        ui_lib.wait_for_element_and_click(AddDashboardPanelElements.ID_DROPDOWN_PANEL, timeout, fail_if_false)
        ui_lib.wait_for_element_and_click(AddDashboardPanelElements.ID_SELECT_PANEL % panel, timeout, fail_if_false)

    @classmethod
    def select_resource(cls, resource, timeout=5, fail_if_false=True):
        logger.debug("select resource [%s]" % resource)
        ui_lib.wait_for_element_and_click(AddDashboardPanelElements.ID_DROPDOWN_RESOURCE, timeout, fail_if_false)

        FusionUIBase.scroll_element_into_viewpoint(AddDashboardPanelElements.ID_SELECT_RESOURCE % resource)
        ui_lib.wait_for_element_and_click(AddDashboardPanelElements.ID_SELECT_RESOURCE % resource, timeout, fail_if_false)

    @classmethod
    def input_title(cls, title, timeout=5, fail_if_false=True):
        logger.debug("input title %s" % title)
        ui_lib.wait_for_element_and_input_text(AddDashboardPanelElements.ID_INPUT_TITLE, title, timeout,
                                               fail_if_false)

    @classmethod
    def input_query(cls, query, timeout=5, fail_if_false=True):
        logger.debug("input query %s" % query)
        ui_lib.wait_for_element_and_input_text(AddDashboardPanelElements.ID_INPUT_QUERY, query, timeout,
                                               fail_if_false)

    @classmethod
    def select_data_sets_type(cls, data_sets_type, timeout=5, fail_if_false=True):
        logger.debug("select data sets type [%s]" % data_sets_type)
        ui_lib.wait_for_element_and_click(AddDashboardPanelElements.ID_DROPDOWN_DATA_SETS_TYPE, timeout, fail_if_false)
        ui_lib.wait_for_element_and_click(AddDashboardPanelElements.ID_SELECT_DATA_SETS_TYPE % data_sets_type, timeout, fail_if_false)

    @classmethod
    def click_add_plus_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click Add +")
        ui_lib.wait_for_element_and_click(AddDashboardPanelElements.ID_BUTTON_ADD_PLUS, timeout, fail_if_false)

    @classmethod
    def click_add_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click Add")
        ui_lib.wait_for_element_and_click(AddDashboardPanelElements.ID_BUTTON_ADD, timeout, fail_if_false)

    @classmethod
    def click_cancel_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click Cancel")
        ui_lib.wait_for_element_and_click(AddDashboardPanelElements.ID_BUTTON_CANCEL, timeout, fail_if_false)

    @classmethod
    def click_datasets_add_slice_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click Add slice")
        ui_lib.wait_for_element_and_click(AddDashboardPanelElements.ID_BUTTON_ADD_SLICE, timeout, fail_if_false)

    @classmethod
    def input_caption(cls, caption, timeout=5, fail_if_false=True):
        logger.debug("input aption [%s]" % caption)
        ui_lib.wait_for_element_and_input_text(AddDashboardPanelElements.ID_INPUT_CAPTION, caption, timeout,
                                               fail_if_false)

    @classmethod
    def input_other_label(cls, other_label, timeout=5, fail_if_false=True):
        logger.debug("input aption [%s]" % other_label)
        ui_lib.wait_for_element_and_input_text(AddDashboardPanelElements.ID_INPUT_OTHER_LABEL, other_label, timeout,
                                               fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_slice_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait for Add Slice dialog shown ")
        ui_lib.wait_for_element_visible(AddDashboardPanelElements.ID_DIALOG_ADD_SLICE_DIALOG, timeout, fail_if_false)

    @classmethod
    def input_add_slice_label(cls, add_slice_label, timeout=5, fail_if_false=True):
        logger.debug("input Add Slice label [%s]" % add_slice_label)
        ui_lib.wait_for_element_and_input_text(AddDashboardPanelElements.ID_INPUT_ADD_SLICE_LABEL, add_slice_label, timeout,
                                               fail_if_false)

    @classmethod
    def input_add_slice_query(cls, add_slice_query, timeout=5, fail_if_false=True):
        logger.debug("input Add Slice label [%s]" % add_slice_query)
        ui_lib.wait_for_element_and_input_text(AddDashboardPanelElements.ID_INPUT_ADD_SLICE_QUERY, add_slice_query, timeout,
                                               fail_if_false)

    @classmethod
    def click_datasets_add_slice_ok(cls, timeout=5, fail_if_false=True):
        logger.debug("click Add slice OK")
        ui_lib.wait_for_element_and_click(AddDashboardPanelElements.ID_BUTTON_ADD_SLICE_OK, timeout, fail_if_false)


class RemoveDashboardPanel(object):

    @classmethod
    def remove_dashboard_panel(cls, dashboard_panel):
        logger.debug("remove dashboard panel [%s]" % dashboard_panel)
        ui_lib.move_to_element_and_click(GeneralDashboardElements.ID_DASHBOARD_PANEL % dashboard_panel, RemoveDashboardPanelElements.ID_REMOVE_DASHBOARD_PANEL % dashboard_panel)

    @classmethod
    def remove_custom_dashboard_panel(cls, dashboard_panel, timeout=5, fail_if_false=True):
        logger.debug("remove custom dashboard panel [%s]" % dashboard_panel)
        ui_lib.move_to_element_and_click(GeneralDashboardElements.ID_DASHBOARD_PANEL % dashboard_panel, RemoveDashboardPanelElements.ID_REMOVE_DASHBOARD_PANEL % dashboard_panel)
        ui_lib.wait_for_element_visible(RemoveDashboardPanelElements.ID_DIALOG_REMOVE_DASHBOARD_PANEL, timeout, fail_if_false)
        ui_lib.wait_for_element_and_click(RemoveDashboardPanelElements.ID_BUTTON_REMOVE_PANEL_YES_REMOVE, timeout, fail_if_false)


class VerifyDashboardPanel(object):

    @classmethod
    def verify_dashboard_panels_added(cls, dashboard_panel, timeout=5, fail_if_false=False):
        logger.debug("verify dashboard panels added [%s]" % dashboard_panel)
        if not ui_lib.wait_for_element_visible(GeneralDashboardElements.ID_DASHBOARD_PANEL % dashboard_panel, timeout, fail_if_false):
            logger.warn("[%s] has not been added!" % dashboard_panel)
            return False
        else:
            return True

    @classmethod
    def verify_dashboard_panels_removed(cls, dashboard_panel, timeout=5, fail_if_false=False):
        logger.debug("verify dashboard panels removed [%s]" % dashboard_panel)
        if not ui_lib.wait_for_element_notvisible(GeneralDashboardElements.ID_DASHBOARD_PANEL % dashboard_panel, timeout, fail_if_false):
            logger.warn("[%s] has not been removed!" % dashboard_panel)
            return False
        else:
            return True
