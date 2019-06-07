# (C) Copyright 2014 Hewlett-Packard Development Company, L.P.

"""
    System Types Page
"""

from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.mantra.systemtypes.systemtypes_elements import systemtypesPage
from FusionLibrary.ui.general import base_page
from FusionLibrary.ui.mantra.utils.constants import mantraConstants
from FusionLibrary.ui.mantra.utils import mantraUtils


def navigate():
    logger._log_to_console_and_log_file("")
    base_page.navigate_base(systemtypesPage.ID_PAGE_LABEL, systemtypesPage.ID_MENU_LINK_SYSTEMTYPES, "css=span.hp-page-item-count")


def navigateMap():
    # Accessing MAP view perspective
    logger._log_to_console_and_log_file("")
    logger._log_to_console_and_log_file("- Changing view to MAP perspective")
    if ui_lib.wait_for_element_and_click(systemtypesPage.ID_BUTTON_MAP):
        # Using checkElements to verify if the elements were displayed
        if mantraUtils.checkElements([[systemtypesPage.ID_MAP_CS, "'System Profile'"],
                                      [systemtypesPage.ID_MAP_SYSTEMS, "'Systems'"],
                                      [systemtypesPage.ID_MAP_SYSTEM_TYPES, "'System Types'"]]):
            ui_lib.fail_test("- At least one element was not found. Please check the 'Overview' page")
        else:
            logger._log_to_console_and_log_file("- All the elements were found")
    else:
        ui_lib.fail_test("- Unable to change view to MAP perspective")


def checkOverviewPage():
    failure = False
    logger._log_to_console_and_log_file("")
    # Using checkElements to verify if the elements were displayed, if not, mark failure as true
    if mantraUtils.checkElements([[systemtypesPage.ID_CS, "'CS'"],
                                  [systemtypesPage.ID_CS_VERSION, "'CS Version'"],
                                  [systemtypesPage.ID_VERSION, "'Version'"],
                                  [systemtypesPage.ID_VERSION_CONTENT, "'Version CONTENT'"],
                                  [systemtypesPage.ID_AUTHOR, "'Author'"],
                                  [systemtypesPage.ID_AUTHOR_CONTENT, "'Author CONTENT'"],
                                  [systemtypesPage.ID_DESCRIPTION, "'Description'"],
                                  [systemtypesPage.ID_DESCRIPTION_CONTENT, "'Description CONTENT'"]]):
        failure = True

    # Using checkElementsText to verify if the purposes were displayed
    if mantraUtils.checkElementsText([[systemtypesPage.ID_CONTENTS_TABLE, "'Purpose: Clusters'", mantraConstants.CLUSTER_HOST],
                                      [systemtypesPage.ID_CONTENTS_TABLE, "'Purpose: CS700 Array'", mantraConstants.CS700_ARRAY],
                                      [systemtypesPage.ID_CONTENTS_TABLE, "'Purpose: CS700 Enclosure'", mantraConstants.CS700_ENCLOSURE],
                                      [systemtypesPage.ID_CONTENTS_TABLE, "'Purpose: CS700 SAN Switch'", mantraConstants.CS700_SAN_SWITCH],
                                      [systemtypesPage.ID_CONTENTS_TABLE, "'Purpose: CS700 TOR'", mantraConstants.CS700_TOR],
                                      [systemtypesPage.ID_CONTENTS_TABLE, "'Purpose: Hosts'", mantraConstants.HOSTS],
                                      [systemtypesPage.ID_CONTENTS_TABLE, "'Purpose: Interconnects'", mantraConstants.INTERCONNECTS],
                                      [systemtypesPage.ID_CONTENTS_TABLE, "'Purpose: Management Server'", mantraConstants.MANAGEMENT_SERVER],
                                      [systemtypesPage.ID_CONTENTS_TABLE, "'Purpose: PDU'", mantraConstants.PDU],
                                      [systemtypesPage.ID_CONTENTS_TABLE, "'Purpose: Rack'", mantraConstants.RACK],
                                      [systemtypesPage.ID_CONTENTS_TABLE, "'Purpose: Servers'", mantraConstants.SERVERS]]):
        failure = True

    # Checking if some verifications reported a failure
    if failure:
        ui_lib.fail_test("- At least one element was not found. Please check the 'Overview' page")
    else:
        logger._log_to_console_and_log_file("- All the elements were found")
