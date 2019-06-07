# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
'''

This file contains all element ID on Fusion enclosure groups page/screen
'''


class FusionEnclosureGroupsPage(object):
    ID_PAGE_LABEL = "//div[@class='hp-page-label']/h1[text()='Enclosure Groups']"
    ID_MENU_LINK_ENCLOSURE_GROUPS = "link=Enclosure Groups"
    ID_LABEL_MAIN_MENU = "id=hp-main-menu-label"
    ID_LINK_CREATE_ENCOLOSURE_GROUPS = "link=Create enclosure group"
    ID_TITLE_ENC_GROUPS = "cic-encgroups-details-title"
    ID_ACTION_CREATE_ENCLOSURE_GROUP_DROPDOWN = "css=#cic-encgroups-actions > label"  # Action Drop-down menu
    ID_ACTION_CREATE_ENCLOSURE_GROUP = "link=Create enclosure group"  # Action->Create
    ID_INPUT_ENC_GROUP_NAME = "id=cic-encgroups-name"  # enc group name input box    t
    ID_INPUT_CHOOSE_LIG = "xpath=//div[@class='cic-enclosuregroups-c7000']//ol[@class='cic-encgroups-lig-%s']//input"
    ID_COMBO_OPTION_LIG = "xpath=//div[@class='cic-enclosuregroups-c7000']//ol[@class='cic-encgroups-lig-%s']//ol/li/span[.='%s']"
    ID_COMBO_LOGICAL_SWITCH_TEMPLATE = "css=div.hp-search-combo-control"  # Logical switch template combo box
    ID_COMBO_LIST_LOGICAL_SWITCH_TEMPLATE = "xpath=//span[@class='hp-name' and text()='%s']"
    ID_ELMNT_ENC_GRP = "xpath=//table//td[.='%s']"
    ID_ELMNT_ENC_GRP_DELETED = "xpath=//table//td[.='%s' and parent::tr[contains(@class, 'hp-not-found')]]"
    ID_ACTION_MAIN_BTN = "xpath=//label[text()='Actions']"
    ID_MENU_ACTION_ENC_GRP_DELETE = "id=cic-encgroups-delete-action"
    ID_MENU_ACTION_ENC_GRP_CREATE = "id=cic-encgroups-create-action"
    ID_MENU_ACTION_ENC_GRP_EDIT = "id=cic-encgroups-edit-action"
    ID_BTN_DELETE_ENCGRP_CONFIRM = "xpath=//button[@class='hp-ok hp-primary' and text()='Yes, delete']"
    ID_BTN_ENCLOSURE_GROUP_CREATE_PLUS = "id=cic-encgroups-submit-plus"
    ID_BTN_ENCLOSURE_GROUP_CREATE = "id=cic-encgroups-submit"
    ID_BTN_ENCLOSURE_GROUP_CANCEL = "id=cic-encgroups-cancel"
    # View
    ID_COMBO_MENU_VIEW_ = "css=div.hp-value"
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
    ID_ENC_GROUP_LIST = "xpath=//*[@class='dataTables_scrollBody']//tbody/tr/td[2]"
    # Common Xpaths,IDs and Links
    WAIT_TIME = 10  # in seconds
    UPDATE_WAIT_TIME = 30  # in seconds
    BAY_SET_MEMBER_INCREMENT = 3
    TIMEOUT = 2  # in minutes
    XPATH_EG_NAME = "xpath=//div[@class='dataTables_scrollBody']/table/tbody//*[translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')=translate('%s','ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')]"
    ID_EG_DROPDOWN = "id=cic-encgroups-panel-selector"
    LINK_EG_GENERAL = "link=General"
    LINK_EG_POWER = "link=Power"
    LINK_EG_IC_BAY_CONFIGURATION = "link=Interconnect Bay Configuration"
    XPATH_EG_C7000_IC_BAY_LIG = "xpath=//*[@id='cic-encgrp-more-details-interconnect-bay-configuration']//*[@id='cic-encgroups-c7000-ic-bays']//*[@class='hp-show-form cic-encgrp-ic-bay-%s']//*[@class='cic-encgrp-logical-interconnect']//*[text()='%s']"
    XPATH_EG_CONFIGURATION_SCRIPT = "xpath=//*[@id='cic-encgroups-more-configscript']//*[@id='cic-encgrp-more-details-configscript']"
    XPATH_EG_TBIRD_ENCLOSURE_ICBAYS = "xpath=//*[@id='cic-encgroups-tbird-ic-bays']//*[@id='hp-physical-enclosure-rows-%s']"
    XPATH_EG_TBIRD_ENCLOSURE_ICBAYS = "xpath=//*[@id='cic-encgroups-tbird-ic-bays']//*[@id='hp-physical-enclosure-rows-%s']"
    XPATH_EG_TBIRD_ENCLOSURE_IC_BAY_LIG = "xpath=//*[@id='hp-physical-enclosure-rows-%s']//*[@id='hp-physical-switch-rows-%s-%s']//*[text()='%s']"
    XPATH_EG_TBIRD_ENCLOSURE_IC_BAY_LIG_NAME = "xpath=//*[@id='hp-physical-enclosure-rows-%s']//*[@id='hp-physical-switch-rows-%s-%s']//*[@class='cic-encgrp-logical-interconnect']"
    XPATH_EG_IPV4_ADDRESSES = "xpath=//*[@id='cic-encgrp-more-details-ipv4Addresses-mode']//*[@id='cic-encgrp-more-details-ipv4Addresses']"
    XPATH_EG_IPV4_ADDRESSES_RANGES_DISPLAYED = "xpath=//*[@id='cic-encgrp-more-details-ipv4AddressPools-table']//*[translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')=translate('%s','ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')]"
    XPATH_EG_POWER_MODE = "xpath=//*[@id='cic-encgroups-more-power']//*[@id='cic-encgroups-more-power-mode-type']"
    XPATH_EG_TBIRD_ENCLOSURE_ICBAYS = "xpath=//*[@id='cic-encgroups-tbird-ic-bays']//*[@id='hp-physical-enclosure-rows-%s']"
    XPATH_EG_TBIRD_ENCLOSURE = "xpath=//*[@id='hp-physical-enclosure-rows-%s']"
