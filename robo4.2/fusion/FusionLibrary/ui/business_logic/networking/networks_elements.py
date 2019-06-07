# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
'''

This File contains all element ID on Fusion Networks page/screen
'''


class GeneralNetworksElements(object):
    """
        Elements on the Network Page
    """
    ID_PAGE_LABEL = "xpath=//div[@class='hp-page-label']/h1[text()='Networks']"
    ID_NETWORK_TITLE = "xpath=//div[@class='hp-page-label']/h1"
    ID_TABLE_MASTER = "id=cic-network-master-table"
    ID_TABLE_NETWORKS = "xpath=//table[@id='cic-network-master-table']/tbody//tr/td[2]"
    ID_TABLE_NETWORK = "xpath=//table[@id='cic-network-master-table']/tbody//tr/td[text()='%s']"  # network_name
    UNABLE_TO_LOCATE_ERROR = "xpath=/html/body/div[2]/div[1]/div/div[3]/div[2]/section[2]/div/h1[text()='%s']"
    ID_STATUS_NETWORK_OK = "xpath=//table[@id='cic-network-master-table']/tbody//tr/td[text()='%s']/../td/div[@class='hp-status hp-status-ok']"  # network_name
    ID_STATUS_NETWORK_WARN = "xpath=//table[@id='cic-network-master-table']/tbody//tr/td[text()='%s']/../td/div[@class='hp-status hp-status-warning']"  # network_name
    ID_STATUS_NETWORK_ERROR = "xpath=//table[@id='cic-network-master-table']/tbody//tr/td[text()='%s']/../td/div[@class='hp-status hp-status-error']"  # network_name
    ID_TABLE_NETWORK_SELECTED = "//table[@id='cic-network-master-table']/tbody//tr[contains(@class, 'hp-selected')]/td[text()='%s']"  # network_name
    ID_TABLE_NETWORK_DELETED = "//table[@id='cic-network-master-table']/tbody//tr[contains(@class, 'hp-not-found')]/td[text()='%s']"  # network_name
    ID_DROPDOWN_ACTIONS = "xpath=//label[text()='Actions']"
    ID_NETWORK_COUNT = "xpath=.//span[@class='hp-page-item-count']"
    ID_TEXT_NETWORK_STATUS_TITLE = "id=cic-network-details-title"
    ID_TEXT_NETWORK_STATUS = "id=cic-network-details-status"  # ok: class="crm-network-data hp-status hp-status-ok" error:
    ID_DROPDOWN_PANEL_SELECTOR = "//*[@id='cic-network-panel-selector']/div"
    ID_SELECT_OVERVIEW_PANEL = "//*[@id='cic-network-panel-selector']/ol/li/a[text()='Overview']"
    ID_SELECT_ACTIVITY_PANEL = "//*[@id='cic-network-panel-selector']/ol/li/a[text()='Activity']"
    ID_SELECT_MAP_PANEL = "//*[@id='cic-network-panel-selector']/ol/li/a[text()='Map']"
    ID_SELECT_LABELS_PANEL = "//*[@id='cic-network-panel-selector']/ol/li/a[text()='Labels']"
    ID_BULK_ENET_ASSIGN_ACTVITY = "xpath=.//*[@id='hp-activities']/tbody/tr[position()=1]//*[contains(text(),'Completed')]"

    ID_RIGHT_SIDEBAR_ACTIVITY = "xpath=//*[@id='cic-network-page']/nav/div[@class='hp-sidebar-control']/div[@class='hp-pin-right']"
    ID_TEXT_ACTIVITY_ACTION_TITLE = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-activity-message']/p/span"  # network_name
    ID_TEXT_ACTIVITY_ACTION_OK = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-ok']"  # network_name
    ID_TEXT_ACTIVITY_ACTION_WARN = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-warning']"  # network_name
    ID_TEXT_ACTIVITY_ACTION_ERROR = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-error']"  # network_name
    ID_TEXT_ACTIVITY_ACTION_DETAILS_OK = "//header[@class='hp-active']/a[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-ok']"  # network_name
    ID_TEXT_ACTIVITY_SPECIFACTION_OK = "//ol[@id='hp-flyout-activities']/li/div/div[@class='hp-activity-message']/p/span[text()='%s']/../../../div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-ok']"  # actionname, network_name
    ID_TEXT_ACTIVITY_SPECIFACTION_WARN = "//ol[@id='hp-flyout-activities']/li/div/div[@class='hp-activity-message']/p/span[text()='%s']/../../../div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-warning']"  # actionname, network_name
    ID_TEXT_ACTIVITY_SPECIFACTION_ERROR = "//ol[@id='hp-flyout-activities']/li/div/div[@class='hp-activity-message']/p/span[text()='%s']/../../../div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-error']"  # actionname, network_name
    ID_TEXT_ACTIVITY_MESSAGE = "//*[@id='hp-flyout-activities']/li/div[@class='hp-full']/div/div[@class='hp-notification-details']"

    ID_TEXT_GENERAL_TYPE = "id=cic-network-show-type"
    ID_TEXT_GENERAL_VLAN = "id=cic-network-vlan-id"
    ID_TEXT_GENERAL_ASSOCIATE_WITH_SAN = "//*[@id='cic-network-san-associate']/span"
    ID_TEXT_GENERAL_SAN_MANAGER = ""
    ID_TEXT_GENERAL_PURPOSE = "id=cic-network-show-purpose"
    ID_TEXT_GENERAL_PREFERRED_BANDWIDTH = "id=cic-network-pref-bandwidth"
    ID_TEXT_GENERAL_MAXIMUM_BANDWIDTH = "id=cic-network-max-bandwidth"
    ID_TEXT_GENERAL_SMART_LINK = "id=cic-network-smart-link"
    ID_TEXT_GENERAL_PRIVATE_NETWORK = "id=cic-network-private-network"
    ID_TEXT_GENERAL_UPLINK_SET = "xpath=//*[@id='cic-network-show-uplinkportgroup']/span"
    ID_TEXT_GENERAL_LOGIN_REDISTRIBUTION = "id=cic-network-show-auto-login-redistribution"
    ID_TEXT_GENERAL_USED_BY_SERVER_PROFILES = "xpath=//*[@id='cic-network-show-used-by']/a"
    ID_TEXT_GENERAL_USED_BY_STORAGE_SYSTEMS = "xpath=//*[@id='cic-network-pools-show-used-by-storagesystems']/span"
    ID_TEXT_GENERAL_MEMBER_OF = "xpath=//*[@id='cic-network-show-member-of']/span"
    ID_TEXT_GENERAL_LINK_STABILITY_INTERVAL = "id=cic-network-show-link-stability-time"

    ID_TEXT_GENERAL_SUBNETID = "id=cic-network-subnet"
    ID_EDIT_NETWORKS_FORM = "id=cic-network-edit-form"


