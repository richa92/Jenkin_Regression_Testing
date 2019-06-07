# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
'''

Server profile page objects
'''
from FusionLibrary.ui.business_logic.base import FusionUIConst


class GeneralServerProfilesElements(object):
    ID_DIALOG_DETAILS_TITLE = "xpath=//span[@data-localize='profiles.add.title']|//span[@data-localize='profiles.edit.title']|//span[@data-localize='profiles.copy.action']|//span[@data-localize='profiles.delete.title']"  # 'Create Server Profile / Edit / Copy / Delete', to get the action type - CREATE / EDIT / COPY / DELETE
    ID_TABLE_SERVER_PROFILE = "xpath=//table[@class='hp-master-table hp-selectable dataTable']/tbody/tr/td[translate(text(),'" + FusionUIConst.CONST_ZERO_WIDTH_SPACE + "','')='%s']"  # server profile name
    ID_TABLE_SERVER_PROFILE_LIST = "xpath=//table[@class='hp-master-table hp-selectable dataTable']/tbody/tr/td[2]"
    ID_DROPDOWN_PANEL_SELECTOR = "id=cic-server-panel-selector"
    ID_ICON_PROFILE_TASK_RUNNING = "//div[@class='hp-status-changing']"
    ID_SELECT_OVERVIEW_PANEL = "xpath=//ol[@class='hp-options']//a[.='Overview']"
    ID_SELECT_GENERAL_PANEL = "xpath=//ol[@class='hp-options']//a[.='General']"
    ID_SELECT_FIRMWARE_PANEL = "xpath=//ol[@class='hp-options']//a[.='Firmware']"
    ID_SELECT_CONNECTIONS_PANEL = "xpath=//ol[@class='hp-options']//a[.='Connections']"
    ID_SELECT_LOCAL_STORAGE_PANEL = "xpath=//ol[@class='hp-options']//a[.='Local Storage']"
    ID_SELECT_SAN_STORAGE_PANEL = "xpath=//ol[@class='hp-options']//a[.='SAN Storage']"
    ID_SELECT_BOOT_SETTINGS_PANEL = "xpath=//ol[@class='hp-options']//a[.='Boot Settings']"
    ID_SELECT_BIOS_SETTINGS_PANEL = "xpath=//ol[@class='hp-options']//a[.='BIOS Settings']"
    ID_SELECT_ADVANCED_PANEL = "xpath=//ol[@class='hp-options']//a[.='Advanced']"
    ID_SELECT_ACTIVITY_PANEL = "xpath=//ol[@class='hp-options']//a[.='Activity']"
    ID_SELECT_MAP_PANEL = "xpath=//ol[@class='hp-options']//a[.='Map']"
    ID_SELECT_LABELS_PANEL = "xpath=//ol[@class='hp-options']//a[.='Labels']"
    ID_STATUS_SERVER_PROFILE_OK = "xpath=//table/tbody//tr/td[translate(text(),'" + FusionUIConst.CONST_ZERO_WIDTH_SPACE + "','')='%s']/../td/div[@class='hp-status hp-status-ok']"  # server profile name
    ID_STATUS_SERVER_PROFILE_WARN = "xpath=//table/tbody//tr/td[translate(text(),'" + FusionUIConst.CONST_ZERO_WIDTH_SPACE + "','')='%s']/../td/div[@class='hp-status hp-status-warning']"  # server profile name
    ID_STATUS_SERVER_PROFILE_ERROR = "xpath=//table/tbody//tr/td[translate(text(),'" + FusionUIConst.CONST_ZERO_WIDTH_SPACE + "','')='%s']/../td/div[@class='hp-status hp-status-error']"  # server profile name
    ID_TABLE_SERVER_PROFILE_SELECTED = "xpath=//table[@class='hp-master-table hp-selectable dataTable']/tbody/tr[contains(@class, 'hp-selected')]/td[translate(text(),'" + FusionUIConst.CONST_ZERO_WIDTH_SPACE + "','')='%s']"  # server profile name
    ID_TABLE_SERVER_PROFILE_DELETED = "xpath=//table[@class='hp-master-table hp-selectable dataTable']/tbody/tr[contains(@class, 'hp-not-found')]/td[translate(text(),'" + FusionUIConst.CONST_ZERO_WIDTH_SPACE + "','')='%s']"  # server profile name
    ID_DROPDOWN_ACTIONS = "xpath=//label[text()='Actions']"
    ID_ICON_SERVER_PROFILE_STATUS = "//div[@id='cic-profile-details-status']/span[text()='%s']/.."
    ID_LABEL_SERVER_POWER = "//div[@id='cic-profile-show-power']/../label[text()='Server power']"
    ID_TEXT_SERVER_POWER_UNSET = "//div[@id='cic-profile-show-power'][@class='hp-form-content hp-unset']"
    ID_TEXT_OVERVIEW_SERVER_POWER = "//div[@id='cic-profile-show-power']"
    ID_TEXT_PROFILE_ERROR = "xpath=//*[@id='hp-page-notifications']/div"
    # ID_RIGHT_SIDEBAR_ACTIVITY = "xpath=//*[@id='cic-profile-page']/div[@class='hp-sub-nav']/div[@class='hp-sidebar-control']/div[@class='hp-pin-right']"
    ID_BUTTON_RIGHT_SIDEBAR_ACTIVITY = "xpath=(//div[@class='hp-sidebar-control']/div[@class='hp-pin-right'])[2]"
    ID_RIGHT_SIDEBAR_TITLE = "xpath=//*[@id='hp-activity-flyout']/header/h1[text()='Activity']"
    # ID_TEXT_LIST_SIDEBAR_ACTIVITY_STATUS = "xpath=(.//*[@id='hp-flyout-activities']/li[@class='hp-activity hp-active']/div[@class='hp-brief']/div[contains(@class, 'hp-status')]/span)[1]"
    ID_TEXT_LIST_SIDEBAR_ACTIVITY_STATUS = "xpath=//*[@id='hp-flyout-activities']/li[@class='hp-activity hp-active']/div[@class='hp-brief']/div[contains(@class, 'hp-status')]/span"
    ID_TEXT_LIST_SIDEBAR_ACTIVITY_MESSAGE = "xpath=//*[@id='hp-flyout-activities']/li[@class='hp-activity hp-active']/div[@class='hp-brief']/div[@class='hp-activity-message']/p/span"
    ID_TEXT_LIST_SIDEBAR_ACTIVITY_SOURCE = "xpath=//*[@id='hp-flyout-activities']/li[@class='hp-activity hp-active']/div[@class='hp-brief']/div[@class='hp-activity-source']"
    ID_RIGHT_SIDEBAR_ACTIVITY = "xpath=//*[@id='hp-flyout-activities']/li[@class='hp-activity hp-active']/div[@class='hp-brief']/div[contains(@class, 'hp-status')]/span[contains(text(),'%s')]" \
                                "/../following-sibling::div[@class='hp-activity-source' and text()='%s']/preceding-sibling::div[@class='hp-activity-message']/p/span[text()='%s']"
    ID_TEXT_ACTIVITY_ACTION_TITLE = "xpath=//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-activity-message']/p/span"  # volume template
    ID_TEXT_ACTIVITY_ACTION_OK = "xpath=//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-ok']"  # volume template
    ID_TEXT_ACTIVITY_ACTION_WARN = "xpath=//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-warning']"  # volume template
    ID_TEXT_ACTIVITY_ACTION_ERROR = "xpath=//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-error']"  # volume template
    ID_TEXT_ACTIVITY_ACTION_DETAILS_OK = "xpath=//header[@class='hp-active']/a[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-ok']"  # volume template
    ID_TEXT_ACTIVITY_MESSAGE = "xpath=//*[@id='hp-flyout-activities']/li/div[@class='hp-full']/div/div[@class='hp-notification-details']"
    ID_ICON_ACTIVITY_COLLAPSER = "//table[@class='hp-index-table hp-activities dataTable']/tbody/tr//span[text()='%s']/../../../td//div[@class='hp-collapser']"  # activity collapser
    ID_TEXT_ACTIVITY_CONTENT = "//table[@class='hp-index-table hp-activities dataTable']/tbody/tr//span[contains(text(), '%s')]"

    ID_TEXT_GENERAL_CONSISTENCY_STATE = "xpath=//div[@id='cic-profile-show-consistencyState']"
    ID_TEXT_GENERAL_SERVER_POWER = "xpath=//*[@id='cic-profile-show-power']"
    ID_TEXT_GENERAL_SERVER_HARDWARE = "xpath=//*[@id='cic-profile-show-server']/*"
    ID_TEXT_GENERAL_SERVER_HARDWARE_TYPE = "xpath=//*[@id='cic-profile-show-serverType']/a"
    ID_TEXT_GENERAL_ENCLOSURE_GROUP = "xpath=//*[@id='cic-profile-show-enclosureGroup']/a"
    ID_TEXT_GENERAL_ISCSI_INITIATOR_NAME_LABEL = "id=cic-profile-show-iscsiInitiatorName-label"
    ID_TEXT_GENERAL_ISCSI_INITIATOR_NAME = "id=cic-profile-show-iscsiInitiatorName"
    ID_TEXT_GENERAL_UUID_LABEL = "xpath=//label[@id='cic-profile-show-uuid-label']"
    ID_TEXT_GENERAL_UUID = "xpath=//div[@id='cic-profile-show-uuid']"
    ID_TEXT_GENERAL_SERIAL_NUMBER_LABEL = "xpath=//label[@id='cic-profile-show-serialNumber-label']"
    ID_TEXT_GENERAL_SERIAL_NUMBER = "xpath=//div[@id='cic-profile-show-serialNumber']"

    ID_ICON_CONNECTION_STATUS = "xpath=//table[@id='cic-profile-show-connections-summary']/tbody/tr/td[text()='%s']/preceding-sibling::td/div[@class='hp-status hp-status-%s']"
    ID_TEXT_CONNECTIONS_REQUESTED_VIRTUAL_FUNCTIONS_LABEL = "xpath=//td[@data-localize='profiles.connections.dialog.requestedVirtualFunctions']"
    ID_TEXT_CONNECTIONS_MAX_BANDWIDTH = "xpath=//td[@data-localize='profiles.connections.maxBandwidth']"
    ID_TEXT_CONNECTIONS_ALLOCATED_BANDWIDTH = "xpath=//td[@data-localize='profiles.connections.allocatedBandwidth']"
    ID_TEXT_CONNECTIONS_ALLOCATED_VIRTUAL_FUNCTIONS = "xpath=//td[@data-localize='profiles.connections.dialog.allocatedVirtualFunctions']"
    ID_TEXT_CONNECTIONS_INTERCONNECT = "xpath=//td[@class='template-connections-row-details-interconnect']"
    ID_TEXT_CONNECTIONS_REQUESTED_VIRTUAL_FUNCTIONS = "xpath=//td[@class='template-connections-row-details-requestedVFs']"

    class Firmware(object):
        # ID_SELECT_FIRMWARE_BASELINE = "xpath=//*[@id='cic-profile-add-firmware-div']/descendant::span[@class='selectBox-arrow']"
        ID_SELECT_FIRMWARE_BASELINE = "cic-profile-add-firmware-baseline|cic-profile-edit-firmware-baseline|cic-profile-copy-firmware-baseline"
        # ID_SELECT_FIRMWARE_BASELINE_BY_TEXT = "xpath=//ul/li/a[text()='%s']"  # 'managed manually' or 'HP Service Pack for ProLiant version 2014.09.0'
        ID_RADIO_INSTALLATION_METHOD_FW_AND_OS_DRIVERS_USING_SUT = "xpath=//*[@id='cic-profile-add-firmware-osdriver-select']|//*[@id='cic-profile-edit-firmware-osdriver-select']|//*[@id='cic-profile-copy-firmware-osdriver-select']"
        ID_RADIO_INSTALLATION_METHOD_FW_ONLY_USING_SUT = "xpath=//*[@id='cic-profile-add-firmware-select']|//*[@id='cic-profile-edit-firmware-select']|//*[@id='cic-profile-copy-firmware-select']"
        ID_RADIO_INSTALLATION_METHOD_FW_ONLY = "xpath=//*[@id='cic-profile-add-firmware-offlinemode-select']|//*[@id='cic-profile-edit-firmware-offlinemode-select']|//*[@id='cic-profile-copy-firmware-offlinemode-select']"
        ID_RADIO_ACTIVATE_FIRMWARE_IMMEDIATELY = "xpath=//*[@id='cic-profile-add-schedule-firmware-immediate']|//*[@id='cic-profile-edit-schedule-firmware-immediate']"
        ID_RADIO_ACTIVATE_FIRMWARE_SCHEDULE = "xpath=//*[@id='cic-profile-add-schedule-firmware-schedule']|//*[@id='cic-profile-edit-schedule-firmware-schedule']"
        ID_RADIO_ACTIVATE_FIRMWARE_NOT_SCHEDULED = "xpath=//*[@id='cic-profile-add-schedule-firmware-no-schedule']|//*[@id='cic-profile-edit-schedule-firmware-no-schedule']"
        ID_CHECKBOX_FORCE_INSTALLATION = "xpath=//*[@id='cic-profile-add-firmware-force']|//*[@id='cic-profile-edit-firmware-force']|//*[@id='cic-profile-copy-firmware-force']"

    class Connection(object):
        ID_TABLE_PROFILE_CONNECTION = "xpath=//table/tbody/tr/td[count(//table/thead/tr/th[.='Network']/preceding-sibling::th)]"
        ID_TEXT_CONNECT_PORT = "xpath=//table/tbody/tr/td[count(//table/thead/tr/th[.='Port']/preceding-sibling::th)+1]"
        ID_EXPAND_CONNECTIONS = "xpath = //*[@id='cic-profile-show-connections-summary']/tbody/tr[%s]/td/div[contains(@class,'hp-collapser')]"
        ID_TEXT_CONNECT_MAC_ADDRESS = "xpath=//td[@class='template-connections-row-details-mac']"
        ID_RADIO_REQUESTED_VIRTUAL_FUNCTIONS_NONE = "xpath=//input[@id='cic-profile-connection-virtual-functions-none']"
        ID_RADIO_REQUESTED_VIRTUAL_FUNCTIONS_AUTO = "xpath=//input[@id='cic-profile-connection-virtual-functions-auto']"
        ID_RADIO_REQUESTED_VIRTUAL_FUNCTIONS_CUSTOM = "xpath=//input[@id='cic-profile-connection-virtual-functions-custom']"
        ID_INPUT_REQUESTED_VIRTUAL_FUNCTIONS_CUSTOM = "xpath=//input[@id='cic-profile-connection-virtual-functions-custom-input']"
        ID_TEXT_CONNECTION_MACADDRESS = "xpath=//td[@class='template-connections-row-details-mac']/span"
        ID_BUTTON_ADD_CONNECTION = "id=cic-networkset-add-networks"
        ID_BUTTON_YES_REMOVE = "//button[text()='Yes, remove']"
        ID_BUTTON_CANCEL_REMOVE = "//button[text()='Cancel']"
        ID_DIALOG = "xpath=//*[@id='cic-profile-connections-dialog-form']/../header/descendant::span[text()='%s Connection']"  # replace %s with 'Add' or 'Edit'
        ID_ADD_CONNECTION_DIALOG = ID_DIALOG % 'Add'
        ID_DIALOG_REMOVE_CONNECTION = 'id=cic-profile-connection-san-delete-confirm-title'
        ID_EDIT_CONNECTION_DIALOG = ID_DIALOG % 'Edit'
        ID_DIALOG_TITLE = "xpath=//*[@id='cic-profile-connection-dialog-title']"
        ID_INPUT_NAME = "xpath=//*[@id='cic-profile-connection-name']"
        ID_SELECT_FUNCTION_TYPE = "cic-profile-connection-device-type"
        ID_SELECTBOX_FUNCTION_TYPE = "xpath=//*[@id='%s']/preceding-sibling::div[contains(@class, 'hp-select')]" % ID_SELECT_FUNCTION_TYPE
        ID_TEXT_FUNCTION_TYPE = "xpath=//*[@id='cic-profile-connections-dialog-form-contents']//label[@for='cic-profile-connection-device-type']/..//div[contains(@class,'hp-value') and (.='%s')]"
        ID_INPUT_NETWORK = "xpath=//*[@id='cic-profile-connection-network-input']"
        ID_OPTION_NETWORK = "xpath=//div[@id='cic-profile-connection-network-control-sec']//ol[@class='hp-search-combo-scroller hp-options']//span[@class='hp-name']"
        ID_INPUT_PORT = "xpath=//*[@id='cic-profile-connection-flexnic-input']"
        ID_OPTION_PORT = "xpath=//*[@id='cic-profile-connection-flexnic-input']/following-sibling::div/descendant::span[text()='%s']"
        # ID_INPUT_REQUESTED_BANDWIDTH_FOR_ETHERNET = "xpath=//*[@id='cic-profile-connection-bandwidth']"
        ID_INPUT_REQUESTED_BANDWIDTH = "xpath=//*[@id='cic-profile-connection-bandwidth']"
        ID_SELECTBOX_REQUESTED_BANDWIDTH = "xpath=//*[@id='cic-profile-connection-bandwidth-discrete-group']/div/div/div"
        ID_SELECT_REQUESTED_BANDWIDTH = "cic-profile-connection-bandwidth-discrete"
        ID_SELECT_BOOT = "cic-profile-connection-boot"
        ID_RADIO_MANAGED_VOLUME = "id=cic-profile-connection-bootTargetSource-volumeAttached"
        ID_TEXT_HELP_RADIO_BOOT = "id=cic-profile-connection-bootTargetSource-volumeAttached-help"
        ID_RADIO_SPECIFY_BOOT_TARGET = "xpath=//*[@id='cic-profile-connection-bootTargetSource-specifyBootTarget']"
        ID_RADIO_USE_ADAPTER_BIOS = "xpath=//*[@id='cic-profile-connection-bootTargetSource-useBios']"
        ID_RADIO_PROFILE_INITIATOR_NAME = "id=cic-profile-connection-iscsi-initiator-name-source-profile"
        ID_RADIO_USER_SPECIFIED = "id=cic-profile-connection-iscsi-initiator-name-source-user"
        ID_INPUT_WWPN = "xpath=//*[@id='cic-profile-connection-wwnTarget']"
        ID_ERR_MSG_WWPN = "xpath=//*[@id='cic-profile-connection-fcoeBootTarget-group']/li/div/label[contains(@class, 'hp-error') and @for='cic-profile-connection-wwnTarget']"
        ID_INPUT_LUN = "xpath=//*[@id='cic-profile-connection-lunTarget']"
        ID_ERR_MSG_LUN = "xpath=//*[@id='cic-profile-connection-fcoeBootTarget-group']/li/div/label[contains(@class, 'hp-error') and @for='cic-profile-connection-lunTarget']"
        ID_INPUT_ISCSI_INITIATOR_NAME = "id=cic-profile-connection-iscsi-initiator-name"
        ID_TEXT_ERROR_ISCSI_INITIATOR_NAME = "xpath=//*[@id='cic-profile-connection-iscsi-initiator-name-container']/li/div/label[contains(@class, 'hp-error') and @for='cic-profile-connection-iscsi-initiator-name']"
        ID_INPUT_ISCSI_INITIATOR_IPV4_ADDRESS = "id=cic-profile-connection-iscsi-initiator-ip"
        ID_TEXT_ERROR_ISCSI_INITIATOR_IPV4_ADDRESS = "xpath=//*[@id='cic-profile-connection-iscsi-initiator-ip-container']/div/label[contains(@class, 'hp-error') and @for='cic-profile-connection-iscsi-initiator-ip']"
        ID_INPUT_ISCSI_SUBNET_MASK = "id=cic-profile-connection-iscsi-initiator-subnet"
        ID_TEXT_ERROR_ISCSI_SUBNET_MASK = "xpath=//*[@id='cic-profile-connection-iscsi-initiator']//div/label[contains(@class, 'hp-error') and @for='cic-profile-connection-iscsi-initiator-subnet']"
        ID_INPUT_ISCSI_GATEWAY = "id=cic-profile-connection-iscsi-initiator-gateway"
        ID_TEXT_ERROR_ISCSI_GATEWAY = "xpath=//*[@id='cic-profile-connection-iscsi-initiator']//div/label[contains(@class, 'hp-error') and @for='cic-profile-connection-iscsi-initiator-gateway']"
        ID_INPUT_ISCSI_VLAN_ID = "id=cic-profile-connection-iscsi-initiator-vlan-id"
        ID_TEXT_ERROR_ISCSI_VLAN_ID = "xpath=//*[@id='cic-profile-connection-iscsi-initiator-vlan-id-container']/div/label[contains(@class, 'hp-error') and @for='cic-profile-connection-iscsi-initiator-vlan-id']"
        ID_INPUT_ISCSI_TARGET_NAME = "id=cic-profile-connection-iscsi-boot-target-name"
        ID_TEXT_ERROR_ISCSI_TARGET_NAME = "xpath=//*[@id='cic-profile-connection-iscsi-boot-target-name-container']/div/div/label[contains(@class, 'hp-error') and @for='cic-profile-connection-iscsi-boot-target-name']"
        ID_INPUT_ISCSI_TARGET_LUN = "id=cic-profile-connection-iscsi-boot-target-lun"
        ID_TEXT_ERROR_ISCSI_TARGET_LUN = "xpath=//*[@id='cic-profile-connection-iscsi-boot-target-lun-container']/div/label[contains(@class, 'hp-error') and @for='cic-profile-connection-iscsi-boot-target-lun']"
        ID_INPUT_ISCSI_TARGET_IP = "id=cic-profile-connection-iscsi-first-boot-target-ip"
        ID_TEXT_ERROR_ISCSI_TARGET_IP = "xpath=//*[@id='cic-profile-connection-iscsi-boot-target-panel']//div/label[contains(@class, 'hp-error') and @for='cic-profile-connection-iscsi-first-boot-target-ip']"
        ID_INPUT_ISCSI_TARGET_PORT = "id=cic-profile-connection-iscsi-first-boot-target-port"
        ID_TEXT_ERROR_ISCSI_TARGET_PORT = "xpath=//*[@id='cic-profile-connection-iscsi-boot-target-panel']//div/label[contains(@class, 'hp-error') and @for='cic-profile-connection-iscsi-first-boot-target-port']"
        ID_INPUT_ISCSI_SECOND_IP = "id=cic-profile-connection-iscsi-second-boot-target-ip"
        ID_TEXT_ERROR_ISCSI_SECOND_IP = "xpath=//*[@id='cic-profile-connection-iscsi-boot-target-panel']//div/label[contains(@class, 'hp-error') and @for='cic-profile-connection-iscsi-second-boot-target-ip']"
        ID_INPUT_ISCSI_SECOND_PORT = "id=cic-profile-connection-iscsi-second-boot-target-port"
        ID_TEXT_ERROR_ISCSI_SECOND_PORT = "xpath=//*[@id='cic-profile-connection-iscsi-boot-target-panel']//div/label[contains(@class, 'hp-error') and @for='cic-profile-connection-iscsi-second-boot-target-port']"
        ID_RADIO_CHAP_LVL_NONE = "id=cic-profile-connection-iscsi-chap-level-none"
        ID_RADIO_CHAP_LVL_CHAP = "id=cic-profile-connection-iscsi-chap-level-chap"
        ID_RADIO_CHAP_LVL_MCHAP = "id=cic-profile-connection-iscsi-chap-level-mchap"
        ID_INPUT_CHAP_NAME = "id=cic-profile-connection-iscsi-chap-name"
        ID_TEXT_ERROR_CHAP_NAME = "xpath=//*[@id='cic-profile-connection-iscsi-auth-panel']//label[contains(@class, 'hp-error') and @for='cic-profile-connection-iscsi-chap-name']"
        ID_INPUT_CHAP_SECRET = "id=cic-profile-connection-iscsi-chap-secret"
        ID_TEXT_ERROR_CHAP_SECRET = "xpath=//*[@id='cic-profile-connection-iscsi-auth-panel']//label[contains(@class, 'hp-error') and @for='cic-profile-connection-iscsi-chap-secret']"
        ID_INPUT_MCHAP_NAME = "id=cic-profile-connection-iscsi-mchap-name"
        ID_TEXT_ERROR_MCHAP_NAME = "xpath=//*[@id='cic-profile-connection-iscsi-auth-panel']//label[contains(@class, 'hp-error') and @for='cic-profile-connection-iscsi-mchap-name']"
        ID_INPUT_MCHAP_SECRET = "id=cic-profile-connection-iscsi-mchap-secret"
        ID_TEXT_ERROR_MCHAP_SECRET = "xpath=//*[@id='cic-profile-connection-iscsi-auth-panel']//label[contains(@class, 'hp-error') and @for='cic-profile-connection-iscsi-mchap-secret']"
        ID_CHECKBOX_USE_USER_SPECIFIED_IDS = "xpath=//*[@id='cic-profile-connection-userSpecifiedID']"
        ID_INPUT_WWPN_USER_SPECIFIED = "xpath=//*[@id='cic-profile-connection-wwpn']"
        ID_ERR_MSG_WWPN_USER_SPECIFIED = "xpath=//*[@id='cic-profile-connection-userSpecifiedID-wwpnGroup']/div/label[contains(@class, 'hp-error') and @for='cic-profile-connection-wwpn']"
        ID_INPUT_WWNN_USER_SPECIFIED = "xpath=//*[@id='cic-profile-connection-wwnn']"
        ID_ERR_MSG_WWNN_USER_SPECIFIED = "xpath=//*[@id='cic-profile-connection-userSpecifiedID-wwnnGroup']/div/label[contains(@class, 'hp-error') and @for='cic-profile-connection-wwnn']"
        ID_INPUT_MAC_ADDRESS_USER_SPECIFIED = "xpath=//*[@id='cic-profile-connection-mac']"
        ID_ERR_MSG_MAC_ADDRESS_USER_SPECIFIED = "xpath=//*[@id='cic-profile-connection-userSpecifiedID-macGroup']/div/label[contains(@class, 'hp-error') and @for='cic-profile-connection-mac']"
        ID_BUTTON_ADD = "xpath=//*[@id='cic-profile-connection-add']"
        ID_BUTTON_ADD_PLUS = "xpath=//*[@id='cic-profile-connection-addAgain']"
        ID_BUTTON_CANCEL = "xpath=//*[@id='cic-profile-connection-addAgain']/following-sibling::button[text()='Cancel']"
        ID_BUTTON_OK = ID_BUTTON_ADD

        ID_BUTTON_EDIT_CONNECTION = "xpath=//*[contains(@id, 'cic-profile-add-connections-table') or contains(@id, 'cic-profile-edit-connections-table') or contains(@id, 'cic-profile-copy-connections-table')]/tbody/tr/td/div[normalize-space(text())='%s']" \
                                    "/../following-sibling::td/div[contains(@class, 'hp-edit')]"  # replace %s with connection name (not network name)

        # format {0} with connection name (not network name): ID_BUTTON_DELETE_CONNECTION.format(connection_name)
        ID_BUTTON_DELETE_CONNECTION = "xpath=//*[contains(@id, 'cic-profile-add-connections-table') or contains(@id, 'cic-profile-edit-connections-table') or contains(@id, 'cic-profile-copy-connections-table')]/tbody/tr/td/div[normalize-space(text())='{0}']/../following-sibling::td/div[contains(@class, 'hp-delete')]"
        # replace %s with connection name (not network name)
        ID_TABLE_CONNECTION = "xpath=//*[contains(@id, 'cic-profile-add-connections-table') or contains(@id, 'cic-profile-edit-connections-table') or contains(@id, 'cic-profile-copy-connections-table')]/tbody/tr/td/div[normalize-space(text())='%s']"
        ID_TABLE_CONNECTION_LIST = "xpath=//*[contains(@id, 'cic-profile-add-connections-table') or contains(@id, 'cic-profile-edit-connections-table') or contains(@id, 'cic-profile-copy-connections-table')]/tbody/tr/td/div[@class='hp-delete']/../preceding-sibling::td[contains(@class, '-numeric')]"
        # ID_STATUS_CONNECTION_DISABLED = "xpath=//*[contains(@id, 'cic-profile-add-connections-table') or contains(@id, 'cic-profile-edit-connections-table')]/tbody/tr/td/div[normalize-space(text())='%s']" \
        #                                 "/../preceding-sibling::td/div[contains(@class, 'hp-status-disabled')]"

        ID_TEXT_CONNECT_DISPLAY_NAME = "xpath=//table[@id='cic-profile-show-connections-summary']/tbody/tr[%d]/td[contains(text(),'%s')]"
        ID_TEXT_CONNECT_DISPLAY_NETWORK = "xpath=//table[@id='cic-profile-show-connections-summary']/tbody/tr[%d]//a[contains(@href, 'ethernet-networks') or contains(@href, 'fc-networks') or contains(@href, 'network-sets') or contains(@href, 'fcoe-networks')]"
        ID_TEXT_CONNECT_DISPLAY_PORT = "xpath=//table[@id='cic-profile-show-connections-summary']/tbody/tr[%d]/td[contains(text(),'%s')]"
        ID_TEXT_CONNECT_DISPLAY_BOOT = "xpath=//table[@id='cic-profile-show-connections-summary']/tbody/tr[%d]/td[contains(text(),'%s')]"
        ID_TEXT_BOOT_MANAGED_MANUALLY = "xpath=//*[@id='cic-profile-connection-port-config-group']//div[text()='managed manually']"
        ID_TEXT_CONNECTION_FUNCTION_TYPE = "xpath=//td[@class='template-connections-row-details-type' and contains(text(),'%s')]"
        ID_TEXT_CONNECTION_WWNN = "xpath=//td[@class='template-connections-row-details-wwnn']"
        ID_TEXT_CONNECTION_WWPN = "xpath=//td[@class='template-connections-row-details-wwpn']"
        ID_TEXT_CONNECTION_BOOT_VOLUME = "xpath=//td[@class='template-connections-row-details-bootVolume']"
        ID_TEXT_CONNECTION_BOOT_TARGET = "xpath=//td[@class='template-connections-row-details-bootTargets']"
        ID_TEXT_CONNECTION_BOOT_LUN = "xpath=//td[@class='template-connections-row-details-bootLun']"
        ID_TEXT_CONNECT_DISPLAY_BANDWIDTH = "xpath=//td[@class='template-connections-row-details-requestedBandwidth']"
        ID_TEXT_CONNECT_MAX_BANDWIDTH = "xpath=//td[@class='template-connections-row-details-maxBandwidth']"
        ID_TEXT_CONNECTION_INITIATOR_NAME = "xpath=//td[@class='template-connections-row-details-initiatorName' and contains(text(),'%s')]"
        ID_TEXT_CONNECTION_INITIATOR_NAME_UNSET = "xpath=//td[@class='template-connections-row-details-initiatorName']/span[contains(text(),'not set')]"
        ID_TEXT_CONNECTION_INITIATOR_IP = "xpath=//td[@class='template-connections-row-details-initiatorIp' and contains(text(),'%s')]"
        ID_TEXT_CONNECTION_INITIATOR_SUBNET_MASK = "xpath=//td[@class='template-connections-row-details-initiatorSubnetMask' and contains(text(),'%s')]"
        ID_TEXT_CONNECTION_INITIATOR_GATEWAY = "xpath=//td[@class='template-connections-row-details-initiatorGateway' and contains(text(),'%s')]"
        ID_TEXT_CONNECTION_INITIATOR_GATEWAY_UNSET = "xpath=//td[@class='template-connections-row-details-initiatorGateway']/span[contains(text(),'not set')]"
        ID_TEXT_CONNECTION_TARGET_NAME = "xpath=//td[@class='template-connections-row-details-bootTargetName' and contains(text(),'%s')]"
        ID_TEXT_CONNECTION_TARGET_LUN = "xpath=//td[@class='template-connections-row-details-bootTargetLun' and contains(text(),'%s')]"
        ID_TEXT_CONNECTION_TARGET_IP = "xpath=//td[@class='template-connections-row-details-firstBootTargetIp' and contains(text(),'%s')]"
        ID_TEXT_CONNECTION_SECOND_IP = "xpath=//td[@class='template-connections-row-details-secondBootTargetIp' and contains(text(),'%s')]"
        ID_TEXT_CONNECTION_CHAP_NAME = "xpath=//td[@class='template-connections-row-details-chapName hp-ellipsis hp-ellipsised' and contains(text(),'%s')]"
        ID_TEXT_CONNECTION_CHAP_NAME_NOT_SET = "xpath=//td[@class='template-connections-row-details-chapName hp-ellipsis hp-ellipsised']/span[contains(text(),'not set')]"
        ID_TEXT_CONNECTION_MCHAP_NAME = "xpath=//td[@class='template-connections-row-details-mutualChapName hp-ellipsis hp-ellipsised' and contains(text(),'%s')]"
        ID_TEXT_CONNECTION_MCHAP_NAME_HEADER = "xpath=//*[@id='cic-profile-show-connections-summary']//tr/td[contains(text(),'Mutual CHAP name')]"
        ID_TABLE_CONNECTION_DETAIL_INFO = "//table[@id='cic-profile-show-connections-summary']/tbody/tr[%d]/td[@class=' sorting_1']/div"
        ID_TABLE_CONNECTION_DETAIL_INFO_EXPAND = "//table[@id='cic-profile-show-connections-summary']/tbody/tr[%d]/td[@class=' sorting_1']/div[@class = 'hp-collapser hp-active']"
        ID_BANDWIDTH_ERROR = "xpath=//*[@id='cic-profile-connection-bandwidth-group']/div/div/label[@class='hp-error']"

    class LocalStorage(object):
        ID_CHECKBOX_MANAGE_LOCAL_STORAGE = "xpath=//*[@id='cic-profile-manage-local-storage']"
        ID_CHECKBOX_MANAGE_INTEGRATED_CONTROLLER = "xpath=//*[@id='cic-profile-manage-local-storage-manage-integrated-controller']"
        ID_BUTTON_MANAGE_LOCAL_STORAGE_CONTROLLER_ALERT_CLOSE = "xpath=//*[@id='hp-body-div']/div[9]/div/div/div/footer/div/button"
        ID_CHECKBOX_REINITIALIZE_INTERNAL_STORAGE = "xpath=//*[@id='cic-profile-local-storage-initialize']"
        ID_SELECT_CONTROLLER_MODE = "cic-profile-local-storage-controller-mode-select"
        ID_CHECKBOX_IMPORT_EXISTING_LOGICAL_DRIVES = "xpath=//*[@id='cic-profile-local-storage-import-logical-drive']"
        ID_SELECT_BOOT_DRIVE = "cic-profile-local-storage-boot-drive"
        ID_BUTTON_EDIT_INTEGRATED_CONTROLLER = "xpath=//*[@id='cic-profile-local-storage-integratedStorage-edit']"
        ID_BUTTON_EDIT_MEZZ_CONTROLLER = "xpath=//*[@id='Mezz-%s']"
        ID_TITLE_EDIT_INTEGRATED_CONTROLLER = "cic-profile-localStorage-dialog-title"
        ID_DROPDOWN_INTEGRATED_CONTROLLER_MODE = "//*[@id='cic-profile-local-storage-controller-mode-select-container']/a/span[@class='selectBox-arrow']"
        ID_SELECT_INTEGRATED_CONTROLLER_MODE = "//a[contains(text(), '%s')"
        ID_BUTTON_OK = "xpath=//*[@id='cic-profile-localStorage-create']"
        ID_BUTTON_CANCEL = "xpath=//*[@id='cic-profile-localStorage-cancel']"
        ID_CHECKBOX_LOCAL_BOOT_DRIVE = "xpath=//td/div/label[text()='%s']/../../following-sibling::td/div/input[@id='cic-profile-local-storage-boot-drive']"

        class LogicalDrive(object):
            ID_BUTTON_CREATE_LOGICAL_DRIVE = "xpath=//*[@id='cic-profile-add-logical-drive']"
            ID_DIALOG = "xpath=//*[@id='cic-profile-logical-drive-dialog-title']"
            ID_DIALOG_TITLE = "xpath=//*[@id='cic-profile-logical-drive-dialog-title']"
            ID_INPUT_NAME = "xpath=//*[@id='cic-profile-logical-drive-name']"
            ID_ERR_MSG_NAME = "xpath=//*[@id='cic-profile-logical-drive-panels']/li/div/label[@for='cic-profile-logical-drive-name']"
            ID_SELECT_RAID_LEVEL = "cic-profile-logical-drive-dialog-raid-level"
            ID_INPUT_NUMBER_OF_PHYSICAL_DRIVES = "xpath=//*[@id='cic-profile-logical-drive-dialog-physical-drives']"
            ID_INPUT_MIN_DRIVE_SIZE = "id=cic-profile-logical-drive-dialog-min-size"
            ID_INPUT_MAX_DRIVE_SIZE = "id=cic-profile-logical-drive-dialog-max-size"
            ID_ERR_MSG_NUMBER_OF_PHYSICAL_DRIVES = "xpath=//*[@id='cic-profile-logical-drive-dialog-physical-drives-select-div']/div/label" \
                                                   "[@for='cic-profile-logical-drive-dialog-physical-drives' and contains(@class, 'hp-error')]"
            ID_SELECT_DRIVE_TECHNOLOGY = "cic-profile-logical-drive-dialog-drive-tech"
            ID_BUTTON_CREATE = "xpath=//*[@id='cic-profile-logical-drive-create']"
            ID_BUTTON_CREATE_PLUS = "xpath=//*[@id='cic-profile-logical-drive-createAgain']"
            ID_BUTTON_CANCEL = "xpath=//*[@id='cic-profile-logical-drive-add-cancel']"

            # format {0} with logical drive name: ID_TABLE_LOGICAL_DRIVE.format(drive_name)
            ID_TABLE_LOGICAL_DRIVE = "//*[@id='cic-profile-add-local-storage-logical-drive-table' or @id='cic-profile-local-storage-logical-drive-table' or @id='cic-profile-edit-local-storage-logical-drive-table' or @id='cic-profile-copy-local-storage-logical-drive-table']/tbody/tr/td/div/label[text()='{0}']"
            # replace %s with logical drive's name
            ID_BUTTON_DELETE_LOGICAL_DRIVE_BY_NAME = "xpath=//*[@id='cic-profile-add-local-storage-logical-drive-table' or @id='cic-profile-local-storage-logical-drive-table' or @id='cic-profile-edit-local-storage-logical-drive-table' or @id='cic-profile-copy-local-storage-logical-drive-table']/tbody/tr/td/div/label[text()='%s']/../parent::td/../td/div[@class='hp-delete']"
            # Logical Drive table
            ID_TABLE_VOLUME = "xpath=//*[contains(@id, 'storageVolumeId-edit') or contains(@id, 'storageVolumeId-add') or contains(@id, 'storageVolumeId-copy')]/td[contains(text(), '{0}')]|//*[contains(@id, 'storageVolumeId-edit') or contains(@id, 'storageVolumeId-add') or contains(@id, 'storageVolumeId-copy')]/td/a[text()='{0}']"
            ID_BUTTON_DELETE_CONFIRM = "xpath=//*[@class='hp-controls']/button[text()='Yes, delete']"
            # Temporarily using td[index] until there's a class name for /div/ or td
            ID_TEXT_LOGICAL_DRIVE_NAME = "xpath=//*[@id='cic-profile-integrated-storage-detail-table0']//td/div/label[text()='%s']"
            ID_TEXT_LOGICAL_DRIVE_MODE = "id=cic-profile-local-storage-integratedStorage-modeText"
            ID_TEXT_LOGICAL_DRIVE_PENDING = "xpath=//*[@id='cic-profile-integrated-storage-detail-table0']//td/div/label[text()='%s']/../../following-sibling::td[%s]/div/label"
            ID_TEXT_LOGICAL_DRIVE_NUMBER = "xpath=//*[@id='cic-profile-integrated-storage-detail-table0']//td/div/label[text()='%s']/../../following-sibling::td[%s]/div/label"
            ID_TEXT_LOGICAL_DRIVE_RAID_LEVEL = "xpath=//*[@id='cic-profile-integrated-storage-detail-table0']//td/div/label[text()='%s']/../../following-sibling::td[%s]/div/label"
            ID_TEXT_LOGICAL_DRIVE_NUM_OF_DRIVES = "xpath=//*[@id='cic-profile-integrated-storage-detail-table0']//td/div/label[text()='%s']/../../following-sibling::td[%s]/div/label"
            ID_TEXT_LOGICAL_DRIVE_MIN_GB = "xpath=//*[@id='cic-profile-integrated-storage-detail-table0']//td/div/label[text()='%s']/../../following-sibling::td[%s]/div/label"
            ID_TEXT_LOGICAL_DRIVE_MAX_GB = "xpath=//*[@id='cic-profile-integrated-storage-detail-table0']//td/div/label[text()='%s']/../../following-sibling::td[%s]/div/label"
            ID_TEXT_LOGICAL_DRIVE_TECH = "xpath=//*[@id='cic-profile-integrated-storage-detail-table0']//td/div/label[text()='%s']/../../following-sibling::td[%s]/div/label"
            ID_TEXT_LOGICAL_DRIVE_BOOT = "xpath=//*[@id='cic-profile-integrated-storage-detail-table0']//td/div/label[text()='%s']/../../following-sibling::td[%s]/div/label"
            ID_TEXT_LOGICAL_DRIVE_STATUS_OK = "xpath=//*[@id='cic-profile-integrated-storage-detail-table0']//td/div/label[text()='%s']/../../preceding-sibling::td/div[@class='hp-status hp-status-ok']"
            ID_TEXT_LOGICAL_DRIVE_ERROR = "xpath=//*[@id='cic-profile-integrated-storage-detail-table0']//td/div/label[text()='%s']/../../preceding-sibling::td/div[@class='hp-status hp-status-error']"
            ID_TEXT_LOGICAL_DRIVE_UNKNOWN = "xpath=//*[@id='cic-profile-integrated-storage-detail-table0']//td/div/label[text()='%s']/../../preceding-sibling::td/div[@class='hp-status hp-status-unknown']"
            ID_LOGICAL_DRIVE_VIEW_DRIVES_TABLE = "//table[@id='cic-profile-integrated-storage-detail-table0']"
            ID_ROW_LOGICAL_DRIVE_VIEW_TABLE_HEAD = ID_LOGICAL_DRIVE_VIEW_DRIVES_TABLE + "/thead/tr"
            ID_LOGICAL_DRIVE_VIEW_NAME_COLUMN_HEAD = "//td[text()='Name']"
            ID_LOGICAL_DRIVE_VIEW_NUM_OF_DRIVES_COLUMN_HEAD = "//td[text()='Number of Drives']"
            ID_LOGICAL_DRIVE_VIEW_RAID_LEVEL_COLUMN_HEAD = "//td[text()='RAID Level']"
            ID_LOGICAL_DRIVE_VIEW_LOGICAL_DRIVE_COLUMN_HEAD = "//td[text()='Logical Drive']"
            ID_LOGICAL_DRIVE_VIEW_MIN_GB_COLUMN_HEAD = "//td[text()='Min GB']"
            ID_LOGICAL_DRIVE_VIEW_MAX_GB_COLUMN_HEAD = "//td[text()='Max GB']"
            ID_LOGICAL_DRIVE_VIEW_DRIVE_TECH_COLUMN_HEAD = "//td[text()='Drive Technology']"
            ID_LOGICAL_DRIVE_VIEW_BOOT_COLUMN_HEAD = "//td[text()='Boot']"
            ID_TITLE_CHANGE_CONTROLLER_MODE_CONFIRM = "xpath=//*[@id='cic-profile-change-controller-mode-dialog-title']"
            ID_BUTTON_CHANGE_CONTROLLER_MODE_OK = "xpath=//*[@id='cic-profile-change-external-controller-mode-ok']"

        class LogicalJbod(object):
            # Temporarily using td[index] until there's a class name for /div/ or td
            ID_LOGICAL_JBOD_VIEW_DRIVES_TABLE = "//table[@id='cic-profile-external-storage-detail-table0Mezz-%s']"
            ID_ROW_LOGICAL_JBOD_VIEW_TABLE_HEAD = ID_LOGICAL_JBOD_VIEW_DRIVES_TABLE + "/thead/tr"
            ID_LOGICAL_JBOD_VIEW_NAME_COLUMN_HEAD = "//td[text()='Name']"
            ID_LOGICAL_JBOD_VIEW_NUM_OF_DRIVES_COLUMN_HEAD = "//td[text()='Number of Drives']"
            ID_LOGICAL_JBOD_VIEW_RAID_LEVEL_COLUMN_HEAD = "//td[text()='RAID Level']"
            ID_LOGICAL_JBOD_VIEW_LOGICAL_DRIVE_COLUMN_HEAD = "//td[text()='Logical Drive']"
            ID_LOGICAL_JBOD_VIEW_MIN_GB_COLUMN_HEAD = "//td[text()='Min GB']"
            ID_LOGICAL_JBOD_VIEW_MAX_GB_COLUMN_HEAD = "//td[text()='Max GB']"
            ID_LOGICAL_JBOD_VIEW_DRIVE_TECH_COLUMN_HEAD = "//td[text()='Drive Technology']"
            ID_LOGICAL_JBOD_VIEW_BOOT_COLUMN_HEAD = "//td[text()='Boot']"
            ID_TEXT_LOGICAL_JBOD_NAME = "xpath=//*[@id='cic-profile-external-storage-detail-table0Mezz-%s']//label[text()='%s']"
            ID_TEXT_LOGICAL_JBOD_MODE = "xpath=//*[@id='cic-profile-local-storage-externalStorage-headerText' and text()='Mezz %s storage controller mode']/following-sibling::label[@id='cic-profile-local-storage-externalStorage-modeText']"
            ID_TEXT_LOGICAL_JBOD_PENDING = "xpath=//*[@id='cic-profile-external-storage-detail-table0Mezz-%s']//div/label[text()='%s']/following-sibling::label"
            ID_TEXT_LOGICAL_JBOD_LOGICAL_DRIVE = "xpath=//*[@id='cic-profile-external-storage-detail-table0Mezz-%s']//td/div/label[text()='%s']/../../following-sibling::td[%s]/div/label"
            ID_TEXT_LOGICAL_JBOD_RAID_LEVEL = "xpath=//*[@id='cic-profile-external-storage-detail-table0Mezz-%s']//td/div/label[text()='%s']/../../following-sibling::td[%s]/div/label"
            ID_TEXT_LOGICAL_JBOD_NUM_OF_DRIVES = "xpath=//*[@id='cic-profile-external-storage-detail-table0Mezz-%s']//td/div/label[text()='%s']/../../following-sibling::td[%s]/div/label"
            ID_TEXT_LOGICAL_JBOD_MIN_GB = "xpath=//*[@id='cic-profile-external-storage-detail-table0Mezz-%s']//td/div/label[text()='%s']/../../following-sibling::td[%s]/div/label"
            ID_TEXT_LOGICAL_JBOD_MAX_GB = "xpath=//*[@id='cic-profile-external-storage-detail-table0Mezz-%s']//td/div/label[text()='%s']/../../following-sibling::td[%s]/div/label"
            ID_TEXT_LOGICAL_JBOD_DRIVE_TECH = "xpath=//*[@id='cic-profile-external-storage-detail-table0Mezz-%s']//td/div/label[text()='%s']/../../following-sibling::td[%s]/div/label"
            ID_TEXT_LOGICAL_JBOD_BOOT = "xpath=//*[@id='cic-profile-external-storage-detail-table0Mezz-%s']//td/div/label[text()='%s']/../../following-sibling::td[%s]/div/label"
            ID_TEXT_LOGICAL_JBOD_STATUS_OK = "xpath=//*[@id='cic-profile-external-storage-detail-table0Mezz-%s']//td/div/label[text()='%s']/../../preceding-sibling::td/div[@class='hp-status hp-status-ok']"
            ID_TEXT_LOGICAL_JBOD_STATUS_ERROR = "xpath=//*[@id='cic-profile-external-storage-detail-table0Mezz-%s']//td/div/label[text()='%s']/../../preceding-sibling::td/div[@class='hp-status hp-status-error']"
            ID_TEXT_LOGICAL_JBOD_UNKNOWN = "xpath=//*[@id='cic-profile-external-storage-detail-table0Mezz-%s']//td/div/label[text()='%s']/../../preceding-sibling::td/div[@class='hp-status hp-status-unknown']"
            ID_LABEL_CHANGE_CONTROLLER_MODE_MANUALLY = "xpath=.//*[@id='cic-profile-change-external-controller-mode-msg']/p/span[contains(text(),'The storage controller will no longer be managed by OneView')]"
            ID_BUTTON_OK_CHANGE_CONTROLLER = "xpath=//*[@id='cic-profile-change-external-controller-mode-ok']"
            ID_LABEL_CHANGE_CONTROLLER_MODE = "xpath=//*[@id='cic-profile-change-external-controller-mode-msg']/p/span[contains(text(), 'Changing the controller mode')]"
            ID_TEXT_ZONED_DRIVE_ENCLOSURE_NAME = "xpath= //table[@id='cic-profile-external-storage-detail-table0Mezz-%s']/tbody/tr/td/div/label[text()='%s']/../../../following-sibling::tr[@class='hp-row-details-cell']//tr[%s]//a[@href]"
            ID_TEXT_ZONED_HARD_DRIVE_NAME = "xpath= //table[@id='cic-profile-external-storage-detail-table0Mezz-%s']/tbody/tr/td/div/label[text()='%s']/../../../following-sibling::tr[@class='hp-row-details-cell']//tr[%s]//td[3]/div"
            ID_TEXT_ZONED_HARD_DRIVE_SIZE = "xpath= //table[@id='cic-profile-external-storage-detail-table0Mezz-%s']/tbody/tr/td/div/label[text()='%s']/../../../following-sibling::tr[@class='hp-row-details-cell']//tr[%s]//td[4]/div"
            ID_BUTTON_JBOD_DETAILS_EXPAND = "xpath=//*[@id='cic-profile-external-storage-detail-table0Mezz-%s']//td/div/label[text()='%s']/../../preceding-sibling::td/div[contains(@class, 'hp-collapser hp-collapsed')]"
            ID_LINK_LI_NAME = "xpath=//*[@id='cic-profile-local-storage-externalStorage-liValue']/a"

    class SANStorage(object):
        ID_CHECKBOX_MANAGE_SAN_STORAGE = "xpath=//*[@id='cic-profile-add-manage-san']|//*[@id='cic-profile-edit-manage-san']|//*[@id='cic-profile-copy-manage-san']"
        # ID_SELECT_HOST_OS_TYPE = "cic-profile-add-storage-os-type"
        # ID_SELECT_HOST_OS_TYPE = "cic-profile-edit-storage-os-type"
        ID_SELECT_HOST_OS_TYPE = "cic-profile-add-storage-os-type|cic-profile-edit-storage-os-type|cic-profile-copy-storage-os-type"
        ID_TEXT_HOST_OS_TYPE = "xpath=//*[@id='cic-profile-show-storage-volumes-ostype']"
        ID_TEXT_VOL_ATTACHMENT_MESSAGE = "xpath=//*[@id='cic-profile-show-volumes-message']"

        class Volume(object):
            ID_BUTTON_ADD_VOLUME = "xpath=//*[@id='cic-profile-add-storage-volumes']|//*[@id='cic-profile-edit-storage-volumes']|//*[@id='cic-profile-copy-storage-volumes']"
            ID_DIALOG = "xpath=//*[@id='cic-profile-storage-dialog']"
            ID_DIALOG_TITLE = "xpath=//span[@id='cic-profile-storage-dialog-title-action']"
            ID_SELECT_TYPE = "cic-profile-storage-volume-type"
            ID_INPUT_EXISTING_VOLUME_NAME = "xpath=//*[@id='cic-profile-storage-existing-volume-name-input']"
            ID_ERR_MSG_EXISTING_VOLUME_NAME = "xpath=//*[@id='cic-profile-storage-volume-div']/label[@class='hp-error' and @for='cic-profile-storage-existing-volume-name']"
            ID_OPTION_EXISTING_VOLUME_NAME = "xpath=//div[@id='cic-profile-storage-volume-div']/div/div[@class='hp-search-combo-spacer']/div/ol[contains(@class, 'hp-options')]/li/span[text()='%s']"   # replace %s with volume's name
            ID_INPUT_NEW_VOLUME_NAME = "xpath=//*[@id='cic-profile-storage-volume-name']"
            ID_ERR_MSG_NEW_VOLUME_NAME = "xpath=//*[@id='cic-profile-storage-volume-name-li']/div/div/label[@class='hp-error' and @for='cic-profile-storage-volume-name']"
            ID_INPUT_NEW_VOLUME_DESCRIPTION = "xpath=//*[@id='cic-profile-storage-volume-description']"
            ID_INPUT_BOOT_FALSE = "xpath=//*[@id='cic-profile-storage-boot-toggle-hpToggle']//li[@class='hp-on']"
            ID_INPUT_BOOT_TRUE = "xpath=//*[@id='cic-profile-storage-boot-toggle-hpToggle']//li[@class='hp-off']"
            ID_RADIO_LUN_AUTO = "xpath=//*[@id='cic-profile-storage-lun-auto']"
            ID_RADIO_LUN_MANUAL = "xpath=//*[@id='cic-profile-storage-lun-manual']"
            ID_INPUT_LUN_MANUAL = "xpath=//*[@id='cic-profile-storage-lun-manual-value']"
            ID_ERR_MSG_LUN_MANUAL = "xpath=//*[@id='cic-profile-storage-lun-section']/div/div/label[contains(@class, 'hp-error') and @for='cic-profile-storage-lun-manual-value']"
            ID_INPUT_NEW_VOLUME_STORAGE_POOL = "xpath=//*[@id='cic-profile-storage-pool-input']"
            ID_OPTION_NEW_VOLUME_STORAGE_POOL = "xpath=//form[@id='cic-profile-storage-dialog-form']//input[@id='cic-profile-storage-pool-input']/../div[@class='hp-search-combo-spacer']/div[@class='hp-search-combo-menu']/ol/li/span[contains(text(), '%s')]/../span[@class='hp-help' and text()='%s']"
            ID_INPUT_NEW_VOLUME_CAPACITY = "xpath=//*[@id='cic-profile-storage-volume-capacity']"
            ID_ERR_MSG_NEW_VOLUME_CAPACITY = "xpath=//*[@id='cic-profile-storage-capacity-div']/div/label[contains(@class, 'hp-error') and @for='cic-profile-storage-volume-capacity']"
            ID_SELECT_NEW_VOLUME_PROVISIONING = "cic-profile-storage-volume-provisioning"
            ID_CHECKBOX_NEW_VOLUME_PERMANENT = "xpath=//*[@id='cic-profile-storage-volume-permanent-input']"

            # ID_BUTTON_DELETE_VOLUME_BY_NAME = "xpath=//*[contains(@id, 'storageVolumeId-add') or contains(@id, 'storageVolumeId-edit')]/td/a[text()='%s']/../following-sibling::td/div[@class='hp-delete']"  # replace %s with volume name
            # format ID_BUTTON_DELETE_VOLUME_BY_NAME with volume name: ID_BUTTON_DELETE_VOLUME_BY_NAME.format(volume_name)
            ID_BUTTON_DELETE_VOLUME_BY_NAME = "xpath=//*[contains(@id, 'storageVolumeId-add') or contains(@id, 'storageVolumeId-edit') or contains(@id, 'storageVolumeId-copy')]/td/a[text()='{0}']/../following-sibling::td/div[@class='hp-delete']|//*[contains(@id, 'storageVolumeId-add') or contains(@id, 'storageVolumeId-edit') or contains(@id, 'storageVolumeId-copy')]/td[contains(text(), '{0}')]/following-sibling::td/div[@class='hp-delete']"
            ID_BUTTON_EDIT_VOLUME_BY_NAME = "xpath=//*[contains(@id, 'storageVolumeId-add') or contains(@id, 'storageVolumeId-edit') or contains(@id, 'storageVolumeId-copy')]/td/a[text()='%s']/../following-sibling::td/div[@class='hp-edit']"  # replace %s with volume name
            ID_CHECKBOX_ENABLE_STORAGE_PATH_BY_VOLUME_NAME_AND_NETWORK_NAME = "xpath=//*[contains(@id, 'storageVolumeId-add') or contains(@id, 'storageVolumeId-edit') or contains(@id, 'storageVolumeId-copy')]/td/a[text()='%s']/../../following-sibling::tr/td/div/table/tbody/tr/td/div/a[text()='%s']/../../following-sibling::td/input[@class='cic-profile-storage-enabled-checkbox']"  # replace (%s, %s) with (volume name, network name)
            ID_BUTTON_ADD = "xpath=//*[@id='cic-profile-storage-add']"
            ID_BUTTON_ADD_PLUS = "xpath=//*[@id='cic-profile-storage-addAgain']"
            ID_BUTTON_CANCEL = "xpath=//*[@id='cic-profile-storage-dialog-form']/footer/div/a[text()='Cancel']"
            ID_BUTTON_OK = ID_BUTTON_ADD
            ID_FORM_VOLUME = "cic-profile-storage-dialog-form"
            # format {0} with volume name: ID_TABLE_VOLUME.format(volume_name)
            ID_TABLE_VOLUME = "xpath=//*[contains(@id, 'storageVolumeId-edit') or contains(@id, 'storageVolumeId-add') or contains(@id, 'storageVolumeId-copy')]/td[contains(text(), '{0}')]|//*[contains(@id, 'storageVolumeId-edit') or contains(@id, 'storageVolumeId-add') or contains(@id, 'storageVolumeId-copy')]/td/a[text()='{0}']"
            ID_BUTTON_DELETE_CONFIRM = "xpath=//*[@class='hp-controls']/button[text()='Yes, delete']"

            ID_TEXT_VOLUME_NAME = "css=#storageVolumeId-show-%d.hp-expanded td a[href*='storage-volumes']"
            ID_TEXT_VOLUME_STORAGE_PERMANENT = "css=#storageVolumeId-show-%d.hp-expanded td div[style*='display']"
            ID_TEXT_VOLUME_LUN_ID = "xpath=//*[@id='storageVolumeId-show-%d']/td[text()='%s']"
            ID_TEXT_VOLUME_STORAGE_POOL = "css=#storageVolumeId-show-%d.hp-expanded td a[href*='storage-pools']"
            ID_TEXT_VOLUME_STORAGE_CAPACITY = "xpath=//*[@id='storageVolumeId-show-%d']/td[contains(text(),'%s')]"
            ID_TEXT_VOLUME_STORAGE_PROVISIONING = "xpath=//*[@id='storageVolumeId-show-%d']/td[contains(text(),'%s')]"
            ID_TEXT_VOLUME_STORAGE_SHARING = "xpath=//*[@id='storageVolumeId-show-%d']/td[contains(text(),'%s')]"
            ID_CHECKBOX_BOOT_BY_EXISTING_VOLUME_NAME = "xpath=//tr[contains(@id, 'storageVolumeId-add-1') or contains(@id, 'storageVolumeId-edit-1') or contains(@id, 'storageVolumeId-copy-1')]/td/div/a[text()='%s']/../../following-sibling::td/input[@class='cic-profile-add-volume-isBootable' or @class='cic-profile-edit-volume-isBootable' or @class='cic-profile-copy-volume-isBootable']"
            ID_CHECKBOX_BOOT_BY_NEW_VOLUME_NAME = "xpath=//tr[contains(@id, 'storageVolumeId-add') or contains(@id, 'storageVolumeId-edit') or contains(@id, 'storageVolumeId-copy')]/td[2][contains(text(),'%s')]/following-sibling::td/input[@class='cic-profile-add-volume-isBootable' or @class='cic-profile-edit-volume-isBootable' or @class='cic-profile-copy-volume-isBootable']"

            ID_TEXT_VOLUME_STORAGE_NETWORK = "xpath=//table[@id='storage-paths-table-%d-show-%d']/tbody/tr[%d]//a[contains(@href, 'fc-networks')]"
            ID_TEXT_VOLUME_STORAGE_NETWORK_STATUS = "xpath=//table[@id='storage-paths-table-%d-show-%d']/tbody/tr[%d]/td[contains(text(),'%s')]"
            ID_TABLE_SANStorage_DETAIL_INFO = "//tr[@id='storageVolumeId-show-%d']/td[@class='hp-icon']/div"

            class StoragePath(object):
                ID_DIALOG_ADD = "xpath=//*[@id='hp-body-div']/div[10]/div/div/div/header/h1[text()='Add Storage Path']"
                ID_DIALOG_EDIT = "xpath=//*[@id='profile-storage-edit-targets']"
                ID_BUTTON_EDIT_STORAGE_PATH_BY_NETWORK_NAME = "xpath=//*[@id='cic-profile-storage-paths-table']/tbody/tr/td/div/a[text()='%s']/../../following-sibling::td/div[@class='hp-edit']"  # replace %s with network's name
                ID_BUTTON_DELETE_STORAGE_PATH_BY_NETWORK_NAME = "xpath=//*[@id='cic-profile-storage-paths-table']/tbody/tr/td/div/a[text()='%s']/../../following-sibling::td/div[@class='hp-delete']"  # replace %s with network's name
                ID_CHECKBOX_ENABLE_STORAGE_PATH_BY_NETWORK_NAME = "xpath=//*[@id='cic-profile-storage-paths-table']/tbody/tr/td/div/a[text()='%s']/../../following-sibling::td/input[@class='cic-profile-storage-enabled-checkbox']"  # replace %s with network's name
                ID_BUTTON_ADD_STORAGE_PATH = "xpath=//*[@id='cic-profile-storage-paths-add']"
                ID_BUTTON_ADD_STORAGE_PATH_DISABLED = "xpath=//*[@id='cic-profile-storage-paths-add' and @disabled='disabled']"
                ID_BUTTON_REMOVE_ALL_STORAGE_PATH = "xpath=//*[@id='cic-profile-storage-paths-remove-all']"
                ID_RADIO_TARGET_PORT_ASSIGNMENT_AUTO = "xpath=//*[@id='profile-storage-edit-targets-auto']"
                ID_RADIO_TARGET_PORT_ASSIGNMENT_MANUAL = "xpath=//*[@id='profile-storage-edit-targets-manual']"
                # replace %s with port name, like '0:2:4', '1:2:4'
                ID_CHECKBOX_PORT_SELECTED_BY_PORT_NAME = "xpath=//*[@id='cic-profile-storage-targetports-table']/tbody/tr/td/div[text()='%s']/../preceding-sibling::td/input[@type='checkbox']"
                # ID_CHECKBOX_PORT_SELECTED_BY_PORT_NAME = "xpath=//*[@id='cic-profile-storage-targetports-table']/tbody/tr/td/div[text()='%s']/../preceding-sibling::td/input"
                ID_BUTTON_ADD = "xpath=//*[@id='hp-body-div']/div/div/div/div/form/div/div/button[text()='Add']"
                ID_BUTTON_ADD_PLUS = "xpath=//*[@id='hp-body-div']/div/div/div/div/form/div/div/button[text()='Add +']"
                ID_BUTTON_CANCEL_FOR_ADD_STORAGE_PATH = "xpath=//*[@id='hp-body-div']/div/div/div/div/form/div/div/button[text()='Cancel']"
                ID_BUTTON_OK = "xpath=//*[@id='profile-storage-edit-targets-add']"
                ID_BUTTON_CANCEL_FOR_EDIT_STORAGE_PATH = "xpath=//*[@id='profile-storage-edit-targets-form']/footer/div/button[text()='Cancel']"
                ID_INPUT_NETWORK_NAME_FOR_SEARCH = "xpath=//*[@id='hp-body-div']/descendant::input[@class='hp-search']"
                ID_OPTION_NETWORK_FOR_ADD_STORAGE_PATH = "xpath=//td[text()='%s']"  # replace %s with network name
                ID_FORM_EDIT_STORAGE_PATH = "profile-storage-edit-targets-form"

    class BootSettings(object):
        ID_CHECKBOX_MANAGE_BOOT_MODE = "xpath=//*[@id='cic-profile-add-manage-boot-mode']|//*[@id='cic-profile-edit-manage-boot-mode']|//*[@id='cic-profile-copy-manage-boot-mode']"
        ID_CHECKBOX_MANAGE_BOOT_ORDER = "xpath=//*[@id='cic-profile-add-manage-boot-order']|//*[@id='cic-profile-edit-manage-boot-order']|//*[@id='cic-profile-copy-manage-boot-order']"
        ID_SELECTBOX_ARROW_PXE_BOOT_POLICY = "xpath=//*[@id='cic-profile-add-pxe-boot-policy-container']/a/span[@class='selectBox-arrow']|//*[@id='cic-profile-edit-pxe-boot-policy-container']/a/span[@class='selectBox-arrow']|//*[@id='cic-profile-copy-pxe-boot-policy-container']/a/span[@class='selectBox-arrow']"
        ID_SELECT_PXE_BOOT_POLICY = "cic-profile-add-pxe-boot-policy|cic-profile-edit-pxe-boot-policy|cic-profile-copy-pxe-boot-policy"
        ID_SELECTBOX_ARROW_PRIMARY_BOOT_DEVICE = "xpath=//*[@id='cic-profile-add-boot-devices-div']/li/div/a/span[@class='selectBox-arrow']|//*[@id='cic-profile-edit-boot-devices-div']/li/div/a/span[@class='selectBox-arrow']|//*[@id='cic-profile-copy-boot-devices-div']/li/div/a/span[@class='selectBox-arrow']"
        ID_SELECT_PRIMARY_BOOT_DEVICE = "cic-profile-add-primary-boot-device|cic-profile-edit-primary-boot-device|cic-profile-copy-primary-boot-device"
        # ID_SELECT_BOOT_MODE = "xpath=//*[@id='cic-profile-add-boot-mode-select-container']/div/div/div"
        ID_SELECT_BOOT_MODE = "cic-profile-add-boot-mode-select|cic-profile-edit-boot-mode-select|cic-profile-copy-boot-mode-select"
        # ID_SELECT_BOOT_MODE_BY_TEXT = "xpath=//*[@id='cic-profile-add-boot-mode-select-container']/div/div/ol/li/span[text()='%s']"  # replace %s with 'UEFI/Legacy BIOS'
        # ID_SELECT_BOOT_MODE_SELECT_MODE = "xpath=//*[@id='cic-profile-add-boot-mode-select-container']/div/div/ol/li/span[text()='Select mode']"
        # ID_SELECT_BOOT_MODE_UEFI = "xpath=//*[@id='cic-profile-add-boot-mode-select-container']/div/div/ol/li/span[text()='UEFI']"
        # ID_SELECT_BOOT_MODE_UEFI_OPTIMIZED = "xpath=//*[@id='cic-profile-add-boot-mode-select-container']/div/div/ol/li/span[text()='UEFI optimized']"
        # ID_SELECT_BOOT_MODE_LEGACY_BIOS = "xpath=//*[@id='cic-profile-add-boot-mode-select-container']/div/div/ol/li/span[text()='Legacy BIOS']"
        ID_ERR_BOOT_MODE_IS_BLANK = "xpath=//*[@id='cic-profile-add-boot-mode-select-container']/label[@class='hp-error' and @for='cic-profile-add-boot-mode-select']|//*[@id='cic-profile-edit-boot-mode-select-container']/label[@class='hp-error' and @for='cic-profile-edit-boot-mode-select']|//*[@id='cic-profile-copy-boot-mode-select-container']/label[@class='hp-error' and @for='cic-profile-copy-boot-mode-select']"
        ID_DIALOG_WARNING = "xpath=//*/header//*[text()='Warning']/../../..//*[@id='cic-profile-reset-confirm-details']"
        ID_DIALOG_WARNING_FOR_UNCHECKING_MANAGE_BOOT_MODE = ID_DIALOG_WARNING + "[contains(text(), 'Unchecking the boot mode')]"
        ID_DIALOG_WARNING_FOR_UNCHECKING_MANAGE_BOOT_ORDER = ID_DIALOG_WARNING + "[contains(text(), 'Unchecking the boot order')]"
        ID_BUTTON_OK_FOR_WARNING = "xpath=//*[@id='cic-profile-reset-ok']"
        ID_BUTTON_CANCEL_FOR_WARNING = "xpath=//*[@id='cic-profile-reset-cancel']"
        ID_TEXT_BOOT_ORDER = "xpath=//*[@id='cic-profile-show-boot-order']"
        ID_TEXT_PXE_BOOT_POLICY = "xpath=//*[@id='cic-profile-show-boot-pxe']"
        ID_TEXT_BOOT_MODE = "xpath=//*[@id='cic-profile-show-boot-mode']"

    class BIOSSettings(object):
        ID_RADIO_INCONSISTENT = "xpath=//*[@id='cic-profile-bios-list-inconsistent']"
        ID_RADIO_MODIFIED = "xpath=//*[@id='cic-profile-bios-list-modified']"
        ID_RADIO_ALL = "xpath=//*[@id='cic-profile-bios-list-all']"
        ID_LABEL_BIOS_SETTINGS = "xpath=//*[@id='cic-profile-panel-details-bios']//span['BIOS Settings']"
        ID_LINK_BIOS_SETTINGS_EDIT = "xpath=//*[@id='cic-profile-panel-details-bios']/label/a[text()='Edit']"
        ID_TEXT_BIOS_SETTINGS_EXPECTED = "xpath=//*[@id='cic-profile-bios-setting-value-%s']"
        ID_SELECT_BIOS_SETTING = "id=bip-%s"
        ID_INPUT_BIOS_SETTING = "id=bip-%s"
        ID_TEXT_BIOS_SETTINGS_NAME = "xpath=//*[@id='cic-profile-bios-setting-name-%s']"
        ID_TEXT_BIOS_SETTINGS_ACTUAL = "xpath=//*[@id='cic-profile-bios-setting-container-%s']/td[@class='template-bios-setting-actual']"
        ID_LABEL_DIALOG_EDIT_BIOS_SETTINGS_TITLE = "xpath=//*[@id='hp-body-div']//span[text()='Edit BIOS Settings']"
        ID_INPUT_TEXT_EDIT_BIOS_SETTINGS = "xpath=//*[@id='bip-%s']"
        ID_BUTTON_OK_EDIT_BIOS_SETTINGS = "xpath=//*[@id='cic-profile-bios-ok']"
        ID_BUTTON_CANCEL_EDIT_BIOS_SETTINGS = "xpath=//*[@id='cic-profile-bios-cancel']"
        ID_CHECKBOX_MANAGE_BIOS_SETTINGS = "xpath=//*[@id='cic-profile-manage-bios']"
        ID_BUTTON_EDIT_BIOS_SETTINGS = "xpath=//*[@id='cic-edit-bios']"

    class Advanced(object):
        ID_TEXT_ISCSI_INITIATOR_NAME = "id=cic-profile-initiatorNameType-summary"
        ID_TEXT_UUID_DISPLAY_INFO = "xpath=//div[@id='cic-profile-serialNumberMode-summary']"
        ID_TEXT_MAC_MODE_DISPLAY_INFO = "xpath=//div[@id='cic-profile-macMode-summary']"
        ID_TEXT_WWN_MODE_DISPLAY_INFO = "xpath=//div[@id='cic-profile-wwnMode-summary']"
        ID_TEXT_HIDE_UNUSED_FLEXNICS_DISPLAY_INFO = "xpath=//div[@id='cic-profile-hideUnusedFlexNics-summary']"


