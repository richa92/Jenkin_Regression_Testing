'''
Created on Mar 4, 2014

@author: Administrator
'''


class GeneralStorageSystemElements(object):
    """
        General Elements found on Storage System Page
    """
    ID_DROPDOWN_ACTIONS = "xpath=//label[text()='Actions']"
    ID_PAGE_LABEL = "xpath=//div[@class='hp-page-label']/h1[text()='Storage Systems']"
    ID_TABLE_STORAGE_SYSTEM = "xpath=//table/tbody/tr/td[text()='%s']"  # storage_system
    ID_TABLE_STORAGE_SYSTEMS = "xpath=//table/tbody/tr/td[2]"
    UNABLE_TO_LOCATE_ERROR = "xpath=/html/body/div[2]/div[1]/div/div[3]/div[2]/section[2]/div/h1[text()='%s']"
    ID_TABLE_STORAGE_SYSTEM_SELECTED = "xpath=//table/tbody/tr[contains(@class, 'hp-selected')]/td[text()='%s']"  # storage_system
    ID_STATUS_STORAGE_SYSTEM_OK = "xpath=//table/tbody/tr/td[text()='%s']/../td/div[@class='hp-status hp-status-ok']"  # storage_system
    ID_STATUS_STORAGE_SYSTEM_WARN = "xpath=//table/tbody/tr/td[text()='%s']/../td/div[@class='hp-status hp-status-warning']"  # storage_system
    ID_STATUS_STORAGE_SYSTEM_ERROR = "xpath=//table/tbody/tr/td[text()='%s']/../td/div[@class='hp-status hp-status-error']"  # storage_system

    # ID_STATUS_ADD_NOTIFICATION = "//div[@class='hp-notification']/header[@class='hp-notification-summary']/div"
    ID_STATUS_NOTIFICATION_ONGOING = "//div[@class='hp-notification']/header[@class='hp-notification-summary']/div[@class='hp-status hp-status-unknown']"
    ID_STATUS_NOTIFICATION_OK = "//div[@class='hp-notification']/header[@class='hp-notification-summary']/div[@class='hp-status hp-status-ok']"
    ID_STATUS_NOTIFICATION_WARN = "//div[@class='hp-notification']/header[@class='hp-notification-summary']/div[@class='hp-status hp-status-warning']"
    ID_STATUS_NOTIFICATION_ERROR = "//div[@class='hp-notification']/header[@class='hp-notification-summary']/div[@class='hp-status hp-status-error']"
    ID_TEXT_NOTIFICATION_MESSAGE = "//div[@class='hp-notification']/header[@class='hp-notification-summary']/div/p/span"
    ID_TEXT_NOTIFICATION_RESOLUTION = "//div[@class='hp-notification']/div/div/div[@class='hp-notification-details']/div[@class='hp-resolution-container']"
    ID_RIGHT_SIDEBAR_ACTIVITY = "//*[@id='cic-storagesystems-page']/nav/div[@class='hp-sidebar-control']/div[@class='hp-pin-right']"
    ID_TEXT_ACTIVITY_ACTION_TITLE = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-activity-message']/p/span"  # storagesystem
    ID_TEXT_ACTIVITY_ACTION_OK = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-ok']"  # storagesystem
    ID_TEXT_ACTIVITY_ACTION_WARN = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-warning']"  # storagesystem
    ID_TEXT_ACTIVITY_ACTION_ERROR = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-error']"  # storagesystem
    ID_TEXT_ACTIVITY_ACTION_DETAILS_OK = "//header[@class='hp-active']/a[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-ok']"  # storagesystem
    ID_TEXT_ACTIVITY_SPECIFACTION_OK = "//ol[@id='hp-flyout-activities']/li/div/div[@class='hp-activity-message']/p/span[text()='%s']/../../../div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-ok']"  # actionname, storagesystem
    ID_TEXT_ACTIVITY_SPECIFACTION_WARN = "//ol[@id='hp-flyout-activities']/li/div/div[@class='hp-activity-message']/p/span[text()='%s']/../../../div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-warning']"  # actionname, storagesystem
    ID_TEXT_ACTIVITY_SPECIFACTION_ERROR = "//ol[@id='hp-flyout-activities']/li/div/div[@class='hp-activity-message']/p/span[text()='%s']/../../../div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-error']"  # actionname, storagesystem
    ID_TEXT_ACTIVITY_MESSAGE = "//*[@id='hp-flyout-activities']/li/div[@class='hp-full']/div/div[@class='hp-notification-details']"

    # Overview - General (same with General view)

    # Overview - Utilization
    ID_TEXT_OVERVIEW_UTILIZATION_TOTAL = "id=cic-storagesystems-details-totalCap"
    ID_TEXT_OVERVIEW_UTILIZATION_ALLOCATED = "id=cic-storagesystems-details-allocatedCap"
    ID_TEXT_OVERVIEW_UTILIZATION_FREE = "id=cic-storagesystems-details-freeCap"

    # General
    ID_TEXT_GENERAL_TYPE = "id=cic-storagesystems-details-%s-family"
    ID_TEXT_GENERAL_STATE = "id=cic-storagesystems-details-%s-state"
    ID_TEXT_GENERAL_STATE_STORESERV = "id=cic-storagesystems-details-storeserv-state"
    ID_TEXT_GENERAL_STATE_STOREVIRTUAL = "id=cic-storagesystems-details-storevirtual-state"
    ID_TEXT_GENERAL_STATE_NIMBLE = "id=cic-storagesystems-details-nimble-state"
    ID_TEXT_GENERAL_USER_NAME = "id=cic-storagesystems-details-%s-username"
    ID_TEXT_GENERAL_IP_HOST_NAME = "id=cic-storagesystems-details-storeserv-ip_hostname"
    ID_TEXT_GENERAL_CLUSTER_IP_HOST_NAME = "id=cic-storagesystems-details-storevirtual-hostname"
    ID_TEXT_GENERAL_STORAGE_DOMAIN = "id=cic-storagesystems-details-storeserv-domain"
    ID_TEXT_GENERAL_MODEL = "id=cic-storagesystems-details-storeserv-model"
    ID_TEXT_GENERAL_FIRMWARE = "id=cic-storagesystems-details-storeserv-firmware"
    ID_TEXT_GENERAL_WWN = "id=cic-storagesystems-details-storeserv-wwn"
    ID_TEXT_GENERAL_SERIAL_NUMBER = "id=cic-storagesystems-details-storeserv-serialnumber"
    ID_TEXT_GENERAL_SOFTWARE_VERSION = "id=cic-storagesystems-details-storevirtual-softwareVersion"
    ID_TEXT_GENERAL_CLUSTER_NAME = "id=cic-storagesystems-details-storevirtual-name"
    ID_TEXT_GENERAL_LUN_MODE = "id=cic-storagesystems-details-storevirtual-lunMode"
    ID_TEXT_GENERAL_USED_BY_STORAGE_POOLS = "xpath=//span[@id='cic-storagesystems-details-storage-pools']|//span[@id='cic-storagesystems-details-storage-pools']/a"
    ID_TEXT_GENERAL_USED_BY_STORAGE_VOLUMES = "xpath=//span[@id='cic-storagesystems-details-volumes']|//span[@id='cic-storagesystems-details-volumes']/a"
    ID_TEXT_GENERAL_ENCRYPTION = "xpath=//*[@id='cic-storagesystems-details-nimble-encryption']"
    ID_TEXT_GENERAL_MGMT_HOST_NAME = "xpath=//*[@id='cic-storagesystems-details-nimble-hostname']"
    ID_TEXT_GENERAL_NIMBLE_SOFTWARE_VERSION = "xpath=//*[@id='cic-storagesystems-details-nimble-softwareVersion']"

    ID_TEXT_GENERAL_NIMBLE_LUN_MODE = "xpath=//*[@id='cic-storagesystems-details-nimble-lunMode']"
    ID_TEXT_GENERAL_NIMBLE_STORAGE_POOLS = "xpath=//*[@id='cic-storagesystems-details-storage_pools']/a"
    ID_TEXT_GENERAL_NIMBLE_VOLUMES = "xpath=//*[@id='cic-storagesystems-details-volumes']/a"
    ID_TEXT_GENERAL_NIMBLE_VOLUMESETS = "//*[@id='cic-storagesystems-details-volumesets']"
    ID_TEXT_GENERAL_ARRAY_TYPE = "xpath=//*[@id='cic-storagesystems-details-nimble-arrayType']"

    ID_LINK_STORAGE_POOLS = "xpath=//*[@id='cic-storagesystems-details-storage_pools']/a"
    ID_LINK_VOLUME_SETS = "xpath=//*[@id='cic-storagesystems-details-volumesets']/a"
    ID_LINK_STORAGE_VOLUMES = "xpath=//*[@id='cic-storagesystems-details-volumes']/a"
    ID_LINK_SANS = "xpath=//*[@id='cic-storagesystems-show-arrayports-table-storeserv']/tbody/tr[5]/td[6]/a"
    ID_LINK_NETWORKS = "xpath=//*[@id='cic-storagesystems-show-arrayports-table-storevirtual']/tbody/tr/td[3]/a"

    # Utilization
    ID_TEXT_UTILIZATION_TOTAL = "id=cic-storagesystems-details-totalCap"
    ID_TEXT_UTILIZATION_ALLOCATED = "id=cic-storagesystems-details-allocatedCap"
    ID_TEXT_UTILIZATION_FREE = "id=cic-storagesystems-details-freeCap"

    # Storage pools
    ID_TEXT_STORAGE_POOLS_ROW_NAME = "xpath=//table[@id='cic-storagesystems-show-arraypools-table']//td[.='%s']"
    ID_TEXT_STORAGE_POOLS_ROW_STATE = "xpath=//table[@id='cic-storagesystems-show-arraypools-table']//td[.='%s']/../td[1]/div/span"
    ID_TEXT_STORAGE_POOLS_ROW_ALLOCATED_CAPACITY = "xpath=//table[@id='cic-storagesystems-show-arraypools-table']//td[.='%s']/../td[3]"
    ID_TEXT_STORAGE_POOLS_ROW_TOTAL_CAPACITY = "xpath=//table[@id='cic-storagesystems-show-arraypools-table']//td[.='%s']/../td[4]"

    # Storage System Ports
    ID_TEXT_STORAGE_SYSTEM_PORTS_ROW_PORT = "xpath=//table[@id='cic-storagesystems-show-arrayports-table']//td[.='%s']"
    ID_TEXT_STORAGE_SYSTEM_PORTS_ROW_STATE = "xpath=//table[@id='cic-storagesystems-show-arrayports-table']//td[.='%s']/../td[2]/div/span"
    ID_TEXT_STORAGE_SYSTEM_PORTS_ROW_LABEL = "xpath=//table[@id='cic-storagesystems-show-arrayports-table']//td[.='%s']/../td[4]/*"
    ID_TEXT_STORAGE_SYSTEM_PORTS_ROW_PROTOCOL = "xpath=//table[@id='cic-storagesystems-show-arrayports-table']//td[.='%s']/../td[5]"
    ID_TEXT_STORAGE_SYSTEM_PORTS_ROW_EXPECTED_SAN_OR_NETWORK = "xpath=//table[@id='cic-storagesystems-show-arrayports-table']//td[.='%s']/../td[6]"
    ID_TEXT_STORAGE_SYSTEM_PORTS_ROW_ACTUAL_SAN = "xpath=//table[@id='cic-storagesystems-show-arrayports-table']//td[.='%s']/../td[7]/span|//table[@id='cic-storagesystems-show-arrayports-table']//td[.='%s']/../td[7]/a"
    ID_TEXT_STORAGE_SYSTEM_PORTS_ROW_PORT_GROUP = "xpath=//table[@id='cic-storagesystems-show-arrayports-table']//td[.='%s']/../td[8]"
    ID_BTN_STORAGE_SYSTEM_PORTS_FOLDING_PORT = "xpath=//table[@id='cic-storagesystems-show-arrayports-table']//td[.='%s']/../td[1]/div"
    # -- extra ports configuration (WWN etc.)
    ID_PANEL_STORAGE_SYSTEM_PORTS_ROW_DETAIL = "xpath=//table[@id='cic-storagesystems-show-arrayports-table']//td[.='%s']/../following-sibling::tr[1][@class='hp-row-details-row']"
    ID_TEXT_STORAGE_SYSTEM_PORTS_WWPN = "xpath=//table[@id='cic-storagesystems-show-arrayports-table']//td[.='%s']/../following-sibling::tr[1]//label[.='WWPN']/../div"
    ID_TEXT_STORAGE_SYSTEM_PORTS_PARTNER_PORT = "xpath=//table[@id='cic-storagesystems-show-arrayports-table']//td[.='%s']/../following-sibling::tr[1]//label[.='Partner port']/../div"
    ID_TEXT_STORAGE_SYSTEM_PORTS_FAILOVER_STATE = "xpath=//table[@id='cic-storagesystems-show-arrayports-table']//td[.='%s']/../following-sibling::tr[1]//label[.='Failover state']/../div"