class CreateNetworksElements(object):
    """
        Elements on the Create Network Page
    """
    ID_BUTTON_CREATE_NETWORK = "link=Create network"
    ID_SELECT_ACTION_CREATE = "id=cic-network-create-action"
    ID_DIALOG_CREATE_NETWORK = "xpath=//section[@class='hp-details-add-section']"
    ID_DIALOG_CREATE_NETWORK_MESSAGE = "xpath=//span[@class='hp-form-message-text']"
    ID_DIALOG_CREATE_NETWORK_FORM_MESSAGE = "hp-form-changes"

    ID_INPUT_NAME = "id=cic-network-name"
    ID_RADIO_ETHERNET_TYPE = "id=cic-network-add-ethernet-type"
    ID_RADIO_FIBRE_CHANNEL_TYPE = "id=cic-network-add-fc-type"
    ID_RADIO_FCOE_TYPE = "id=cic-network-add-fcoe-type"

    ID_DROPDOWN_VLAN = "xpath=//div[@id='cic-network-data-section']/li/label[text()='VLAN']/..//div[@class='hp-select']"
    ID_SELECT_VLAN = "xpath=//div[@id='cic-network-data-section']/li/label[text()='VLAN']/..//div[@class='hp-select hp-active']/ol/li[span[text()='%s']]"  # %Tagged, Untagged, Tunnel

    ID_INPUT_NETWORK_VLAND_ID = "id=cic-network-vlan-id"
    ID_DROPDOWN_PURPOSE = "//div[@id='cic-network-data-section']/li/label[text()='Purpose']/../div/div/div/div"
    ID_SELECT_PURPOSE = "//div[@id='cic-network-data-section']/li/label[text()='Purpose']/../div/div/div/ol/li/span[text()='%s']"  # %General, Management, VM Migration, Fault Tolerance
    ID_INPUT_PREFERRED_BANDWIDTH = "id=cic-network-pref-bandwidth"
    ID_INPUT_MAXIMUM_BANDWIDTH = "id=cic-network-max-bandwidth"
    ID_CHECKBOX_SMART_LINK = "id=cic-network-smart-link"
    ID_CHECKBOX_PRIVATE_NETWORK = "id=cic-network-private-network"

    ID_DROPDOWN_FABRIC_TYPE = "xpath=//div[@id='cic-network-data-section']//label[text()='Fabric type']/following-sibling::div//div[contains(@class, 'select')]/div[contains(@class, 'value')]"
    ID_SELECT_FABRIC_TYPE = "xpath=//li[.='%s']"  # %Fabric attach, Direct attach
    ID_INPUT_ASSOCIATE_WITH_SAN = "id=cic-network-add-san-select-input"
    # ID_SELECT_ASSOCIATE_WITH_SAN = "xpath=.//*[@id='cic-network-add-san-section']//table/tbody/tr/td[text()='%s']"  # %wpstsan14.vse.rdlabs.hpecorp.net-10:00:00:27:f8:fe:0c:54
    ID_SELECT_ASSOCIATE_WITH_SAN = "xpath=//*[@id='cic-network-add-san-section']//table/tbody/tr/td[contains(text(), '%s')]"  # %wpstsan14.vse.rdlabs.hpecorp.net-10:00:00:27:f8:fe:0c:54
    ID_TOGGLE_LOGIN_REDISTRIBUTION_AUTO_VISIBLE = "xpath=//*[@id='cic-network-add-auto-login-redistribution-hpToggle' and @class='hp-toggle hp-checked']"
    ID_TOGGLE_LOGIN_REDISTRIBUTION_AUTO = "xpath=//*[@id='cic-network-add-auto-login-redistribution-hpToggle']/ol/li[text()='Auto']"
    ID_TOGGLE_LOGIN_REDISTRIBUTION_MANUAL = "xpath=//*[@id='cic-network-add-auto-login-redistribution-hpToggle']/ol/li[text()='Manual']"
    ID_INPUT_LINK_STABILITY_INTERVAL = "id=cic-network-add-link-stability-time"
    ID_BUTTON_CREATE = "id=cic-network-add"
    ID_BUTTON_CREATE_PLUS = "id=cic-network-add-again"
    ID_BUTTON_CANCEL = "id=cic-network-add-close"
    ID_TEXT_VERIFYING_PARAMETERS = "xpath=//*[@id='hp-form-message']/div[1]/span[contains(.,'Verifying parameters')]"

    ID_INPUT_SUBNETID = "xpath=//input[@id='cic-network-add-subnet-select-input' and @class='hp-search-combo-input']"
    ID_OPTION_SUBNETID = "xpath=//input[@id='cic-network-add-subnet-select-input']/..//div[@class='hp-search-combo-menu']/..//tr[td[text()='%s']]"


