class GeneralEnclosuresElements(object):
    ID_PAGE_LABEL = "//div[@class='hp-page-label']/h1[text()='Enclosures']"

    # action button
    ID_BUTTON_ACTIONS = "xpath=//label[text()='Actions']"
    ID_OPTION_ACTIONS_ADD = "xpath=//li[@id='cic-enclosure-add-action-element']/a"
    ID_OPTION_ACTIONS_EDIT = "xpath=//li[@id='cic-enclosure-edit-action-element']/a"
    ID_OPTION_ACTIONS_REAPPLY_CONFIGURATION = "xpath=//li[@id='cic-enclosure-reconfigure-action-element']/a"
    ID_OPTION_ACTIONS_REFRESH = "xpath=//li[@id='cic-enclosure-refresh-action-element']/a"
    ID_OPTION_ACTIONS_REMOVE = "xpath=//li[@id='cic-enclosure-remove-action-element']/a"
    ID_BUTTON_ADD_ENCLOSURE = "xpath=//table/tbody/tr/td[text()='Add enclosure']"

    # for verify
    ID_TABLE_ENCLOSURE = "xpath=//table/tbody/tr[not(contains(@class, 'hp-not-found'))]/td[text()='%s']"
    ID_TABLE_ENCLOSURES = "xpath=//table/tbody/tr/td[2]"
    ID_TABLE_ENCLOSURE_SELECTED = "xpath=//table/tbody/tr[contains(@class, 'hp-selected')]/td[text()='%s']"
    ID_STATUS_ENCLOSURE_OK = "xpath=//table/tbody/tr/td[text()='%s']/../td/div[@class='hp-status hp-status-ok']"
    ID_STATUS_ENCLOSURE_WARN = "xpath=//table/tbody/tr/td[text()='%s']/../td/div[@class='hp-status hp-status-warning']"
    ID_STATUS_ENCLOSURE_ERROR = "xpath=//table/tbody/tr/td[text()='%s']/../td/div[@class='hp-status hp-status-error']"

    ID_STATUS_NOTIFICATION_ONGOING = "//div[@class='hp-notification']/header[@class='hp-notification-summary']/div[@class='hp-status hp-status-unknown']"
    ID_STATUS_NOTIFICATION_OK = "//div[@class='hp-notification']/header[@class='hp-notification-summary']/div[@class='hp-status hp-status-ok']"
    ID_STATUS_NOTIFICATION_WARN = "//div[@class='hp-notification']/header[@class='hp-notification-summary']/div[@class='hp-status hp-status-warning']"
    ID_STATUS_NOTIFICATION_ERROR = "//div[@class='hp-notification']/header[@class='hp-notification-summary']/div[@class='hp-status hp-status-error']"
    ID_TEXT_NOTIFICATION_MESSAGE = "//div[@class='hp-notification']/header[@class='hp-notification-summary']/div/p/span"
    ID_TEXT_NOTIFICATION_RESOLUTION = "//div[@class='hp-notification']/div/div/div[@class='hp-notification-details']/div[@class='hp-resolution-container']"
    ID_RIGHT_SIDEBAR_ACTIVITY = "//*[@id='cic-enclosures-page']/nav/div[@class='hp-sidebar-control']/div[@class='hp-pin-right']"
    ID_TEXT_ACTIVITY_ACTION_TITLE = "//ol[@id='hp-flyout-activities']/li[div/div[@class='hp-activity-source' and text()='%s']][1]/div/div/p/span"
    ID_TEXT_ACTIVITY_ACTION_OK = "//ol[@id='hp-flyout-activities']/li[div/div[@class='hp-activity-source' and text()='%s' and ../div[@class='hp-activity-message'][starts-with(., '%s')]]][1]/div/div[@class='hp-status hp-status-ok']"
    ID_TEXT_ACTIVITY_ACTION_WARN = "//ol[@id='hp-flyout-activities']/li[div/div[@class='hp-activity-source' and text()='%s' and ../div[@class='hp-activity-message'][starts-with(., '%s')]]][1]/div/div[@class='hp-status hp-status-warning']"
    ID_TEXT_ACTIVITY_ACTION_ERROR = "//ol[@id='hp-flyout-activities']/li[div/div[@class='hp-activity-source' and text()='%s' and ../div[@class='hp-activity-message'][starts-with(., '%s')]]][1]/div/div[@class='hp-status hp-status-error']"
    ID_TEXT_ACTIVITY_ACTION_DETAILS_OK = "//header[@class='hp-active']/a[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-ok']"
    ID_TEXT_ACTIVITY_MESSAGE = "//*[@id='hp-flyout-activities']/li/div[@class='hp-full']/div/div[@class='hp-notification-details']"

    # overview
    ID_TEXT_OVERVIEW_GENERAL_STATE = "id=cic-enclosure-details-state"
    ID_TEXT_OVERVIEW_GENERAL_MODEL = "id=cic-enclosure-details-model"
    ID_TEXT_OVERVIEW_GENERAL_LOGICAL_ENCLOSURE = "xpath=//div[@id='cic-enclosure-details-logical-enclosure']|//div[@id='cic-enclosure-details-logical-enclosure']/a"
    ID_TEXT_OVERVIEW_GENERAL_SERVER_LICENSING_POLICY = "id=cic-enclosure-details-license"
    ID_TEXT_OVERVIEW_HARDWARE_OA = "xpath=//div[@id='cic-enclosure-oa']/a"
    ID_TEXT_OVERVIEW_HARDWARE_LOCATION = "xpath=//div[@id='cic-enclosure-details-location']|//div[@id='cic-enclosure-details-location']/a"
    ID_TEXT_OVERVIEW_HARDWARE_POWERED_BY = "id=cic-enclosure-details-poweredBy"
    ID_TEXT_OVERVIEW_HARDWARE_SERIAL_NUMBER = "id=cic-enclosure-details-serialNumber"
    ID_ELEMENT_OVERVIEW_REAR_VIEW_NAME = "xpath=//*[@id='cic-enclosure-show-switchbays']/descendant::div/a[text()='%s']/ancestor::div[1]/../.."
    ID_ELEMENT_OVERVIEW_REAR_VIEW_BAY = "xpath=//div[@id='cic-enclosure-show-switchbays']//li[@class='hp-bay']//div[@class='hp-status hp-status-ok' and following-sibling::div/a[text()='%s']/ancestor::li[1]/label[text()='%s']]"
    ID_ELEMENT_OVERVIEW_REAR_VIEW_HEALTH_STATUS = "xpath=//*[@id='cic-enclosure-show-switchbays']//li[@class='hp-bay']//div/a[text()='%s']/ancestor::li[1]/div[@class='hp-device hp-switch hp-flyout-wrapper']/div[contains(@class,'hp-status hp-status')]"
    ID_ELEMENT_OVERVIEW_REAR_VIEW_MODEL = "xpath=//div[@id='cic-enclosure-show-switchbays']//div[@class='hp-status hp-status-ok' and following-sibling::div/a[text()='%s']/../following-sibling::div[contains(text(),'%s')]]"

    # general
    ID_TEXT_GENERAL_STATE = "id=cic-enclosure-more-state"
    ID_TEXT_GENERAL_MODEL = "id=cic-enclosure-more-model"
    ID_TEXT_GENERAL_LOGICAL_ENCLOSURE = "xpath=//div[@id='cic-enclosure-more-logical-enclosure' or @id='cic-enclosure-details-logical-enclosure']/a|//div[@id='cic-enclosure-more-logical-enclosure' or @id='cic-enclosure-details-logical-enclosure']"
    ID_TEXT_GENERAL_SERVER_LICENSING_POLICY = "id=cic-enclosure-more-license"
    # hardware
    ID_TEXT_HARDWARE_PRIMARY_OA_HOST_NAME = "xpath=//td[@id='cic-enclosure-more-oa-active-hostname']/a"
    ID_TEXT_HARDWARE_PRIMARY_OA_IPV4 = "xpath=//td[@id='cic-enclosure-more-oa-active-ipv4']/a"
    ID_TEXT_HARDWARE_PRIMARY_OA_IPV6 = "xpath=//td[@id='cic-enclosure-more-oa-active-ipv6']/ol//a"
    ID_TEXT_HARDWARE_PRIMARY_OA_IPV6_NONE = "xpath=//td[@id='cic-enclosure-more-oa-active-ipv6']/ol/span"
    ID_TEXT_HARDWARE_LOCATION = "xpath=//div[@id='cic-enclosure-more-location']/a|//div[@id='cic-enclosure-more-location']"
    ID_TEXT_HARDWARE_POWERED_BY = "id=cic-enclosure-more-poweredBy"
    ID_TEXT_HARDWARE_SERIAL_NUMBER = "id=cic-enclosure-more-serialNumber"
    ID_TEXT_HARDWARE_PART_NUMBER = "id=cic-enclosure-more-partNumber"
    ID_TEXT_HARDWARE_MAXIMUM_POWER = "id=cic-enclosure-maximumPower"
    # firmware
    ID_TEXT_FIRMWARE_ROW_NAME = "xpath=//table[@id='cic-enclosure-more-fw-table']//tr[td[1][.='%s']]"
    ID_TEXT_FIRMWARE_ROW_COMPONENT_1 = "xpath=//table[@id='cic-enclosure-more-fw-table']//tr[td[1][a[.='%s'] or .='%s']]/td[2]"
    ID_TEXT_FIRMWARE_ROW_COMPONENT_2 = "xpath=//table[@id='cic-enclosure-more-fw-table']//tr[td[1][a[.='%s']]]/following::tr[1]/td[2]"
    ID_TEXT_FIRMWARE_ROW_INSTALLED_1 = "xpath=//table[@id='cic-enclosure-more-fw-table']//tr[td[1][a[.='%s'] or .='%s']]/td[3]"
    ID_TEXT_FIRMWARE_ROW_INSTALLED_2 = "xpath=//table[@id='cic-enclosure-more-fw-table']//tr[td[1][a[.='%s']]]/following::tr[1]/td[3]"
    # device
    ID_TEXT_DEVICES_ROW_BAY = "xpath=//table[@id='cic-enclosure-more-devbays-table']//tr[td[1][.='%s']]"
    ID_TEXT_DEVICES_ROW_STATUS = "xpath=//table[@id='cic-enclosure-more-devbays-table']//tr[td[1][.='%s']]/td[2]//span"
    ID_TEXT_DEVICES_ROW_SERVER_HARDWARE = "xpath=//table[@id='cic-enclosure-more-devbays-table']//tr[td[1][.='%s']]//td[3]|//table[@id='cic-enclosure-more-devbays-table']//tr[td[1][.='%s']]//td[1+count(//table[@id='cic-enclosure-more-devbays-table']/thead//td[.='Hardware']/preceding-sibling::td)]/a"
    ID_TEXT_DEVICES_ROW_SERVER_MODEL = "xpath=//table[@id='cic-enclosure-more-devbays-table']//tr[td[1][.='%s']]//td[1+count(//table[@id='cic-enclosure-more-devbays-table']/thead//td[.='Model']/preceding-sibling::td)]"
    ID_TEXT_DEVICES_ROW_SERVER_PROFILE = "xpath=//table[@id='cic-enclosure-more-devbays-table']//tr[td[1][.='%s']]//td[1+count(//table[@id='cic-enclosure-more-devbays-table']/thead//td[.='Server Profile']/preceding-sibling::td)]|//table[@id='cic-enclosure-more-devbays-table']//tr[td[1][.='%s']]//td[1+count(//table[@id='cic-enclosure-more-devbays-table']/thead//td[.='Server Profile']/preceding-sibling::td)]/a"
    # interconnects
    ID_TEXT_INTERCONNECTS_ROW_BAY = "xpath=//table[@id='cic-enclosure-icbays-table']//tr[td[1][.='%s']]"
    ID_TEXT_INTERCONNECTS_ROW_STATUS = "xpath=//table[@id='cic-enclosure-icbays-table']//tr[td[1][.='%s']]/td[2]//span"
    ID_TEXT_INTERCONNECTS_ROW_INTERCONNECT = "xpath=//table[@id='cic-enclosure-icbays-table']//tr[td[1][.='%s']]/td[3]//a"
    ID_TEXT_INTERCONNECTS_ROW_INSTALLED_MODULE = "xpath=//table[@id='cic-enclosure-icbays-table']//tr[td[1][.='%s']]/td[4]"
    ID_TEXT_INTERCONNECTS_ROW_BAY_EMPTY = "xpath=//table[@id='cic-enclosure-icbays-table']//tr[td[1][.='%s']]/td/span[.='empty']"
    # power supplies
    ID_TEXT_POWER_SUPPLIES_ROW_BAY = "xpath=//table[@id='cic-enclosure-more-power-supply-bays-table']//tr[td[1][.='%s']]"

    ID_TEXT_POWER_SUPPLIES_ROW_STATUS = "xpath=//table[@id='cic-enclosure-more-power-supply-bays-table']//tr[td[1][.='%s']]//td[2]//span"
    ID_TEXT_POWER_SUPPLIES_ROW_MODEL = "xpath=//table[@id='cic-enclosure-more-power-supply-bays-table']//tr[td[1][.='%s']]//td[3]"
    ID_TEXT_POWER_SUPPLIES_ROW_SERIAL_NUMBER = "xpath=//table[@id='cic-enclosure-more-power-supply-bays-table']//tr[td[1][.='%s']]//td[4]"
    ID_TEXT_POWER_SUPPLIES_ROW_PART_NUMBER = "xpath=//table[@id='cic-enclosure-more-power-supply-bays-table']//tr[td[1][.='%s']]//td[5]"
    ID_TEXT_POWER_SUPPLIES_ROW_SPARE_PART_NUMBER = "xpath=//table[@id='cic-enclosure-more-power-supply-bays-table']//tr[td[1][.='%s']]//td[6]"
    # fans
    ID_TEXT_FANS_FANS_REQUIRED = "id=cic-enclosure-more-fansrequired"
    ID_TEXT_FANS_DEVICE_BAYS_COOLED = "id=cic-enclosure-more-devbayscooled"
    ID_TEXT_FANS_ROW_BAY = "xpath=//table[@id='cic-enclosure-more-fanbays-table']//tr[td[1][.='%s']]"
    ID_TEXT_FANS_ROW_STATUS = "xpath=//table[@id='cic-enclosure-more-fanbays-table']//tr[td[1][.='%s']]/td[2]//span"
    ID_TEXT_FANS_ROW_MODEL = "xpath=//table[@id='cic-enclosure-more-fanbays-table']//tr[td[1][.='%s']]/td[3]"
    ID_TEXT_FANS_ROW_STATE = "xpath=//table[@id='cic-enclosure-more-fanbays-table']//tr[td[1][.='%s']]/td[4]"
    ID_TEXT_FANS_ROW_REQUIRED = "xpath=//table[@id='cic-enclosure-more-fanbays-table']//tr[td[1][.='%s']]/td[5]"
    ID_TEXT_FANS_ROW_PART_NUMBER = "xpath=//table[@id='cic-enclosure-more-fanbays-table']//tr[td[1][.='%s']]/td[5]"
    ID_TEXT_FANS_ROW_SPARE_PART_NUMBER = "xpath=//table[@id='cic-enclosure-more-fanbays-table']//tr[td[1][.='%s']]/td[6]"
    # tbird fan
    ID_TEXT_TBIRD_FANS_ROW_SERIAL_NUMBER = "xpath=//table[@id='cic-enclosure-more-fanbays-table']//tr[td[1][.='%s']]/td[4]"
    ID_TEXT_TBIRD_FANS_ROW_PART_NUMBER = "xpath=//table[@id='cic-enclosure-more-fanbays-table']//tr[td[1][.='%s']]/td[5]"
    ID_TEXT_TBIRD_FANS_ROW_SPARE_PART_NUMBER = "xpath=//table[@id='cic-enclosure-more-fanbays-table']//tr[td[1][.='%s']]/td[6]"
    # tbird cim
    ID_TEXT_TBIRD_CIM_ROW_BAY = "xpath=//table[@id='cic-enclosure-more-ci-mgr-bays-table']//tr[td[.='%s']]"
    ID_TEXT_TBIRD_CIM_ROW_STATUS = "xpath=//table[@id='cic-enclosure-more-ci-mgr-bays-table']//tr[td[1][.='%s']]/td[2]//span"
    ID_TEXT_TBIRD_CIM_ROW_MODEL = "xpath=//table[@id='cic-enclosure-more-ci-mgr-bays-table']//tr[td[1][.='%s']]/td[3]"
    ID_TEXT_TBIRD_CIM_ROW_POWER = "xpath=//table[@id='cic-enclosure-more-ci-mgr-bays-table']//tr[td[1][.='%s']]/td[4]"
    ID_TEXT_TBIRD_CIM_ROW_SERIAL_NUMBER = "xpath=//table[@id='cic-enclosure-more-ci-mgr-bays-table']//tr[td[1][.='%s']]/td[5]"
    ID_TEXT_TBIRD_CIM_ROW_PART_NUMBER = "xpath=//table[@id='cic-enclosure-more-ci-mgr-bays-table']//tr[td[1][.='%s']]/td[6]"
    ID_TEXT_TBIRD_CIM_ROW_SPARE_PART_NUMBER = "xpath=//table[@id='cic-enclosure-more-ci-mgr-bays-table']//tr[td[1][.='%s']]/td[7]"
    # tbird linked modules
    ID_TEXT_TBIRD_LINKED_MODULES_BAY_EMPTY = "xpath=//table[@id='cic-enclosure-more-em-bays-table']/tbody/tr[%s]/td[.='empty']"
    ID_TEXT_TBIRD_LINKED_MODULES_BAY_OK_STATUS = "xpath=//table[@id='cic-enclosure-more-em-bays-table']/tbody/tr[%s]//div[@class='hp-status hp-status-ok']"
    ID_TEXT_TBIRD_LINKED_MODULES_ROW_BAY = "xpath=//table[@id='cic-enclosure-more-em-bays-table']//tr[td[.='%s']]"
    ID_TEXT_TBIRD_LINKED_MODULES_ROW_STATUS = "xpath=//table[@id='cic-enclosure-more-em-bays-table']//tr[td[2][.='%s']]/td[3]//span"
    ID_TEXT_TBIRD_LINKED_MODULES_ROW_MODEL = "xpath=//table[@id='cic-enclosure-more-em-bays-table']//tr[td[2][.='%s']]/td[4]"
    ID_TEXT_TBIRD_LINKED_MODULES_ROW_STATE = "xpath=//table[@id='cic-enclosure-more-em-bays-table']//tr[td[2][.='%s']]/td[5]"
    ID_TEXT_TBIRD_LINKED_MODULES_ROW_MGMT_PORT_STATE = "xpath=//table[@id='cic-enclosure-more-em-bays-table']//tr[td[2][.='%s']]/td[6]"
    ID_TEXT_TBIRD_LINKED_MODULES_ROW_LINK_PORT_STATE = "xpath=//table[@id='cic-enclosure-more-em-bays-table']//tr[td[2][.='%s']]/td[7]"

    # option panel
    ID_DROPDOWN_PANEL_SELECTOR = "id=cic-enclosure-panel-selector"
    ID_SELECT_OVERVIEW_PANEL = "xpath=//ol[@class='hp-options']//a[.='Overview']"
    ID_SELECT_GENERAL_PANEL = "xpath=//ol[@class='hp-options']//a[.='General']"
    ID_SELECT_HARDWARE_PANEL = "xpath=//ol[@class='hp-options']//a[.='Hardware']"
    ID_SELECT_FIRMWARE_PANEL = "xpath=//ol[@class='hp-options']//a[.='Firmware']"
    ID_SELECT_DEVICE_BAYS_PANEL = "xpath=//ol[@class='hp-options']//a[.='Device Bays']"
    ID_SELECT_INTERCONNECT_BAYS_PANEL = "xpath=//ol[@class='hp-options']//a[.='Interconnect Bays']"
    ID_SELECT_POWER_SUPPLY_BAYS_PANEL = "xpath=//ol[@class='hp-options']//a[.='Power Supply Bays']"
    ID_SELECT_FAN_BAYS_PANEL = "xpath=//ol[@class='hp-options']//a[.='Fan Bays']"
    ID_SELECT_PORT_EXTENDER_TOPOLOGY_PANEL = "xpath=//ol[@class='hp-options']//a[.='Port Extender Topology']"
    ID_SELECT_CONVERGED_INFRASTRUCTURE_MANAGER_BAYS_PANEL = "xpath=//ol[@class='hp-options']//a[.='Converged Infrastructure Manager Bays']"
    ID_SELECT_ENCLOSURE_MANAGER_BAYS_PANEL = "xpath=//ol[@class='hp-options']//a[.='Enclosure Manager Bays']"
    ID_SELECT_UTILIZATION_PANEL = "xpath=//ol[@class='hp-options']//a[.='Utilization']"
    ID_SELECT_ACTIVITY_PANEL = "xpath=//ol[@class='hp-options']//a[.='Activity']"
    ID_SELECT_MAP_PANEL = "xpath=//ol[@class='hp-options']//a[.='Map']"
    ID_ACTIVITY_CONTROL_NEW_COUNT = "xpath=//div[@id='hp-activity-control']/div[@id='hp-activity-control-new-count' and text()>0]"
    ID_TEXT_ACTIVITY_CONTENT = "//table[@class='hp-index-table hp-activities dataTable']/tbody/tr//span[contains(text(), '%s')]"
    ID_TEXT_ACTIVITY_SUB_TASK = "//tr/td/div[.='%s']/../span[text()='%s']/../..//a[.='%s']"

    # scopes
    ID_TEXT_SCOPE = "//table[@id='hp-scopes-resource-show-table']//td[text()='%s']"

    # activity
    ID_ICON_ACTIVITY_COLLAPSER = "//table[@class='hp-index-table hp-activities dataTable']/tbody/tr//span[text()='%s']/../../../td//div[@class='hp-collapser']"  # activity collapser

    # migrate enclosure
    ID_TEXT_ERROR_MIGRATE_REPORT_MESSAGE = "xpath=//p[@id='cic-enclosure-migrate-report-summary']/b[contains(text(),'error')]"


