# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
'''

Server profile templates page objects
    2015-10-22 Alex Ma
            - simply inherited below class from serverprofiles_elements.py since the UI is mostly the same
                - GeneralServerProfilesElements
                - CreateServerProfilesElements
                - EditServerProfilesElements
                - CopyServerProfilesElements

ps: imported CreateServerProfilesElements (serverprofiles_elements.py) to be reused on Action -> Create Server Profile
'''
from FusionLibrary.ui.business_logic.servers.serverprofiles_elements import GeneralServerProfilesElements
from FusionLibrary.ui.business_logic.servers.serverprofiles_elements import CreateServerProfilesElements
from FusionLibrary.ui.business_logic.servers.serverprofiles_elements import EditServerProfilesElements
from FusionLibrary.ui.business_logic.servers.serverprofiles_elements import CopyServerProfilesElements


class GeneralServerProfileTemplatesElements(GeneralServerProfilesElements):
    ID_TABLE_SERVER_PROFILE_TEMPLATE = GeneralServerProfilesElements.ID_TABLE_SERVER_PROFILE
    # ID_TABLE_SERVER_PROFILE_TEMPLATE = "xpath=//table[@class='hp-master-table hp-selectable dataTable']/tbody/tr/td[text()='%s']"  # server hardware name
    ID_TABLE_SERVER_PROFILE_TEMPLATE_LIST = GeneralServerProfilesElements.ID_TABLE_SERVER_PROFILE_LIST
    # ID_TABLE_SERVER_PROFILE_TEMPLATE_LIST = "xpath=//table[@class='hp-master-table hp-selectable dataTable']/tbody/tr/td[2]"
    ID_STATUS_SERVER_PROFILE_TEMPLATE_OK = GeneralServerProfilesElements.ID_STATUS_SERVER_PROFILE_OK  # server profile name
    # ID_STATUS_SERVER_PROFILE_TEMPLATE_OK = "xpath=//table/tbody//tr/td[text()='%s']/../td/div[@class='hp-status hp-status-ok']"  # server profile name
    ID_STATUS_SERVER_PROFILE_TEMPLATE_WARN = GeneralServerProfilesElements.ID_STATUS_SERVER_PROFILE_WARN  # server profile name
    # ID_STATUS_SERVER_PROFILE_TEMPLATE_WARN = "xpath=//table/tbody//tr/td[text()='%s']/../td/div[@class='hp-status hp-status-warning']"  # server profile name
    ID_STATUS_SERVER_PROFILE_TEMPLATE_ERROR = GeneralServerProfilesElements.ID_STATUS_SERVER_PROFILE_ERROR  # server profile name
    # ID_STATUS_SERVER_PROFILE_TEMPLATE_ERROR = "xpath=//table/tbody//tr/td[text()='%s']/../td/div[@class='hp-status hp-status-error']"  # server profile name
    ID_TABLE_SERVER_PROFILE_TEMPLATE_SELECTED = GeneralServerProfilesElements.ID_TABLE_SERVER_PROFILE_SELECTED  # server profile name
    # ID_TABLE_SERVER_PROFILE_TEMPLATE_SELECTED = "xpath=//table[@class='hp-master-table hp-selectable dataTable']/tbody/tr[contains(@class, 'hp-selected')]/td[text()='%s']"  # server profile name
    ID_TABLE_SERVER_PROFILE_TEMPLATE_DELETED = GeneralServerProfilesElements.ID_TABLE_SERVER_PROFILE_DELETED  # server profile name
    # ID_TABLE_SERVER_PROFILE_TEMPLATE_DELETED = "xpath=//table[@class='hp-master-table hp-selectable dataTable']/tbody/tr[contains(@class, 'hp-not-found')]/td[text()='%s']"  # server profile name
    ID_TEXT_GENERAL_SERVER_HARDWARE_TYPE = "xpath=//*[@id='cic-profile-templates-show-serverType']/a"
    ID_TEXT_GENERAL_ENCLOSURE_GROUP = "xpath=//*[@id='cic-profile-templates-show-enclosureGroup']/a"
    # ID_TEXT_GENERAL_USED_BY = "xpath=//*[@id='cic-profile-templates-show-usedby'][1]"
    ID_TEXT_GENERAL_USED_BY = "xpath=//*[@id='cic-profile-templates-show-usedby']"

    class Connection(object):
        ID_TABLE_CONNECTION_DETAIL_INFO = "xpath=//*[@id='cic-profiletemplate-show-connections-summary']/tbody/tr[%d]/td[1]/div"
        ID_TEXT_CONNECT_DISPLAY_NAME = "xpath=//table[@id='cic-profiletemplate-show-connections-summary']/tbody/tr[%d]/td[contains(text(),'%s')]"
        ID_TEXT_CONNECT_DISPLAY_PORT = "xpath=//table[@id='cic-profiletemplate-show-connections-summary']/tbody/tr[%d]/td[contains(text(),'%s')]"
        ID_TEXT_CONNECT_DISPLAY_NETWORK = "xpath=//table[@id='cic-profiletemplate-show-connections-summary']/tbody/tr[%d]//a[contains(@href, 'ethernet-networks')]"
        ID_TEXT_CONNECT_DISPLAY_BOOT = "xpath=//table[@id='cic-profiletemplate-show-connections-summary']/tbody/tr[%d]/td[contains(text(),'%s')]"
        ID_TEXT_CONNECTION_FUNCTION_TYPE = "xpath=//td[@class='template-connections-row-details-type' and contains(text(),'%s')]"
        ID_TEXT_CONNECT_DISPLAY_BANDWIDTH = "xpath=//td[@class='template-connections-row-details-requestedBandwidth']"
        ID_TEXT_CONNECTION_INITIATOR_NAME_NOT_SET = "xpath=//td[@class='template-connections-row-details-initiatorName']/span[contains(text(),'not set')]"
        ID_TEXT_CONNECTION_INITIATOR_IP_NOT_SET = "xpath=//td[@class='template-connections-row-details-initiatorIp']/span[contains(text(),'not set')]"
        ID_TEXT_CONNECTION_INITIATOR_SUBNET_MASK = "xpath=//td[@class='template-connections-row-details-initiatorSubnetMask' and contains(text(),'%s')]"
        ID_TEXT_CONNECTION_INITIATOR_GATEWAY = "xpath=//td[@class='template-connections-row-details-initiatorGateway' and contains(text(),'%s')]"
        ID_TEXT_CONNECTION_INITIATOR_GATEWAY_NOT_SET = "xpath=//td[@class='template-connections-row-details-initiatorGateway']/span[contains(text(),'not set')]"
        ID_TEXT_CONNECTION_TARGET_NAME_NOT_SET = "xpath=//td[@class='template-connections-row-details-bootTargetName']/span[contains(text(),'not set')]"
        ID_TEXT_CONNECTION_TARGET_LUN_NOT_SET = "xpath=//td[@class='template-connections-row-details-bootTargetLun']/span[contains(text(),'not set')]"
        ID_TEXT_CONNECTION_TARGET_IP = "xpath=//td[@class='template-connections-row-details-firstBootTargetIp' and contains(text(),'%s')]"
        ID_TEXT_CONNECTION_TARGET_IP_NOT_SET = "xpath=//td[@class='template-connections-row-details-firstBootTargetIp']/span[contains(text(),'not set')]"
        ID_TEXT_CONNECTION_SECOND_IP = "xpath=//td[@class='template-connections-row-details-secondBootTargetIp' and contains(text(),'%s')]"
        ID_TEXT_CONNECTION_SECOND_IP_NOT_SET = "xpath=//td[@class='template-connections-row-details-secondBootTargetIp']/span[contains(text(),'not set')]"
        ID_TEXT_CONNECTION_CHAP_NAME_NOT_SET = "xpath=//td[@class='template-connections-row-details-chapName hp-ellipsis hp-ellipsised']/span[contains(text(),'not set')]"
        ID_TEXT_CONNECTION_MCHAP_NAME_NOT_SET = "xpath=//td[@class='template-connections-row-details-mutualChapName hp-ellipsis hp-ellipsised']/span[contains(text(),'not set')]"
        ID_TEXT_CONNECTION_MCHAP_NAME_HEADER = "xpath=//*[@id='cic-profiletemplate-show-connections-summary']//tr/td[contains(text(),'Mutual CHAP name')]"