class EditNetworksElements(object):
    """
        Elements on the Edit Network Page
    """
    ID_SELECT_ACTION_EDIT = "id=cic-network-edit-action"
    ID_DIALOG_EDIT_NETWORK = "id=cic-network-edit-form"
    ID_INPUT_NAME = "id=cic-network-name"
    ID_TEXT_TYPE = "id=cic-network-edit-type"
    ID_INPUT_PREFERRED_BANDWIDTH = "id=cic-network-pref-bandwidth"
    ID_INPUT_MAXIMUM_BANDWIDTH = "id=cic-network-max-bandwidth"

    ID_DROPDOWN_PURPOSE = "xpath=//*[@id='cic-network-edit-form']//label[text()='Purpose']/..//div[@class='hp-select']"
    ID_SELECT_PURPOSE = "xpath=//*[@id='cic-network-edit-form']//label[text()='Purpose']/../div//ol/li/span[text()='%s']"

    ID_CHECKBOX_SMART_LINK = "id=cic-network-edit-smart-link"
    ID_CHECKBOX_PRIVATE_NETWORK = "id=cic-network-edit-private-network"
    ID_INPUT_ASSOCIATE_WITH_SAN = "id=cic-network-edit-san-select-input"
    ID_SELECT_ASSOCIATE_WITH_SAN = "//*[@id='cic-network-edit-san-section']/div/div/div/ol/li/span[text()='%s']"  # wpstsan14.vse.rdlabs.hpecorp.net-10:00:00:27:f8:fe:0c:55 remember to test, sometimes a pop window appear if input firstly
    ID_TOGGLE_LOGIN_REDISTRIBUTION_AUTO_VISIBLE = "xpath=//*[@id='cic-network-edit-auto-login-redistribution-hpToggle' and @class='hp-toggle hp-checked']"
    ID_TOGGLE_LOGIN_REDISTRIBUTION_AUTO = "xpath=//*[@id='cic-network-edit-auto-login-redistribution-hpToggle']/ol/li[text()='Auto']"
    ID_TOGGLE_LOGIN_REDISTRIBUTION_MANUAL = "xpath=//*[@id='cic-network-edit-auto-login-redistribution-hpToggle']/ol/li[text()='Manual']"
    ID_INPUT_LINK_STABILITY_INTERVAL = "id=cic-network-edit-link-stability-time"
    ID_BUTTON_OK = "id=cic-network-update"
    ID_BUTTON_CANCEL = "id=cic-network-edit-cancel"

    ID_INPUT_EDIT_SUBNETID = "xpath=//input[@id='cic-network-edit-subnet-select-input' and @class='hp-search-combo-input']"
    ID_OPTION_EDIT_SUBNETID = "xpath=//input[@id='cic-network-edit-subnet-select-input']/..//div[@class='hp-search-combo-menu']/..//tr[td[text()='%s']]"
    ID_TEXT_ACTION_NO_AUTHORIZATION = "xpath=//*[@id='cic-network-actions']/div//ol[@id='hp-unauthorized-message']/li"