class AddEnclosuresElements(object):
    ID_BUTTON_ADD_ENCLOSURE = "link=Add enclosure"
    ID_SELECT_ACTION_ADD = "id=cic-enclosure-add-action-element"

    # dialog
    ID_DIALOG_ADD_ENCLOSURE = "id=hp-change-page-container"
    ID_DIALOG_EDIT_LIG = "id=cic-enclosure-lst"

    # dailog element
    ID_INPUT_OA_IP_ADDRESS_OR_HOST_NAME = "id=cic-enclosure-hostname"
    ID_ERR_MSG_INPUT_OA_IP_ADDRESS_OR_HOST_NAME = "xpath=//label[@for='cic-enclosure-hostname']"
    ID_RADIO_ADD_ENCLOSURE_FOR_MANAGEMENT = "id=cic-enclosure-addas-managed"
    ID_RADIO_ADD_ENCLOSURE_FOR_MONITORING = "id=cic-enclosure-addas-monitored"
    ID_RADIO_MIGRATE_VIRTUAL_CONNECT_DOMAIN = "id=cic-enclosure-addas-migrated"
    ID_ERR_MSG_ENCLOSURE_ADD_AS = "xpath=//label[@for='enclosureaddas']"
    ID_CHECKBOX_FORCE_ADD_ENCLOSURE = "id=cic-enclosure-force"
    ID_INPUT_USER_NAME = "id=cic-enclosure-username"
    ID_ERR_MSG_USER_NAME = "xpath=//label[@for='cic-enclosure-username']"
    ID_INPUT_PASSWORD = "id=cic-enclosure-password"
    ID_INPUT_VCM_USERNAME = "id=cic-enclosure-vcm-username"
    ID_INPUT_VCM_PASSWORD = "id=cic-enclosure-vcm-password"
    ID_BUTTON_TEST_COMPATIBILITY = "id=cic-enclosure-migrate-test-compatibility-button"
    ID_TEXT_MIGRATE_REPORT_SUMMARY = "id=cic-enclosure-migrate-report-summary"
    ID_CHECKBOX_MIGRATE_VC_BACKUP = "id=VirtualConnectBackup_cbox"
    ID_CHECKBOX_RESOURCES_NOT_MODIFIED = "id=ResourcesNotModified_cbox"
    ID_CHECKBOX_PROFILE_NOT_MIGRATED = "id=ProfileNotMigrated_cbox"
    ID_CHECKBOX_IN_Service_Migration = "id=InServiceMigration_cbox"
    ID_CHECKBOX_BIOS = "id=Bios_cbox"
    ID_ERR_MSG_PASSWORD = "xpath=//label[@for='cic-enclosure-password']"
    ID_COMBO_ENCLOSURE_GROUP = "id=cic-enclosure-group-select-input"
    ID_ERR_MSG_ENCLOSURE_GROUP = "xpath=//label[@for='cic-enclosure-group-select-input']"
    ID_INPUT_ENCLOSURE_GROUP_NAME = "id=cic-enclosure-new-group"
    ID_ERR_MSG_ENCLOSURE_GROUP_NAME = "xpath=//label[@for='cic-enclosure-new-group']"
    ID_COMBO_LOGICAL_INTERCONNECT_GROUP = "id=cic-enclosure-lst-select-input"
    ID_ERR_MSG_LOGICAL_INTERCONNECT_GROUP = "xpath=//label[@for='cic-enclosure-lst-select-input']"
    ID_RADIO_LICENSING_HP_ONEVIEW_ADVANCED = "id=cic-enclosure-licensing-oneview-advanced"
    ID_RADIO_LICENSING_HP_ONEVIEW_ADVANCED_WO_ILO = "id=cic-enclosure-licensing-oneview-noilo"
    ID_SELECT_FIRMWARE_BASELINE = "id=cic-enclosure-firmware-baseline"
    ID_SELECT_FIRMWARE_BASELINE_CONTROL = "xpath=//select[@id='cic-enclosure-firmware-baseline']/../div"
    ID_CHECKBOX_FORCE_INSTALLATION = "id=cic-enclosure-firmware-force"
    ID_TEXT_VERIFYING_PARAMETERS = "xpath=//div/span[contains(., 'Verifying parameters...')]"
    ID_TEXT_CREATING_LIG = "xpath=//div/span[.='Creating logical interconnect group %s logical interconnect group']"
    ID_TEXT_ADDING_ENCLOSURE = "xpath=//div/span[contains(., 'Adding enclosure')]"
    ID_BUTTON_ADD = "id=cic-enclosure-add"
    ID_BUTTON_ADD_PLUS = "id=cic-enclosure-addplus"
    ID_BUTTON_CANCEL = "id=cic-enclosure-add-cancel"

    # create lig
    ID_CHECKBOX_OPERATING_MODE = "id=cic-switchtemplate-add-fcoemode"
    # ID_SELECT_BAY_TYPE = "id=cic-switch-template-edit-switch-type-1-%s"
    ID_SELECT_BAY_TYPE = "id=cic-switch-template-edit-switch-type-1-%s"
    ID_JAVASCRIPT_BAY_TYPE = "$('#cic-switch-template-edit-switch-type-1-%s').parent().find('div[class=\"hp-select\"]').trigger('click');"
    ID_JAVASCRIPT_SELECT_BAY_TYPE = "$('#cic-switch-template-edit-switch-type-1-%s').parent().find('span').filter(function(idx, elt){return $(elt).text()=='%s';}).trigger('click');"
    ID_DROPDOWN_BAY_TYPE_OPTION_LAYER = "xpath=//select[@id='cic-switch-template-edit-switch-type-1-%s']/..//ol[@class='hp-options']"
    ID_SELECTED_BAY_TYPE = "xpath=//select[@id='cic-switch-template-edit-switch-type-1-%s']/..//div[@class='hp-value'][.='%s']"

    ID_BUTTON_EDIT_LIG_ADD_UPLINK_SET = "id=cic-add-uplink-li"
    ID_BUTTON_EDIT_LIG_OK_AND_ADD_ENCLOSURE = "id=cic-switch-template-edit-ok-button"
    ID_BUTTON_EDIT_LIG_CANCEL = "id=cic-switch-template-edit-cancel-button"

    # internal networks
    ID_BUTTON_EDIT_LIG_EDIT_INTERNAL_NETWORKS = "xpath=//div[contains(@class, 'cic-internal-networks-edit-button')]"
    ID_DIALOG_EDIT_LIG_EDIT_INTERNAL_NETWORKS = "xpath=//h1[.='Edit Internal Networks']"
    ID_BUTTON_EDIT_LIG_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS = "id=cic-internal-nets-dialog-networks-addNetworks"
    ID_BUTTON_EDIT_LIG_EDIT_INTERNAL_NETWORKS_REMOVE_ALL = "id=cic-internal-nets-dialog-networks-removeAll"
    ID_DIALOG_EDIT_LIG_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS = "xpath=//h1[.='Add Networks']"
    ID_INPUT_EDIT_LIG_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS_SEARCH_NETWORK = "xpath=//div[@class='hp-association-selector']//input[@class='hp-search']"
    ID_TABLE_ROW_EDIT_LIG_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS = "xpath=//table//tr[td[.='%s']]"
    ID_BUTTON_EDIT_LIG_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS_ADD = "xpath=//button[.='Add']"
    ID_BUTTON_EDIT_LIG_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS_ADD_PLUS = "xpath=//button[.='Add +']"
    ID_BUTTON_EDIT_LIG_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS_CANCEL = "xpath=//form[@id='cic-internal-nets-dialog-form']//button[.='Cancel']"
    ID_BUTTON_EDIT_LIG_EDIT_INTERNAL_NETWORKS_OK = "id=cic-internal-nets-dialog-add"
    ID_BUTTON_EDIT_LIG_EDIT_INTERNAL_NETWORKS_CANCEL = "xpath=//form[@id='cic-internal-nets-dialog-form']//a[.='Cancel']"

    # create uplink set
    ID_DIALOG_EDIT_LIG_CREATE_UPLINK_SET = "id=cic-switchtemplate-dialog-form"  # dialog
    ID_INPUT_EDIT_LIG_CREATE_UPLINK_SET_NAME = "id=cic-switchtemplate-dialog-name"
    ID_SELECT_EDIT_LIG_CREATE_UPLINK_SET_TYPE = "id=cic-switchtemplate-dialog-type"
    ID_RADIO_EDIT_LIG_CREATE_UPLINK_SET_CONNECTION_MODE_AUTOMATIC = "id=cic-switchtemplate-dialog-auto-conntype"  # for ethernet
    ID_RADIO_EDIT_LIG_CREATE_UPLINK_SET_CONNECTION_MODE_FAILOVER = "id=cic-switchtemplate-dialog-fail-conntype"  # for ethernet
    ID_SELECT_EDIT_LIG_CREATE_UPLINK_SET_LACP_TIMER = "id=cic-switchtemplate-dialog-lacp-timer-select"  # for ethernet
    ID_BUTTON_EDIT_LIG_CREATE_UPLINK_SET_ADD_NETWORKS = "id=cic-switchtemplate-dialog-networks-addNetworks"  # for ethernet
    ID_BUTTON_EDIT_LIG_CREATE_UPLINK_SET_REMOVE_ALL_ETHERNET_NETWORKS = "id=cic-switchtemplate-dialog-networks-removeAll"  # for ethernet
    ID_BUTTON_EDIT_LIG_CREATE_UPLINK_SET_REMOVE_ALL_ETHERNET_PORTS = "id=cic-switchtemplate-dialog-ports-removeAll"  # for ethernet, tunnel, untagged
    ID_BUTTON_EDIT_LIG_CREATE_UPLINK_SET_ADD_UPLINK_PORTS = "id=cic-switchtemplate-dialog-uplinks-addUplinks"  # port of ethernet, tunnel, untagged
    ID_COMBO_EDIT_LIG_CREATE_UPLINK_SET_FC_NETWORK = "id=cic-switchtemplate-dialog-fc-addNetwork-input"  # fc network
    ID_COMBO_EDIT_LIG_CREATE_UPLINK_SET_FC_INTERCONNECT = "id=cic-switchtemplate-dialog-fc-switch-input"  # fc interconnect
    ID_COMBO_EDIT_LIG_CREATE_UPLINK_SET_TUNNEL_NETWORK = "id=cic-switchtemplate-dialog-tunnel-addNetwork-input"  # tunnel
    ID_COMBO_EDIT_LIG_CREATE_UPLINK_SET_UNTAGGED_NETWORK = "id=cic-switchtemplate-dialog-untagged-addNetwork-input"  # untagged
    ID_CHECKBOX_EDIT_LIG_CREATE_UPLINK_SET_ETHERNET_NATIVE = "xpath=//table//tr[td[.='%s']]//input"  # ethernet native network
    ID_CHECKBOX_EDIT_LIG_CREATE_UPLINK_SET_ETHERNET_PREFERRED_PORT = "xpath=//table//tr[td[2][.='%s'] and td[3][.='%s']]//input"  # ethernet preferred port
    ID_BUTTON_EDIT_LIG_CREATE_UPLINK_SET_REMOVE_ETHERNET_NETWORK = "xpath=//table//tr[td[.='%s']]//div"  # ethernet - remove network
    ID_BUTTON_EDIT_LIG_CREATE_UPLINK_SET_REMOVE_ETHERNET_PORT = "xpath=//table//tr[td[2][.='%s'] and td[3][.='%s']]//div"  # ethernet, tunnel, untagged - remove port
    ID_CHECKBOX_EDIT_LIG_CREATE_UPLINK_SET_FC_PORT = "xpath=//tr[@id='cic-switchtemplate-uplink-port-row-%s']//input"  # fc port
    ID_SELECT_CREATE_UPLINK_SET_FC_PORT_SPEED = "xpath=//table[@id='cic-switchtemplate-dialog-port-assigned']//tr[td[2][.='%s'] and td[3][.='%s']]/td[4]/div/div/div"  # fc port speed
    ID_DROPDOWN_CREATE_UPLINK_SET_FC_PORT_SPEED = "xpath=//table[@id='cic-switchtemplate-dialog-port-assigned']//tr[td[2][.='%s'] and td[3][.='%s']]/td[4]/div//ol/li[span[.='%s']]"  # fc port speed
    # - add networks to (ethernet)
    ID_DIALOG_EDIT_LIG_CREATE_UPLINK_SET_ADD_NETWORKS_TO = "xpath=//h1[contains(., 'Add Networks to')]"  # dialog
    ID_INPUT_EDIT_LIG_CREATE_UPLINK_SET_ADD_NETWORKS_TO_SEARCH_NETWORK = "xpath=//div[@class='hp-association-selector']//input[@class='hp-search']"
    ID_TABLE_ROW_EDIT_LIG_CREATE_UPLINK_SET_ADD_NETWORKS_TO = "xpath=//table//tr[td[.='%s']]"
    ID_BUTTON_EDIT_LIG_CREATE_UPLINK_SET_ADD_NETWORKS_TO_ADD = "xpath=//button[.='Add']"
    ID_BUTTON_EDIT_LIG_CREATE_UPLINK_SET_ADD_NETWORKS_TO_ADD_PLUS = "xpath=//button[.='Add +']"
    ID_BUTTON_EDIT_LIG_CREATE_UPLINK_SET_ADD_NETWORKS_TO_CANCEL = "xpath=//button[.='Cancel']"
    # - add uplink port (ethernet)
    ID_DIALOG_EDIT_LIG_CREATE_UPLINK_SET_ADD_UPLINK_PORTS_TO = "xpath=//h1[contains(., 'Add Uplink Ports to')]"  # dialog
    ID_INPUT_EDIT_LIG_CREATE_UPLINK_SET_ADD_UPLINK_PORT_SEARCH_PORT = "xpath=//div[@class='hp-association-selector']//input[@class='hp-search']"
    ID_TABLE_ROW_EDIT_LIG_CREATE_UPLINK_SET_ADD_UPLINK_PORT = "xpath=//table//tr[td[2][.='%s'] and td[3][.='%s']]"
    ID_BUTTON_EDIT_LIG_CREATE_UPLINK_SET_ADD_UPLINK_PORTS_ADD = "xpath=//button[.='Add']"
    ID_BUTTON_EDIT_LIG_CREATE_UPLINK_SET_ADD_UPLINK_PORTS_ADD_PLUS = "xpath=//button[.='Add +']"
    ID_BUTTON_EDIT_LIG_CREATE_UPLINK_SET_ADD_UPLINK_PORTS_CANCEL = "xpath=//button[.='Cancel']"

    ID_BUTTON_EDIT_LIG_CREATE_UPLINK_SET_ADD = "id=cic-switchtemplate-dialog-add"
    ID_BUTTON_EDIT_LIG_CREATE_UPLINK_SET_ADD_PLUS = "id=cic-switchtemplate-dialog-add-again"
    ID_BUTTON_EDIT_LIG_CREATE_UPLINK_SET_ADD_CANCEL = "xpath=//form[@id='cic-switchtemplate-dialog-form']//a[.='Cancel']"