class CreateServerProfilesElements(object):
    ID_BUTTON_CREATE_PROFILE = "link=Create profile"
    ID_SELECT_ACTION_CREATE = "xpath=//*[@id='cic-profile-actions']/div/ol/li/a[text()='Create']"

    ID_DIALOG_CREATE_SERVER_PROFILE = "//section[@class='hp-details-add-section']"
    ID_INPUT_NAME = "xpath=//*[@id='cic-profile-add-name']"
    ID_INPUT_SERVER_PROF_TEMP = "id=cic-profile-add-template-input"
    ID_OPTION_SERVER_PROF_TEMP = "xpath=//div[@class='hp-search-combo-spacer']//span[text()='%s']"
    ID_INPUT_DESCRIPTION = "xpath=//*[@id='cic-profile-add-description']"
    ID_INPUT_SERVER_HARDWARE = "xpath=//*[@id='cic-profile-add-server-input']"
    # ID_OPTION_SERVER_HARDWARE = "xpath=//*[@id='cic-profile-panel-add-basic']/fieldset/descendant::span[text()='%s']"
    ID_OPTION_SERVER_HARDWARE = "xpath=//*[@id='cic-profile-panel-add-basic']/fieldset/ol/li[5]//div/ol[@class='hp-search-combo-scroller hp-options']/li/span[contains(text(),'%s')]"
    ID_SEARCH_COMBO_SERVER_HARDWARE = "xpath=//*[@id='cic-profile-add-server-input']/../div[@class='hp-search-combo-control']"
    # ID_LABEL_SERVER_HARDWARE_POWER_ERR = "xpath=//*[@id='cic-profile-panel-add-basic']/fieldset/descendant::span[text()='%s']/following-sibling::span[text()='Powered on']"
    ID_LABEL_SERVER_HARDWARE_POWER_ERR = "xpath=//*[@id='cic-profile-add-panels']//fieldset/descendant::li[@name='%s']//span[contains(text(),'Powered on')]"
    # ID_TEXT_SERVER_HARDWARE_TYPE_LIST = "xpath=//*[@id='cic-profile-panel-add-basic']/fieldset/descendant::span/following-sibling::span"
    ID_TEXT_SERVER_HARDWARE_TYPE_LIST = "xpath=//*[@id='cic-profile-add-server-input']/following-sibling::*/descendant::span/following-sibling::span"
    # ID_TEXT_SERVER_HARDWARE_TYPE_LISTED = "xpath=//*[@id='cic-profile-panel-add-basic']/fieldset/descendant::span[text()='%s']/following-sibling::span"
    ID_TEXT_SERVER_HARDWARE_TYPE_LISTED = "xpath=//*[@id='cic-profile-panel-add-basic']/fieldset/descendant::ol[@class='hp-search-combo-scroller hp-options']/li[@name='%s']"
    ID_TEXT_SERVER_HARDWARE_TYPE_SELECTED = "xpath=//*[@id='cic-profile-add-server-type']"
    ID_ERR_SERVER_HARDWARE_INVALID = "xpath=//*[@for='cic-profile-add-server-input']"
    ID_ERR_SERVER_HARDWARE_POWERED_ON = "xpath=//*[@for='cic-profile-server-power-validator']"
    ID_LINK_POWER_OFF_SERVER_HARDWARE = "xpath=//*[@id='cic-profile-server-power-validator-link']"
    ID_BUTTON_MOMENTARY_PRESS = "xpath=//*[@id='cic-server-momentary-press']"
    ID_BUTTON_PRESS_AND_HOLD = "xpath=//*[@id='cic-server-press-and-hold']"
    ID_DIALOG_POWER_OFF_SERVER_HARDWARE = "xpath=//*[@class='hp-dialog']"
    ID_TEXT_SERVER_HARDWARE_SELECTED = "xpath=//*[@id='cic-profile-add-server']/option"
    ID_TEXT_ENCLOSURE_GROUP_SELECTED = "xpath=//*[@id='cic-profile-add-enclosure-group' or @id='cic-profile-edit-enclosure-group']"

    ID_INPUT_SERVER_HARDWARE_TYPE = "xpath=//*[@id='cic-profile-add-server-type-input']"
    # ID_OPTION_SERVER_HARDWARE_TYPE = "xpath=//input[@id='cic-profile-add-server-type-input']/following-sibling::div[contains(@class, 'hp-search-combo-menu')]/ol[contains(@class, 'hp-search-combo-scroller hp-options')]/li/span[text()='%s']"
    ID_OPTION_SERVER_HARDWARE_TYPE = "xpath=//input[@id='cic-profile-add-server-type-input']/following-sibling::div//ol/li/span[text()='%s']"  # replace %s with server hardware type
    ID_ERR_SERVER_HARDWARE_TYPE_INVALID = "xpath=//*[@for='cic-profile-add-server-type-input']"

    ID_INPUT_ENCLOSURE_GROUP = "xpath=//*[@id='cic-profile-add-enclosure-group-input']"
    ID_OPTION_ENCLOSURE_GROUP = "xpath=//*[@id='cic-profile-add-enclosure-group-input']/following-sibling::div//ol/li/span[text()='%s']"  # replace %s with enclosure group
    ID_ERR_ENCLOSURE_GROUP_INVALID = "xpath=//*[@for='cic-profile-add-enclosure-group-input']"

    ID_SELECT_AFFINITY = "cic-profile-add-affinity"
    # ID_SELECT_AFFINITY = "xpath=//*[@for='cic-profile-add-affinity']/following-sibling::div[@class='hp-select-form']/div[contains(@class, 'hp-select')]/div[@class='hp-value']"
    # ID_SELECT_AFFINITY_BY_TEXT = "xpath=//*[@for='cic-profile-add-affinity']/following-sibling::div[@class='hp-select-form']/descendant::span[text()='%s']"  # 'Device bay' or 'Device bay + server hardware'
    ID_CREATION_ERROR = "xpath=//*[@id='hp-form-message']/div[@class='hp-form-message-details']/div/div[@class='hp-details']"
    ID_UPDATE_ERROR = "xpath=.//*[@id='hp-form-message']/div[@class='hp-form-message-details']//div[@class='hp-resolution-container']/span/p/span"

    class Advanced(object):
        # TODO: move Advanced class into GeneralServerProfilesElements by using '|' to merge '-add-' and '-edit-'
        # TODO: for maintaining 1 xpath for 1 element for both Create/Add and Edit page
        ID_RADIO_ISCSI_INITIATOR_NAME_VIRTUAL = "id=cic-profile-add-advanced-initiator-name-virtual"
        ID_RADIO_ISCSI_INITIATOR_NAME_USER_SPECIFIED = "id=cic-profile-add-advanced-initiator-name-user-specified"
        ID_INPUT_USER_SPECIFIED_ISCSI_INITIATOR_NAME = "id=cic-profile-add-advanced-initiator-name-iscsiInitiatorName"
        ID_TEXT_ERROR_ISCSI_INITIATOR_NAME = "xpath=//*[@id='cic-profile-add-advanced-initiator-name-group']/li/div/label[contains(@class, 'hp-error') and @for='cic-profile-add-advanced-initiator-name-iscsiInitiatorName']"
        ID_RADIO_MAC_ADDRESSES_VIRTUAL = "xpath=//*[@id='cic-profile-advanced-mac-virtual']"
        ID_RADIO_MAC_ADDRESSES_PHYSICAL = "xpath=//*[@id='cic-profile-advanced-mac-physical']"
        ID_RADIO_WWN_ADDRESSES_VIRTUAL = "xpath=//*[@id='cic-profile-advanced-wwn-virtual']"
        ID_RADIO_WWN_ADDRESSES_PHYSICAL = "xpath=//*[@id='cic-profile-advanced-wwn-physical']"
        ID_RADIO_SERIAL_NUMBER_UUID_VIRTUAL = "xpath=//*[@id='cic-profile-advanced-sntype-virtual']"
        ID_RADIO_SERIAL_NUMBER_UUID_PHYSICAL = "xpath=//*[@id='cic-profile-advanced-sntype-physical']"
        ID_RADIO_SERIAL_NUMBER_UUID_USER_SPECIFIED = "xpath=//*[@id='cic-profile-advanced-sntype-user-specified']"
        ID_INPUT_USER_SPECIFIED_SERIAL_NUMBER = "xpath=//*[@id='cic-profile-advanced-sntype-serialNumber']"
        ID_INPUT_USER_SPECIFIED_UUID = "xpath=//*[@id='cic-profile-advanced-sntype-uuid']"
        ID_RADIO_HIDE_UNUSED_FLEXNICS_YES = "xpath=//*[@id='cic-profile-add-advanced-hide-unused-flexnics-true']"
        ID_RADIO_HIDE_UNUSED_FLEXNICS_NO = "xpath=//*[@id='cic-profile-add-advanced-hide-unused-flexnics-false']"

    ID_BUTTON_CREATE = "xpath=//*[@id='cic-profile-create']"
    ID_BUTTON_CREATE_PLUS = "xpath=//*[@id='cic-profile-createAgain']"
    ID_BUTTON_CANCEL = "xpath=//*[@id='cic-profile-add-cancel']"
    ID_ERROR_SAVE_CREATE = "css=div.hp-details,div.hp-details span"

    ID_DIALOG_TITLE = "xpath=//*[@data-localize='profiles.add.title']"