class CreateServerProfileTemplatesElements(CreateServerProfilesElements):
    ID_BUTTON_CREATE_SERVER_PROFILE_TEMPLATE = "link=Create server profile template"
    ID_SELECT_ACTION_CREATE = "xpath=//*[@id='cic-profile-templates-actions']/div/ol/li/a[text()='Create']"

    ID_DIALOG_CREATE_SERVER_PROFILE_TEMPLATE = "//section[@class='hp-details-add-section']"
    ID_INPUT_SERVER_PROFILE_DESCRIPTION = "xpath=//*[@id='cic-profile-add-serverProfileDescription']"


class EditServerProfileTemplatesElements(EditServerProfilesElements):
    ID_SELECT_ACTION_EDIT = "xpath=//*[@id='cic-profile-templates-actions']/div/ol/li/a[text()='Edit']"
    ID_DIALOG_EDIT_SERVER_PROFILE_TEMPLATE = "//div[@class='hp-details-edit-section']"

    class Advanced(object):
        ID_RADIO_ISCSI_INITIATOR_NAME_VIRTUAL = "id=cic-profile-add-advanced-initiator-name-virtual"
        ID_RADIO_ISCSI_INITIATOR_NAME_USER_SPECIFIED = "id=cic-profile-add-advanced-initiator-name-user-specified"
        ID_RADIO_HIDE_UNUSED_FLEXNICS_YES = "xpath=//*[@id='cic-profile-edit-advanced-hide-unused-flexnics-true']"
        ID_RADIO_HIDE_UNUSED_FLEXNICS_NO = "xpath=//*[@id='cic-profile-edit-advanced-hide-unused-flexnics-false']"