class AddStorageSystemElements(object):
    """
        Elements found on Add Storage System Page
    """
    ID_BUTTON_ADD_STORAGE_SYSTEM = "link=Add storage system"
    ID_SELECT_ACTION_ADD = "id=cic-storagesystems-add-action"
    ID_DIALOG_ADD_STORAGE_SYSTEM = "id=hp-change-page-container"
    ID_SELECT_STORAGE_SYSTEM_TYPE = "id=cic-storagesystems-add-family"
    ID_INPUT_IP_ADDRESS_OR_HOST_NAME = "//input[@id='cic-storagesystems-add-host-txt-storeServ']"
    ID_INPUT_IP_ADDRESS_OR_HOST_NAME_VIRTUAL = "//input[@id='cic-storagesystems-add-host-txt-storeVirtual']"
    ID_INPUT_IP_ADDRESS_OR_HOST_NAME_NSA = "//input[@id='cic-storagesystems-add-host-txt-nimble']"
    ID_INPUT_USER_NAME = "id=cic-storagesystems-username-storeServ"
    ID_INPUT_USER_NAME_VIRTUAL = "id=cic-storagesystems-username-storeVirtual"
    ID_INPUT_USER_NAME_NSA = "id=cic-storagesystems-username-nimble"
    ID_INPUT_PASSWORD = "id=cic-storagesystems-password-storeServ"
    ID_INPUT_PASSWORD_VIRTUAL = "id=cic-storagesystems-password-storeVirtual"
    ID_INPUT_PASSWORD_NSA = "id=cic-storagesystems-password-nimble"
    ID_BUTTON_CONNECT = "id=cic-storagesystems-connect"
    ID_TEXT_CONNECTED_STORAGE = "xpath=//div/span[text()='Connected to storage system.']"
    ID_DROPDOWN_PANEL_SELECTOR = "xpath=//*[@id='cic-storagesystems-panel-add-selector']/div"
    ID_SELECT_PANEL_CREDENTIALS = "xpath=//*[@id='cic-storagesystems-panel-add-selector']/ol/li/a[text()='Credentials']"
    ID_SELECT_PANEL_GENERAL = "xpath=//*[@id='cic-storagesystems-panel-add-selector']/ol/li/a[text()='General']"
    ID_SELECT_PANEL_STORAGE_POOLS = "xpath=//*[@id='cic-storagesystems-panel-add-selector']/ol/li/a[text()='Storage Pools']"
    ID_SELECT_PANEL_STORAGE_SYSTEM_PORTS = "xpath=//*[@id='cic-storagesystems-panel-add-selector']/ol/li/a[text()='Storage System Ports']"
    ID_TEXT_STORAGE_SHORT_NAME = "xptah=//*[@id='cic-storagesystems-details-arrayname' and text()='%s']"  # storage short name
    ID_INPUT_STORAGE_DOMAIN = "id=cic-storagesystems-add-domain-input"
    ID_SELECT_STORAGE_DOMAIN = "xpath=//div[@class='hp-search-combo-menu']/ol/li/span[text()='%s']"  # storage domain name
    ID_CHECKBOX_MANAGE_STORAGE_POOL = "//*[@id='cic-storagesystems-add-pools-assigned-storeServ']/tbody/tr/td[text()='%s']/following-sibling::td/input[@type='checkbox']"  # pool name for all but nimble
    ID_CHECKBOX_SELECT_STORAGE_POOL = "//*[@id='cic-storagesystems-add-pools-assigned-nimble']/tbody/tr/td[text()='%s']/following-sibling::td/input[@type='checkbox']"  # pool name for nimble
    ID_BUTTON_ADD_STORAGE_POOLS = "id=cic-storagesystems-add-addpools"
    ID_DIALOG_ADD_STORAGE_POOLS = "xpath=//div[@class='hp-dialog']/header/h1[text()='Add storage pools']"
    ID_INPUT_STORAGE_POOL = "xpath=//div[@class='hp-dialog']/form/div/fieldset/ol/li/div/div/div/input"
    ID_SELECT_STORAGE_POOL = "xpath=//div/table/tbody/tr/td[text()='%s']"  # storage pool name
    ID_BUTTON_STORAGE_POOL_SELECT_ALL = "xpath=//input[@id='cic-storagesystems-add-selectPools']"
    ID_BUTTON_STORAGE_POOL_DESELECT_ALL = "xpath=//input[@id='cic-storagesystems-add-deselectPools']"
    ID_BUTTON_STORAGE_POOL_ADD = "xpath=//button[@class='hp-add hp-primary' and text()='Add']"
    ID_BUTTON_STORAGE_POOL_ADD_PLUS = "xpath=//button[@class='hp-add-again' and text()='Add +']"
    ID_BUTTON_STORAGE_POOL_CANCEL = "xpath=//button[@class='hp-cancel' and text()='Cancel']"
    ID_TEXT_STORAGE_POOL = "xpath=//table[@id='cic-storagesystems-add-pools-assigned']/tbody/tr/td[text()='%s']"  # storage pool name
    ID_TABLE_STORAGE_SYSTEM_PORTS = "xpath=//table[@id='cic-storagesystems-add-ports-assigned']"
    ID_CLOSE_EXPECTED_SAN_OR_NETWORK = "xpath=//table[@id='cic-storagesystems-add-ports-assigned-storeServ']/tbody/tr/td[contains(@class, 'sorting_1') and text()='%s']/../td//select[contains(@id, 'cic-storagesystems-add-ports-san-chooser')]/following-sibling::div[@class='hp-search-combo-close']/div"
    ID_INPUT_EXPECTED_SAN_OR_NETWORK = "xpath=//table[@id='cic-storagesystems-add-ports-assigned-storeServ']/tbody/tr/td[contains(@class, 'sorting_1') and text()='%s']/../td/div[@class='hp-search-combo hp-active']/input[contains(@id, 'cic-storagesystems-add-ports-san-chooser')]"
    ID_SELECT_EXPECTED_SAN_OR_NETWORK = "xpath=//table[@id='cic-storagesystems-add-ports-assigned-storeServ']/tbody/tr/td[contains(@class, 'sorting_1') and text()='%s']/following-sibling::td/div/div[@class='hp-search-combo-spacer']/div[@class='hp-search-combo-menu']/ol[@class='hp-search-combo-scroller hp-options']/li[span[contains(text(), '%s')]]"
    ID_TEXT_ACTUAL_SAN = "xpath=//table[@id='cic-storagesystems-add-ports-assigned']/tbody/tr/td[contains(@class, 'sorting_1') and text()='%s']/../td[5]/a[text()='%s']"  # port_id, san
    ID_CLOSE_PORT_GROUP = "xpath=//table[@id='cic-storagesystems-add-ports-assigned-storeServ']/tbody/tr/td[contains(@class, 'sorting_1') and text()='%s']/../td//input[contains(@id, 'cic-storagesystems-add-ports-port-group-chooser')]/following-sibling::div[@class='hp-search-combo-close']/div"
    ID_INPUT_PORT_GROUP = "xpath=//table[@id='cic-storagesystems-add-ports-assigned-storeServ']/tbody/tr/td[contains(@class, 'sorting_1') and text()='%s']/../td//input[2][contains(@id, 'cic-storagesystems-add-ports-port-group-chooser')]"
    ID_SELECT_PORT_GROUP = "xpath=//table[@id='cic-storagesystems-add-ports-assigned-storeServ']/tbody/tr/td[contains(@class, 'sorting_1') and text()='%s']/../td//input[contains(@id, 'cic-storagesystems-add-ports-port-group-chooser')]/following-sibling::div[@class='hp-search-combo-spacer']/div/ol[@class='hp-search-combo-scroller hp-options']/li/span[text()='%s']"
    ID_INPUT_VIPNETWORK = "xpath=//input[@id='cic-storagesystems-add-ports-network-chooser-id0-input' and @class='hp-search-combo-input']"
    ID_OPTION_VIPNETWORK = "xpath=//input[@id='cic-storagesystems-add-ports-network-chooser-id0-input']//..//div[@class='hp-search-combo-menu']//..//li[span[text()='%s']]"  # vipnetwork
    ID_BUTTON_ADD = "id=cic-storagesystems-add"
    ID_BUTTON_ADD_PLUS = "id=cic-storagesystems-add-plus"
    ID_BUTTON_CANCEL = "id=cic-storagesystems-add-cancel"
    ID_TEXT_ADDING_STORAGE_SYSTEM = "xpath=//*[@id='hp-form-message']/div[1]/span[contains(.,'Adding storage system')]"
    ID_TEXT_ADD_ERROR_MESSAGE = "xpath=//*[@id='cic-storagesystems-add-form']/div/div[1]/div/div[2]/div[1]/span"


