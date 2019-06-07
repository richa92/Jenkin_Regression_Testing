# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
'''

This file contains all element ID on Fusion base UI page

'''


class FusionBasePage(object):
    ID_PAGE_LABEL = "xpath=//div[@class='hp-page-label']/h1"
    ID_MASTER_PANE = "xpath=//div[contains(@class, 'hp-master-pane')]"
    ID_ACTIVITY_CONTROL = "hp-activity-control"
    ID_ACTIVITY_NOTIFICATION = "//div[@id='hp-activity-notification']"
    ID_ACTIVE_ACTIVITY_NOTIFICATION = "//div[@id='hp-activity-notification'][contains(@class, 'hp-active')]"
    ID_ACTIVITY_MESSAGE = ID_ACTIVITY_NOTIFICATION + "//div[@class='hp-message']"
    ID_DASHBOARD = "hp-dashboard-primary"
    ID_EMPTYMESSAGE = "div.hp-empty-message"
    ID_HELP = "css=div.hp-icon.hp-help"
    ID_HELP_ON_THIS_PAGE = "link=Help on this page"
    ID_HP_LOGO = "hp-logo"
    ID_MAIN_BANNER = "hp-main-banner"
    ID_MAIN_MENU = "hp-main-menu"
    ID_MAIN_MENU_CONTROL = "hp-main-menu-control"
    ID_SEARCH_CONTROL = "hp-search-control"
    ID_SESSION_CONTROL = "hp-session-control"
    ID_SESSION_LOGOUT = "hp-session-logout"
    ID_MENU_LINK_ACTIVITY = "link=Activity"
    ID_MENU_ACTIVITY = "xpath=.//*[@id='hp-main-menu']//li/a[text()='Activity']"
    ID_MENU_LINK_DASHBOARD = "link=Dashboard"
    ID_MENU_LINK_FIRMWARE_BUNDLES = "link=Firmware Bundles"
    ID_MENU_LINK_SERVER_PROFILE = "link=Server Profiles"
    ID_MENU_LINK_LOGICAL_ENCLOSURES = "link=Logical Enclosures"
    ID_MENU_LINK_ENCLOSURE_GROUPS = "link=Enclosure Groups"
    ID_MENU_LINK_ENCLOSURES = "link=Enclosures"
    ID_MENU_LINK_SERVER_HARDWARE = "link=Server Hardware"
    ID_MENU_LINK_SERVER_HARDWARE_TYPES = "link=Server Hardware Types"
    ID_MENU_LINK_LOGICAL_INTERCONNECT_GROUPS = "link=Logical Interconnect Groups"
    ID_MENU_LINK_LOGICAL_INTERCONNECTS = "link=Logical Interconnects"
    ID_MENU_LINK_NETWORKS = "link=Networks"
    ID_MENU_LINK_NETWORK_SETS = "link=Network Sets"
    ID_MENU_LINK_INTERCONNECTS = "link=Interconnects"
    ID_MENU_LINK_DATA_CENTERS = "link=Data Centers"
    ID_MENU_LINK_RACKS = "link=Racks"
    ID_MENU_LINK_POWER_DELIVERY_DEVICES = "link=Power Delivery Devices"
    ID_MENU_LINK_UNMANAGED_DEVICES = "link=Unmanaged Devices"
    ID_MENU_LINK_SETTINGS = "link=Settings"
    ID_MENU_LINK_STORAGE_SYSTEMS = "link=Storage Systems"
    ID_MENU_LINK_STORAGE_POOLS = "link=Storage Pools"
    ID_MENU_LINK_STORAGE_TEMPLATES = "link=Volume Templates"
    ID_MENU_LINK_STORAGE_VOLUMES = "link=Volumes"
    ID_MENU_LINK_USERS_AND_GROUPS = "link=Users and Groups"
    ID_MENU_LINK_SAN_MANAGERS = "link=SAN Managers"
    ID_MENU_LINK_SAN = "link=SANs"
    ID_MENU_LINK_PROFILE_TEMPLATE = "link=Server Profile Templates"
    ID_SIDEBAR_CONTROL = 'hp-sidebar-control'
    ID_MENU_ONE_VIEW = "id=hp-main-menu-labels"
    ID_LINK_NETWORK_SET = "link=Network Sets"
    ID_SIDEBAR_CONTROL = 'hp-sidebar-control'
    HELP_PAGE_TITLE = "HP OneView 1.05 help"
    HELP_PAGE_FRAME_NAME = "xpath=//frame[contains(@name, 'mainhelp_pane')]"

    # Search Generic-----------
    ID_MENU_LINK_BASE = "link=%s"
    ID_PAGE_LABEL_BASE = "xpath=//div[@class='hp-page-label']/h1[text()='%s']"
    ID_TABLE_MASTER_BASE = "xpath=.//div[@class='dataTables_scrollBody']/table[@class='hp-master-table hp-selectable dataTable']"
    ID_INPUT_SEARCH = "xpath=//div[@id='hp-search-input']/input"
    ID_SEARCH_BAR = "xpath=//h2[@id='hp-search-control']"
    ID_SEARCH_CLEAR = "xpath=//div[@id='hp-search-clear']"
    ID_LABEL_FIRMWARE_BUNDLE_BASE = "xpath=//div[@id='cic-fwdriver-page']//div[text()='%s']"
    ID_LABEL_ENCLOSURE_GROUPS_BASE = "xpath=//li[starts-with(@class,'hp-master-grid-item')]/header/div[text()='%s']"
    ID_LABEL_SERVER_HARDWARE_TYPE_BASE = "xpath=//div[@id='cic-servertypes-page']//div[text()='%s']"
    ID_MENU_LINK_REPORTS = "link=Reports"

    # Help page
    ID_HELP_CONTROL = "hp-help-control"
    HELP_PAGE_CONTENT_LIST = "xpath=//div[@class='toc']/dl/dd[%s]/table/tbody/tr/td[2]"
    HELP_PAGE_SUB_CONTENT = "xpath=//div[@class='toc']/dl/dd[%s]/dl/dd[%s]"
    HELP_PAGE_SUB_CONTENT_LIST = "xpath=//div[@class='toc']/dl/dd[%s]/dl/dd[%s]/table/tbody/tr/td[2]"
    ID_LINK_BROWSE_HELP = "href=/doc#/cic"