class CopyServerProfileTemplatesElements(CopyServerProfilesElements):
    ID_SELECT_ACTION_COPY = "xpath=//*[@id='cic-profile-templates-actions']/div/ol/li/a[text()='Copy']"
    ID_DIALOG_COPY_SERVER_PROFILE_TEMPLATE = "//section[@class='hp-details-add-section']"

    class Advanced(object):
        ID_RADIO_ISCSI_INITIATOR_NAME_VIRTUAL = "id=cic-profile-add-advanced-initiator-name-virtual"
        ID_RADIO_ISCSI_INITIATOR_NAME_USER_SPECIFIED = "id=cic-profile-add-advanced-initiator-name-user-specified"
        ID_RADIO_MAC_ADDRESSES_VIRTUAL = "xpath=//*[@id='cic-profile-advanced-mac-virtual']"
        ID_RADIO_MAC_ADDRESSES_PHYSICAL = "xpath=//*[@id='cic-profile-advanced-mac-physical']"
        ID_RADIO_WWN_ADDRESSES_VIRTUAL = "xpath=//*[@id='cic-profile-advanced-wwn-virtual']"
        ID_RADIO_WWN_ADDRESSES_PHYSICAL = "xpath=//*[@id='cic-profile-advanced-wwn-physical']"
        ID_RADIO_SERIAL_NUMBER_UUID_VIRTUAL = "xpath=//*[@id='cic-profile-advanced-sntype-virtual']"
        ID_RADIO_SERIAL_NUMBER_UUID_PHYSICAL = "xpath=//*[@id='cic-profile-advanced-sntype-physical']"
        ID_RADIO_SERIAL_NUMBER_UUID_USER_SPECIFIED = "xpath=//*[@id='cic-profile-advanced-sntype-user-specified']"
        ID_RADIO_HIDE_UNUSED_FLEXNICS_YES = "xpath=//*[@id='cic-profile-copy-advanced-hide-unused-flexnics-true']"
        ID_RADIO_HIDE_UNUSED_FLEXNICS_NO = "xpath=//*[@id='cic-profile-copy-advanced-hide-unused-flexnics-false']"


