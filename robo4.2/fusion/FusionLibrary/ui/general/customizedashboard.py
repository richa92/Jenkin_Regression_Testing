"""
    Dashboard
"""
from FusionLibrary.ui.business_logic.base import SectionType
from FusionLibrary.ui.business_logic.general.dashboard import *
from RoboGalaxyLibrary.data.test_data import DataObj


def add_dashboard_panels(*dashboard_panels_obj):
    """Add Dashboard Panels"""
    FusionUIBase.navigate_to_section(SectionType.DASHBOARD)
    AddDashboardPanel.click_add_dashboard_panel()
    AddDashboardPanel.wait_add_dashboard_panel_shown()

    if isinstance(dashboard_panels_obj, DataObj):
        dashboard_panels_obj = [dashboard_panels_obj]
    elif isinstance(dashboard_panels_obj, tuple):
        dashboard_panels_obj = list(dashboard_panels_obj)

    for n, dashboard_panel in enumerate(dashboard_panels_obj):
        if getattr(dashboard_panel, "panel", "") == "Custom":
            AddDashboardPanel.select_panel(dashboard_panel.panel)
            AddDashboardPanel.select_resource(dashboard_panel.resource)
            AddDashboardPanel.input_title(dashboard_panel.title)
            AddDashboardPanel.input_query(dashboard_panel.query)
            AddDashboardPanel.select_data_sets_type(dashboard_panel.datasetstype)
            if getattr(dashboard_panel, "datasetstype", "") == "Custom":
                AddDashboardPanel.input_caption(dashboard_panel.caption)
                AddDashboardPanel.input_other_label(dashboard_panel.otherlabel)
                if getattr(dashboard_panel, "addslice", "") != "":

                    for slice in dashboard_panel.addslice:
                        AddDashboardPanel.click_datasets_add_slice_button()
                        AddDashboardPanel.wait_add_slice_shown()
                        AddDashboardPanel.input_add_slice_label(slice.label)
                        AddDashboardPanel.input_add_slice_query(slice.query)
                        AddDashboardPanel.click_datasets_add_slice_ok()
        else:
            AddDashboardPanel.select_panel(dashboard_panel.panel)

        AddDashboardPanel.click_add_plus_button()

    AddDashboardPanel.click_cancel_button()

    total_add_fail = 0
    for n, dashboard_panel in enumerate(dashboard_panels_obj):

        if not VerifyDashboardPanel.verify_dashboard_panels_added(dashboard_panel.title):
            total_add_fail += 1
    if total_add_fail > 0:
        logger.warn("Failed to add Dashboard Panels ,the total number is [%d]" % total_add_fail)
        return False

    return True


def remove_dashboard_panels(*dashboard_panels_obj):
    """Remove Dashboard Panels"""
    FusionUIBase.navigate_to_section(SectionType.DASHBOARD)

    if isinstance(dashboard_panels_obj, DataObj):
        dashboard_panels_obj = [dashboard_panels_obj]
    elif isinstance(dashboard_panels_obj, tuple):
        dashboard_panels_obj = list(dashboard_panels_obj)

    for n, dashboard_panel in enumerate(dashboard_panels_obj):
        if getattr(dashboard_panel, "panel", "") == "Custom":
            RemoveDashboardPanel.remove_custom_dashboard_panel(dashboard_panel.title)
        else:
            RemoveDashboardPanel.remove_dashboard_panel(dashboard_panel.title)

    total_remove_fail = 0

    for n, dashboard_panel in enumerate(dashboard_panels_obj):
        if not VerifyDashboardPanel.verify_dashboard_panels_removed(dashboard_panel.title):
            total_remove_fail += 1
    if total_remove_fail > 0:
        logger.warn("Failed to remove Dashboard Panels ,the total number is [%d]" % total_remove_fail)
        return False
    return True
