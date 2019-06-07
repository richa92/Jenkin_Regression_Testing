# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
'''

This file contains all element ID on Fusion SAN page/screen

'''


class FusionSANPage(object):

    ID_PAGE_LABEL = "xpath=//div[@class='hp-page-label']/h1[text()='SANs']"
    ID_PAGE_LINK = "link=SANs"
    ID_SAN_LIST = "xpath=//div[@class='dataTables_scrollBody']/table/tbody/tr/td"
    ID_SAN_ACTIVITY = "//*[@id='cic-sans-page']/nav/div[8]/div"

# SAN general section
    ID_ELEMENT_SAN = "xpath=//td[text()='%s']"  # Replace %s with SAN IP
    ID_SAN_HEADING_TOP = "xpath=.//*[@id='cic-sans-page']/nav/div[2]/h1"
    ID_SAN_HEADING_TOP_SECTION_GENERAL = "id('cic-sans-panels')/x:div[1]/x:div/x:div/x:header/x:h2"
    ID_SAN_MAIN_HEADING = "xpath=//h1[@id='cic-sans-details-title' and"
    ID_SAN_ACTIVITY_MESSAGE = "//*[@id='hp-flyout-activities']/li/div[1]/div[2]"
    ID_SAN_SECTION_NAME = "xpath=//*[@id='cic-sans-more-panels']/li[@class='hp-stacked-panel hp-active']/label"
    ID_SAN_TAB = "xpath=//*[@id='cic-sans-panel-selector']/div"

# tabs on san screen
    ID_MENU_VIEW_MAIN_BTN = "id=cic-sans-panel-selector"
    ID_VIEW_GENERAL_SAN = "xpath=.//*[@id='cic-sans-panel-selector']/ol/li[1]/a"
    ID_VIEW_ZONINGPOLICY_SAN = "xpath=.//*[@id='cic-sans-panel-selector']/ol/li[2]/a"
    ID_VIEW_SANENDPOINTS_SAN = "xpath=.//*[@id='cic-sans-panel-selector']/ol/li[3]/a"
    ID_VIEW_ACTIVITY_SAN = "xpath=.//*[@id='cic-sans-panel-selector']/ol/li[4]/a"
    ID_VIEW_MAP_SAN = "xpath=.//*[@id='cic-sans-panel-selector']/ol/li[5]/a"
    ID_VIEW_LABELS_SAN = "xpath=.//*[@id='cic-sans-panel-selector']/ol/li[6]/a"
# action menu items on san screen
    ID_SAN_MENU_ACTION_MAIN_BTN = "xpath=//label[text()='Actions']"
    ID_SAN_MENU_ACTION_NOAUTH = "//*[@id='cic-sans-actions']/div/ol[3]/li"
    ID_SAN_MENU_ACTION_EDIT = "link=Edit"
    ID_SAN_MENU_ACTION_REFRESH = "link=Refresh"
    ID_SAN_MENU_ACTION_REMOVE = "link=Remove"
    ID_SAN_MENU_ACTION_DOWNLOAD = "link=Download endpoints table"
    ID_SAN_MENU_ACTION_REPORT = "link=Unexpected zoning report"
    ID_SAN_ZONED_POLICY_EDIT = "xpath=//a[@id='cic-sans-zoning-policy-edit-link']"
# Unexpected Zoning Report
    ID_UNEXPECTED_ZONING_REPORT_MESSAGE = "id=cic-sans-issues-report-sections"
    ID_UNEXPECTED_ZONING_REPORT_HEADING = "id=cic-sans-issues-report-overview-title"

# SAN General section
    ID_SAN_TYPE = "//div[@id='cic-sans-general-type'/label[text()='Type']"
    ID_SAN_STATE = "//div[@id='cic-sanmanagers-general-state'/label]"
    ID_SAN_PRINCIPAL_SWITCH = "//div[@id='cic-sanmanagers-general-version']"
    ID_SAN_MANAGER_LINK = "Link "
    ID_SAN_ASSOCIATED_NETWORK = "//div[@id='cic-sanmanagers-dynamic-attribute-0']"

# SAN zoning policy section
    ID_SAN_AUTOMATE_ZONING = "//*[@id='cic-sans-zoning-policy-automate-zoning']"      # //text()="
    ID_SAN_AUTOMATE_ZONING_LABEL = "//*[@id='cic-sans-more-zoning-policy']/form/ol[1]/li[2]/label"
    ID_SAN_ZONING_POLICY_LABEL = "//*[@id='cic-sans-more-zoning-policy']/form/div/fieldset[2]/ol/li[1]/label"
    ID_SAN_ZONING_POLICY = "//*[@id='cic-sans-zoning-policy-zoning-policy']"
    ID_SAN_ZONE_NAME_FORMAT = "//div[@class='hp-token-text hp-editable hp-active']"
    ID_SAN_ZONE_NAME_FORMAT_LABEL = "css=#cic-sans-edit-san-form > div > fieldset > ol > li:nth-child(4) > label"
    ID_SAN_USE_ALIASES = "//*[@id='cic-sans-zoning-policy-use-aliases']//text()"

