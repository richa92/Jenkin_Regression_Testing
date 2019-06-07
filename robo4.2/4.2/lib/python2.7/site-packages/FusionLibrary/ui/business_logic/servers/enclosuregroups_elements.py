class GeneralEnclosureGroupElements(object):
    ID_PAGE_LABEL = "//div[@class='hp-page-label']/h1[text()='Enclosure Groups']"

    # action button
    ID_BUTTON_ACTIONS = "//label[text()='Actions']"

    # for verify
    ID_TABLE_ENCLOSURE_GROUP = "xpath=//table/tbody/tr/td[text()='%s']"
    ID_TABLE_ITEM_SELECTED = "//table[contains(@id, 'DataTables_Table')]//td[.='%s' and parent::tr[contains(@class, 'hp-selected')]]"
    ID_TABLE_ENCLOSURE_GROUPS = "xpath=//table/tbody/tr/td[2]"
    ID_TABLE_ENCLOSURE_GROUP_SELECTED = "xpath=//table/tbody/tr[contains(@class, 'hp-selected')]/td[text()='%s']"
    ID_STATUS_ENCLOSURE_GROUP_OK = "xpath=//table/tbody/tr/td[text()='%s']/../td/div[@class='hp-status hp-status-ok']"
    ID_STATUS_ENCLOSURE_GROUP_WARN = "xpath=//table/tbody/tr/td[text()='%s']/../td/div[@class='hp-status hp-status-warning']"
    ID_STATUS_ENCLOSURE_GROUP_ERROR = "xpath=//table/tbody/tr/td[text()='%s']/../td/div[@class='hp-status hp-status-error']"
    ID_ELEMENT_ENC_GRP_DELETED = "xpath=//table//td[.='%s' and parent::tr[contains(@class, 'hp-not-found')]]"
    ID_DIALOG_DELETE_REFUSE = "//div[@id='cic-encgroups-delete-confirm-details']"

    ID_STATUS_NOTIFICATION_ONGOING = "//div[@class='hp-notification']/header[@class='hp-notification-summary']/div[@class='hp-status hp-status-unknown']"
    ID_STATUS_NOTIFICATION_OK = "//div[@class='hp-notification']/header[@class='hp-notification-summary']/div[@class='hp-status hp-status-ok']"
    ID_STATUS_NOTIFICATION_WARN = "//div[@class='hp-notification']/header[@class='hp-notification-summary']/div[@class='hp-status hp-status-warning']"
    ID_STATUS_NOTIFICATION_ERROR = "//div[@class='hp-notification']/header[@class='hp-notification-summary']/div[@class='hp-status hp-status-error']"
    ID_TEXT_NOTIFICATION_MESSAGE = "//div[@class='hp-notification']/header[@class='hp-notification-summary']/div/p/span"
    ID_TEXT_NOTIFICATION_RESOLUTION = "//div[@class='hp-notification']/div/div/div[@class='hp-notification-details']/div[@class='hp-resolution-container']"
    ID_RIGHT_SIDEBAR_ACTIVITY = "//*[@id='cic-enclosures-page']/nav/div[@class='hp-sidebar-control']/div[@class='hp-pin-right']"
    ID_TEXT_ACTIVITY_ACTION_TITLE = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-activity-message']/p/span"
    ID_TEXT_ACTIVITY_ACTION_OK = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-ok']"
    ID_TEXT_ACTIVITY_ACTION_WARN = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-warning']"
    ID_TEXT_ACTIVITY_ACTION_ERROR = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-error']"
    ID_TEXT_ACTIVITY_ACTION_DETAILS_OK = "//header[@class='hp-active']/a[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-ok']"
    ID_TEXT_ACTIVITY_MESSAGE = "//*[@id='hp-flyout-activities']/li/div[@class='hp-full']/div/div[@class='hp-notification-details']"
    ID_TEXT_GENERAL_STATE = "id=cic-encgroups-details-status"

    ID_TEXT_C7000_LIG = "//li[div[contains(text(),'%s')]]//a[text()='%s']"
    ID_TEXT_C7000_SCRIPT = "//div[@id='cic-encgrp-more-details-configscript']/pre[text()='%s']"
    ID_TEXT_C7000_ENCLOSURE_RELATED = "xpath=//*[@id='cic-encgrp-more-details-usedby']/span[text()='%s']"
    # option panel
    ID_DROPDOWN_PANEL_SELECTOR = "id=cic-encgroups-panel-selector"
    ID_SELECT_ICBAYCFG_PANEL = "xpath=//ol[@class='hp-options']//a[.='Interconnect Bay Configuration']"
    ID_SELECT_GENERAL_PANEL = "xpath=//ol[@class='hp-options']//a[.='General']"
    ID_SELECT_CFGSCRIPT_PANEL = "xpath=//ol[@class='hp-options']//a[.='Configuration Script']"
    ID_SELECT_LABEL_PANEL = "xpath=//ol[@class='hp-options']//a[.='Labels']"
    ID_SELECT_ACTIVITY_PANEL = "xpath=//ol[@class='hp-options']//a[.='Activity']"
    ID_SELECT_MAP_PANEL = "xpath=//ol[@class='hp-options']//a[.='Map']"
    ID_SELECT_ENCLOSUREGROUP_IPRANGE_NAME = "xpath=//*[@class='hp-association-selector']//*[@class='hp-selectable hp-association-selector-table dataTable']//*[translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')=translate('%s','ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')]"
    ID_BUTTON_ENCLOSURE_GROUP_ADD_RANGE = "xpath=//*[@class='hp-form-controls hp-controls']//button[text()='Add']"
    ID_BUTTON_ENCLOSURE_GROUP_CANCEL_RANGE = "xpath=//*[@class='hp-form-controls hp-controls']//button[text()='Cancel']"
    ID_EG_REMOVE_IP_RANGE = "xpath=//*[@class='hp-close cic-encgroups-range-remove']"
    ID_TEXT_ON_ACTION_ENCLOSURE_GROUP = "xpath =//*[@id='cic-encgroups-actions']/div//ol[@class='hp-unauthorized']/li"
    ID_EG_SELECT_IPRANGE_NAME = "xpath=//*[@class='hp-association-selector']//*[@class='hp-selectable hp-association-selector-table dataTable']//*[translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')=translate('%s','ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')]"