class EditEnclosuresElements(object):
    ID_SELECT_ACTION_EDIT = "id=cic-enclosure-edit-action"
    ID_DIALOG_EDIT_ENCLOSURE = "id=cic-enclosure-edit-form"
    ID_INPUT_EDIT_ENCLOSURE_ENCLOSURE_NAME = "id=cic-enclosure-name"
    ID_BUTTON_EDIT_ENCLOSURE_OK = "id=cic-enclosure-update"
    ID_BUTTON_EDIT_ENCLOSURE_CANCEL = "id=cic-enclosure-edit-cancel"
    ID_TEXT_INVALID_NAME_ERROR = "//label[text()='32 or fewer alphanumeric, dash, or underscore characters.']"


class ResetLinkModuleElements(object):
    ID_STATUS_NOTIFICATION_UNKNOWN = "xpath=//div[@id='hp-page-notifications']/div/header/div[@class='hp-status hp-status-unknown']"
    ID_STATUS_NOTIFICATION_OK = "xpath=//div[@id='hp-page-notifications']/div/header/div[@class='hp-status hp-status-ok']"
    ID_STATUS_NOTIFICATION_WARN = "xpath=//div[@id='hp-page-notifications']/div/header/div[@class='hp-status hp-status-warning']"
    ID_SELECT_ACTION_RESET_LINK_MODULE = "id=cic-enclosure-reset-em-action"
    ID_DIALOG_RESET_LINK_MODULE = "id=cic-enclosure-reset-em-form"
    ID_BUTTON_YES_RESET = "xpath=//button[.='Yes, reset']"
    ID_BUTTON_CANCEL = "xpath=//button[.='Cancel']"
    ID_CHECKBOX_RESET_UNKNOWN_LINK_MODULE = "xpath=//div[@id='cic-enclosure-reset-em-radio']/ul/li/label[text()='unknown']"
    ID_CHECKBOX_RESET_STANDBY_LINK_MODULE = "xpath=//div[@id='cic-enclosure-reset-em-radio']/ul/li/label[text()='standby']"
    ID_CHECKBOX_RESET_ACTIVE_LINK_MODULE = "xpath=//div[@id='cic-enclosure-reset-em-radio']/ul/li/label[text()='active']"