# SAN endpoints section
    ID_SAN_DOWNLOAD_ENDPOINTS = "//*[@id='cic-sans-endpoints-download-button']"
    ID_SAN_ENDPOINTS_UPDATE = "//*[@id='cic-sans-endpoints-update']"
    ID_SAN_ENDPOINTS_COUNT = "//*[@id='cic-sans-endpoints-count']"
    ID_SAN_ENDPOINTS_FILTER_ENDPOINT = "//*[@id='cic-sans-endpoints-endpoints-filter-input']"
    ID_SAN_ENDPOINTS_FILTER_WWPN = "//*[@id='cic-sans-endpoints-wwpn-filter]"
    ID_SAN_ENDPOINTS_FILTER_ALIAS = "//*[@id='cic-sans-endpoints-alias-filter-input']"
    ID_SAN_ENDPOINTS_FILTER_ONLINE = "//*[@id='cic-sans-endpoints-table']/tbody/tr[1]/td[4]/div/div/div"
    ID_SAN_ENDPOINTS_FILTER_ZONE = "//*[@id='cic-sans-endpoints-zone-filter-input']"
    ID_SAN_ENDPOINTS_MESSAGE = "//*[@id='cic-sans-endpoints-none']"

# Edit SANs screen
    ID_SAN_EDIT_PAGE_TITLE = "//div[@id='cic-sanmanagers-dynamic-attribute-1']"
    ID_SAN_EDIT_AUTOMATE_ZONING = "xpath=//*[@id='cic-sans-edit-san-form']/div/fieldset/ol/li[1]/label"
    ID_SAN_EDIT_AUTOMATE_ZONING_YES = "xpath=//*[@id='cic-sans-edit-san-automate-zoning-hpToggle']/ol/li[1]"
    ID_SAN_EDIT_AUTOMATE_ZONING_NO = "xpath=//*[@id='cic-sans-edit-san-automate-zoning-hpToggle']/ol/li[2]"
    ID_SAN_EDIT_YES_MESSAGE = "//span[@id='cic-sans-edit-san-enable-zoning-message']"
    ID_SAN_EDIT_NO_MESSAGE = "//span[@id='cic-sans-edit-san-disable-zoning-message']"
    ID_SAN_EDIT_AUTOMATE_ZONING_BTN = "id=cic-sans-edit-san-automate-zoning-hpToggle"

    ID_SAN_ENABLE_ZONING_MESSAGE = "//div[@class='hp-message-container']"
    ID_SAN_EDIT_ZONING_POLICY_LABEL = "xpath=//*[@id='cic-sans-panel-edit-zoningPolicy']/fieldset/ol/li[3]/label"
    ID_SAN_EDIT_ZONING_POLICY_SIAT = "xpath=//*[@id='cic-sans-panel-edit-zoningPolicy']/fieldset/ol/li[3]/div/div/div/ol/li[1]/span"    # /ol/li[1]/span
    ID_SAN_EDIT_ZONING_POLICY_SIST = "xpath=//*[@id='cic-sans-panel-edit-zoningPolicy']/fieldset/ol/li[3]/div/div/div/ol/li[3]/span"
    ID_SAN_EDIT_ZONING_POLICY_SISSS = "xpath=//*[@id='cic-sans-panel-edit-zoningPolicy']/fieldset/ol/li[3]/div/div/div/ol/li[2]/span"
    ID_SAN_EDIT_ZONING_POLICY_SELECT = "xpath=//*[@id='cic-sans-panel-edit-zoningPolicy']/fieldset/ol/li[3]/div/div/div/div"
    ID_SAN_EDIT_ZONE_NAME_LABEL = "//*[@id='cic-sans-panel-edit-zoningPolicy']/div/fieldset/ol/li[4]/label"
    ID_SAN_EDIT_ZONE_NAME = "xpath=//*[@id='cic-sans-edit-san-zone-name-container']/div/div/span[3]"
# ID_SAN_EDIT_ZONE_NAME = "//*[@id='cic-sans-edit-san-zone-name-container']"
    ID_SAN_EDIT_USE_ALIASES = "xpath=//*[@id='cic-sans-panel-edit-zoningPolicy']/div/fieldset/ol/li[5]/label"
    ID_SAN_EDIT_USE_ALIASES_YES = "xpath=//*[@id='cic-sans-edit-san-enable-aliasing-zoning-hpToggle']/ol/li[1]"
    ID_SAN_EDIT_USE_ALIASES_NO = "xpath=//*[@id='cic-sans-edit-san-enable-sliasing-hpToggle']/ol/li[2]"
    ID_SAN_EDIT_INITIATOR_ALIAS_LABEL = "//*[@id='cic-sans-edit-san-form']/div/fieldset/ol/li[4]/label"
    ID_SAN_EDIT_INITIATOR_ALIAS = "//*[@id='cic-sans-edit-san-zone-name-container']/div/div/span[2]"
    ID_SAN_EDIT_TARGET_ALIAS_LABEL = "//*[@id='cic-sans-edit-san-form']/div/fieldset/ol/li[4]/label"
    ID_SAN_EDIT_TARGET_ALIAS = "//*[@id='cic-sans-edit-san-zone-name-container']/div/div/span[2]"
    ID_SAN_EDIT_TARGET_GRP_ALIAS_LABEL = "//*[@id='cic-sans-edit-san-form']/div/fieldset/ol/li[4]/label"
    ID_SAN_EDIT_TARGET_GRP_ALIAS = "//*[@id='cic-sans-edit-san-zone-name-container']/div/div/span[1]"

    ID_SAN_EDIT_OK_BUTTON = "//div[@class='hp-form-controls']/input[@id='cic-sans-edit-san-ok']"
    ID_SAN_EDIT_CANCEL_BUTTON = "//div[@class='hp-form-controls']/input[@id='cic-sans-edit-san-cancel']"
    ID_SAN_EDIT_HELP_LINK = "//*[@id='hp-change-page-container']/section/div/div[2]/a/div"
    ID_SAN_EDIT_ERROR_MESSAGE = "//div[@id='hp-form-message']//span[@class='hp-form-message-text']"

    ID_SAN_DETAILS_TITLE = "xpath=//*[@id='cic-sans-details-title']"