class EditStorageSystemElements(object):
    """
        Elements found on Edit Storage System Page
    """
    ID_SELECT_ACTION_EDIT = "id=cic-storagesystems-edit-action"
    ID_DIALOG_EDIT = "id=cic-storagesystems-edit-dialog"
    ID_INPUT_EXPECTED_SAN_OR_NETWORK = "xpath=//*[@id='cic-storagesystems-edit-ports-san-chooser-id1-input']"
    ID_SELECT_EXPECTED_SAN_OR_NETWORK = "xpath=//*[@id='cic-storagesystems-edit-ports-storeserv']/tbody/tr[2]/td[4]/div/div[2]/div[@class='hp-search-combo-control']"
    ID_INPUT_PORT_GROUP = "xpath=//*[@id='cic-storagesystems-edit-ports-port-group-chooser-id1-input']"  # port_id
    ID_INPUT_VIPNETWORK = "xpath=//input[@id='cic-storagesystems-edit-ports-network-chooser-id0-input' and @class='hp-search-combo-input']"
    ID_OPTION_VIPNETWORK = "xpath=//input[@id='cic-storagesystems-edit-ports-network-chooser-id0-input']//..//div[@class='hp-search-combo-menu']//..//li[span[text()='%s']]"  # vipnetwork
    ID_BUTTON_OK = "id=cic-storagesystems-edit"
    ID_BUTTON_CANCEL = "id=cic-storagesystems-edit-cancel"
    ID_TEXT_EDIT_ERROR_MESSAGE = "xpath=//*[@id='cic-storagesystems-edit-form']/div[2]/div[1]/div/div[2]/div[1]/span"