class CreateEnclosureGroupElements(object):
    ID_PAGE_LABEL = "//div[@class='hp-page-label']/h1[text()='Enclosure Groups']"
    ID_LABEL_MAIN_MENU = "id=hp-main-menu-label"
    ID_BUTTON_CREATE_ENCLOSURE_GROUP = "//a[text()='Create enclosure group']"
    ID_TITLE_ENC_GROUPS = "//h1[@id='cic-encgroups-details-title' and text()='%s']"
    ID_ACTION_CREATE_ENCLOSURE_GROUP_DROPDOWN = "//div[@id='cic-encgroups-actions']/label"  # Action Drop-down menu
    ID_ACTION_CREATE_ENCLOSURE_GROUP = "//div[@id='cic-encgroups-actions']//a[text()='Create']"  # Action->Create

    ID_DIALOG_CREATE_ENCLOSURE_GROUP = "id=cic-enclosuregroups-add-form"
    ID_INPUT_ENC_GROUP_NAME = "xpath=//input[@id='cic-encgroups-name']"  # enc group name input box
    ID_TBIRD_SELECT_ENCLOSURE_COUNT = "id=cic-enclosure-group-create-enclosure-count"
    ID_TBIRD_SELECT_DEPLOYMENT_NETWORK_TYPE = "id=cic-encgroups-imagestreamerconfiguration"
    ID_TBIRD_RADIO_IPV4_ADDRESSES_USE_ADDRESS_POOL = "id=cic-encgroups-pool"
    ID_TBIRD_RADIO_IPV4_ADDRESSES_USE_DHCP = "id=cic-encgroups-dhcp"
    ID_TBIRD_RADIO_IPV4_ADDRESSES_USE_MANAGE_EXTERNALLY = "id=cic-encgroups-external"
    # ID_TBIRD_TITLE_LABEL_ENCLOSURE = "xpath=//*[@class='enclosuregroups-create_and_edit-index-%s']"
    ID_COMBO_SEARCH_LIG = "xpath=//h3[@class='enclosuregroups-create_and_edit-index-%s']/../..//div[contains(@class, 'cic-encgroups-lig-%s')]//div[@class='hp-search-combo-control']"
    ID_TBIRD_INPUT_LIG_CLEAR = "xpath=//h3[@class='enclosuregroups-create_and_edit-index-%s']/../..//div[contains(@class, 'cic-encgroups-lig-%s')]//div[@class='hp-close']"
    ID_TBIRD_INPUT_CHOOSE_LIG = "xpath=//*[@class='enclosuregroups-create_and_edit-index-%s']/../..//div[contains(@class, 'cic-encgroups-lig-%s')]//input"
    ID_TBIRD_CHOOSE_LIG_LAYER = "xpath=//*[@class='enclosuregroups-create_and_edit-index-%s']/../..//div[contains(@class, 'cic-encgroups-lig-%s')]//div[@class='hp-search-combo-menu']"
    ID_TBIRD_SELECT_OPTION_CHOOSE_LIG = "xpath=//*[@class='enclosuregroups-create_and_edit-index-%s']/../..//div[contains(@class, 'cic-encgroups-lig-%s')]//div[@class='hp-search-combo-menu']/ol/li[span[.='%s']]"
    ID_TBIRD_SELECT_POWER_MODE = "id=cic-encgroups-power-mode-select-type"
    ID_INPUT_CONFIG_SCRIPT = "xpath=//textarea[@id='cic-encgroups-config-script']"
    ID_INPUT_C7000_CHOOSE_LIG = "xpath=//*[@id='cic-enclosuregroups-panel-add-lig']/fieldset/div[@class='cic-enclosuregroups-c7000']//ol//div[@class='hp-device-contents cic-encgroups-lig-%s']//input"
    ID_COMBO_C7000_OPTION_LIG = "xpath=//*[@id='cic-enclosuregroups-panel-add-lig']/fieldset/div[@class='cic-enclosuregroups-c7000']//ol//div[@class='hp-device-contents cic-encgroups-lig-%s']//ol/li/span[.='%s']"
    ID_BUTTON_ENCLOSURE_GROUP_CREATE_PLUS = "id=cic-encgroups-submit-plus"
    ID_BUTTON_ENCLOSURE_GROUP_CREATE = "id=cic-encgroups-submit"
    ID_BUTTON_ENCLOSURE_GROUP_CANCEL = "id=cic-encgroups-cancel"
    ID_EG_CREATE_NO_RANGES_SIDE_MSG = "id=cic-encgroups-create-no-ranges-side-msg"
    ID_TBIRD_EG_SEARCH_COMBO_MENU = "xpath=//*[@class='cic-enclosuregroups-tbird']//*[@class='hp-physical-switch-rows cic-enclosuregroups-set-%s']//*[@class='hp-device-contents cic-encgroups-lig-%s']//*[@class='hp-search-combo-menu']"
    ID_TBIRD_EG_SEARCH_COMBO_MENU_HEADER = "xpath=//*[@class='cic-enclosuregroups-tbird']//*[@class='hp-physical-switch-rows cic-enclosuregroups-set-%s']//*[@class='hp-device-contents cic-encgroups-lig-%s']//*[@class='hp-search-combo-menu']//*[@class='hp-header']"
    ID_TBIRD_EG_LIG_OPTIONS_SEARCH_BUTTON = "xpath=//*[@class='cic-enclosuregroups-tbird']//*[@class='hp-physical-switch-rows cic-enclosuregroups-set-%s']//*[@class='hp-device-contents cic-encgroups-lig-%s']//*[@class='hp-search-combo-control']"
    ID_TBIRD_EG_LIG_DROPDOWN_OPTIONS = "xpath=//*[@class='cic-enclosuregroups-tbird']//*[@class='hp-physical-switch-rows cic-enclosuregroups-set-%s']//*[@class='hp-device-contents cic-encgroups-lig-%s']//*[@class='hp-search-combo-scroller hp-options']//*[text()='%s']"
    ID_TEXT_TBIRD_SELECTED_LIG = "xpath=//div[@class='cic-enclosuregroups-tbird']//ol[@class='hp-physical-switch-rows cic-enclosuregroups-set-%s']//div[@class='hp-device-contents cic-encgroups-lig-%s']//input[@id='undefined-input']"
    ID_DIALOG_CHANGE_LIG_CONFIRM = "id=cic-encgroups-change-confirm-header"
    ID_BUTTON_CHANGE_LIG_CONFIRM = "xpath=//div[@id='cic-encgroups-change-confirm-prompt']/../footer//button[text()='Yes, select']"
    ID_BUTTON_CANCEL_CHANGE_LIG_CONFIRM = "xpath=//div[@id='cic-encgroups-change-confirm-prompt']/../footer//button[text()='Cancel']"
    ID_TEXT_EG_CHANGE_PROMPT = "xpath=//div[@id='hp-body-div']//div[@class='hp-dialog-notification']"
    ID_TBIRD_COMBO_ACTIVE_SEARCH_MENU = "xpath=//*[@class='cic-enclosuregroups-tbird']//*[@class='hp-physical-switch-rows cic-enclosuregroups-set-%s']//*[@class='hp-device-contents cic-encgroups-lig-%s']//div[@class='hp-search-combo hp-active']//ol[@class='hp-search-combo-scroller hp-options']"
    ID_BUTTON_CREATE_ENCLOSUREGROUP_ADD_ADDRESS_RANGES = "xpath=.//*[@id='cic-encgroups-create-add-ranges']"