class DeleteServerProfileTemplatesElements(object):
    ID_SELECT_ACTION_DELETE = "xpath=//*[@id='cic-profile-templates-actions']/div/ol/li/a[text()='Delete']"

    ID_CHECKBOX_FORCE_DELETE = "xpath=//*[@id='cic-profile-force-delete']"
    ID_BUTTON_YES_DELETE = "xpath=//button[@class='hp-ok hp-primary' and @data-localize='profiletemplates.delete.confirm']"
    ID_BUTTON_CANCEL = "xpath=//button[@class='hp-cancel' and @data-localize='core.common.cancel']"
    ID_LABEL_PROFILE_TEMPLATE_NAME = "xpath=//*[@id='cic-profile-delete-name']"
    # ID_DIALOG_DELETE_SERVER_PROFILE_TEMPLATE = "xpath=//*[@id='cic-profile-templates-delete-prompt']"

    # replace below %s with server profile template name
    ID_DIALOG_DELETE_SERVER_PROFILE_TEMPLATE = "xpath=//span[text()='Delete']/following-sibling::span[text()='%s']"
    # ID_DIALOG_DELETE_SERVER_PROFILE_TEMPLATE = "xpath=//*[@id='cic-profile-delete-ok']"

    # replace below %s with the expected error message, which should be defined as attribute 'expected_error_message' in test data
    ID_LABEL_ERROR_MSG_DELETE_USED_SPT = "xpath=//*[@class='hp-notify']/span[text()='%s']"
    ID_LINK_USED_BY_PROFILE_COUNT = "xpath=//*[@id='cic-profile-templates-delete-profiles']/label/a"
    ID_BUTTON_CLOSE = "xpath=//button[text()='Close']"


class CreateServerProfileFromTemplatesElements(CreateServerProfilesElements):
    """
    2015-10-22 Alex Ma
            - simply inherited from serverprofiles_elements.py - CreateServerProfilesElements since the UI is mostly the same
            -
    """
    ID_SELECT_ACTION_CREATE_SERVER_PROFILE = "xpath=//*[@id='cic-profile-templates-actions']/div/ol/li/a[text()='Create server profile']"