class EditServerProfilesElements(object):
    ID_SELECT_ACTION_EDIT = "xpath=//*[@id='cic-profile-actions']/div/ol/li/a[text()='Edit']"

    ID_LINK_EDIT_GENERAL_FROM_PANE = "xpath=//*[@id='cic-profile-edit-summary-pane']"
    ID_LINK_EDIT_GENERAL_FROM_VIEW = "xpath=//*[@id='cic-profile-panel-details-summary']/label/a"
    ID_LINK_EDIT_FIRMWARE_FROM_PANE = "xpath=//*[@id='cic-profile-edit-firmware-pane']"
    ID_LINK_EDIT_FIRMWARE_FROM_VIEW = "xpath=//*[@id='cic-profile-panel-details-firmware']/label/a"
    ID_LINK_EDIT_CONNECTIONS_FROM_PANE = "xpath=//*[@id='cic-profile-edit-connections-pane']"
    ID_LINK_EDIT_CONNECTIONS_FROM_VIEW = "xpath=//*[@id='cic-profile-panel-details-connections']/label/a"
    ID_LINK_EDIT_SAN_STORAGE_FROM_PANE = "xpath=//*[@id='cic-profile-show-overview-sanstorage']/div/header/a"
    ID_LINK_EDIT_SAN_STORAGE_FROM_VIEW = "xpath=//*[@id='cic-profile-panel-details-storages']/label/a"
    ID_LINK_EDIT_LOCAL_STORAGE_FROM_PANE = "xpath=//*[@id='cic-profile-show-overview-localstorage']/div/header/a"
    ID_LINK_EDIT_LOCAL_STORAGE_FROM_VIEW = "xpath=//*[@id='cic-profile-panel-details-local-storage']/label/a"
    ID_LINK_EDIT_BIOS_SETTINGS_FROM_PANE = "xpath=//*[@id='cic-profile-show-overview-bios']/div/header/a"
    ID_LINK_EDIT_BIOS_SETTINGS_FROM_VIEW = "xpath=//*[@id='cic-profile-panel-details-bios']/label/a"
    ID_LINK_EDIT_BOOT_SETTINGS_FROM_VIEW = "xpath=//*[@id='cic-profile-panel-details-boot-order']/label/a"
    ID_DIAGLOG_REASSIGN_SERVER_HARDWARE = "xpath=//*[@id='hp-body-div']//div[@class='hp-prompt' and contains(text(), 'Reassign server hardware')]"
    ID_SELECT_SERVER_HARDWARE_DROPDOWN = "xpath=//*[@id='cic-profile-panel-edit-basic']//span[@class='hp-name' and contains(text(), '%s')]"
    ID_BUTTON_YES_REASSIGN_HARDWARE = "xpath=//*[@id='hp-body-div']//button[@class='hp-ok' and contains(text(), 'Yes')]"
    ID_BUTTON_CANCEL_REASSIGN_HARDWARE = "xpath=//*[@id='hp-body-div']//button[@class='hp-cancel' and contains(text(), 'Cancel')]"
    ID_DIALOG_EDIT_SERVER_PROFILE = "//div[@class='hp-details-edit-section']"

    ID_INPUT_NAME = "xpath=//*[@id='cic-profile-edit-name']"
    ID_INPUT_DESCRIPTION = "xpath=//*[@id='cic-profile-edit-description']"
    ID_INPUT_SERVER_HARDWARE = "xpath=//*[@id='cic-profile-edit-server-input']"
    ID_OPTION_SERVER_HARDWARE = "xpath=//div[@class='hp-search-combo-spacer']//span[text()='%s']"
    ID_SEARCH_COMBO_SERVER_HARDWARE = "xpath=//*[@id='cic-profile-edit-server-input']/../div[@class='hp-search-combo-control']"
    ID_LABEL_SERVER_HARDWARE_POWER_ERR = "xpath=//*[@id='cic-profile-edit-panels']//fieldset/descendant::li[@name='%s']//span[contains(text(),'Powered on')]"
    ID_TEXT_SERVER_HARDWARE_TYPE_LISTED = "xpath=//*[@id='cic-profile-panel-edit-basic']/fieldset/descendant::span[text()='%s']/following-sibling::span"
    ID_TEXT_SERVER_HARDWARE_TYPE_SELECTED = "xpath=//*[@id='cic-profile-edit-server-type']"
    ID_TEXT_SERVER_HARDWARE_SELECTED = "xpath=//*[@id='cic-profile-edit-server']/option"
    ID_TEXT_ENCLOSURE_GROUP_SELECTED = "xpath=//*[@id='cic-profile-edit-enclosure-group']"
    ID_ERR_SERVER_HARDWARE_INVALID = "xpath=//*[@for='cic-profile-edit-server-input']"
    ID_ERR_SERVER_HARDWARE_POWERED_ON = "xpath=//*[@id='cic-profile-edit-server-power-link']"
    ID_LINK_POWER_OFF_SERVER_HARDWARE = "xpath=//*[@id='cic-profile-server-power-validator-link']"
    ID_BUTTON_MOMENTARY_PRESS = "xpath=//*[@id='cic-server-momentary-press']"
    ID_BUTTON_PRESS_AND_HOLD = "xpath=//*[@id='cic-server-press-and-hold']"
    ID_DIALOG_POWER_OFF_SERVER_HARDWARE = "xpath=//*[@class='hp-dialog']"
    ID_SELECT_AFFINITY = "cic-profile-edit-affinity"

    # class BootSettings(object):
    #     ID_CHECKBOX_MANAGE_BOOT_MODE = "xpath=//*[@id='cic-profile-edit-manage-boot-mode']"
    #     ID_CHECKBOX_MANAGE_BOOT_ORDER = "xpath=//*[@id='cic-profile-edit-manage-boot-order']"
    #     ID_SELECTBOX_ARROW_PXE_BOOT_POLICY = "xpath=//*[@id='cic-profile-edit-pxe-boot-policy-container']/a/span[@class='selectBox-arrow']"
    #     ID_SELECT_PXE_BOOT_POLICY = "id=cic-profile-edit-pxe-boot-policy"
    #     ID_SELECTBOX_ARROW_PRIMARY_BOOT_DEVICE = "xpath=//*[@id='cic-profile-edit-boot-devices-div']/li/div/a/span[@class='selectBox-arrow']"
    #     ID_SELECT_PRIMARY_BOOT_DEVICE = "id=cic-profile-edit-primary-boot-device"
    # ID_SELECT_BOOT_MODE = "xpath=//*[@id='cic-profile-edit-boot-mode-select-container']/div/div/div"
    #     ID_SELECT_BOOT_MODE = "cic-profile-edit-boot-mode-select"
    # ID_SELECT_BOOT_MODE_BY_TEXT = "xpath=//*[@id='cic-profile-edit-boot-mode-select-container']/div/div/ol/li/span[text()='%s']"  # replace %s with 'UEFI/Legacy BIOS'
    # ID_SELECT_BOOT_MODE_SELECT_MODE = "xpath=//*[@id='cic-profile-edit-boot-mode-select-container']/div/div/ol/li/span[text()='Select mode']"
    # ID_SELECT_BOOT_MODE_UEFI = "xpath=//*[@id='cic-profile-edit-boot-mode-select-container']/div/div/ol/li/span[text()='UEFI']"
    # ID_SELECT_BOOT_MODE_UEFI_OPTIMIZED = "xpath=//*[@id='cic-profile-edit-boot-mode-select-container']/div/div/ol/li/span[text()='UEFI optimized']"
    # ID_SELECT_BOOT_MODE_LEGACY_BIOS = "xpath=//*[@id='cic-profile-edit-boot-mode-select-container']/div/div/ol/li/span[text()='Legacy BIOS']"
    #     ID_ERR_BOOT_MODE_IS_BLANK = "xpath=//*[@id='cic-profile-edit-boot-mode-select-container']/label[@class='hp-error' and @for='cic-profile-edit-boot-mode-select']"
    #
    class ChangeServerHardwareTypeAndEnclosureGroup(object):

        ID_LINK_CHANGE_SERVER_HARDWARE_TYPE_AND_EG = "xpath=//*[@id='cic-profile-edit-changesht']"
        ID_DIALOG_CHANGE_SERVER_HARDWARE_TYPE_AND_ENCLOSURE_GROUP = "xpath=//*[@id='cic-profile-changeshtenclosuregroup-form']/../../div"
        ID_INPUT_SERVER_HARDWARE_TYPE = "xpath=//*[@id='cic-profile-edit-select-server-type-input']"
        # replace below %s with exact Server Hardware Type like 'BL460c Gen8 1', including 1 or 2
        ID_OPTION_SERVER_HARDWARE_TYPE = "xpath=//*[@id='cic-profile-changeshtenclosuregroup-form']//div//span[text()='%s']"
        ID_INPUT_ENCLOSURE_GROUP = "xpath=//*[@id='cic-profile-edit-select-enclosure-group-input']"
        # replace below %s with Enclosure Group
        ID_OPTION_ENCLOSURE_GROUP = "xpath=//*[@id='cic-profile-edit-select-enclosure-group-div']//span[text()='%s']"
        ID_BUTTON_OK = "xpath=//*[@id='cic-profile-changeshtenclosuregroup-form']/footer/div/button[text()='OK']"
        ID_BUTTON_CANCEL = "xpath=//*[@id='profiles-chgshtenclosurgroupbutton']"
        ID_POPUP_CONFIRM = "xpath=//div[@class='hp-form-confirmation']"
        ID_CHECKBOX_CONFIRM = "xpath=//input[@id='cic-sht-eg-confirm-checkbox']"
        ID_BUTTON_YES_CHANGE = "xpath=//input[@id='cic-sht-eg-confirm-ok']"
        ID_BUTTON_CONFIRM_CANCEL = "xpath=//input[@id='cic-sht-eg-confirm-ok']"

    class Advanced(object):
        # TODO: move Advanced class into GeneralServerProfilesElements by using '|' to merge '-add-' and '-edit-'
        # TODO: for maintaining 1 xpath for 1 element for both Create/Add and Edit page
        # for editing server profile, there's NO 'MAC address/WWN address/Serial number UUID' options available to change,
        # only 'Hide Unused FlexNICs' option for user to change
        ID_RADIO_ISCSI_INITIATOR_NAME_VIRTUAL = "id=cic-profile-edit-advanced-initiator-name-virtual"
        ID_RADIO_ISCSI_INITIATOR_NAME_USER_SPECIFIED = "id=cic-profile-edit-advanced-initiator-name-user-specified"
        ID_INPUT_USER_SPECIFIED_ISCSI_INITIATOR_NAME = "id=cic-profile-edit-advanced-initiator-name-iscsiInitiatorName"
        ID_RADIO_HIDE_UNUSED_FLEXNICS_YES = "xpath=//*[@id='cic-profile-edit-advanced-hide-unused-flexnics-true']"
        ID_RADIO_HIDE_UNUSED_FLEXNICS_NO = "xpath=//*[@id='cic-profile-edit-advanced-hide-unused-flexnics-false']"

    ID_BUTTON_OK = "xpath=//*[@id='cic-profile-edit-ok']"
    ID_BUTTON_CANCEL = "xpath=//*[@id='cic-profile-edit-cancel']"
    ID_ERROR_SAVE_EDIT = "css=div.hp-details,div.hp-details span"