class EditEnclosureGroupElements(object):
    ID_PAGE_LABEL = "//div[@class='hp-page-label']/h1[text()='Enclosure Groups']"
    ID_LABEL_MAIN_MENU = "id=hp-main-menu-label"
    ID_BUTTON_CREATE_ENCLOSURE_GROUP = "//a[text()='Create enclosure group']"
    ID_TITLE_ENC_GROUPS = "//h1[@id='cic-encgroups-details-title' and text()='%s']"
    ID_ACTION_EDIT_ENCLOSURE_GROUP = "//div[@id='cic-encgroups-actions']//a[text()='Edit']"  # Action->Create

    ID_DIALOG_EDIT_ENCLOSURE_GROUP = "id=cic-enclosuregroups-edit-form"
    ID_DIALOG_EDIT_ENCLOSURE_GROUP_CONFIRM = "//span[@id='cic-encgroups-change-confirm-header']"

    ID_INPUT_ENC_GROUP_NAME = "//input[@id='cic-encgroups-name']"  # enc group name input box    t
    ID_INPUT_CONFIG_SCRIPT = "//textarea[@id='cic-encgroups-config-script']"
    ID_INPUT_C7000_CHOOSE_LIG = "//li[@class='hp-switch hp-device hp-template']/div[@class='hp-device-contents cic-encgroups-lig-%s']/div/div//input"
    ID_COMBO_C7000_OPTION_LIG = "//li[@class='hp-switch hp-device hp-template']/div[@class='hp-device-contents cic-encgroups-lig-%s']/div/div//ol/li/span[.='%s']"

    ID_BUTTON_ENCLOSURE_GROUP_OK = "xpath = //*[@id='cic-encgroups-submit']"
    ID_BUTTON_ENCLOSURE_GROUP_CANCEL = "id=cic-encgroups-cancel"
    ID_BUTTON_EDIT_ENCGRP_CONFIRM = "xpath=//button[@class='hp-ok hp-primary' and text()='Yes, select']"
    ID_EG_EDIT_NO_RANGESIDE_MSG = "id=cic-encgroups-edit-no-ranges-side-msg"
    ID_BUTTON_ENCLOSUREGROUP_EDIT_ADD_ADDRESS_RANGES = "xpath=.//*[@id='cic-encgroups-edit-add-ranges']"
    ID_EDIT_CHECK_IPRANGE_NAME_IN_TABLE = "xpath=//*[@id='cic-encgroups-edit-ranges-table']//td[text()='%s']"
    ID_EG_EDIT_HP_STATUS_ERROR = "xpath=//*[@id='cic-enclosuregroups-edit-form']//*[@class='hp-status hp-status-error']"
    ID_EG_EDIT_FORM_MESSAGE_SUMMARY = "xpath=//*[@id='cic-enclosuregroups-edit-form']//*[@class='hp-form-message-summary']"
    ID_EG_EDIT_FORM_MESSAGE_DETAILS = "xpath=//*[@id='cic-enclosuregroups-edit-form']//*[@class='hp-form-message-details']"
    ID_EG_EDIT_NO_RANGES_SIDE_MSG = "id=cic-encgroups-edit-no-ranges-side-msg"
    ID_EDIT_EG_REMOVE_IP_RANGE = "xpath=//*[@id='cic-encgroups-edit-ranges-table']//td[text()='%s']//following-sibling::td/div[@class='hp-close cic-encgroups-range-remove']"
    ID_EDIT_DELETE_BUTTON_IPRANGE_CONFIRM = "xpath=//button[@class='hp-ok hp-primary' and text()='Yes, delete']"