class RemoveEnclosuresElements(object):
    ID_SELECT_ACTION_REMOVE = "link=Remove"
    # ID_DIALOG_REMOVE = "id=hp-enclosure-remove-dialog"  # dialog
    # 2015-12-22 Alex Ma changed Remove Enclosure dialog xpath from hp-enclosure-remove-dialog to cic-enclosure-remove-dialog due to failure during OVAQual
    ID_DIALOG_REMOVE = "id=cic-enclosure-remove-dialog"  # dialog
    ID_CHECKBOX_FORCE_REMOVE_ENCLOSURE = "//*[@id='cic-enclosure-force-remove']"
    ID_BUTTON_YES_REMOVE = "xpath=//button[.='Yes, remove']"
    ID_BUTTON_CANCEL = "xpath=//button[.='Cancel']"
    ID_TABLE_ENCLOSURE_DELETED = "xpath=//table/tbody/tr[contains(@class, 'hp-not-found')]/td[text()='%s']"  # enclosure table list
    ID_TEXT_REMOVE_PROFILE = "id=cic-enclosure-details-remove-profiles"
    ID_BUTTON_CLOSE = "xpath=//button[.='Close']"


class RefreshEnclosuresElements(object):
    ID_SELECT_ACTION_REFRESH = "id=cic-enclosure-refresh-action"