class CopyServerProfilesElements(object):
    ID_SELECT_ACTION_COPY = "xpath=//*[@id='cic-profile-actions']/div/ol/li/a[text()='Copy']"
    # ID_SELECT_ACTION_COPY = "xpath=//*[@id='cic-profile-copy-action']"

    ID_DIALOG_COPY_SERVER_PROFILE = "//section[@class='hp-details-add-section']"

    ID_INPUT_NAME = "xpath=//*[@id='cic-profile-copy-name']"
    ID_INPUT_DESCRIPTION = "xpath=//*[@id='cic-profile-copy-description']"
    ID_INPUT_SERVER_HARDWARE = "xpath=//*[@id='cic-profile-copy-server-input']"
    ID_OPTION_SERVER_HARDWARE = "xpath=//*[@id='cic-profile-copy-panel-basic']/fieldset/ol/li[4]//div/ol[@class='hp-search-combo-scroller hp-options']/li/span[contains(text(),'%s')]"
    ID_LABEL_SERVER_HARDWARE_POWER_ERR = "xpath=//*[@id='cic-profile-copy-panels']//fieldset/descendant::li[@name='%s']//span[contains(text(),'Powered on')]"
    # ID_TEXT_SERVER_HARDWARE_TYPE_LISTED = "xpath=//*[@id='cic-profile-panel-edit-basic']/fieldset/descendant::span[text()='%s']/following-sibling::span"
    ID_TEXT_SERVER_HARDWARE_TYPE_SELECTED = "xpath=//*[@id='cic-profile-copy-server-type']"
    ID_ERR_SERVER_HARDWARE_INVALID = "xpath=//*[@for='cic-profile-copy-server-input']"
    ID_ERR_SERVER_HARDWARE_POWERED_ON = "xpath=//*[@for='cic-profile-server-power-validator']"
    ID_LINK_POWER_OFF_SERVER_HARDWARE = "xpath=//*[@id='cic-profile-server-power-validator-link']"
    ID_TEXT_SERVER_HARDWARE_SELECTED = "xpath=//*[@id='cic-profile-copy-server']/option"
    ID_TEXT_ENCLOSURE_GROUP_SELECTED = "xpath=//*[@id='cic-profile-copy-enclosure-group']"

    # ID_ERR_SERVER_HARDWARE_POWERED_ON = "xpath=//*[@for='cic-profile-server-power-validator']"
    # ID_LINK_POWER_OFF_SERVER_HARDWARE = "xpath=//*[@id='cic-profile-server-power-validator-link']"

    ID_BUTTON_MOMENTARY_PRESS = "xpath=//*[@id='cic-server-momentary-press']"
    ID_BUTTON_PRESS_AND_HOLD = "xpath=//*[@id='cic-server-press-and-hold']"
    ID_DIALOG_POWER_OFF_SERVER_HARDWARE = "xpath=//*[@class='hp-dialog']"
    ID_SELECT_AFFINITY = "cic-profile-copy-affinity"

    class Advanced(object):
        ID_RADIO_ISCSI_INITIATOR_NAME_VIRTUAL = "id=cic-profile-copy-advanced-initiator-name-virtual"
        ID_RADIO_ISCSI_INITIATOR_NAME_USER_SPECIFIED = "id=cic-profile-copy-advanced-initiator-name-user-specified"
        ID_INPUT_USER_SPECIFIED_ISCSI_INITIATOR_NAME = "id=cic-profile-copy-advanced-initiator-name-iscsiInitiatorName"
        ID_RADIO_MAC_ADDRESSES_VIRTUAL = "xpath=//*[@id='cic-profile-advanced-mac-virtual']"
        ID_RADIO_MAC_ADDRESSES_PHYSICAL = "xpath=//*[@id='cic-profile-advanced-mac-physical']"
        ID_RADIO_WWN_ADDRESSES_VIRTUAL = "xpath=//*[@id='cic-profile-advanced-wwn-virtual']"
        ID_RADIO_WWN_ADDRESSES_PHYSICAL = "xpath=//*[@id='cic-profile-advanced-wwn-physical']"
        ID_RADIO_SERIAL_NUMBER_UUID_VIRTUAL = "xpath=//*[@id='cic-profile-advanced-sntype-virtual']"
        ID_RADIO_SERIAL_NUMBER_UUID_PHYSICAL = "xpath=//*[@id='cic-profile-advanced-sntype-physical']"
        ID_RADIO_SERIAL_NUMBER_UUID_USER_SPECIFIED = "xpath=//*[@id='cic-profile-advanced-sntype-user-specified']"
        ID_RADIO_HIDE_UNUSED_FLEXNICS_YES = "xpath=//*[@id='cic-profile-copy-advanced-hide-unused-flexnics-true']"
        ID_RADIO_HIDE_UNUSED_FLEXNICS_NO = "xpath=//*[@id='cic-profile-copy-advanced-hide-unused-flexnics-false']"

    ID_BUTTON_CREATE = "xpath=//*[@id='cic-profile-create']"
    ID_BUTTON_CREATE_PLUS = "xpath=//*[@id='cic-profile-createAgain']"
    ID_BUTTON_CANCEL = "xpath=//*[@id='cic-profile-copy-cancel']"