class RemoveStorageSystemElements(object):
    """
        Elements found on Remove Storage System Page
    """
    ID_SELECT_ACTION_REMOVE = "link=Remove"
    ID_DIALOG_REMOVE = "id=cic-storagesystems-remove-confirm-header"
    ID_BUTTON_YES_REMOVE = "xpath=//button[text()='Yes, Remove']"
    ID_BUTTON_CANCEL = "xpath=//button[text()='Cancel']"
    ID_TABLE_STORAGE_SYSTEM_DELETED = "//table/tbody/tr[contains(@class, 'hp-not-found')]/td[text()='%s']"  # storage system


class RefreshStorageSystemElements(object):
    """
        Elements found on Refresh Storage System Page
    """
    ID_SELECT_ACTION_REFRESH = "id=cic-storagesystems-refresh-action"
    ID_TEST_REFRESH_ONGOING = "xpath=//*[@id='cic-storagesystems-details-state' and text()='Refreshing']"
    ID_TEXT_REFRESH_COMPLETED = "xpath=//*[@id='cic-storagesystems-details-state' and text()='Configured']"


class EditStorageSystemCredentialsElements(object):
    """
        Elements found on Edit Storage System Credentials Page
    """
    ID_SELECT_ACTION_EDIT_CREDENTIALS = "id=cic-storagesystems-editcredentials-action"
    ID_DIALOG_EDIT_CREDENTIALS = "id=cic-storagesystems-editcredentials-title"
    ID_INPUT_IP_HOSTNAME = "id=cic-storagesystems-editcredentials-hostname"
    ID_INPUT_USERNAME = "id=cic-storagesystems-editcredentials-username"
    ID_INPUT_PASSWORD = "id=cic-storagesystems-editcredentials-password"
    ID_BUTTON_OK = "id=cic-storagesystems-editcredentials-ok"
    ID_BUTTON_CANCEL = "id=cic-storagesystems-editcredentials-cancel"