class DeleteNetworksElements(object):
    """
        Elements on the Delete Network Page
    """
    ID_SELECT_ACTION_DELETE = "cic-network-delete-action"
    ID_DIALOG_DELETE = "xpath=//div[@id='cic-delete-dialog-prompt']"
    ID_BUTTON_YES_DELETE = "id=cic-delete-dialog-yes"
    ID_BUTTON_CANCEL = "xpath=//button[text()='Cancel']"


class EditScopeElements(object):
    """
        Elements on the Scope Page related to networks
    """
    ID_HEADER_SCOPE = "//li[@id='hp-scopes-resource-show-panel']/label/span[text()='Scopes']"
    ID_TEXT_SCOPE_NOT_LOAD = "//li[@id='hp-scopes-resource-show-panel']/div[@class='hp-unavailable']"
    ID_BUTTON_EDIT = "//li[@id='hp-scopes-resource-show-panel']/label/a[.='Edit']"
    ID_DIALOG_EDIT = "//header[@id='hp-scopes-edit-header']"
    ID_DIALOG_ASSIGN = "//*[@class='hp-ellipsised']//span[contains(text(),'Assign to Scopes')]"
    ID_BUTTON_OK = "id=hp-scopes-edit-ok"
    ID_BUTTON_CANCEL = "id=hp-scopes-edit-cancel"
    ID_BUTTON_CLOSE = "id=hp-scopes-edit-close"
    ID_BUTTON_ASSIGN = "hp-scopes-edit-add"
    ID_BUTTON_ADD = "xpath=//button[text()='Add']"
    ID_BUTTON_ADD_PLUS = "xpath=//button[text()='Add +']"
    ID_BUTTON_CANCEL_ASSIGN = "xpath=//button[text()='Cancel']"
    ID_INPUT_SEARCH_TEXT = "//input[@class='hp-search']"
    ID_TABLE_SCOPE_NAME = "//form[@class='hp-edit-form']//table/tbody/tr/td[text()='%s']"
    ID_TABLE_REMOVE_SCOPE = "//form[@class='hp-edit-form']//table/tbody/tr[td[text()='%s']]//div"