class DeleteServerProfilesElements(object):
    ID_SELECT_ACTION_DELETE = "xpath=//*[@id='cic-profile-actions']/div/ol/li/a[text()='Delete']"

    ID_CHECKBOX_FORCE_DELETE = "xpath=//*[@id='cic-profile-force-delete']"
    ID_BUTTON_YES_DELETE = "xpath=//button[@class='hp-ok hp-primary' and @data-localize='profiles.delete.ok']"
    ID_BUTTON_CANCEL = "xpath=//button[@class='hp-cancel' and @data-localize='core.details.cancel']"
    ID_LABEL_PROFILE_NAME = "xpath=//*[@id='cic-profile-delete-name']"
    ID_DIALOG_DELETE_SERVER_PROFILE = "xpath=//*[@id='cic-profile-delete-form']/../../div"
    # ID_DIALOG_DELETE_SERVER_PROFILE = "xpath=//*[@id='cic-profile-delete-ok']"


class PowerOnServerProfilesElements(object):
    ID_SELECT_ACTION_POWER_ON = "xpath=//*[@id='cic-server-power-on-action']"


class PowerOffServerProfilesElements(object):
    ID_SELECT_ACTION_POWER_OFF = "xpath=//*[@id='cic-server-power-off-action']"
    ID_BUTTON_MOMENTARY_PRESS = "xpath=//*[@id='cic-server-momentary-press']"
    ID_BUTTON_PRESS_AND_HOLD = "xpath=//*[@id='cic-server-press-and-hold']"
    ID_BUTTON_CLOSE = "xpath=//*[@id='cic-server-poweroff-cancel']"


