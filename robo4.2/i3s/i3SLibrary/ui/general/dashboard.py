# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
"""
    Dashboard
"""


from i3SLibrary.ui.general.dashboard_elements import i3SDashboardPage
from i3SLibrary.ui.general.base_elements import i3SBasePage
from i3SLibrary.ui.general import base_page


def navigate():
    base_page.navigate_base(i3SDashboardPage.ID_PAGE_LABEL, i3SBasePage.ID_MENU_LINK_DASHBOARD, "css=span.hp-count")