class DeleteEnclosureGroupElements(object):
    ID_ELEMENT_ENC_GRP_DELETED = "xpath=//table//td[.='%s' and parent::tr[contains(@class, 'hp-not-found')]]"
    ID_ELEMENT_ENC_GRP_NOT_FOUND = "xpath=//td[@class='dataTables_empty' and text()='No enclosure groups']"
    ID_ACTION_MAIN_BTN = "xpath=//label[text()='Actions']"
    ID_MENU_ACTION_ENC_GRP_DELETE = "id=cic-encgroups-delete-action"

    ID_DIALOG_DELETE_ENCLOSURE_GROUP = "id=cic-encgroups-delete-confirm-header"

    ID_BUTTON_DELETE_ENCGRP_CONFIRM = "xpath=//button[@class='hp-button hp-ok hp-primary' and text()='Yes, delete']"
    ID_BUTTON_DELETE_ENCGRP_CANCEL = "xpath=//button[@class='hp-cancel' and text()='Cancel']"
    ID_BUTTON_DELETE_ENCGRP_CLOSE = "xpath=//button[@class='hp-cancel hp-primary' and text()='Close']"
    # View
    ID_COMBO_MENU_VIEW = "css=div.hp-value"
    ID_LINK_GENERAL = "link=General"
    ID_LINK_RELATED = "link=Related"
    ID_COMBO_CLICK = "css=div.hp-search-combo-control"  # used by edit enclosure group function
    ID_LINK_Search_For_Another = "link=Search for another"  # used by edit eenclosure group function
    ID_EDIT_ENC_GROUP_SUBMIT = "id=cic-encgroups-submit"  # used by edit eenclosure group function
    ID_ENCLOSURE_PAGE_LABEL = "xpath=//div[@class='hp-page-label']/h1[text()='Enclosure Groups']"
    ID_COMBO_LOGICAL_INTERCONNECT_GROUP = "xpath=//span[@class='hp-name' and text()='%s']"  # used by edit eenclosure group function
    ID_ENCLOSURE_GROUP_NAME = "xpath=//div[text()='%s']"  # aused by edit eenclosure group function
    ID_LINK_EDIT = "link=Edit"
    ID_TABLE_ITEM_SELECTED = "//table[contains(@id, 'DataTables_Table')]//td[.='%s' and parent::tr[contains(@class, 'hp-selected')]]"
    ID_ERROR_MSG_FOR_DELETE_ENCLOSURE_GROUP = "xpath=//*[@class='hp-dialog-container hp-wide hp-active']//*[@class='hp-notify hp-notify-warning hp-active']"


class VerifyEnclosureGroupElements(object):
    ID_TEXT_GENERAL_IPV4_ADDRESS = "id=cic-encgrp-more-details-ipv4Addresses"
    ID_TEXT_GENERAL_USED_BY = "id=cic-encgrp-more-details-usedby"
    ID_TEXT_POWER_MODE = "id=cic-encgroups-more-power-mode-type"
    ID_TEXT_DEPLOYMENT_NETWORK_TYPE = "id=cic-encgrp-more-details-deploymentmode"
    ID_TEXT_ENG_SELECTED_LOGICAL_INTERCONNECT_GROUP = "xpath=//li[@id='hp-physical-switch-rows-%s-%s']//div[contains(@class, 'cic-encgrp-logical-interconnect')]"
    ID_TEXT_ENG_SELECTED_INTERCONNECT_TYPE = "xpath=//li[@id='hp-physical-switch-rows-%s-%s']//div[@class='cic-encgrp-interconnect-type']"