class ResetServerProfilesElements(object):
    ID_SELECT_ACTION_RESET = "xpath=//*[@id='cic-server-reset-action']"
    ID_BUTTON_RESET = "xpath=//button[@id='cic-server-reset']"
    ID_BUTTON_COLD_BOOT = "xpath=//button[@id='cic-server-cold-boot']"
    ID_BUTTON_CANCEL = "xpath=//button[@id='cic-server-reset-cancel']"


class UpdateFromTemplateElements(object):
    ID_SELECT_ACTION_UPDATE_FROM_TEMPLATE = "xpath=//*[@id='cic-profile-actions']/div/ol/li/a[text()='Update from template']"


class ServerProfilesPage(object):
    ID_PAGE_LABEL = "xpath=//div[@class='hp-page-label']/h1[text()='Server Profiles']"
    ID_PAGE_LABEL_STORAGE_SYSTEM = "xpath=//div[@class='hp-page-label']/h1[text()='Storage Systems']"
    ID_PROFILE_LIST = "xpath=//div[@class='dataTables_scrollBody']/table"
    ID_PROFILE_CHANGING = ID_PROFILE_LIST + "/tbody/tr//div[@class='hp-status hp-changing']"
    ID_PROFILE_EDIT_COMPLETE = "//header[@class='hp-notification-summary']/div[@class='hp-state' andtext()='Completed']"
    ID_PROFILE_EDIT_INPROCESS = "//header[@class='hp-notification-summary']/div[@class='hp-state']/div[@class-'hp-progress']"
    ID_PROFILE_EDIT_VERIFY = "id=hp-form-message"
    ID_PROFILE_LIST_NAMES = ID_PROFILE_LIST + '/tbody/tr/td[2]'
    # Create Server Profile
    ID_LABEL_HP_MAIN_MENU = "id=hp-main-menu-label"
    ID_LINK_CREATE_SERVER_PROFILES = "link=Create profile"
    ID_INPUT_SERVER_PROFILE_NAME = "id=cic-profile-add-name"
    ID_INPUT_SERVER_PROFILE_DESCRIPTION = "id=cic-profile-add-description"
    ID_INPUT_SERVER_HARDWARE_TYPE = "id=cic-profile-add-server-type-input"
    ID_BTN_CREATE_PLUS_SERVER_PROFILE = "id=cic-profile-createAgain"
    ID_BTN_CREATE_SERVER_PROFILE = "id=cic-profile-create"
    ID_BTN_CANCEL_SERVER_PROFILE = "id=cic-profile-add-cancel"
    ID_BTN_ADD_NETWORK_CONNECTION = "id=cic-networkset-add-networks"
    ID_CHKBOX_PROFILE_BOOT_LOADER = "id=cic-profile-add-boot-order"
    ID_LINK_SEARCH_FOR_ANOTHER = "link=Search for another"
    ID_COMPLETE_STATUS_PROFILE = "xpath=//span[@class='hp-value' and text()='ok']/../../following-sibling::td[text()='%s']"
    ID_RADIO_VIRTUAL_MAC = "id=cic-profile-advanced-mac-virtual"
    ID_RADIO_PHYSICAL_MAC = "id=cic-profile-advanced-mac-physical"
    ID_RADIO_PHYSICAL_WWN = "id=cic-profile-advanced-wwn-physical"
    ID_RADIO_VIRTUAL_WWN = "id=cic-profile-advanced-wwn-virtual"
    ID_RADIO_PHYSICAL_SERIAL = "id=cic-profile-advanced-sntype-physical"
    ID_RADIO_VIRTUAL_SERIAL = "id=cic-profile-advanced-sntype-virtual"
    ID_RADIO_USER_SPECIFIED_SERIAL = "id=cic-profile-advanced-sntype-user-specified"
    ID_INPUT_SERIAL_NUMBER = "id=cic-profile-advanced-sntype-serialNumber"
    ID_INPUT_UUID_NUMBER = "id=cic-profile-advanced-sntype-uuid"
    # Action Menu
    ID_NO_SERVER_PROFILE_MESSAGE = "xpath=//div[text()='No server profiles']"
    ID_MENU_MAIN_ACTION = "xpath=//label[text()='Actions']"
    # ID_MENU_ACTION_CREATE = "id=cic-profile-create-action"
    ID_MENU_ACTION_CREATE = "xpath = //li/a[text()='Create']"
    ID_MENU_ACTION_EDIT = "xpath = //li/a[text()='Edit']"
    ID_MENU_ACTION_COPY = "id=cic-profile-copy-action"
    ID_MENU_ACTION_POWERON = "id=cic-server-power-on-action"
    ID_MENU_ACTION_POWEROFF = "id=cic-server-power-off-action"
    ID_BTN_POWEROFF_MEMORY_PRESS = "id=cic-server-momentary-press"
    ID_BTN_POWEROFF_PRESS_HOLD = "id=cic-server-press-and-hold"
    ID_MENU_ACTION_RESET = "id=cic-server-reset-action"
    ID_BTN_RESET_COLD_BOOT = "id=cic-server-cold-boot"
    ID_BTN_RESET_RESET = "id=cic-server-reset"
    ID_BTN_RESET_CANCEL = "id=cic-server-reset-cancel"
    ID_MENU_ACTION_DELETE = "id=cic-profile-delete-action"
    ID_CHK_FORCE_DELETE = "cic-profile-force-delete"
    ID_BTN_CONFIRM_DELETE = "//button[@class='hp-ok hp-primary' and text()='Yes, delete']"
    ID_BTN_CONFIRM_CANCEL = "css=button.hp-cancel"
    # VIEW
    ID_COMBO_MENU_VIEW = "css=#cic-profile-panel-add-selector > div.hp-value"
    ID_LINK_OVERVIEW = "xpath=//div[@id='cic-profile-panel-selector']/div"
    ID_LINK_GENERAL = "link=General"
    ID_LINK_BOOTORDER = "link=Boot Order"
    ID_LINK_BIOS = "link=BIOS"
    ID_LINK_CONNECTIONS = "link=Connections"
    ID_LINK_ADVANCED = "link=Advanced"
    ID_LINK_RELATED = "link=Related"
    ID_INPUT_BOOT_ORDER_CD = "name=CD"
    ID_INPUT_BOOT_ORDER_FLOPPY = "name=Floppy"
    ID_INPUT_BOOT_ORDER_HARDDISK = "name=HardDisk"
    ID_INPUT_BOOT_ORDER_USB = "name=USB"
    ID_INPUT_BOOT_ORDER_PXE = "name=PXE"
    ID_CHKBOX_PROFILE_MANAGE_BIOS = "id=cic-profile-manage-bios"
    ID_RADIO_BTN_UUID_VIRTUAL = "id=cic-profile-advanced-uuid-virtual"
    ID_RADIO_BTN_UUID_PHYSICAL = "id=cic-profile-advanced-uuid-physical"
    ID_RADIO_BTN_MAC_VIRTUAL = "id=cic-profile-advanced-mac-physical"
    ID_RADIO_BTN_WWN_VIRTUAL = "id=cic-profile-advanced-wwn-physical"
    # Add Connection Page
    ID_COMBO_DEVICE_TYPE = "xpath=//label[text()='Device type']//following-sibling::div/a"
    ID_COMBO_SERVER_HARDWARE_DROPDOWN = "//input[@id='cic-profile-add-server-input']/following-sibling::div[2]"
    ID_COMBO_SERVER_HARDWARE_TYPE_DROPDOWN = "//input[@id='cic-profile-add-server-type-input']/following-sibling::div[2]"
    ID_COMBO_ENCLOSURE_GROUP_DROPDOWN = "//input[@id='cic-profile-add-enclosure-group-input']/following-sibling::div[2]"
    ID_COMBO_FLEXNIC_ADD_CONNECTION = "//select[@id='cic-profile-connection-flexnic']/preceding-sibling::a"
    ID_COMBO_CLICK_BUTTON = "xpath = .//*[@id='cic-profile-connections-dialog-form']/fieldset/ol[1]/li[4]/div/a/span[2]"
    ID_COMBO_BOOT_ADD_CONNECTION = "//select[@id='cic-profile-connection-boot']/preceding-sibling::a"
    ID_COMBO_NETWORK_ADD_CONNECTION = "//input[@id='cic-profile-connection-network-input']/following-sibling::div[2]"
    ID_INPUT_NETWORK_ADD_CONNECTION = "id=cic-profile-connection-network-input"
    ID_INPUT_REQUESTED_BW_ADD_CONNECTION = "id=cic-profile-connection-bandwidth"
    ID_BTN_ADD_NETWORK_ADD_CONNECTON = "id=cic-profile-connection-add"
    ID_BTN_ADD_NETWORK_ADD_PLUS_CONNECTON = "id=cic-profile-connection-addAgain"
    ID_BTN_CANCEL_NETWORK_ADD_CONNECTION = "css=button.hp-cancel"
    ID_ELEMENT_NETWORK_NAME_BASE = "xpath=//span[@class='hp-name' and text()='%s']"  # Replace %s with network name
    ID_ELEMENT_PROFILE_NAME_BASE = "xpath=//td[@class='' and text()='%s']"  # Replace %s with profile name
    ID_ELEMENT_MESSAGE_SERVER_PROFILE = "xpath=//span[@class='hp-form-message-text' and text()='Created server profile: %s']"  # replace %s with profile name
    ID_ELEMENT_DEVICE_TYPE_ETHERNET = "//a[contains(text(),'Ethernet')]"
    ID_ELEMENT_DEVICE_TYPE_FIBER_CHANNEL = "//a[contains(text(),'Fibre Channel')]"
    ID_LINK_DEVICE_TYPE_SEARCH_FOR_ANOTHER = "link=Search for another"
    ID_INPUT_FIBERCHANNEL_WWPN = "id=cic-profile-connection-wwpn"
    ID_INPUT_FIBERCHANNEL_WWNN = "id=cic-profile-connection-wwnn"
    ID_INPUT_FIBERCHANNEL_MAC = "id=cic-profile-connection-mac"
    ID_INPUT_FIBERCHANNEL_WWN_TARGET = "id=cic-profile-connection-wwnTarget"
    ID_INPUT_FIBERCHANNEL_LUN_TARGET = "id=cic-profile-connection-lunTarget"
    ID_RADIO_SPECIFIY_BOOT_TARGET = "id=cic-profile-connection-bootTargetSource-specifyBootTarget"
    ID_RADIO_USE_BIOS = "id=cic-profile-connection-bootTargetSource-useBios"
    ID_INPUT_CONNECTION_NAME = "id=cic-profile-connection-name"

    # For F506
    ID_SELECT_STORAGE_POOL = "xpath=//*[@class='hp-help' and contains(text(),'%s')]"  # replace %s with Storage System name to locate the desired Storage Pool and click it in combo list
    ID_INPUT_STORAGE_POOL = "cic-profile-storage-pool-input"
    ID_SELECT_OS_TYPE = "cic-profile-add-storage-os-type"
    ID_SELECT_OS_TYPE_EDIT = "cic-profile-edit-storage-os-type"
    ID_BTN_ADD_VOLUME = "id=cic-profile-add-storage-volumes"
    ID_BTN_ADD_VOLUME_WHEN_EDIT_PROFILE = "id=cic-profile-edit-storage-volumes"
    ID_ADD_VOLUME_FORM = "id=cic-profile-storage-dialog-title"
    ID_SELECT_VOLUME_TYPE = "cic-profile-storage-volume-type"
    ID_INPUT_VOLUME_NAME = "id=cic-profile-storage-volume-name"
    ID_SELECT_EXISTING_VOLUME_NAME = "cic-profile-storage-existing-volume-name"
    ID_INPUT_EXISTING_VOLUME_NAME = "cic-profile-storage-existing-volume-name-input"
    ID_INPUT_VOLUME_DESCRIPTION = "id=cic-profile-storage-volume-description"
    ID_BTN_ADD_VOLUME_ADD = "id=cic-profile-storage-add"
    ID_BTN_ADD_VOLUME_ADD_AGAIN = "cic-profile-storage-addAgain"
    ID_BTN_SELECT_TARGET_PORTS = ".//*[@id='cic-profile-storage-paths-table']/tbody/tr/td/div/a[text()='%s']/../../following-sibling::*/div[@title='Edit']"
    #       - xpath for the gear button of Edit action to set target ports on Add/Edit Volume page.
    #       - Use the network of profile connection to replace the parameter %s
    ID_LINK_STORAGE_SYSTEMS = "xpath=//div[@class='dataTables_scrollBody']//table[contains(@class, 'hp-master-table')]//td[text()='%s']"
    # replace %s with Storage System name, to click a storage system in the left table
    ID_TABLE_STORAGE_SYSTEM_PORTS = "//table[@id='cic-storagesystems-show-arrayports-table']"
    ID_MENU_SELECTOR_STORAGE_SYSTEM = "id=cic-storagesystems-panel-selector"
    ID_LINK_STORAGE_SYSTEM_PORTS = "xpath=//*[@id='cic-storagesystems-panel-selector']/ol/li/a[text()='Storage System Ports']"
    ID_GEAR_TARGET_PORTS = "xpath=//*[@id='cic-profile-storage-paths-table']/tbody/tr/td/div/a[text()='%s']/../../following-sibling::*/div[@title='Edit']"
    # replace the specifier with connection's network name
    ID_RADIO_BTN_TARGET_PORT_AUTO = "id=profile-storage-edit-targets-auto"
    ID_RADIO_BTN_TARGET_PORT_MANUAL = "id=profile-storage-edit-targets-manual"
    ID_CHKBOX_TARGET_PORT = "xpath=//*[@id='cic-profile-storage-targetports-table']/tbody/tr/td/div[text()='%s']/../preceding-sibling::*[2]/*[@type='checkbox']"
    # replace the specifier with target port name (eg., 0:2:3)
    ID_BTN_OK_TARGET_PORT = "id=profile-storage-edit-targets-add"
    ID_TD_STORAGE_PORT_INFO_TITLE = "//*[@id='cic-storagesystems-show-arrayports-table']/descendant-or-self::*/thead/tr/td[%s]"
    # replace %s with column index (started with 1) of title cell, to get title text
    ID_TD_STORAGE_PORT_INFO_DATA = "//*[@id='cic-storagesystems-show-arrayports-table']/descendant-or-self::*/tbody/tr[%s]/td[%s]"
    # replace %s %s with tuple (column index, row index) (started with 1) of a data cell, to get data text
    ID_TD_STORAGE_PORT_INFO_DATA_LINK_ONLY = "//*[@id='cic-storagesystems-show-arrayports-table']/descendant-or-self::*/tbody/tr[%s]/td[%s]/a"
    # replace %s %s with tuple (column index, row index) (started with 1) of a data cell, to get data text
    ID_LABEL_SERVER_PROFILE_TITLE = "id=cic-profile-show-title"
    ID_LABEL_SAN_STORAGE = "//*[@id='cic-profile-panel-details-storages']/label/span[text()='SAN Storage']"
    ID_MENU_LINK_SERVER_PROFILE = "link=Server Profiles"
    ID_MENU_LINK_STORAGE_SYSTEM = "link=Storage Systems"
    ID_ADD_PROFILE_FORM = "id=cic-profile-add-form"         # 20141101 Alex added for F506
    ID_EDIT_PROFILE_FORM = "id=cic-profile-edit-form"       # 20141106 Alex added for F506
    ID_COMBO_SERVER_HARDWARE_TYPE = "cic-profile-add-server-type-input"     # 20141101 Alex added for F506
    ID_COMBO_SERVER_HARDWARE = "cic-profile-add-server-input"   # 20141101 Alex added for F506
    ID_COMBO_SERVER_HARDWARE_EDIT = "cic-profile-edit-server-input"   # 20141101 Alex added for F506
    ID_COMBO_ENCLOSURE_GROUP = "cic-profile-add-enclosure-group-input"   # 20141101 Alex added for F506
    ID_GEAR_EDIT_VOLUME = "xpath=//*[@id='cic-profile-edit-storage-volumes-table']/descendant-or-self::a[text()='%s']/../following-sibling::*/*[@title='Edit']"
    # replace %s with volume name, to click the gear button to open EDIT page
    ID_LABEL_SERVER_HARDWARE = "id=cic-profile-show-server"
    ID_LABEL_SERVER_HARDWARE_TYPE = "//*[@id='cic-server-type']/a"
    ID_MENU_SELECTOR_SERVER_HARDWARE = "id=cic-server-panel-selector"
    ID_MENU_LINK_HARDWARE = "link=Hardware"
    ID_LABEL_EDIT_SERVER_PROFILE = "id=cic-profile-edit-title"
    ID_LABEL_SERVER_POWER_VALIDATOR = "xpath=//*[@class='hp-error' and @for='cic-profile-server-power-validator']"
    ID_INPUT_VOLUME_CAPACITY = "id=cic-profile-storage-volume-capacity"

    # For F194 - 20141225 Alex Ma
    ID_SELECT_VOLUME_PROVISIONING = "cic-profile-storage-volume-provisioning"
    ID_CHBOX_VOLUME_PERMANENT = "id=cic-profile-storage-volume-permanent-input"
    ID_LABEL_SERVER_PROFILE_TITLE_TEXT = "xpath=//*[@id='cic-profile-show-title' and text()='%s']"
    ID_LABEL_SP_VOLUME_CAPACITY = "xpath=//*[@id='cic-profile-page']/descendant::a[text()='%s']/../following-sibling::*[4]"     # replace %s with an attached volume name

    # Edit Bios Page
    ID_BTN_EDIT_BIOS = "id=cic-edit-bios"
    ID_COMBO_ADV_MEMORY_PROTECTION = "//select[@id='bip-64']/preceding-sibling::a"
    ID_COMBO_SMART_ARRAY_RAID = "//select[@id='bip-268']/preceding-sibling::a"
    ID_COMBO_EMBEDED_SERIAL_PORT = "//select[@id='bip-23']/preceding-sibling::a"
    ID_COMBO_VIRTUAL_SERIAL_PORT = "//select[@id='bip-85']/preceding-sibling::a"
    ID_COMBO_USB_CONTROLL = "//select[@id='bip-67']/preceding-sibling::a"
    ID_BTN_OK = "css=button.hp-ok.hp-primary"
    ID_BTN_OCANCEL = "css=button.hp-cancel"
    # USB Option
    ID_COMBO_USB_BOOT_SUPPORT = "//select[@id='bip-248']/preceding-sibling::a"
    ID_COMBO_USB_FLASH_MEDIA_SEQUENCE = "//select[@id='bip-251']/preceding-sibling::a"
    # Processor Options
    ID_COMBO_NO_EXECUTE_MEM_PROTECTION = "//select[@id='bip-135']/preceding-sibling::a"
    ID_COMBO_INTEL_VITULIZATION_TECH = "//select[@id='bip-158']/preceding-sibling::a"
    ID_COMBO_INTEL_HYPER_THREADING_OPTION = "//select[@id='bip-176']/preceding-sibling::a"
    ID_COMBO_INTEL_TURBO_BOOST_TECH = "//select[@id='bip-181']/preceding-sibling::a"
    ID_COMBO_INTEL_VTd = "//select[@id='bip-186']/preceding-sibling::a"
    # Other
    ID_INPUT_PROCESSOR_CORE_DISABLE = "id=bip-177"
    ID_COMBO_NETWORK_BOOT_RETRY = "//select[@id='bip-313']/preceding-sibling::a"
    ID_COMBO_SRIOV = "//select[@id='bip-269']/preceding-sibling::a"
    ID_COMBO_MEMORY_POWER_SAVING_MODE = "//select[@id='bip-314']/preceding-sibling::a"
    # Advanced Option
    ID_COMBO_VIDEO_OPTION = "//select[@id='bip-180']/preceding-sibling::a"
    ID_COMBO_THERMAL_CONFIGURATION = "//select[@id='bip-142']/preceding-sibling::a"
    ID_COMBO_ASSET_TAG = "//select[@id='bip-254']/preceding-sibling::a"
    # Advanced System ROM Option
    ID_COMBO_MPS_TABLE_MODE = "//select[@id='bip-20']/preceding-sibling::a"
    ID_COMBO_ROM_SELECTION = "//select[@id='bip-29']/preceding-sibling::a"
    ID_COMBO_NMI_DEBUG_BUTTON = "//select[@id='bip-86']/preceding-sibling::a"
    ID_COMBO_VIRTUAL_INSTALL_DISK = "//select[@id='bip-134']/preceding-sibling::a"
    ID_COMBO_PCI_BUS_PADDING_OPTION = "//select[@id='bip-203']/preceding-sibling::a"
    ID_COMBO_POWER_ON_LOGO = "//select[@id='bip-69']/preceding-sibling::a"
    ID_COMBO_F11_BOOT_MENU_PROMPT = "//select[@id='bip-286']/preceding-sibling::a"
    # Advanced Performance Tuning Option
    ID_COMBO_HW_PREFETCHER = "//select[@id='bip-138']/preceding-sibling::a"
    ID_COMBO_ADJACENT_SECTOR_PREFETCH = "//select[@id='bip-139']/preceding-sibling::a"
    ID_COMBO_DCU_STREAMER_PREFETCHER = "//select[@id='bip-260']/preceding-sibling::a"
    ID_COMBO_DCU_IP_PREFETCHER = "//select[@id='bip-262']/preceding-sibling::a"
    ID_COMBO_NODE_INTERLEAVING = "//select[@id='bip-155']/preceding-sibling::a"
    ID_COMBO_DATA_DIRECT_IO = "//select[@id='bip-307']/preceding-sibling::a"
    ID_COMBO_MEMORY_CHANNEL_MODE = "//select[@id='bip-280']/preceding-sibling::a"
    # Power Management Option
    ID_COMBO_HP_POWER_PROFILE = "//select[@id='bip-210']/preceding-sibling::a"
    ID_COMBO_HP_POWER_REGULATOR = "//select[@id='bip-140']/preceding-sibling::a"
    # Advanced Power Management Options
    ID_COMBO_ACPI_SLIP_PREFERENCE = "//select[@id='bip-311']/preceding-sibling::a"
    ID_COMBO_MINIMUM_PROC_IDLE_POW_STATE = "//select[@id='bip-204']/preceding-sibling::a"
    ID_COMBO_MINIMUM_PROC_IDLE_POW_PACKG_STATE = "//select[@id='bip-247']/preceding-sibling::a"
    ID_COMBO_ENERGY_PERFORMANCE_BIAS = "//select[@id='bip-308']/preceding-sibling::a"
    ID_COMBO_MAX_MEMORY_BUS_FREQUENCY = "//select[@id='bip-159']/preceding-sibling::a"
    ID_COMBO_CHANNEL_INTERLEAVING = "//select[@id='bip-187']/preceding-sibling::a"
    ID_COMBO_MAXIMUM_PCI_EXPRESS_SPEED = "//select[@id='bip-179']/preceding-sibling::a"
    ID_COMBO_DYNAMIC_POWER_SAV_MODE_RESPONSE = "//select[@id='bip-191']/preceding-sibling::a"
    ID_COMBO_COLLABARATIVE_POWER_CONTROL = "//select[@id='bip-192']/preceding-sibling::a"
    ID_COMBO_DIMM_VOLTAGE_PREFERENCE = "//select[@id='bip-293']/preceding-sibling::a"
    # Server Availability
    ID_COMBO_ASR_STATUS = "//select[@id='bip-49']/preceding-sibling::a"
    ID_COMBO_ASR_TIMOUT = "//select[@id='bip-50']/preceding-sibling::a"
    ID_COMBO_THERMAL_SHUTDOWN = "//select[@id='bip-91']/preceding-sibling::a"
    ID_COMBO_WAKE_ON_LAN = "//select[@id='bip-63']/preceding-sibling::a"
    ID_COMBO_POST_F1_PROMPT = "//select[@id='bip-18']/preceding-sibling::a"
    ID_COMBO_POWER_BUTTON = "//select[@id='bip-137']/preceding-sibling::a"
    ID_COMBO_AUTOMATIC_POWER_ON = "//select[@id='bip-136']/preceding-sibling::a"
    ID_COMBO_POWER_ON_DELAY = "//select[@id='bip-150']/preceding-sibling::a"
    # Server Asset Teaxt
    ID_INPUT_CUSTOM_POST_MESSAGE = "id=bip-133"
    ID_INPUT_SERVER_NAME = "id=bip-100"
    ID_INPUT_SERVER_PRIMARY_OS = "id=bip-104"
    ID_INPUT_OTHER_TEXT = "id=bip-106"
    # Administrator info text
    ID_INPUT_ADMIN_NAME_TEXT = "id=bip-108"
    ID_INPUT_ADMIN_PHONE_NUMBER = "id=bip-110"
    ID_INPUT_ADMIN_PAGER_NUMBER = "id=bip-112"
    ID_INPUT_ADMIN_OTHER_TEXT = "id=bip-114"
    # BIOS SERIAL CONSOLE AND EMS
    ID_COMBO_BIOS_SERIEL_CONSOLE_PORT = "//select[@id='bip-145']/preceding-sibling::a"
    ID_COMBO_BIOS_SERIEL_CONSOLE_BOARD_RATE = "//select[@id='bip-146']/preceding-sibling::a"
    ID_COMBO_EMS_CONSOLE = "//select[@id='bip-148']/preceding-sibling::a"
    ID_COMBO_BIOS_INTERFACE_MODE = "//select[@id='bip-149']/preceding-sibling::a"
    # System Default Option
    ID_COMBO_SAVE_USER_DEFAULTS = "//select[@id='bip-43']/preceding-sibling::a"
    ID_COMBO_ERASE_USER_DEFAULTS = "//select[@id='bip-47']/preceding-sibling::a"
    # new objects
    ID_CHKBOX_USER_SPECIFIED_IDS = "id=cic-profile-connection-userSpecifiedID"
    ID_COMBO_FIRMWARE_BASELINE = "xpath=//*[@id='cic-profile-add-panels']//span[@class='selectBox-label']"
    ID_COMBO_FIRMWARE_BASELINE_LIST = "xpath=//ul/li/a[text()='%s']"
    ID_LINK_ADD_PROFILE_CONNECTIONS_TABLE = "xpath =//*[@id='cic-profile-add-connections-table']/tbody/tr/td/a[text()='%s']"
    ID_ADD_PROFILE_NOTIFICATION = "xpath =//span[contains(text(),'Unable to add profile')]"
    ID_ADD_PROFILE_NOTIFICATION_CONTENT = "//*[@id='hp-form-message']/div[@ class='hp-form-message-details']"
    ID_ACTIVITY_PROGRESS = "xpath= //tr/td[@class='hp-icon' and div[@class='hp-status hp-status-changing']]/following-sibling::td[@class='hp-name' and p/span[contains(text(),'Create')]]/following-sibling::td/a[contains(text(),'%s')]"  # %s replaces enclosure name
    ID_ACTIVITY_TIMESTAMP = "xpath= //td[div[@class='hp-status hp-status-changing']]/following-sibling::td[p/span[contains(text(),'Create')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp]"  # %s replaces with enclosure name
    ID_ACTIVITY_SUCCESS = "xpath= //td[div[@class='hp-status hp-status-ok']]/following-sibling::td[p/span[contains(text(),'Create')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # %s replace with enclosure namd and time stamp
    ID_ACTIVITY_WARNING = "xpath= //td[div[@class='hp-status hp-status-warning']]/following-sibling::td[p/span[contains(text(),'Create')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # %s replace with enclosure namd and time stamp
    ID_ACTIVITY_ERROR = "xpath= //td[div[@class='hp-status hp-status-error']]/following-sibling::td[p/span[contains(text(),'Create')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # %s replace with enclosure namd and time stamp
    # fusion bois setting update value
    ID_BIOS_UPDATED_VALUE = "xpath=//td[@class='template-bios-setting-value' and text()='%s']"
    ID_BTN_EDIT_BIOS_OK = "xpath=//div[@id='hp-body-div']/div[7]/div/div/div/footer/div/button[@class='hp-ok hp-primary']"
    ID_EDIT_SERVER_PROFILE = "link=Edit"
    ID_EDIT_DROPDOWN_SEARCH_SERVER_HARDWARE = "xpath = //label[text()='Server hardware']/following-sibling::div//div[@class='hp-search-combo-control']"
    ID_EDIT_SEARCH_HARDWARE = "link=Search for another"
    ID_UPDATE_SERVER_PROFILE = "id=cic-profile-edit-ok"
    ID_UPDATE_PROFILE_TIMESTAMP = "xpath = //div[1]/header/div[@class='hp-aside']/div[@class='hp-timestamp']"
    ID_PROFILE_POWER_STATUS = "xpath = //div[@id='cic-profile-show-power' and contains(text(),'%s')]"
    # server status
    ID_NO_SERVER_PROFILE = "//*[@id='cic-profile-details']/div[@class]"
    ID_SELECT_SERVER = "//div[@class='dataTables_scrollBody']/table/tbody/tr/td[contains(text(),'%s')]"
    ID_SERVER_STATUS_OK = "//*[@id='cic-profile-details-status' and @class='hp-status hp-status-ok']"
    ID_SERVER_STATUS_ERROR = "//*[@id='cic-profile-details-status' and @class='hp-status hp-status-error']"
    ID_ERROR_WARN_MSG = "//*[@id='hp-page-notifications']/div/header/div/p/span"
    ID_ERROR_WARN_DETAILS = "//*[@id='hp-page-notifications']/div/div/div[@class='hp-details-container']/div/div[@class='hp-details']"
    # Server power status
    ID_SERVER_POWER_STATUS = "//*[@id='cic-profile-show-power']"
    # Edit Server Profiles with Firmware Baseline
    ID_MENU_EDIT_ACTION = "link=Edit"
    ID_BTN_CONFIRM_UPDATE_FIRMWARE = "xpath=//*[@id='cic-profile-edit-ok']"
    ID_BTN_CANCEL_UPDATE_FIRMWARE = "xpath=//*[@id='cic-profile-edit-cancel']"
    ID_DROPDOWN_FIRMWARE_BASELINE = "xpath=//*[@id='cic-profile-panel-edit-basic']/fieldset/ol/li[6]/div/a/span[1]"
    ID_DROPDOWN_BTN_FIRMWARE_BASELINE = "//*[@id='cic-profile-panel-edit-basic']/fieldset/ol/li[6]/div/a/span[2]"  # ID_COMBO_FIRMWARE_BASELINE = "xpath=//*[@id='cic-profile-edit-form']/div[@class='hp-form-contents']/fieldset/ol/li[@class='hp-form-item']/a[@class='selectBox hp-select selectBox-dropdown']/span[2]"
    ID_STATUS_CHANGING = "//*[@id='cic-profile-details-status']/div[@class='hp-status-changing']"
    ID_STATUS_OK = "xpath=//td[text()='%s']/../td/div[@class='hp-status hp-status-ok']"  # 20141101 Alex added for F506
    ID_STATUS_PROFILE_NAME = "//div[@id='cic-profile-details']//header/h1"
    ID_NEW_ACTIVITY_PROGRESS = "xpath= //tr/td[@class='hp-icon' and div[@class='hp-status hp-status-changing']]/following-sibling::td[@class='hp-name' and p/span[contains(text(),'Update')]]/following-sibling::td/a[contains(text(),'%s')]"  # %s replaces enclosure name
    ID_NEW_ACTIVITY_TIMESTAMP = "xpath= //td[div[@class='hp-status hp-status-changing']]/following-sibling::td[p/span[contains(text(),'Update')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp]"  # %s replaces with enclosure name
    ID_NEW_ACTIVITY_SUCCESS = "xpath=  //td[div[@class='hp-status hp-status-ok']]/following-sibling::td[p/span[contains(text(),'Update')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # %s replace with enclosure namd and time stamp
    ID_NEW_ACTIVITY_ERROR = "xpath=  //td[div[@class='hp-status hp-status-error']]/following-sibling::td[p/span[contains(text(),'Update')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # %s replace with enclosure namd and time stamp
    ID_MAIN_PAGE = "xpath=//*[@id='hp-main-menu-control']/div[2]"
    ID_ERROR_POPUP = "//*[@id='hp-form-message']"
    ID_ERROR_MSG = "//*[@id='hp-form-message']/div[2]/span"
    ID_PROFILE_HARDWARE = "//*[@id='cic-profile-show-serverType']/a"
    ID_COPY_SERVER_PROFILE = "link=Copy"
    # Edit Profile
    ID_EDIT_SERVER_PROFILE_NAME = "id=cic-profile-edit-name"
    ID_EDIT_OVERVIEW = "xpath=//div[@id='cic-profile-panel-edit-selector']/div"
    ID_LINK_LOCAL_STORAGE = "link=Local Storage"
    ID_EDIT_SERVER_PROFILE_DESCRIPTION = "id=cic-profile-edit-description"
    ID_EDIT_SERVER_PROFILE_OK = "id=cic-profile-edit-ok"
    ID_LOCAL_STORAGE = "id=cic-profile-manage-local-storage"
    ID_INITIALIZE_LOCAL_STORAGE = "id=cic-profile-local-storage-initialize"
    ID_SELECT_OK_AFTER_INITIALIZE_LOCAL_STORAGE = "css=footer > div.hp-controls > button.hp-ok.hp-primary"
    ID_EDIT_BOOTABLE = "id=cic-profile-local-storage-bootable"
    ID_COMBO_EDIT_LOGICAL_DRIVE_DROPDOWN = "xpath=//div[@id='cic-profile-local-storage-logical-drive-select-container']/a/span"

    # Validating unassigned profile
    ID_ACTVITY_PROFILE = "xpath = .//*[@id='cic-profile-page']/div[@class='hp-sub-nav']/div[@class='hp-sidebar-control']/div"
    ID_CLICK_ACTIVITY = "xpath = .//div[@class='hp-activity-message']/p/span[text()='Delete']//following::div[text()='%s']"
    ID_PROFILE_UNASSIGNED_SELECT = "xpath = .//div[@class='hp-brief']/div[@class='hp-activity-message']/p/span[text()='Create']//following::div[text()='%s']"
    ID_PROFILE_UNASSIGNED_SUCCESS = "xpath = .//div[@class='hp-status hp-status-ok']/following-sibling::div[@class='hp-activity-message']/p/span[text()='Create']//following::a[text()='%s']"  # %s replace with name of profile
    ID_PROFILE_UNASSIGNED_FAIL = "xpath = .//div[@class='hp-status hp-status-error']/following-sibling::div[@class='hp-activity-message']/p/span[text()='Create']//following::a[text()='%s']"  # %s replace with name of profile
    ID_PROFILE_UNASSIGNED_WARNING = "xpath = .//div[@class='hp-status hp-status-warning']/following-sibling::div[@class='hp-activity-message']/p/span[text()='Create']//following::a[text()='%s']"  # %s replace with name of profile
    ID_SELECT_DROP_DOWN = "xpath = .//ol/li[3]/div/a"
    # Validation for move profile
    ID_ACTIVITY_PROGRESS_MOVE = "xpath= //tr/td[@class='hp-icon' and div[@class='hp-status hp-status-changing']]/following-sibling::td[@class='hp-name' and p/span[contains(text(),'%s')]]/following-sibling::td/a[contains(text(),'%s')]"  # %s replaces enclosure name
    ID_ACTIVITY_TIMESTAMP_MOVE = "xpath= //td[div[@class='hp-status hp-status-changing']]/following-sibling::td[p/span[contains(text(),'%s')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp]"  # %s replaces with enclosure name
    ID_ACTIVITY_SUCCESS_MOVE = "xpath= //td[div[@class='hp-status hp-status-ok']]/following-sibling::td[p/span[contains(text(),'%s')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # %s replace with enclosure namd and time stamp
    ID_ACTIVITY_WARNING_MOVE = "xpath= //td[div[@class='hp-status hp-status-warning']]/following-sibling::td[p/span[contains(text(),'%s')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # %s replace with enclosure namd and time stamp
    ID_ACTIVITY_ERROR_MOVE = "xpath= //td[div[@class='hp-status hp-status-error']]/following-sibling::td[p/span[contains(text(),'%s')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # %s replace with enclosure namd and time stamp
    ID_MOVE_VALIDATION = "xpath = .//*[@id='cic-profile-show-server']/a"
    # New Objects for Delete Profile
    # 20141101 Alex commented below 2 duplicated lines
    # ID_ACTVITY_PROFILE = "xpath = .//*[@id='cic-profile-page']/div[@class='hp-sub-nav']/div[@class='hp-sidebar-control']/div"
    # ID_CLICK_ACTIVITY = "xpath = .//div[@class='hp-activity-message']/p/span[text()='Delete']//following::div[text()='%s']"
    ID_PROFILE_DELETE_SUCCESS = "xpath = .//div[@class='hp-status hp-status-ok']/following-sibling::div[@class='hp-activity-message']/p/span[text()='Delete']//following::a[text()='%s']"  # %s replace with name of profile
    ID_PROFILE_DELETE_FAIL = "xpath = .//div[@class='hp-status hp-status-error']/following-sibling::div[@class='hp-activity-message']/p/span[text()='Delete']//following::a[text()='%s']"  # %s replace with name of profile
    ID_SELECT_PROFILE = "xpath=//td[text()='%s']"
    ID_VALIDATE_NETWORK = "xpath = .//td/a[text()='%s']"
    ID_FORCE_DELETE = "id=cic-profile-force-delete"
    # Power on
    # ID_SERVER_POWER_STATE = "id=cic-profile-show-power"
    ID_SERVER_POWER_STATE = "id=cic-server-power-state"
    ID_SERVER_ASSIGNED_STATUS = "//div[@id='cic-profile-show-server']"
    ID_SERVER_HARDWARE = "//span[@id='cic-profile-show-server']/a[text()='%s']"
    ID_SERVER_POWER_ON = "xpath =//div[@id='cic-profile-show-power' and text()='On']"
    ID_SERVER_POWER_OFF = "xpath =//div[@id='cic-profile-show-power']"
    ID_LINK_ACTIVITY = "link=Activity"
    ID_PROFILE_CREATION_STATUS = "xpath=//td[div[@class='hp-status hp-status-ok']]/following-sibling::td[p/span[contains(text(),'%s')]]/following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # Activity name and time
    ID_DROP_DOWN_VAL = "//ul//li//a[text()='%s']"
    ID_MENU_SELECTOR = "xpath=//*[@id='cic-profile-panel-selector']/div"
    ID_DROPDOWN_SELECT = "xpath=//*[@id='cic-profile-panel-selector']/ol/li/a[text()='%s']"
    # 20141101 Alex commented below: duplicated
    # ID_SERVER_HARDWARE = "xpath=//fieldset/ol/li/label[text()='Server hardware']/following-sibling::div"
    ID_PROFILE_OFF_ERROR = "xpath=//*[@id='cic-profile-server-power-validator-link']"
    ID_BTN_POWER_PRESS_AND_HOLD = "id=cic-server-press-and-hold"
    ID_SERVER_POWER_OFF_VALIDATE = ".//*[@id='cic-server-power-state' and text()='Off']"
    # Extended MAT
    # 20141101 Alex commented below 2 lines: duplicated
    # ID_DROP_DOWN_VAL = "//ul//li//a[text()='%s']"

    # ID_LINK_ACTIVITY = "link=Activity"
    ID_SUCCESSFULL_PROFILE_STATUS_IN_Activity = "xpath=//td[div[@class='hp-status hp-status-ok']]/following-sibling::td[p/span[contains(text(),'%s')]]/following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # Activity name and time
    # Fusion1.1 Create Server Profile
    ID_AFFINITY_DROP_DOWN_SELECT = "xpath=//*[@id='cic-profile-panel-add-basic']//span[@class='hp-name' and text()='%s']"
    ID_AFFINITY_DROP_DOWN = "xpath=//*[@id='cic-profile-panel-add-basic']/fieldset/ol/li[6]/div/div/div"
    ID_AFFINITY_DROP_DOWN_EDIT = "xpath=//*[@id='cic-profile-panel-add-basic']/fieldset/ol/li[6]/div/div/div"
    ID_AFFINITY_SELECT = "cic-profile-add-affinity"     # 20141101 Alex added for F506
    ID_AFFINITY_SELECT_EDIT = "cic-profile-edit-affinity"     # 20141101 Alex added for F506
    ID_CHKBOX_SAN_STORAGE = "xpath=//*[@id='cic-profile-add-manage-san']"
    ID_OS_TYPE_DROP_DOWN = "xpath=//*[@id='cic-profile-manage-storage-volumes-container']//span[@class='selectBox-arrow']"
    ID_OS_TYPE_SELECT = "xpath=html//a[text()='%s']"
    ID_ERROR_NO_STORAGE_VOLUMES = "xpath=//*[@id='cic-profile-add-no-volumes']"
    ID_BTN_ADD_STORAGE = "xpath=//*[@id='cic-profile-add-storage-volumes']"
    ID_VOLUME_SELECT_DROPDOWN = "xpath=//*[@id='cic-profile-storage-volume-div']/div/div[2]"
    ID_VOLUME_SELECT = "xpath=//*[@id='cic-profile-storage-volume-div']//span[text()='%s']"
    ID_RADIO_BTN_AUTO = "xpath=//*[@id='cic-profile-storage-lun-auto']"
    ID_RADIO_BTN_MANUAL = "xpath=//*[@id='cic-profile-storage-lun-manual']"
    ID_TEXT_LUN = "xpath=//*[@id='cic-profile-storage-lun-manual-value']"
    ID_BTN_STORAGE_ADD = "//*[@id='cic-profile-storage-add']"
    ID_LINK_SANSTORAGE = "link=SAN Storage"
    ID_POP_UP_ERROR = "xpath=//*[@id='hp-form-message']/div[2]/p"
    # Edit Storage and add sec shared volume
    ID_EDIT_SAN_COMBO_MENU_VIEW = "xpath=//*[@id='cic-profile-panel-edit-selector']/div"
    ID_EDIT_LINK_SANSTORAGE = "xpath=//a[contains(text(),'SAN Storage')]"
    ID_EDIT_CHKBOX_SAN_STORAGE = "xpath=//*[@id='cic-profile-edit-manage-san']"
    ID_EDIT_BTN_ADD_STORAGE = "xpath=//*[@id='cic-profile-edit-storage-volumes']"

    # SHQA
    ID_NO_SERVER_PROFILE_MESSSAGE = "//div[text()='No server profiles']"
    ID_LINK_LOCAL_STORAGE = "link=Local Storage"
    ID_CHKBOX_LOCAL_STORAGE = "xpath=//*[@id='cic-profile-manage-local-storage']"
    ID_CLOSE_LOCAL_STORAGE = "//button[text()='Close']"
    ID_LABEL_LOCAL_STORAGE = "xpath=//span[text()='Manage Local Storage']"
    ID_RRESET_INIT_LOCAL_STORAGE_MSG = "xpath=//span[@class='hp-form-message-text' and text()='Reset: Initialize local storage']"
    ID_CHKBOX_MANAGE_INTEGRATED_CONTROLLER = "xpath=//*[@id='cic-profile-manage-local-storage-manage-integrated-controller']"
    ID_COMBO_CONTROLLER_MODE_DROPDOWN = "xpath=//div[@id='cic-profile-local-storage-controller-mode-select-container']/a/span"

    ID_DROPDOWN_CONTROLLER_MODE = "xpath=//li/a[@rel='RAID' and text()='%s']"

    ID_CHKBOX_IMPORT_DRIVES = "id=cic-profile-local-storage-import-logical-drive"
    # logical drive
    ID_ADD_LOGICAL_DRIVE = "id=cic-profile-add-logical-drive"
    ID_INPUT_LOGICAL_DRIVE_NAME = "id=cic-profile-logical-drive-name"
    ID_BIN_RAID_LEVEL = "xpath=//div[@data-id='RAID0']"
    ID_SELECT_RAID_LEVEL = "xpath=//*[@id='cic-profile-logical-drive-panels']//ol[@class='hp-options']/li/span[text()='%s']"
    ID_INPUT_PHYSICAL_DRIVES_NUM = "id=cic-profile-logical-drive-dialog-physical-drives"
    ID_BIN_DRIVE_TECHNOLOGY = "//*[@id='cic-profile-logical-drive-dialog-drive-tech-select-div']/div/div/div"
    ID_SELECT_DRIVE_TECHNOLOGY = "xpath=//*[@id='cic-profile-logical-drive-dialog-drive-tech-select-div']/div/div/ol/li/span[text()='%s']"
    ID_BUTTON_CREATE_DRIVE = "id=cic-profile-logical-drive-create"
    ID_TABLE_DIVER_NAME = "//*[@id='cic-profile-local-storage-logical-drive-table']/tbody/tr/td/div[text()='%s']"
    ID_TABLE_DIVER_DETAILS = "//*[@id='cic-profile-local-storage-logical-drive-table']/tbody/tr/td/div[text()='%s']/../../td/div[text()='%s']"
    ID_BIN_BOOT_DRIVE = "//*[@id='cic-profile-local-storage-bootDrive-select-div']/a/span[@class='selectBox-label']"
    ID_SELECT_BOOT_DRIVE = "//a[text()='%s']"
