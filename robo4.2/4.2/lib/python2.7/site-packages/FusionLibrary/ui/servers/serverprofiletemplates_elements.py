# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
'''

Server profile page objects
'''


class FusionServerProfileTemplatesPage(object):
    ID_LINK_CREATE_PROFILE_TEMPLATE = "link=Create server profile template"
    ID_PAGE_LABEL = "xpath=//div[@class='hp-page-label']/h1[text()='Server Profile Templates']"
    ID_PROFILE_LIST = "xpath=//div[@class='dataTables_scrollBody']/table"
    ID_PROFILE_CHANGING = ID_PROFILE_LIST + "/tbody/tr//div[@class='hp-status hp-changing']"
    ID_PROFILE_EDIT_COMPLETE = "//header[@class='hp-notification-summary']/div[@class='hp-state' and text()='Completed']"
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
    ID_CHKBOX_MANAGE_BOOT = "id=cic-profile-add-manage-boot-order"
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
    ID_RADIO_NO_HIDE_UNSUDE_FLEXNICS = "id=cic-profile-add-advanced-hide-unused-flexnics-false"
    ID_RADIO_YES_HIDE_UNSUDE_FLEXNICS = "id=cic-profile-add-advanced-hide-unused-flexnics-true"
    ID_SELECT_PROFILE_TEMPLATE = "xpath=//td[text()='%s']"
    ID_MENU_ACTION_CREATE_SERVER_PROFILE = "link=Create server profile"
    ID_INPUT_PROFILE_NAME = "id=cic-profile-add-name"
    ID_INPUT_PROFILE_DESCRIPTION = "id=cic-profile-add-description"
    ID_ELEMENT_SERVER_NAME = "xpath = //*[@id='cic-profile-panel-add-basic']/fieldset//div/ol[@class='hp-search-combo-scroller hp-options']//span[contains(text(),'%s')]"   # Replace %s with server name
    ID_CHECKBOX_OVERRIDE_TEMPALTE = "id=cic-profile-add-override"
    ID_BTN_CREATE_PROFILE = "id=cic-profile-create"
    ID_DIALOG_CREATE_PROFILE = "xpath = //div[@class='hp-status hp-changing']/following-sibling::span[contains(text(), 'Verifying parameters...')]"
    ID_DIALOG_CREATE_PROFILE_ERROR = "xpath = //div[@id='hp-form-message']"
    ID_DIALOG_CREATE_PROFILE_ERROR_WARNING = "xpath = //*[@id='hp-form-message']//div[@class='hp-status hp-status-warning']"
    ID_ELEMENT_ACTIVITY = "xpath = //ol[@id='hp-flyout-activities']/li/div/div[text()='%s']"  # Replace with profile name
    ID_ACTIVITY_STATUS_OK = "xpath = //ol[@id='hp-flyout-activities']/li/div/div/span[text()='ok']"
    ID_ACTIVITY_STATUS_WARNING = "xpath = //ol[@id='hp-flyout-activities']/li/div/div/span[text()='warning']"
    # Action Menu
    ID_MENU_MAIN_ACTION = "xpath=//label[text()='Actions']"
    ID_MENU_ACTION_CREATE = "id=cic-profile-create-action"
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
    ID_COMBO_MENU_VIEW = "xpath=//div[@id='cic-profile-add-panel-selector']/div[@class='hp-value']"
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
    ID_COMBO_DEVICE_TYPE = "xpath=//label[text()='Function type']//following-sibling::div/a"
    ID_INPUT_CONNECTION_NAME = "id=cic-profile-connection-name"
    ID_COMBO_FUNCTION_TYPE = "xpath=//label[text()='Function type']//following-sibling::div/a"
    ID_COMBO_SERVER_HARDWARE_DROPDOWN = "//input[@id='cic-profile-add-server-input']/following-sibling::div[2]"
    ID_COMBO_SERVER_HARDWARE_TYPE_DROPDOWN = "//input[@id='cic-profile-add-server-type-input']/following-sibling::div[2]"
    ID_COMBO_ENCLOSURE_GROUP_DROPDOWN = "//input[@id='cic-profile-add-enclosure-group-input']/following-sibling::div[2]"
#   {2015-03-31 Alex Ma fixed UI change due to OVAQual testing failure
#    ID_COMBO_FLEXNIC_ADD_CONNECTION = "//select[@id='cic-profile-connection-flexnic']/preceding-sibling::a"
    ID_COMBO_FLEXNIC_ADD_CONNECTION = "//*[@id='cic-profile-connection-flexnic-input']"
