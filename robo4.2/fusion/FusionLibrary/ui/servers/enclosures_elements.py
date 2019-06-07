'''
Created on  Jun 17, 2013

This file   contains all element ID on  Fusion enclosures page/screen
'''

__version__ = "$Revision: 98f42236d1af $"
# $Source$


class FusionEnclosuresPage(object):
    ID_PAGE_LABEL = "//div[@class='hp-page-label']/h1[text()='Enclosures']"
    ID_ENCLOSURE_LIST = "xpath=//div[@class='dataTables_scroll']//table"
    ID_ENCLOSURE_LIST_NAMES = ID_ENCLOSURE_LIST + '/tbody/tr/td[2]'
    ID_LINK_ADD_ENCLOSURE = "link=Add enclosure"
    ID_ELEMENT_ENCLOSURE_BASE = "xpath=//td[@class='' and text()='%s']"  # replace %s with Enclosure
    ID_INPUT_ENCLOSURE_IP_ADDRESS = "id=cic-enclosure-hostname"
    ID_SELECT_ADD_AS_MANAGED = "id=cic-enclosure-addas-managed"
    ID_SELECT_ADD_AS_MONITORED = "id=cic-enclosure-addas-monitored"
    ID_INPUT_OA_USERNAME = "id=cic-enclosure-username"
    ID_INPUT_OA_PASSWORD = "id=cic-enclosure-password"
    ID_COMBO_ENCLOSURE_GROUP = "css=div.hp-search-combo-control"
    ID_INPUT_ENCLOSURE_NEW_GROUP = "cic-enclosure-new-group"
    ID_INPUT_ENCLOSURE_GROUP = "cic-enclosure-group-select-input"
    # ID_COMBO_ENCLOSURE_GROUP_LIST = "xpath=//span[@class='hp-name' and text()='%s']"  # Replace %s with enclosure Group
    ID_BTN_ENCLOSURE_ADD = "id=cic-enclosure-add"
    ID_BTN_ENCLOSURE_ADD_PLUS = "id=cic-enclosure-addplus"
    ID_BTN_ENCLOSURE_CANCEL = "cic-enclosure-add-cancel"
    ID_ACTION_MAIN_BTN = "xpath=//div[@id='cic-enclosure-actions']"
    ID_MENU_ACTION_ADD_ENCLOSURE = "id=cic-enclosure-add-action"
    ID_MENU_ACTION_UPDATE_FIRMWARE = "id=cic-enclosure-editFirmware-action"
    ID_MENU_ACTION_REMOVE = ID_ACTION_MAIN_BTN + "//a[text()='Remove']"
    ID_BTN_CONFIRM_REMOVE = "id=cic-enclosure-remove-action"
    ID_BTN_REMOVE_CANCEL = "css=button.hp-cancel"
    ID_ENCLOSURE_ACTION_REMOVE = "id=cic-enclosure-remove-action"
    ID_BTN_CANCEL_REMOVE_ENCLOSURE = "css=button.hp-cancel"
    ID_BTN_CONFIRM_REMOVE_ENCLOSURE = "css=button.hp-ok.hp-primary"

    ID_ADD_ENCLOSURE_GREEN = "//table[@id='DataTables_Table_0']/tbody/tr/td[text()='%s']/../td/div[@class='hp-status hp-status-ok']"

    # Newly added
    ID_BTN_CONFIRM_REMOVE_ENCLOSURE = "xpath=//button[text()='Yes, remove']"
    ID_CHKBOX_FORCE_ADD_ENCLOSURE = "id=cic-enclosure-force"
    ID_DLG_ENCLOSURE_REMOVE = "hp-enclosure-remove-dialog"
    ID_LINK_ENCLOSURE_NAME = "xpath=//table//td[text()='%s']"
    ID_ENCLOSURE_ITEM_IN_TABLE = "xpath=//div[@class='dataTables_scrollBody']//table//td[.='%s']"

    ID_BTN_EDIT_OK_LIG = "id=cic-switch-template-edit-ok-button"
    ID_BTN_EDIT_CANCEL_LIG = "id=cic-switch-template-edit-cancel-button"
    ID_BTN_CANCEL_ADD_ENCLOSURE = "xpath=//*[@id='hp-body-div']//footer/div/button[text()='Yes, discard group and cancel adding the enclosure']"

    ID_ENCLOSURE_PAGE_LABEL = "xpath=//div[@class='hp-page-label']/h1[text()='Enclosures']"
    ID_ADD_ENCLOSURE_NOTIFICATION = "xpath=//*[@id='hp-form-message']/div/div[@class='hp-status hp-status-error']/span[text()='error']"
    ID_ADD_ENCLOSURE_STATUS_CHANGING = "xpath=//*[@id='DataTables_Table_0']//div[@class='hp-status-changing']"
    ID_DELETE_ENCLOSURE_NOTIFICATION = "xpath=//div[@id='hp-enclosure-remove-dialog']/header/h1"
    ID_ADD_ENCLOSURE_NOTIFICATION_CONTENT = "xpath=//*[@id='hp-form-message']/div[@class='hp-form-message-details']"

    ID_COMBO_ENCLOSURE_LIG = "xpath=//*[@id='cic-enclosure-lst-fields']//div[@class='hp-search-combo-control']"
    ID_LINK_SEARCH_FOR_ANOTHER = "link=Search for another"
    ID_COMBO_ENCLOSUE_LIG_LIST = "xpath=//*[@id='cic-enclosure-lst-fields']//span[@class='hp-name' and text()='%s']"
    ID_INPUT_ENCLOSURE_LIG = "id=cic-enclosure-lst-select-input"
    # ID_COMBO_FIRMWARE_BASELINE = "xpath=//*[@id='cic-enclosures-add-panels']//span[@class='selectBox-label']"
    ID_COMBO_FIRMWARE_BASELINE = "xpath=//*[@id='cic-enclosures-add-panels']//div[@class='hp-value']"
    ID_COMBO_FIRMWARE_BASELINE_LIST = "xpath=//ul/li/a[text()='%s']"
    ID_BTN_LICENSING_ONEVIEW = "id=cic-enclosure-licensing-oneview-advanced"
    ID_BTN_LICENSING_ONEVIEW_NOILO = "id=cic-enclosure-licensing-oneview-noilo"
    ID_COMBO_ENCLOSURE_GROUP_LIST = "xpath=//*[@id='cic-enclosure-group-fields']//span[@class='hp-name' and text()='%s']"

    ID_ENCLOSURE_STATUS_OK = "xpath=//*[@id='cic-enclosure-details-status']//span[@class='hp-value' and text()='ok']"
    ID_ENCLOSURE_STATUS_ERROR = "xpath=//*[@id='cic-enclosure-details-status']//span[@class='hp-value' and text()='error']"
    ID_ENCLOSURE_STATUS_WARNING = "xpath=//*[@id='cic-enclosure-details-status']//span[@class='hp-value' and text()='warning']"
    ID_ENCLOSURE_STATUS_CHANGING = "xpath=//*[@id='cic-enclosure-details-status']/div[@class = 'hp-status-changing']"
    # View
    ID_COMBO_MENU_VIEW_ = "css=div.hp-value"
    ID_COMBO_MENU_OVERVIEW = "xpath=//*[@id='cic-enclosure-panel-selector']/descendant::div[@class='hp-value' and text()='Overview']"
    ID_LINK_OVERVIEW = "link=Overview"
    ID_LINK_GENERAL = "link=General"
    ID_LINK_HARDWARE = "link=Hardware"
    ID_LINK_DEVICE_BAYS = "link=Device Bays"
    ID_LINK_FAN_BAYS = "link=Fan Bays"
    ID_LINK_INTERCONNECT_BAYS = "link=Interconnect Bays"
    ID_LINK_UTILIZATION = "id=cic-enclosure-utilization-selector"
    ID_LINK_ALERTS = "css=li.hp-selected > a.hp-anchor-uri"
    ID_LINK_RELATED = "link=Related"

    # Enclosure Firmware Update

    # ID_BTN_CONFIRM_UPDATE_FIRMWARE = "id=cic-enclosure-edit-ok"
    ID_BTN_CONFIRM_UPDATE_FIRMWARE = "id=cic-enclosure-fw-edit-ok"
    ID_BTN_ENCLOSURE_FIRMWARE_CANCEL = "id=cic-enclosure-edit-cancel"
    ID_SELECT_ENCLOSURE = "xpath=//td[text()='%s']"  # replace with enclosure name
    ID_ENCLOSURE_FIRMWARE_STATE_COMPLETE_MANUAL = "xpath=//tr[1]/td[@class='hp-name' and p/span[contains(text(),'Update firmware')]]/following-sibling::td[@date-timestamp]/following-sibling::td/span[contains(text(),'Completed')]"
    ID_ENCLOSURE_ADD_BUTTON = "xpath=.//a[@class='hp-button hp-secondary']"
    ID_LINK_CLICK_UPDATE_FIRMWARE = "xpath=//a[contains(text(),'Update Firmware')]"
    ID_ENCLOSURE_TITLE = "xpath=.//*[@id='cic-enclosure-details-title' and text()='%s']"  # %s will be replace with name of the enclosure
    ID_ENCLOSURE_FIRMWARE_STATE_START = "xpath=//tr/td[@class='hp-name' and p/span[contains(text(),'Update firmware')]]/following-sibling::td[@date-timestamp]/following-sibling::td/span[contains(text(),'Starting')]"
    ID_ENCLOSURE_FIRMWARE_STATE_COMPLETE = "xpath=//tr/td[@class='hp-name' and p/span[contains(text(),'Update firmware')]]/following-sibling::td[@date-timestamp]/following-sibling::td/span[contains(text(),'Completed')]"
    ID_COMBO_BOX_UPDATE_FIRMWARE_FOR = "xpath=.//*[@id='cic-enclosure-firmware-update-for']/label[text()='Update firmware for']/following-sibling::a"
    # ID_COMBO_BOX_FIRMWARE_BASELINE = "xpath=.//*[@id='cic-enclosure-edit-form']/div[@class='hp-form-contents']/fieldset/ol/li[@class='hp-form-item']/a[@class='selectBox hp-select selectBox-dropdown']/span[2]"
    ID_COMBO_BOX_FIRMWARE_BASELINE = "xpath=.//*[@id='cic-enclosure-edit-form-contents']//span[@class='selectBox-label']"
    ID_COMBO_BOX_SELECT_FIRMWARE = "xpath=.//ul[@class='selectBox-dropdown-menu selectBox-options']/li/a[text()='%s']"  # %s selects  firmware baseline

    ID_ACTIVITY_OVERVIEW = "xpath=.//*[@id='cic-enclosure-panel-selector']/div[@class='hp-value' and contains(text(),'Overview')]"
    ID_ACTIVITY_ACTIVITY = "xpath=(//a[contains(text(),'Activity')])[2]"
    ID_ACTIVITY_FIRMWARE_SUCCESS = "xpath=//tr/td[@class='hp-icon' and div[@class='hp-status hp-status-ok']]/following-sibling::td[@class='hp-name' and p/span[contains(text(),'Update firmware')]]/following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # %s will be replaced with time stamp
    ID_ACTIVITY_TIMESTAMP = "xpath=//tr/td[@class='hp-icon' and div[@class='hp-status hp-status-unknown']]/following-sibling::td[@class='hp-name' and p/span[contains(text(),'Update firmware')]]/following-sibling::td[@date-timestamp]"
    ID_ACTIVITY_FIRMWARE_WARNING = "xpath=//tr/td[@class='hp-icon' and div[@class='hp-status hp-status-warning']]/following-sibling::td[@class='hp-name' and p/span[contains(text(),'Update firmware')]]/following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # %s will be replaced with time stamp

    ID_ACTIVITY_MANUALLY_VALIDATION = "xpath=//tr[1]/td[@class='hp-icon' and div[@class='hp-status hp-status-ok']]/following-sibling::td[@class='hp-name' and p/span[contains(text(),'Update firmware')]]"
    ID_ACTIVITY_FIRMWARE_VALIDATION = "xpath=//tr/td[@class='hp-icon' and div[@class='hp-status hp-status-unknown']]/following-sibling::td[@class='hp-name']/p/span[contains(text(),'Update firmware')]"

    # Enclosure Update Firmware Validation

    ID_NEW_ACTIVITY_PROGRESS = "xpath= //tr/td[@class='hp-icon' and div[@class='hp-status hp-status-changing']]/following-sibling::td[@class='hp-name' and p/span[contains(text(),'Update firmware')]]/following-sibling::td/a[contains(text(),'%s')]"  # %s replaces enclosure name
    ID_NEW_ACTIVITY_TIMESTAMP = "xpath= //td[div[@class='hp-status hp-status-changing']]/following-sibling::td[p/span[contains(text(),'Update firmware')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp]"  # %s replaces with enclosure name
    ID_NEW_ACTIVITY_SUCCESS = "xpath=  //td[div[@class='hp-status hp-status-ok']]/following-sibling::td[p/span[contains(text(),'Update firmware')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # %s replace with enclosure namd and time stamp
    ID_NEW_ACTIVITY_WARNING = "xpath=  //td[div[@class='hp-status hp-status-warning']]/following-sibling::td[p/span[contains(text(),'Update firmware')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # %s replace with enclosure namd and time stamp
    ID_NEW_ACTIVITY_ERROR = "xpath=  //td[div[@class='hp-status hp-status-error']]/following-sibling::td[p/span[contains(text(),'Update firmware')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # %s replace with enclosure namd and time stamp
    ID_MAIN_PAGE = "id= hp-main-menu-control"

    ID_ADD_ENCLOSURE_MSG = "xpath=.//*[@id='hp-form-message']/div[1]/span[@class='hp-form-message-text']"
    ID_ADDENCLOSURE_TIMESTAMP = "xpath=.//*/div[1]/header/div[@class='hp-aside']/div[@class='hp-timestamp']"
    ID_ACTIVITY_COLLAPSE = "xpath=//td[@date-timestamp and contains(text(),'%s')]//preceding-sibling::td[a[text()='%s']]/preceding-sibling::td[p/span[contains(text(),'Add')]]/preceding-sibling::td/div[@class='hp-collapser']"
    ID_ACTIVITY_NOTIFY_DETAILS = "xpath=.//tbody/tr/td/div/table/tbody/tr[td/span[text()='Add'] and td/a[text()='%s']]/following::*[1]/td//div/p/span[contains(text(),'License server hardware for ')]"
    ID_ACTIVITY_NOTIFY_CONTAINER = "xpath=.//*[@id='hp-activities']/tbody/tr[@class='hp-row-details-row hp-selected']/td/div/div[@class='hp-task-notification-container']"
    ID_DEVICE_BAYS = "xpath=.//*[@id='cic-enclosure-show-bladebays']//ol[1]/li[1]/label"
    ID_FIRST_DEVICE_BAY = "xpath=//table[@id='cic-enclosure-more-devbays-table']/tbody/tr[1]/td[3]/a"

    ID_ELEMENT_LI_NAME = "xpath=//td[@class='cic-enclosure-icm-ls-name']/a[text()='%s-LI']"
    ID_BAY_LOCATION = "xpath=.//*[@id='cic-enclosure-show-switchbays']//li[@class='hp-bay']//div/a[text()='%s']/ancestor::li[1]/label"
    ID_OA_IP = "xpath=.//*[@id='cic-enclosure-more-oa-active-hostname']/a"
    ID_GENERAL_VIEW = "xpath=.//fieldset/ol/li/label[text()='%s']/following-sibling::div"
    ID_MENU_SELECTOR = "xpath=.//*[@id='cic-enclosure-panel-selector']/div"
    ID_DROPDOWN_SELECT = "xpath=.//*[@id='cic-enclosure-panel-selector']/ol/li/a[text()='Hardware']"

    # FAN UI overview - Chassis Rear View
    ID_ELEMENT_OVERVIEW_FAN_TABLE = "xpath=//*[@id='cic-enclosure-show-switchbays']"
    ID_ELEMENT_OVERVIEW_FAN_BAY = "xpath=//*[@id='cic-enclosure-show-switchbays']/descendant::div/a[text()='fan %s']/ancestor::div[1]/../.."
    # Replace with fan bay number
    ID_LINK_OVERVIEW_TOOLTIP_FAN_BAY = "link=fan %s"
    # Replace with fan bay number
    ID_ELEMENT_TOOLTIP_FAN_HEALTH_STATUS = "xpath=//div[@id='cic-enclosure-show-switchbays']/descendant::div/a[text()='fan %s']/../preceding-sibling::div[contains(@class,'hp-status hp-status')]/span"
    # Replace with fan bay number
    ID_ELEMENT_TOOLTIP_FAN_MODEL = "xpath=//div[@id='cic-enclosure-show-switchbays']/descendant::div/a[text()='fan %s']/../following-sibling::div[contains(text(),'Fan')]"
    # Replace with fan bay number
    ID_ELEMENT_FAN_ROW = "xpath=//*[@id='cic-enclosure-show-switchbays']/ol[@class='hp-fan-bays']"
    ID_ELEMENT_FAN_NAME_ROW = ID_ELEMENT_FAN_ROW + "//li/div/div[@class='hp-device-name']/a"
    ID_ELEMENT_FAN_STATUS_ROW = ID_ELEMENT_FAN_ROW + '//li/div/div[contains(@class,"hp-status hp-status")]/span'
    ID_ELEMENT_FAN_STATE_ROW = ID_ELEMENT_FAN_ROW + "//li/div/div[contains(@class,'hp-secondary')]"
    ID_ELEMENT_FAN_MODEL_ROW = "xpath=//*[@id='cic-enclosure-show-switchbays']/ol[@class='hp-fan-bays']//li/div/div[contains(@class,'hp-secondary') and text()='Active Cool 200 Fan'] | //*[@id='cic-enclosure-show-switchbays']/ol[@class='hp-fan-bays']//li/div/div[@class='hp-unset' and text()='empty'] | //*[@id='cic-enclosure-show-switchbays']/ol[@class='hp-fan-bays']//li/div/div[@class='hp-secondary cic-enclosure-fan-model' and text()='']"

    # FAN UI details page
    ID_PAGE_FAN_LABEL = "xpath=//*[@id='cic-enclosure-more-fans']/label"
    ID_ELEMENT_PANEL_SELECTOR = "id=cic-enclosure-panel-selector"
    ID_LABEL_FANS_REQUIRED = "xpath=//*[@id='cic-enclosure-more-fans']//label[text()='Fans required']"
    ID_LABEL_DEVICE_BAYS_COOLED = "xpath=//*[@id='cic-enclosure-more-fans']//label[text()='Device bays cooled']"
    ID_ELEMENT_NUMBER_OF_FANS = "id=cic-enclosure-more-fansrequired"
    ID_ELEMENT_NUMBER_OF_DEVICES = "id=cic-enclosure-more-devbayscooled"
    ID_ELEMENT_DETAILS_FAN_TABLE = "xpath=//table[@id='cic-enclosure-more-fanbays-table']"
    ID_ELEMENT_FAN_HEADER_LIST = ID_ELEMENT_DETAILS_FAN_TABLE + '//thead/tr/td'
    ID_ELEMENT_FAN_BAY_LIST = "xpath=//table[@id='cic-enclosure-more-fanbays-table']//tbody/tr/td[2]"
    ID_ELEMENT_FAN_STATE_LIST = "xpath=//table[@id='cic-enclosure-more-fanbays-table']//tbody/tr/td[3]"
    ID_ELEMENT_FAN_HLTICON_LIST = "xpath=//*[@id='cic-enclosure-more-fanbays-table']/tbody/tr[%s]/td[1]/div/span[@class='hp-value']"
    ID_ELEMENT_FAN_REQUIRED_LIST = "xpath=//table[@id='cic-enclosure-more-fanbays-table']//tbody/tr/td[4]"
    ID_ELEMENT_FAN_MODEL_LIST = "xpath=//table[@id='cic-enclosure-more-fanbays-table']//tbody/tr/td[5]"
    ID_ELEMENT_FAN_PART_NUMBER_LIST = "xpath=//table[@id='cic-enclosure-more-fanbays-table']//tbody/tr/td[6]"
    ID_ELEMENT_FAN_SPARE_PART_NUMBER_LIST = "xpath=//table[@id='cic-enclosure-more-fanbays-table']//tbody/tr/td[7]"

    # Power Supply Overview - Chassis Front View

    ID_POWERSUPPLY_BAYS = "xpath=//*[@id='cic-enclosure-show-bladebays']//ol[@class='hp-power-bays']"
    ID_POWERSUPPLY_POPUP = ID_POWERSUPPLY_BAYS + '//li[%s]/div[@class="hp-device"]'                     # replace with PS bay number
    ID_POWERSUPPLY_BAY_NUMBER = ID_POWERSUPPLY_BAYS + '//li[%s]/div/div'                                # replace with PS bay number
    ID_POWERSUPPLY_HEALTH_POPUP = ID_POWERSUPPLY_BAYS + '//li[%s]/div/div[1]'                           # replace with PS bay number
    ID_POWERSUPPLY_MODEL_POPUP = ID_POWERSUPPLY_BAYS + '//li[%s]/div/div[@class="hp-secondary"]'        # replace with PS bay number
    ID_POWERSUPPLY_NAME_POPUP = ID_POWERSUPPLY_BAYS + '//li[%s]/div/div[@class="hp-device-name"]/a'     # replace with PS bay number
    ID_POWERSUPPLY_HEALTH = ID_POWERSUPPLY_BAYS + '//li/div/div[1]//span[@class="hp-value"]'
    ID_POWERSUPPLY_MODEL = "xpath=//*[@id='cic-enclosure-show-bladebays']/ol[@class='hp-power-bays']//li/div/div[@class='hp-secondary'] | //*[@id='cic-enclosure-show-bladebays']/ol[@class='hp-power-bays']//li/div/div[@class='hp-unset']"
    ID_POWERSUPPLY_NAME = ID_POWERSUPPLY_BAYS + '//li/div/div[@class="hp-device-name"]/a'
    ID_LINK_POWERSUPPLY_DETAILS = ID_POWERSUPPLY_BAYS + '//li[%s]/div/div[@class="hp-device-name"]/a'   # replace with PS bay number

    # Power Supply Details

    ID_POWERSUPPLY_LIST = "xpath=//table[@id='cic-enclosure-more-power-supply-bays-table']"
    ID_POWERSUPPLY_LIST_HEADER = ID_POWERSUPPLY_LIST + '//thead/tr/td'
    ID_POWERSUPPLY_LIST_BAYS = ID_POWERSUPPLY_LIST + '//tbody/tr/td[2]'
    ID_POWERSUPPLY_LIST_HEALTH = ID_POWERSUPPLY_LIST + '//tbody/tr/td[1]//span[@class="hp-value"]'
    ID_POWERSUPPLY_LIST_MODEL = ID_POWERSUPPLY_LIST + '//tbody/tr/td[3]'
    ID_POWERSUPPLY_LIST_SERNUM = ID_POWERSUPPLY_LIST + '//tbody/tr/td[4]'
    ID_POWERSUPPLY_LIST_PARTNUM = ID_POWERSUPPLY_LIST + '//tbody/tr/td[5]'
    ID_POWERSUPPLY_LIST_SPAREPARTNUM = ID_POWERSUPPLY_LIST + '//tbody/tr/td[6]'

    ID_POWERSUPPLY_DETAILS_LINK = "xpath=//*[@id='cic-enclosure-panel-selector']//a[contains(text(),'Power Supply Bays')]"
    ID_POWERSUPPLY_BAYS_LABEL = "xpath=//*[@id='cic-enclosure-more-power-supply-bays']/label"
    ID_POWERSUPPLY_DETAILS_HEALTH_ICON = "xpath=//*[@id='cic-enclosure-more-power-supply-bays-table']/tbody/tr[%s]/td[1]/div[contains(@class,'hp-status hp-status')]/span"  # replace with PS bay number
    ID_POWERSUPPLY_DETAILS_BAY = "xpath=//*[@id='cic-enclosure-more-power-supply-bays-table']/tbody/tr[%s]/td[2]"                   # replace with PS bay number
    ID_POWERSUPPLY_DETAILS_MODEL = "xpath=//*[@id='cic-enclosure-more-power-supply-bays-table']/tbody/tr[%s]/td[3]"                 # replace with PS bay number
    ID_POWERSUPPLY_DETAILS_SERIAL_NUMBER = "xpath=//*[@id='cic-enclosure-more-power-supply-bays-table']/tbody/tr[%s]/td[4]"         # replace with PS bay number
    ID_POWERSUPPLY_DETAILS_PART_NUMBER = "xpath=//*[@id='cic-enclosure-more-power-supply-bays-table']/tbody/tr[%s]/td[5]"           # replace with PS bay number
    ID_POWERSUPPLY_DETAILS_SPARE_PART_NUMBER = "xpath=//*[@id='cic-enclosure-more-power-supply-bays-table']/tbody/tr[%s]/td[6]"     # replace with PS bay number

    # Enclosure General View Objects
    ID_TABLE_ENCLOSURE_NAMES = "xpath=//*[@id='DataTables_Table_0']/tbody/tr/td[2]"
    ID_FRAME_ENCL_GENERAL_HARDWARE = "id=cic-enclosure-more-hardware"
    ID_LINK_ENCL_GENERAL_IPV4 = "id=cic-enclosure-more-oa-active-ipv4"
    ID_BTN_ENCL_VIEW_SELECTORS = "id=cic-enclosure-panel-selector"
    ID_SEL_ENCL_GENERAL_VIEW = "xpath=.//*[@id='cic-enclosure-panel-selector']/ol/li[2]/a"
    ID_CLICK_LOGICAL_ENCLOSURE = "xpath=//div[@id='cic-enclosure-details-logical-enclosure']/a"

    ID_CLICK_OVERVIEW = "xpath=//div[@id='cic-enclosure-panel-selector']/div"
    ID_SELECT_INTERCONNECTBAYS = "link=Interconnects"
    ID_SELECT_INTERCONNECT = "xpath= //table[@class='cic-enclosure-icm-inner-table dataTable']/tbody/tr[1]/td/a[text()='%s']"

    ID_BAY_NUMBER = "xpath =//*[@id='cic-enclosure-icbays-table']/tbody/tr[1]/td[1]"
    ID_LINK_RESET = "link=Reset"

    # Enclosure Edit Objects
    TIMEOUT = 15
    ID_LINK_ENCLOSURE_EDIT = "xpath=//a[contains(text(),'Edit')]"
    ID_BTN_ENCLOSURE_EDIT_OK = "xpath=//*[@id='cic-enclosure-update']"
    ID_BTN_ENCLOSURE_EDIT_CANCEL = "xpath=//*[@id='cic-enclosure-edit-cancel']"
    IN_INPUT_ENCLOSURE_NAME_EDIT = "xpath=//*[@id='cic-enclosure-name']"
    ID_ERR_SPECIAL_ENCL_NAME = "xpath=//label[contains(text(),'32 or fewer alphanumeric, dash, or underscore characters.')]"
    ID_ERR_APLHABET_LIMIT_ENCL_NAME = "xpath=//label[contains(text(),'Enter no more than 32 characters.')]"
    ID_ERR_EXISTING_ENCL_NAME_UNABLE = "xpath=//span[contains(text(),'Unable to update enclosure. Resolve the following issues to proceed.')]"
    ID_ERR_ALREADY_INUSE_ENCL_NAME_UNABLE = "xpath=//span[contains(text(),'The enclosure name specified is already used by another enclosure.')]"
    ID_ERR_UNIQUE_ENCL_NAME_UNABLE = "xpath=//span[contains(text(),'Please specify a unique enclosure name.')]"
    ID_RESET = "xpath = //a[text()='Reset']"
    ID_DROPDOWN = "xpath = //div[@id='cic-enclosure-panel-selector']"
    ID_DROPDOWN_SELECT_LABEL = ID_DROPDOWN + "/descendant::li/a[text()='Labels']"
    ID_EDIT_LABEL = "xpath = //li[@id='hp-labels-show-panel']/label/a[@class='hp-panel-edit' and text()='Edit']"
    ID_LABEL = "xpath = //li[@id='hp-labels-show-panel']/label/span[text()='Labels']"
    ID_EDIT_LABEL_PANEL = "xpath = //header[@id='hp-labels-edit-header']/h1/span[text()='Edit Labels']"
    ID_LABEL_NAME = "xpath = //input[@id='hp-labels-edit-search-input']"
    ID_ADD_LABEL_BTN = "xpath = //button[@id='hp-labels-edit-add']"
    ID_OK_LABEL_BTN = "xpath = //input[@id='hp-labels-edit-ok']"
    ID_ADDED_LABEL = "xpath = //table[@id='hp-labels-show-table']/descendant::a[text()='%s']"
    ID_ALL_ENCLOSURE_LIST = "xpath = //tbody/tr/td[2]"
    ID_MULTIPLE_ENCLOSURE_TITLE = "xpath = //h1[@id='cic-enclosure-details-title' and text()='%s Enclosures']"
    ID_UPDATE_FROM_GROUP_ACTION = "xpath = //a[text()='Update from group']"
    ID_MUTIPLE_SELECT_MESSAGE = "xpath = //div[@id='cic-enclosure-multiple-items-message' and text()='%s']"
    ID_UPDATE_FROM_GROUP_PANEL = "xpath = //span[text()='Update from Group']"
    ID_UPDATE_FROM_GROUP_BUTTON = "xpath = //input[@id='cic-enclosure-update-from-group-confirm']"
    ID_ENCLOSURES_COUNT = "xpath = //li/div/descendant::div[@class='hp-activity-source']"
    ID_ACTION_SELECTION = "xpath = //div[div[p/span[text()='%s']]/following-sibling::div[text()='%s']]"
    ID_UPDATE_ERROR_NUMBER = "xpath = //ol[@id='hp-flyout-activities']/li/descendant::div[@class='hp-details']"
    ID_SIDEBAR_CONTROL = "xpath = //div[@id='cic-enclosures-page']/descendant::div[@class='hp-sidebar-control']/div"
    ID_ACTION_STATUS = "xpath = //div[div[p/span[text()='%s']]/following-sibling::div[text()='%s']]/div[@class='hp-status hp-status-changing']"
    ID_LABEL_SEARCH = "xpath = //tbody/tr/td/label[text()='%s']"
    ID_DELETE_BUTTON = "xpath = //label[text()='%s']/ancestor::tr/td/div[@class='hp-close']"
    ID_EMPTY_LABEL = "xpath = //div[text()='no labels']"
    ID_REFRESH_ENCLOSURE_NOTIFICATION = "xpath=//*[@id='hp-page-notifications']/div[1]/header"
    ID_MENU_ACTION_REFRESH = "xpath=//*[@id='cic-enclosure-refresh-action']"
    ID_PROGRESS = "xpath=//*[@id='hp-page-notifications']/div[1]/header/div[4]/div"

    ID_MAIN_DASHBOARD_XPATH = "xpath=//*[@id='hp-main-menu-label']"
    ID_ENCLOSURE_LINK_XPATH = "link=Enclosures"
    ID_XPATH_FIND_ENCLOSURE_ONE = "xpath=//table/tbody/tr[not(contains(@class, 'hp-not-found'))]/td[text()='%s']"
    ID_XPATH_SELECTOR_ENC = "//*[@id='cic-enclosure-panel-selector']"
    ID_XPATH_NEG_TEXT_ENC = "//*[@class='hp-details-show-view hp-active']//*[@class='hp-task-notification-container']//*[@class='hp-details']//*[text()='No update required. Selected firmware is already installed for the Onboard Administrator.']"

    ID_XPATH_ADD_BUTTON_ACTIVITY_XPATH = "//tbody/tr[td[@class='hp-name']//span[text()='Add']][1]//following::tr[td[@class='hp-status-name']//*[text()='Update firmware']]//parent::td/following-sibling::td[@class='hp-source']/a[text()='SGH420HHYA-LIG_B1-1']"
    ID_XPATH_ADD_BTN_TEXT_ENC = "//tbody/tr[td[@class='hp-name']//span[text()='Add']][1]//following::tr[td[@class='hp-status-name']//*[text()='Update firmware']]//parent::td/following-sibling::td[@class='hp-source']/a[text()='SGH420HHYA-LIG_B1-1']//parent::td/following-sibling::td[@class='hp-state']"

    ID_XPATH_ADD_TEXT = "//tbody/tr[td[@class='hp-name']//span[text()='Add']][1]"
    ID_XPATH_CHECK_FOR_OVERALL_TEXT = "//tbody/tr[td[@class='hp-name']//span[text()='Add']][1]//following::tr[td[@class='hp-status-name']//*[text()='Update firmware']]//parent::td/following-sibling::td[@class='hp-source']/a[text()='SGH420HHYA-LIG_B1-1']//following::node()[@class='hp-details'][1]"
    ID_XPATH_ISSUE_VISIBLE_DETAILES = "//tbody/tr[td[@class='hp-name']//span[text()='Add']][1]//following::tr[td[@class='hp-status-name']//*[text()='Update firmware']]//parent::td/following-sibling::td[@class='hp-source']/a[text()='SGH420HHYA-LIG_B1-1']//following::node()[@class='hp-details'][1]/following-sibling::div[@class='hp-details-correlations-container']//div[@class='hp-details-container']//p"
    ID_GET_TEXT_ISSUE = "//tbody/tr[td[@class='hp-name']//span[text()='Add']][1]//following::tr[td[@class='hp-status-name']//*[text()='Update firmware']]//parent::td/following-sibling::td[@class='hp-source']/a[text()='SGH420HHYA-LIG_B1-1']//following::node()[@class='hp-details'][1]/following-sibling::div[@class='hp-details-correlations-container']//div[@class='hp-details-container']//p"

    ID_RESOLUTION_XPATH = "//tbody/tr[td[@class='hp-name']//span[text()='Add']][1]//following::tr[td[@class='hp-status-name']//*[text()='Update firmware']]//parent::td/following-sibling::td[@class='hp-source']/a[text()='SGH420HHYA-LIG_B1-1']//following::node()[@class='hp-details'][1]/following-sibling::div[@class='hp-details-correlations-container']//div[@class='hp-resolution-container']//p"

    ID_ACTIVITY = "link=Activity"
    ID_LE_ACTIVITY_RESOURCE_VIEW = "id=hp-activity-resource-view"
    XPATH_LE_UPDAtE_ACTIVITY = "xpath=//tbody/tr[td[@class='hp-name']/p/span[text()='%s']][1]"
    ID_enc_ACTIVITY_COLLAPSER = "xpath=//tbody/tr[td[@class='hp-name']//span[text()='Add']][1]//div[@class='hp-collapser']"