class ServerProfileTemplatesPage(object):
    ID_PAGE_LABEL = "xpath=//div[@class='hp-page-label']/h1[text()='Server Profiles']"
    ID_PAGE_LABEL_STORAGE_SYSTEM = "xpath=//div[@class='hp-page-label']/h1[text()='Storage Systems']"
    ID_PROFILE_TEMPLATE_LIST = "xpath=//div[@class='dataTables_scrollBody']/table"
    ID_PROFILE_TEMPLATE_CHANGING = ID_PROFILE_TEMPLATE_LIST + "/tbody/tr//div[@class='hp-status hp-changing']"
    ID_PROFILE_TEMPLATE_EDIT_COMPLETE = "//header[@class='hp-notification-summary']/div[@class='hp-state' andtext()='Completed']"
    ID_PROFILE_TEMPLATE_EDIT_INPROCESS = "//header[@class='hp-notification-summary']/div[@class='hp-state']/div[@class-'hp-progress']"
    ID_PROFILE_TEMPLATE_EDIT_VERIFY = "id=hp-form-message"
    ID_PROFILE_TEMPLATE_LIST_NAMES = ID_PROFILE_TEMPLATE_LIST + '/tbody/tr/td[2]'
    # Create Server Profile Template
    ID_LABEL_HP_MAIN_MENU = "id=hp-main-menu-label"
    ID_LINK_CREATE_SERVER_PROFILE_TEMPLATES = "link=Create profile"
    ID_INPUT_SERVER_PROFILE_TEMPLATE_NAME = "id=cic-profile-add-name"
    ID_INPUT_SERVER_PROFILE_TEMPLATE_DESCRIPTION = "id=cic-profile-add-description"
    ID_INPUT_SERVER_HARDWARE_TYPE = "id=cic-profile-add-server-type-input"
    ID_BTN_CREATE_PLUS_SERVER_PROFILE_TEMPLATE = "id=cic-profile-createAgain"
    ID_BTN_CREATE_SERVER_PROFILE_TEMPLATE = "id=cic-profile-create"
    ID_BTN_CANCEL_SERVER_PROFILE_TEMPLATE = "id=cic-profile-add-cancel"
    ID_BTN_ADD_NETWORK_CONNECTION = "id=cic-networkset-add-networks"
    ID_CHKBOX_PROFILE_TEMPLATE_BOOT_LOADER = "id=cic-profile-add-boot-order"
    ID_LINK_SEARCH_FOR_ANOTHER = "link=Search for another"
    ID_COMPLETE_STATUS_PROFILE_TEMPLATE = "xpath=//span[@class='hp-value' and text()='ok']/../../following-sibling::td[text()='%s']"
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
    ID_NO_SERVER_PROFILE_TEMPLATE_MESSAGE = "xpath=//div[text()='No server profiles']"
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
    ID_CHKBOX_PROFILE_TEMPLATE_MANAGE_BIOS = "id=cic-profile-manage-bios"
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
    ID_ELEMENT_PROFILE_TEMPLATE_NAME_BASE = "xpath=//td[@class='' and text()='%s']"  # Replace %s with profile name
    ID_ELEMENT_MESSAGE_SERVER_PROFILE_TEMPLATE = "xpath=//span[@class='hp-form-message-text' and text()='Created server profile: %s']"  # replace %s with profile name
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
    ID_LABEL_SERVER_PROFILE_TEMPLATE_TITLE = "id=cic-profile-show-title"
    ID_LABEL_SAN_STORAGE = "//*[@id='cic-profile-panel-details-storages']/label/span[text()='SAN Storage']"
    ID_MENU_LINK_SERVER_PROFILE_TEMPLATE = "link=Server Profiles"
    ID_MENU_LINK_STORAGE_SYSTEM = "link=Storage Systems"
    ID_ADD_PROFILE_TEMPLATE_FORM = "id=cic-profile-add-form"         # 20141101 Alex added for F506
    ID_EDIT_PROFILE_TEMPLATE_FORM = "id=cic-profile-edit-form"       # 20141106 Alex added for F506
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
    ID_LABEL_EDIT_SERVER_PROFILE_TEMPLATE = "id=cic-profile-edit-title"
    ID_LABEL_SERVER_POWER_VALIDATOR = "xpath=//*[@class='hp-error' and @for='cic-profile-server-power-validator']"
    ID_INPUT_VOLUME_CAPACITY = "id=cic-profile-storage-volume-capacity"

    # For F194 - 20141225 Alex Ma
    ID_SELECT_VOLUME_PROVISIONING = "cic-profile-storage-volume-provisioning"
    ID_CHBOX_VOLUME_PERMANENT = "id=cic-profile-storage-volume-permanent-input"
    ID_LABEL_SERVER_PROFILE_TEMPLATE_TITLE_TEXT = "xpath=//*[@id='cic-profile-show-title' and text()='%s']"
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
    ID_COMBO_HP_POWER_PROFILE_TEMPLATE = "//select[@id='bip-210']/preceding-sibling::a"
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
    ID_LINK_ADD_PROFILE_TEMPLATE_CONNECTIONS_TABLE = "xpath =//*[@id='cic-profile-add-connections-table']/tbody/tr/td/a[text()='%s']"
    ID_ADD_PROFILE_TEMPLATE_NOTIFICATION = "xpath =//span[contains(text(),'Unable to add profile')]"
    ID_ADD_PROFILE_TEMPLATE_NOTIFICATION_CONTENT = "//*[@id='hp-form-message']/div[@ class='hp-form-message-details']"
    ID_ACTIVITY_PROGRESS = "xpath= //tr/td[@class='hp-icon' and div[@class='hp-status hp-status-changing']]/following-sibling::td[@class='hp-name' and p/span[contains(text(),'Create')]]/following-sibling::td/a[contains(text(),'%s')]"  # %s replaces enclosure name
    ID_ACTIVITY_TIMESTAMP = "xpath= //td[div[@class='hp-status hp-status-changing']]/following-sibling::td[p/span[contains(text(),'Create')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp]"  # %s replaces with enclosure name
    ID_ACTIVITY_SUCCESS = "xpath= //td[div[@class='hp-status hp-status-ok']]/following-sibling::td[p/span[contains(text(),'Create')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # %s replace with enclosure namd and time stamp
    ID_ACTIVITY_WARNING = "xpath= //td[div[@class='hp-status hp-status-warning']]/following-sibling::td[p/span[contains(text(),'Create')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # %s replace with enclosure namd and time stamp
    ID_ACTIVITY_ERROR = "xpath= //td[div[@class='hp-status hp-status-error']]/following-sibling::td[p/span[contains(text(),'Create')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # %s replace with enclosure namd and time stamp
    # fusion bois setting update value
    ID_BIOS_UPDATED_VALUE = "xpath=//td[@class='template-bios-setting-value' and text()='%s']"
    ID_BTN_EDIT_BIOS_OK = "xpath=//div[@id='hp-body-div']/div[7]/div/div/div/footer/div/button[@class='hp-ok hp-primary']"
    ID_EDIT_SERVER_PROFILE_TEMPLATE = "link=Edit"
    ID_EDIT_DROPDOWN_SEARCH_SERVER_HARDWARE = "css=div.hp-search-combo-control"
    ID_EDIT_SEARCH_HARDWARE = "link=Search for another"
    ID_UPDATE_SERVER_PROFILE_TEMPLATE = "id=cic-profile-edit-ok"
    ID_UPDATE_PROFILE_TEMPLATE_TIMESTAMP = "xpath = //div[1]/header/div[@class='hp-aside']/div[@class='hp-timestamp']"
    ID_PROFILE_TEMPLATE_POWER_STATUS = "xpath = //div[@id='cic-profile-show-power' and contains(text(),'%s')]"
    # server status
    ID_NO_SERVER_PROFILE_TEMPLATE = "//*[@id='cic-profile-details']/div[@class]"
    ID_SELECT_SERVER = "//div[@class='dataTables_scrollBody']/table/tbody/tr/td[contains(text(),'%s')]"
    ID_SERVER_STATUS_OK = "//*[@id='cic-profile-details-status' and @class='hp-status hp-status-ok']"
    ID_SERVER_STATUS_ERROR = "//*[@id='cic-profile-details-status' and @class='hp-status hp-status-error']"
    ID_ERROR_WARN_MSG = "//*[@id='hp-page-notifications']/div/header/div/p/span"
    # Server power status
    ID_SERVER_POWER_STATUS = "//*[@id='cic-profile-show-power']"
    # Edit Server Profile Templates with Firmware Baseline
    ID_MENU_EDIT_ACTION = "link=Edit"
    ID_BTN_CONFIRM_UPDATE_FIRMWARE = "xpath=//*[@id='cic-profile-edit-ok']"
    ID_BTN_CANCEL_UPDATE_FIRMWARE = "xpath=//*[@id='cic-profile-edit-cancel']"
    ID_DROPDOWN_FIRMWARE_BASELINE = "xpath=//*[@id='cic-profile-panel-edit-basic']/fieldset/ol/li[6]/div/a/span[1]"
    ID_DROPDOWN_BTN_FIRMWARE_BASELINE = "//*[@id='cic-profile-panel-edit-basic']/fieldset/ol/li[6]/div/a/span[2]"  # ID_COMBO_FIRMWARE_BASELINE = "xpath=//*[@id='cic-profile-edit-form']/div[@class='hp-form-contents']/fieldset/ol/li[@class='hp-form-item']/a[@class='selectBox hp-select selectBox-dropdown']/span[2]"
    ID_STATUS_CHANGING = "//*[@id='cic-profile-details-status']/div[@class='hp-status-changing']"
    ID_STATUS_OK = "xpath=//td[text()='%s']/../td/div[@class='hp-status hp-status-ok']"  # 20141101 Alex added for F506
    ID_STATUS_PROFILE_TEMPLATE_NAME = "//div[@id='cic-profile-details']//header/h1"
    ID_NEW_ACTIVITY_PROGRESS = "xpath= //tr/td[@class='hp-icon' and div[@class='hp-status hp-status-changing']]/following-sibling::td[@class='hp-name' and p/span[contains(text(),'Update')]]/following-sibling::td/a[contains(text(),'%s')]"  # %s replaces enclosure name
    ID_NEW_ACTIVITY_TIMESTAMP = "xpath= //td[div[@class='hp-status hp-status-changing']]/following-sibling::td[p/span[contains(text(),'Update')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp]"  # %s replaces with enclosure name
    ID_NEW_ACTIVITY_SUCCESS = "xpath=  //td[div[@class='hp-status hp-status-ok']]/following-sibling::td[p/span[contains(text(),'Update')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # %s replace with enclosure namd and time stamp
    ID_NEW_ACTIVITY_ERROR = "xpath=  //td[div[@class='hp-status hp-status-error']]/following-sibling::td[p/span[contains(text(),'Update')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # %s replace with enclosure namd and time stamp
    ID_MAIN_PAGE = "xpath=//*[@id='hp-main-menu-control']/div[2]"
    ID_ERROR_POPUP = "//*[@id='hp-form-message']"
    ID_ERROR_MSG = "//*[@id='hp-form-message']/div[2]/span"
    ID_PROFILE_TEMPLATE_HARDWARE = "//*[@id='cic-profile-show-serverType']/a"
    ID_COPY_SERVER_PROFILE_TEMPLATE = "link=Copy"
    # Edit Profile Template
    ID_EDIT_SERVER_PROFILE_TEMPLATE_NAME = "id=cic-profile-edit-name"
    ID_EDIT_OVERVIEW = "xpath=//div[@id='cic-profile-panel-edit-selector']/div"
    ID_LINK_LOCAL_STORAGE = "link=Local Storage"
    ID_EDIT_SERVER_PROFILE_TEMPLATE_DESCRIPTION = "id=cic-profile-edit-description"
    ID_EDIT_SERVER_PROFILE_TEMPLATE_OK = "id=cic-profile-edit-ok"
    ID_LOCAL_STORAGE = "id=cic-profile-manage-local-storage"
    ID_INITIALIZE_LOCAL_STORAGE = "id=cic-profile-local-storage-initialize"
    ID_SELECT_OK_AFTER_INITIALIZE_LOCAL_STORAGE = "css=footer > div.hp-controls > button.hp-ok.hp-primary"
    ID_EDIT_BOOTABLE = "id=cic-profile-local-storage-bootable"
    ID_COMBO_EDIT_LOGICAL_DRIVE_DROPDOWN = "xpath=//div[@id='cic-profile-local-storage-logical-drive-select-container']/a/span"

    # Validating unassigned profile
    ID_ACTVITY_PROFILE_TEMPLATE = "xpath = .//*[@id='cic-profile-page']/div[@class='hp-sub-nav']/div[@class='hp-sidebar-control']/div"
    ID_CLICK_ACTIVITY = "xpath = .//div[@class='hp-activity-message']/p/span[text()='Delete']//following::div[text()='%s']"
    ID_PROFILE_TEMPLATE_UNASSIGNED_SELECT = "xpath = .//div[@class='hp-brief']/div[@class='hp-activity-message']/p/span[text()='Create']//following::div[text()='%s']"
    ID_PROFILE_TEMPLATE_UNASSIGNED_SUCCESS = "xpath = .//div[@class='hp-status hp-status-ok']/following-sibling::div[@class='hp-activity-message']/p/span[text()='Create']//following::a[text()='%s']"  # %s replace with name of profile
    ID_PROFILE_TEMPLATE_UNASSIGNED_FAIL = "xpath = .//div[@class='hp-status hp-status-error']/following-sibling::div[@class='hp-activity-message']/p/span[text()='Create']//following::a[text()='%s']"  # %s replace with name of profile
    ID_PROFILE_TEMPLATE_UNASSIGNED_WARNING = "xpath = .//div[@class='hp-status hp-status-warning']/following-sibling::div[@class='hp-activity-message']/p/span[text()='Create']//following::a[text()='%s']"  # %s replace with name of profile
    ID_SELECT_DROP_DOWN = "xpath = .//ol/li[3]/div/a"
    # Validation for move profile template
    ID_ACTIVITY_PROGRESS_MOVE = "xpath= //tr/td[@class='hp-icon' and div[@class='hp-status hp-status-changing']]/following-sibling::td[@class='hp-name' and p/span[contains(text(),'%s')]]/following-sibling::td/a[contains(text(),'%s')]"  # %s replaces enclosure name
    ID_ACTIVITY_TIMESTAMP_MOVE = "xpath= //td[div[@class='hp-status hp-status-changing']]/following-sibling::td[p/span[contains(text(),'%s')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp]"  # %s replaces with enclosure name
    ID_ACTIVITY_SUCCESS_MOVE = "xpath= //td[div[@class='hp-status hp-status-ok']]/following-sibling::td[p/span[contains(text(),'%s')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # %s replace with enclosure namd and time stamp
    ID_ACTIVITY_WARNING_MOVE = "xpath= //td[div[@class='hp-status hp-status-warning']]/following-sibling::td[p/span[contains(text(),'%s')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # %s replace with enclosure namd and time stamp
    ID_ACTIVITY_ERROR_MOVE = "xpath= //td[div[@class='hp-status hp-status-error']]/following-sibling::td[p/span[contains(text(),'%s')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # %s replace with enclosure namd and time stamp
    ID_MOVE_VALIDATION = "xpath = .//*[@id='cic-profile-show-server']/a"
    # New Objects for Delete Profile Template
    # 20141101 Alex commented below 2 duplicated lines
    # ID_ACTVITY_PROFILE = "xpath = .//*[@id='cic-profile-page']/div[@class='hp-sub-nav']/div[@class='hp-sidebar-control']/div"
    # ID_CLICK_ACTIVITY = "xpath = .//div[@class='hp-activity-message']/p/span[text()='Delete']//following::div[text()='%s']"
    ID_PROFILE_TEMPLATE_DELETE_SUCCESS = "xpath = .//div[@class='hp-status hp-status-ok']/following-sibling::div[@class='hp-activity-message']/p/span[text()='Delete']//following::a[text()='%s']"  # %s replace with name of profile
    ID_PROFILE_TEMPLATE_DELETE_FAIL = "xpath = .//div[@class='hp-status hp-status-error']/following-sibling::div[@class='hp-activity-message']/p/span[text()='Delete']//following::a[text()='%s']"  # %s replace with name of profile
    ID_SELECT_PROFILE_TEMPLATE = "xpath=//td[text()='%s']"
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
    ID_PROFILE_TEMPLATE_CREATION_STATUS = "xpath=//td[div[@class='hp-status hp-status-ok']]/following-sibling::td[p/span[contains(text(),'%s')]]/following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # Activity name and time
    ID_DROP_DOWN_VAL = "//ul//li//a[text()='%s']"
    ID_MENU_SELECTOR = "xpath=//*[@id='cic-profile-panel-selector']/div"
    ID_DROPDOWN_SELECT = "xpath=//*[@id='cic-profile-panel-selector']/ol/li/a[text()='%s']"
    # 20141101 Alex commented below: duplicated
    # ID_SERVER_HARDWARE = "xpath=//fieldset/ol/li/label[text()='Server hardware']/following-sibling::div"
    ID_PROFILE_TEMPLATE_OFF_ERROR = "xpath=//*[@id='cic-profile-server-power-validator-link']"
    ID_BTN_POWER_PRESS_AND_HOLD = "id=cic-server-press-and-hold"
    ID_SERVER_POWER_OFF_VALIDATE = ".//*[@id='cic-server-power-state' and text()='Off']"
    # Extended MAT
    # 20141101 Alex commented below 2 lines: duplicated
    # ID_DROP_DOWN_VAL = "//ul//li//a[text()='%s']"

    # ID_LINK_ACTIVITY = "link=Activity"
    ID_SUCCESSFULL_PROFILE_TEMPLATE_STATUS_IN_Activity = "xpath=//td[div[@class='hp-status hp-status-ok']]/following-sibling::td[p/span[contains(text(),'%s')]]/following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # Activity name and time
    # Fusion1.1 Create Server Profile Template
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
    ID_NO_SERVER_PROFILE_TEMPLATE_MESSSAGE = "//div[text()='No server profiles']"
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