#   }
    ID_COMBO_CLICK_BUTTON = "xpath = .//*[@id='cic-profile-connections-dialog-form']/fieldset/ol[1]/li[4]/div/a/span[2]"
    ID_COMBO_BOOT_ADD_CONNECTION = "//select[@id='cic-profile-connection-boot']/preceding-sibling::a"
    ID_COMBO_NETWORK_ADD_CONNECTION = "//input[@id='cic-profile-connection-network-input']/following-sibling::div[2]"
    ID_INPUT_NETWORK_ADD_CONNECTION = "id=cic-profile-connection-network-input"
    ID_INPUT_REQUESTED_BW_ADD_CONNECTION = "id=cic-profile-connection-bandwidth"
    ID_SELECT_REQUESTED_BW_ADD_CONNECTION = "//select[@id='cic-profile-connection-bandwidth-discrete']/preceding-sibling::a"
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
    ID_LINK_ADD_PROFILE_CONNECTIONS_TABLE = "xpath =//div[@id='cic-profile-add-connections-div']//table//td/a[.='%s']"
    ID_ADD_PROFILE_NOTIFICATION = "xpath =//span[contains(text(),'Unable to add profile')]"
    ID_ADD_PROFILE_NOTIFICATION_CONTENT = "//*[@id='hp-form-message']/div[@ class='hp-form-message-details']"
    # Activity
    ID_ACTIVITY_PROGRESS = "xpath= //tr/td[@class='hp-icon' and div[@class='hp-status hp-status-changing']]/following-sibling::td[@class='hp-name' and p/span[contains(text(),'Create')]]/following-sibling::td/a[contains(text(),'%s')]"  # %s replaces enclosure name
    ID_ACTIVITY_TIMESTAMP = "xpath= //td[div[@class='hp-status hp-status-changing']]/following-sibling::td[p/span[contains(text(),'Create')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp]"  # %s replaces with enclosure name
    ID_ACTIVITY_SUCCESS = "xpath= //td[div[@class='hp-status hp-status-ok']]/following-sibling::td[p/span[contains(text(),'Create')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # %s replace with enclosure namd and time stamp
    ID_ACTIVITY_WARNING = "xpath= //td[div[@class='hp-status hp-status-warning']]/following-sibling::td[p/span[contains(text(),'Create')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # %s replace with enclosure namd and time stamp
    ID_ACTIVITY_ERROR = "xpath= //td[div[@class='hp-status hp-status-error']]/following-sibling::td[p/span[contains(text(),'Create')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # %s replace with enclosure namd and time stamp
    ID_ACTIVITY_BAR = "//div[@id='cic-profile-page']/div/div[6]/div"
    ID_LAST_ACTIVITY = "//li[1]/div/div[3]"
    ID_ACTIVITY_STATUS = "//ol[@id='hp-flyout-activities']/li[1]/div[2]/header/div[1]"
    ID_ACTIVITY_NAME = "//ol[@id='hp-flyout-activities']/li[1]/div[2]/header/div[2]"
    ID_MULTIPLE_ACTIVITY_ENTITY = "//ol[@id='hp-flyout-activities']/li[1]/div[2]/header/span"
    ID_SINGLE_ACTIVITY_ENTITY = "//ol[@id='hp-flyout-activities']/li[1]/div[2]/header/a"
    ID_ACTIVITY_MESSAGE = "//ol[@id='hp-flyout-activities']/li[1]/div[2]/div[2]/div/div"
    # fusion bois setting update value
    ID_BIOS_UPDATED_VALUE = "xpath=//td[@class='template-bios-setting-value' and text()='%s']"
    ID_BTN_EDIT_BIOS_OK = "xpath=//div[@id='hp-body-div']/div[7]/div/div/div/footer/div/button[@class='hp-ok hp-primary']"
    ID_EDIT_SERVER_PROFILE = "link=Edit"
    ID_EDIT_DROPDOWN_SEARCH_SERVER_HARDWARE = "css=div.hp-search-combo-control"
    ID_EDIT_SEARCH_HARDWARE = "link=Search for another"
    ID_UPDATE_SERVER_PROFILE = "id=cic-profile-edit-ok"
    ID_UPDATE_PROFILE_TIMESTAMP = "xpath = //div[1]/header/div[@class='hp-aside']/div[@class='hp-timestamp']"
    ID_PROFILE_POWER_STATUS = "xpath = //div[@id='cic-profile-show-power' and text()='%s']"
    # server status
    ID_NO_SERVER_PROFILE = "//*[@id='cic-profile-details']/div[@class]"
    ID_SELECT_SERVER = "//div[@class='dataTables_scrollBody']/table/tbody/tr/td[contains(text(),'%s')]"
    ID_SERVER_STATUS_OK = "//*[@id='cic-profile-details-status' and @class='hp-status hp-status-ok']"
    ID_SERVER_STATUS_ERROR = "//*[@id='cic-profile-details-status' and @class='hp-status hp-status-error']"
    ID_ERROR_WARN_MSG = "//*[@id='hp-page-notifications']/div/header/div/p/span"
    ID_SERVER_DESCRIPTION = "//div[@id='cic-profile-show-description']"
    ID_SERVER_HARDWARE_NAME = "css=#cic-profile-show-server"
    ID_ASSOCIATED_SERVER = "//span[@id='cic-profile-show-associatedServer']"
    ID_SERVER_ENC_GROUP = "//div[@id='cic-profile-show-enclosureGroup']"
    ID_SERVER_AFFINITY = "//div[@id='cic-profile-show-affinity']"
    ID_SERVER_SERIAL_NUMBER = "//div[@id='cic-profile-show-serialNumber']"
    ID_SERVER_UUID = "//div[@id='cic-profile-show-uuid']"
    ID_MULTIPLE_SERVERS_TITLE = "//h1[@id='cic-profile-show-title' and text()='%s Server Profiles']"
    # Server power status
    ID_SERVER_POWER_STATUS = "//*[@id='cic-profile-show-power']"
    # Edit Server Profiles with Firmware Baseline
    ID_MENU_EDIT_ACTION = "link=Edit"
    ID_BTN_CONFIRM_UPDATE_FIRMWARE = "xpath=//*[@id='cic-profile-edit-ok']"
    ID_BTN_CANCEL_UPDATE_FIRMWARE = "xpath=//*[@id='cic-profile-edit-cancel']"
    ID_DROPDOWN_FIRMWARE_BASELINE = "xpath=//*[@id='cic-profile-panel-edit-basic']/fieldset/ol/li[6]/div/a/span[1]"
    ID_DROPDOWN_BTN_FIRMWARE_BASELINE = "//*[@id='cic-profile-panel-edit-basic']/fieldset/ol/li[6]/div/a/span[2]"  # ID_COMBO_FIRMWARE_BASELINE = "xpath=.//*[@id='cic-profile-edit-form']/div[@class='hp-form-contents']/fieldset/ol/li[@class='hp-form-item']/a[@class='selectBox hp-select selectBox-dropdown']/span[2]"
    ID_STATUS_CHANGING = "//*[@id='cic-profile-details-status']/div[@class='hp-status-changing']"
    ID_STATUS_PROFILE_NAME = "//div[@id='cic-profile-details']//header/h1"
    ID_NEW_ACTIVITY_PROGRESS = "xpath= //tr/td[@class='hp-icon' and div[@class='hp-status hp-status-changing']]/following-sibling::td[@class='hp-name' and p/span[contains(text(),'Update')]]/following-sibling::td/a[contains(text(),'%s')]"  # %s replaces enclosure name
    ID_NEW_ACTIVITY_TIMESTAMP = "xpath= //td[div[@class='hp-status hp-status-changing']]/following-sibling::td[p/span[contains(text(),'Update')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp]"  # %s replaces with enclosure name
    ID_NEW_ACTIVITY_SUCCESS = "xpath=  //td[div[@class='hp-status hp-status-ok']]/following-sibling::td[p/span[contains(text(),'Update')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # %s replace with enclosure namd and time stamp
    ID_NEW_ACTIVITY_ERROR = "xpath=  //td[div[@class='hp-status hp-status-error']]/following-sibling::td[p/span[contains(text(),'Update')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # %s replace with enclosure namd and time stamp
    ID_MAIN_PAGE = "xpath=//*[@id='hp-main-menu-control']/div[2]"
    ID_ERROR_POPUP = "//*[@id='hp-form-message']"
    ID_ERROR_MSG = "//*[@id='hp-form-message']/div[2]/span"
    ID_PROFILE_HARDWARE = "//*[@id='cic-profile-show-serverType']|//*[@id='cic-profile-show-serverType']/a"
    ID_PROFILE_SERVER = "//*[@id='cic-profile-show-server']|//*[@id='cic-profile-show-server']/a"
    ID_PROFILE_ENCLOSUREGROUP = "//*[@id='cic-profile-show-enclosureGroup']/a"
    ID_COPY_SERVER_PROFILE = "link=Copy"
    # Edit Profile
    ID_EDIT_SERVER_PROFILE_NAME = "id=cic-profile-edit-name"
    ID_EDIT_OVERVIEW = "xpath=//div[@id='cic-profile-panel-edit-selector']/div"
    ID_LINK_LOCAL_STORAGE = "link=Local Storage"
    ID_EDIT_SERVER_PROFILE_DESCRIPTION = "id=cic-profile-edit-description"
    ID_EDIT_SERVER_PROFILE_OK = "id=cic-profile-edit-ok"
    ID_EDIT_LOCAL_STORAGE = "id=cic-profile-manage-local-storage"
    ID_EDIT_INITIALIZE_LOCAL_STORAGE = "id=cic-profile-local-storage-initialize"
    ID_SELECT_OK_AFTER_INITIALIZE_LOCAL_STORAGE = "css=footer > div.hp-controls > button.hp-ok.hp-primary"
    ID_EDIT_BOOTABLE = "id=cic-profile-local-storage-bootable"
    ID_COMBO_EDIT_LOGICAL_DRIVE_DROPDOWN = "xpath=//div[@id='cic-profile-local-storage-logical-drive-select-container']/a/span"
    ID_COMBO_EDIT_CONTROLLER_MODE_DROPDOWN = "xpath=//div[@id='cic-profile-local-storage-controller-mode-select-container']/a/span"
    # Validating unassigned profile
    ID_ACTVITY_PROFILE = "xpath = .//*[@id='cic-profile-page']/div[@class='hp-sub-nav']/div[@class='hp-sidebar-control']/div"
    ID_CLICK_ACTIVITY = "xpath = .//div[@class='hp-activity-message']/p/span[text()='Delete']//following::div[text()='%s']"
    ID_PROFILE_UNASSIGNED_SELECT = "xpath = .//div[@class='hp-brief']/div[@class='hp-activity-message']/p/span[text()='Create']//following::div[text()='%s']"
    ID_PROFILE_UNASSIGNED_SUCCESS = "xpath = .//div[@class='hp-status hp-status-ok']/following-sibling::div[@class='hp-activity-message']/p/span[text()='Create']//following::a[text()='%s']"  # %s replace with name of profile
    ID_PROFILE_UNASSIGNED_FAIL = "xpath = .//div[@class='hp-status hp-status-error']/following-sibling::div[@class='hp-activity-message']/p/span[text()='Create']//following::a[text()='%s']"  # %s replace with name of profile
    ID_PROFILE_UNASSIGNED_WARNING = "xpath = .//div[@class='hp-status hp-status-warning']/following-sibling::div[@class='hp-activity-message']/p/span[text()='Create']//following::a[text()='%s']"  # %s replace with name of profile
    # ID_SELECT_DROP_DOWN = "xpath=.//ol/li[3]/div/a"    2015-01-07 Alex Ma replaced this with below, since this xpath identifies 2 elements in 2.0 PB10
    ID_SELECT_DROP_DOWN = "xpath = //*[@id='cic-profile-connection-flexnic-validator']/../a"