class ReapplyEnclosuresElements(object):
    ID_SELECT_ACTION_REAPPLY_CONFIGURATION = "id=cic-enclosure-reconfigure-action"


class EditScopeElements(object):
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


class InterconnectLinkTopologyElements(object):
    # tbird interconnect link topology
    ID_ENCLOSURE_LIST = "xpath=//*[@class='hp-device-header' and starts-with(@id, 'cic-enclosure-cxport-cxpencl')]/a"
    ID_DROPDOWN_INTERCONNECT_BAYSET = "xpath=//*[@id='cic-enclosure-cxport-form']//li/label[text()='View interconnect bay set']/following-sibling::div[@class='hp-form-content']//div[@class='hp-value']"
    ID_SELECT_INTERCONNECT_BAYSET = "xpath=//*[@id='cic-enclosure-cxport-form']//li/label[text()='View interconnect bay set']/following-sibling::div[@class='hp-form-content']//div/ol/li[@data-id='%s']"
    ID_DROPDOWN_VIEWSIDE = "xpath=//*[@id='cic-enclosure-cxport-form']//li/label[text()='View side']/following-sibling::div[@class='hp-form-content']//div[@class='hp-value']"
    ID_SELECT_VIEWSIDE = "xpath=//*[@id='cic-enclosure-cxport-form']//li/label[text()='View side']/following-sibling::div[@class='hp-form-content']//div/ol/li[@data-id='%s']"
    ID_TEXT_INTERCONNECT_BAYSET_DROPDOWN = "xpath=//*[@id='cic-enclosure-cxport-form']//li/label[text()='View interconnect bay set']/following-sibling::div[@class='hp-form-content']//div[@data-id='%s']"
    ID_TEXT_VIEWSIDE_DROPDOWN = "xpath=//*[@id='cic-enclosure-cxport-form']//li/label[text()='View side']/following-sibling::div[@class='hp-form-content']//div[@data-id='%s']"
    ID_ENCLOSURE_CXPPORT_BAY_INFORMATION = "xpath=//div[@id='cic-enclosure-cxport-cxp-encl-name-%s']/div[not(contains(@class,'disabled')) ]"
    ID_CLICK_ENCLOSURE_CXPPORT = "id=cic-enclosure-cxport-cxp-e%sb%sp%s"
    ID_ENCLOSURE_CXPPORT_STATUS = "xpath=//*[@id='cic-enclosure-cxport-cxp-e%sb%sp%s']/div/span[@class='hp-value']"
    ID_ENCLOSURE_CXPPORT_CONNECTED_WEBELEMENT = "xpath=//*[@id='cic-enclosure-cxport-cxp-e%sb%sp%s']@data-connect"
    ID_ENCLOSURE_CXPPORT_CONNECTED_PORT = "xpath=//*[@id='%s']/div[@class='hp-name']"
    ID_LABEL_PAGE_ERROR_COUNT = "xpath = //*[@id='hp-page-notifications']//div/header/ol/li[@class='hp-summary-error']//div[not(contains(@class, 'hp-unset'))]/following-sibling::div[@class='hp-count']"
    ID_ENCLOSURE_CXPPORT_CONNECTED_IC = "xpath =//*[@id='%s']/a"
    ID_FILTER_ALL_STATES = "xpath = //div[@id='hp-activity-state-filter']/div[@class='hp-value' and contains(text(),'All states')]"
    ID_FILTER_BY_STATE = "xpath = //div[@id='hp-activity-state-filter']/ol/li[text()='%s']"
    ID_LABEL_PAGE_CLICK_ERROR = "xpath = //*[@class='dataTables_wrapper']//tbody/tr[%s]/td/div[contains(@class,'hp-collapser')]"
    ID_LABEL_PAGE_ERROR = "xpath = //*[@class='dataTables_wrapper']//tbody[@role='alert']/tr[%s]/td[@class='hp-name']"
    ID_LABEL_PAGE_ERROR_FULL = "xpath=//*[@class='dataTables_wrapper']//tbody/tr[%s]/td//span[@class='hp-resolution']"
    ID_LABEL_EVENT_CLICK_ERROR = "//*[@class='dataTables_wrapper']//tbody/tr[%s]//div/label[@data-localize='fs.alerts.eventData.eventDetails']"
    ID_EVENT_MESSAGE = "//*[@class='dataTables_wrapper']//tbody/tr[%s]//div[contains(@class, 'hp-alert-events')]"
    ID_CXPPORT_CXPENCLOSURE = "xpath = //*[@id='cic-enclosure-cxport-cxpencl%s']/a"
    ID_CXPPORT_CXPENCLOSURE_STATUS = "//*[@id='cic-enclosure-cxport-cxpencl%s']//span[@class='hp-value']"
    ID_TEXT_CXPPORT_CXP_INTERCONNECTS = "//*[@id='cic-enclosure-cxport-cxp-bay-id-%s']//a[.='%s']"
    ID_ALERT_STATE = "xpath = //*[@id='hp-page-notifications']//div/header/div[@class='hp-state']"
    ID_ALERT_MSG = "xpath = //*[@id='hp-page-notifications']//div/header/div[@class='hp-message']"