# Edit SAN errors
    ID_SAN_EDIT_ERROR_MESSAGE = "//div[@id='hp-form-message']//span[@class='hp-form-message-text']"
    EDIT_SAN_ERR_MSG = "//*[@id='hp-form-message']//span[text()='Unable to add SAN manager.']"
    EDIT_SAN_ERR_RESOLUTION = "/b[text() = 'Resolution: ']"
    EDIT_SAN_ERR_ERR_FIELD = "//*[@id='hp-form-message']/div[2][text()='One or more fields have an invalid value.']"
    EDIT_SAN_ERR_LINE_DETAILS = "//*[@id='hp-form-message']/div[2][text()[2]='Correct the indicated issues.']"
    EDIT_SAN_REQUIRED_ERR_MSG = "//*[@id='cic-sans-edit-san-form']/div/fieldset']//label[text()='This field is required.']"
# San Screen Filter
    ID_SAN_ALL_STATUSES = "xpath=//*[@id='cic-sans-page']/nav/div[3]/div"
    ID_SAN_STATUSES_CRITICAL = "xpath=//*[@id='cic-sans-page']/nav/div[3]/ol/li[2]"
    ID_SAN_STATUSES_WARNING = "xpath=//*[@id='cic-sans-page']/nav/div[3]/ol/li[3]"
    ID_SAN_STATUSES_OK = "xpath=//*[@id='cic-sans-page']/nav/div[3]/ol/li[4]"
    ID_SAN_STATUSES_UNKNOWN = "xpath=//*[@id='cic-sans-page']/nav/div[3]/ol/li[5]"
    ID_SAN_STATUSES_DISABLED = "xpath=//*[@id='cic-sans-page']/nav/div[3]/ol/li[6]"
    ID_SAN_ALL_STATES = "xpath=//*[@id='cic-sans-page']/nav/div[5]/div"
    ID_SAN_ALL_STATES_DISCOVERED = "xpath=//*[@id='cic-sans-page']/nav/div[5]/ol/li[2]"
    ID_SAN_ALL_STATES_MANAGED = "xpath=//*[@id='cic-sans-page']/nav/div[5]/ol/li[3]"

#  MAP tab
    ID_MAP_TOP_LEVEL = "//*[@id='cic-sans-details-show-view']/div/div/ol/li[1]/ol/li/div[2]"
    ID_MAP_SECOND_LEVEL = "//*[@id='cic-sans-details-show-view']/div/div/ol/li[2]/ol/li/div[2]"
    ID_MAP_THIRD_LEVEL = "//*[@id='cic-sans-details-show-view']/div/div/ol/li[3]/ol/li"

# Edit SAN Zone name format
    ID_SAN_EDIT_ZONE_NAME_FORMAT = "xpath=//*[@id='cic-sans-edit-san-zone-name-container']/div/div"
    ID_SAN_EDIT_INITIATOR_ALIAS = "xpath=//*[@id='cic-sans-edit-san-initiator-alias-container']/div/div"
    ID_SAN_EDIT_TARGET_ALIAS = "xpath=//*[@id='cic-sans-edit-san-target-alias-container']/div/div"
    ID_SAN_EDIT_TARGET_GROUP_ALIAS = "xpath=//*[@id='cic-sans-edit-san-target-group-alias-container']/div/div"
    ID_SAN_EDIT_FORMAT_SERVER_PROFILE = "xpath=.//*[@id='cic-sans-edit-san-zone-name-container']/div/ul/li/span[text()='server profile']"
    ID_SAN_EDIT_FORMAT_WWPN = "xpath=.//*[@id='cic-sans-edit-san-zone-name-container']/div/ul/li/span[text()='server initiator WWPN']"
    ID_SAN_EDIT_ALIASING_YES = "xpath=//*[@id='cic-sans-edit-san-enable-aliasing-hpToggle']/ol/li[1]"
    ID_SAN_EDIT_ALIASING_NO = "xpath=//*[@id='cic-sans-edit-san-enable-aliasing-hpToggle']/ol/li[2]"