#   {2015-03-31 Alex Ma fixed UI change due to OVAQual testing failure
#    ID_SELECT_PORT_DROP_DOWN = "xpath=//select[@id='cic-profile-connection-flexnic']/..//a"
    ID_SELECT_PORT_DROP_DOWN = "xpath=//*[@id='cic-profile-connection-flexnic-input']"
#   }
    # Validation for move profile
    ID_ACTIVITY_PROGRESS_MOVE = "xpath= //tr/td[@class='hp-icon' and div[@class='hp-status hp-status-changing']]/following-sibling::td[@class='hp-name' and p/span[contains(text(),'%s')]]/following-sibling::td/a[contains(text(),'%s')]"  # %s replaces enclosure name
    ID_ACTIVITY_TIMESTAMP_MOVE = "xpath= //td[div[@class='hp-status hp-status-changing']]/following-sibling::td[p/span[contains(text(),'%s')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp]"  # %s replaces with enclosure name
    ID_ACTIVITY_SUCCESS_MOVE = "xpath= //td[div[@class='hp-status hp-status-ok']]/following-sibling::td[p/span[contains(text(),'%s')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # %s replace with enclosure namd and time stamp
    ID_ACTIVITY_WARNING_MOVE = "xpath= //td[div[@class='hp-status hp-status-warning']]/following-sibling::td[p/span[contains(text(),'%s')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # %s replace with enclosure namd and time stamp
    ID_ACTIVITY_ERROR_MOVE = "xpath= //td[div[@class='hp-status hp-status-error']]/following-sibling::td[p/span[contains(text(),'%s')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # %s replace with enclosure namd and time stamp
    ID_MOVE_VALIDATION = "xpath = .//*[@id='cic-profile-show-server']/a"
    # New Objects for Delete Profile
    ID_ACTVITY_PROFILE = "xpath = .//*[@id='cic-profile-page']/div[@class='hp-sub-nav']/div[@class='hp-sidebar-control']/div"
    ID_CLICK_ACTIVITY = "xpath = .//div[@class='hp-activity-message']/p/span[text()='Delete']//following::div[text()='%s']"
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
    ID_MENU_SELECTOR = "xpath=.//*[@id='cic-profile-panel-selector']/div"
    ID_DROPDOWN_SELECT = "xpath=.//*[@id='cic-profile-panel-selector']/ol/li/a[text()='%s']"
    ID_SERVER_HARDWARE = "xpath=.//fieldset/ol/li/label[text()='Server hardware']/following-sibling::div"
    ID_PROFILE_OFF_ERROR = "xpath=.//*[@id='cic-profile-server-power-validator-link']"
    ID_BTN_POWER_PRESS_AND_HOLD = "id=cic-server-press-and-hold"
    ID_SERVER_POWER_OFF_VALIDATE = ".//*[@id='cic-server-power-state' and text()='Off']"
    # Extended MAT
    ID_DROP_DOWN_VAL = "//ul//li//a[text()='%s']"

    ID_LINK_ACTIVITY = "link=Activity"
    ID_SUCCESSFULL_PROFILE_STATUS_IN_Activity = "xpath=//td[div[@class='hp-status hp-status-ok']]/following-sibling::td[p/span[contains(text(),'%s')]]/following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # Activity name and time
    # Fusion1.1 Create Server Profile
    ID_AFFINITY_DROP_DOWN_SELECT = "xpath=//*[@id='cic-profile-panel-add-basic']//span[@class='hp-name' and text()='%s']"
    ID_AFFINITY_DROP_DOWN = "xpath=//*[@id='cic-profile-panel-add-basic']/fieldset/ol/li[6]/div/div/div"
    ID_CHKBOX_SAN_STORAGE = "xpath=//*[@id='cic-profile-add-manage-san']"
    ID_OS_TYPE_DROP_DOWN = "xpath=//*[@id='cic-profile-manage-storage-volumes-container']//span[@class='selectBox-arrow']"
    ID_OS_TYPE_SELECT = "xpath=html//a[text()='%s']"
    ID_ERROR_NO_STORAGE_VOLUMES = "xpath=//*[@id='cic-profile-add-no-volumes']"
    ID_BTN_ADD_STORAGE = "xpath=//*[@id='cic-profile-add-storage-volumes']"
    ID_VOLUME_SELECT_DROPDOWN = "xpath=//*[@id='cic-profile-storage-volume-div']/div/div[2]"
    ID_VOLUME_SELECT = "xpath=//*[@id='cic-profile-storage-volume-div']//span[text()='%s']"
    ID_RADIO_BTN_AUTO = "xpath=//*[@id='cic-profile-storage-lun-auto']"
    ID_RADIO_BTN_MANUAL = "xpaht=//*[@id='cic-profile-storage-lun-manual']"
    ID_TEXT_LUN = "xpath=//*[@id='cic-profile-storage-lun-manual-value']"
    ID_BTN_STORAGE_ADD = "//*[@id='cic-profile-storage-add']"
    ID_LINK_SANSTORAGE = "link=SAN Storage"
    ID_POP_UP_ERROR = "xpath=//*[@id='hp-form-message']/div[2]/p"
    # Edit Storage and add sec shared volume
    ID_EDIT_SAN_COMBO_MENU_VIEW = "xpath=//*[@id='cic-profile-panel-edit-selector']/div"
    ID_EDIT_LINK_SANSTORAGE = "xpath=//a[contains(text(),'SAN Storage')]"
    ID_EDIT_CHKBOX_SAN_STORAGE = "xpath=//*[@id='cic-profile-edit-manage-san']"
    ID_EDIT_BTN_ADD_STORAGE = "xpath=//*[@id='cic-profile-edit-storage-volumes']"

    XP_CREATE_SP_ADD_CONN_BW_DROPDOWN = "//li[@id='cic-profile-connection-bandwidth-discrete-group']/div/a"
    XP_CREATE_SP_ADD_CONN_BW_DD_SELECT = "//div/div[@id='cic-modal-dialog-body']/parent::div/following-sibling::ul[last()-1]/li/a[text()='%s']"
#   {2015-03-31 Alex Ma fixed UI change due to OVAQual testing failure
#    XP_CREATE_SP_ADD_CONN_NIC_DD_SELECT = "//div/div[@id='cic-modal-dialog-body']/parent::div/following-sibling::ul[last()]/li/a[text()='%s']"
    XP_CREATE_SP_ADD_CONN_NIC_DD_SELECT = "//*[@id='cic-profile-connection-port-config-group']/descendant::li/span[text()='%s']"
#    XP_CREATE_SP_ADD_CONN_BOOT_DD_SELECT = "//div/div[@id='cic-modal-dialog-body']/parent::div/following-sibling::ul[last()%s]/li/a[text()='%s']"
    XP_CREATE_SP_ADD_CONN_BOOT_DD_SELECT = "//div/div[@id='cic-modal-dialog-body']/parent::div/following-sibling::ul[last()]/li/a[text()='%s']"
#   }
    ID_ITEM_STATUS_CHANGING = "xpath=//div[@class='dataTables_scrollBody']/table/tbody/tr/td[.='%s']/../td//div[contains(@class, 'hp-status-changing')]"
    ID_ITEM_STATUS_OK = "xpath=//div[@class='dataTables_scrollBody']/table/tbody/tr/td[.='%s']/../td//div[contains(@class, 'hp-status-ok')]"
    ID_ITEM_STATUS_ERROR = "xpath=//div[@class='dataTables_scrollBody']/table/tbody/tr/td[.='%s']/../td//div[contains(@class, 'hp-status-error')]"
    ID_ITEM_STATUS_WARN = "xpath=//div[@class='dataTables_scrollBody']/table/tbody/tr/td[.='%s']/../td//div[contains(@class, 'hp-status-warning')]"

    ID_ITEM_NAME = "xpath=//div[@class='dataTables_scrollBody']/table/tbody/tr/td[.='%s']/../td//span"
    ID_CHKBOX_MANAGE_INTEGRATED_CONTROLLER = "xpath=//*[@id='cic-profile-manage-local-storage-manage-integrated-controller']"

    ID_TEMPLATE_LIST = "xpath=//div[@class='dataTables_scrollBody']/table"
    ID_TEMPLATE_CHANGING = ID_TEMPLATE_LIST + "/tbody/tr//div[@class='hp-status hp-changing']"
    ID_TEMPLATE_EDIT_COMPLETE = "//header[@class='hp-notification-summary']/div[@class='hp-state' and text()='Completed']"
    ID_TEMPLATE_EDIT_INPROCESS = "//header[@class='hp-notification-summary']/div[@class='hp-state']/div[@class-'hp-progress']"
    ID_TEMPLATE_EDIT_VERIFY = "id=hp-form-message"
    ID_TEMPLATE_LIST_NAMES = ID_TEMPLATE_LIST + '/tbody/tr/td[2]'

    # Edit Rpofile template
    ID_LINK_EDIT_PROFILE_TEMPLATE = "link=Edit"
    ID_INPUT_EDIT_TEMPLATE_NAME = "id=cic-profile-edit-name"
    ID_COMBO_EDIT_MENU = "css=#cic-profile-panel-edit-selector > div.hp-value"
    ID_LINK_EDIT_PROFILE_NETWORKS = "xpath = //table[@id='cic-profile-panel-edit-networks']//td/*[contains(text(), '%s')]"
    ID_BTN_EDIT_TEMPLATE_OK = "id=cic-profile-edit-ok"
    ID_ELEMENT_TEMPLATE_NAME_BASE = "xpath=//td[text()='%s']"
    ID_ELEMENT_EDIT_WARNING = "xpath = //div[@class='hp-status hp-status-warning']/following-sibling::span"
    ID_CONNECTION_ERROR = "xpath = //label[@class='hp-error' and @generated='true']"
    ID_ELEMENT_RIGHT_PIN = "xpath = //div[@id='cic-profile-templates-page']/div[@class='hp-sub-nav']//div[@class='hp-pin-right']"
