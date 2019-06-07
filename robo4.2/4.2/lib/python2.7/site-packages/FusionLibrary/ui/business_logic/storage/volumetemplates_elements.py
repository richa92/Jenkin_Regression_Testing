"""
    Elements used on the Volume Templates Page
"""


class GeneralVolumeTemplateElements(object):
    """
        General Elements used on the Volume Templates Page
    """

    ID_DROPDOWN_ACTIONS = "xpath=//label[text()='Actions']"
    ID_PAGE_LABEL = "xpath=//div[@class='hp-page-label']/h1[text()='Volume Templates']"
    ID_TABLE_VOLUME_TEMPLATE = "xpath=//table/tbody/tr/td[text()='%s']"  # volume template
    ID_TABLE_VOLUME_TEMPLATES = "xpath=//table/tbody/tr/td[2]"
    ID_TABLE_VOLUME_TEMPLATE_SELECTED = "xpath=//table/tbody/tr[contains(@class, 'hp-selected')]/td[text()='%s']"  # volume template
    ID_TABLE_VOLUME_TEMPLATE_DELETED = "xpath=//table/tbody/tr[contains(@class, 'hp-not-found')]/td[text()='%s']"  # volume template
    ID_STATUS_VOLUME_TEMPLATE_OK = "xpath=//table/tbody/tr/td[text()='%s']/../td/div[@class='hp-status hp-status-ok']"  # volume template
    ID_STATUS_VOLUME_TEMPLATE_WARN = "xpath=//table/tbody/tr/td[text()='%s']/../td/div[@class='hp-status hp-status-warning']"  # volume template
    ID_STATUS_VOLUME_TEMPLATE_ERROR = "xpath=//table/tbody/tr/td[text()='%s']/../td/div[@class='hp-status hp-status-error']"  # volume template
    ID_RIGHT_SIDEBAR_ACTIVITY = "xpath=//*[@id='cic-storagetemplates-page']/nav/div[@class='hp-sidebar-control']/div[@class='hp-pin-right']"
    ID_TEXT_ACTIVITY_ACTION_TITLE = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-activity-message']/p/span"  # volume template
    ID_TEXT_ACTIVITY_ACTION_OK = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-ok']"  # volume template
    ID_TEXT_ACTIVITY_ACTION_WARN = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-warning']"  # volume template
    ID_TEXT_ACTIVITY_ACTION_ERROR = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-error']"  # volume template
    ID_TEXT_ACTIVITY_ACTION_DETAILS_OK = "//header[@class='hp-active']/a[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-ok']"  # volume template
    ID_TEXT_ACTIVITY_MESSAGE = "//*[@id='hp-flyout-activities']/li/div[@class='hp-full']/div/div[@class='hp-notification-details']"
    ID_TEXT_ACTIVITY_EDIT_SETTINGS_TITLE = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-message']/p/span[text()='Edit Settings']"
    ID_TEXT_ACTIVITY_EDIT_SETTINGS_OK = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-message']/p/span[text()='Edit Settings']/../../../div[@class='hp-status hp-status-ok']"
    ID_TEXT_ACTIVITY_EDIT_SETTINGS_WARN = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-message']/p/span[text()='Edit Settings']/../../../div[@class='hp-status hp-status-warning']"
    ID_TEXT_ACTIVITY_EDIT_SETTINGS_ERROR = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-message']/p/span[text()='Edit Settings']/../../../div[@class='hp-status hp-status-error']"
    ID_TEXT_ACTIVITY_SPECIFACTION_OK = "//ol[@id='hp-flyout-activities']/li/div/div[@class='hp-activity-message']/p/span[text()='%s']/../../../div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-ok']"  # actionname, volume template
    ID_TEXT_ACTIVITY_SPECIFACTION_WARN = "//ol[@id='hp-flyout-activities']/li/div/div[@class='hp-activity-message']/p/span[text()='%s']/../../../div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-warning']"  # actionname, volume template
    ID_TEXT_ACTIVITY_SPECIFACTION_ERROR = "//ol[@id='hp-flyout-activities']/li/div/div[@class='hp-activity-message']/p/span[text()='%s']/../../../div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-error']"  # actionname, volume template
    ID_DROPDOWN_PANEL_SELECTOR = "id=cic-storagetemplates-panel-selector"
    ID_SELECT_PANEL_OVERVIEW = "//ol[@class='hp-options']/li/a[text()='Overview']"
    ID_SELECT_PANEL_GENERAL = "//ol[@class='hp-options']/li/a[text()='General']"
    ID_SELECT_PANEL_ADVANCED = "//ol[@class='hp-options']/li/a[text()='Advanced']"
    ID_SELECT_PANEL_VOLUME_PROPERTIES = "//ol[@class='hp-options']/li/a[text()='Volume Properties']"
    ID_TEXT_GENERAL_DESCRIPTION = "id=cic-storagetemplates-details-description"
    ID_TEXT_GENERAL_STORAGE_SYSTEM = "id=cic-storagetemplates-details-array"
    ID_TEXT_GENERAL_STORAGE_POOL = "id=cic-storagetemplates-details-pool"
    ID_TEXT_GENERAL_SNAPSHOT_STORAGE_POOL = "id=cic-storagetemplates-details-snapshotpool"
    ID_TEXT_VOLUME_PROPERTIES_CAPACITY = "id=cic-storagetemplates-details-requestedSize"
    ID_TEXT_VOLUME_PROPERTIES_PROVISIONING = "id=cic-storagetemplates-details-provisioningType"
    ID_TEXT_VOLUME_PROPERTIES_SHARING = "id=cic-storagetemplates-details-sharableLabel"
    ID_LINK_STORAGE_SYSTEMS = "xpath=//*[@id='cic-storagetemplates-details-array-value']/a"
    ID_LINK_STORAGE_POOLS = "xpath=//*[@id='cic-storagetemplates-details-storagePool-value']/a"
    ID_LINK_STORAGE_VOLUMES = "xpath=//*[@id='cic-storagetemplates-details-used-by']/div/a[1]"
    UNABLE_TO_LOCATE_ERROR = "xpath=/html/body/div[2]/div[1]/div/div[3]/div[2]/section[2]/div/h1[text()='%s']"


class CreateVolumeTemplateElements(object):
    """
        Elements used on the Create Volume Templates Page
    """
    ID_BUTTON_CREATE_VOLUME_TEMPLATE = "link=Create volume template"
    ID_SELECT_ACTION_CREATE = "id=cic-storagetemplates-create-action"
    ID_DIALOG_CREATE_VOLUME_TEMPLATE = "id=cic-storagetemplates-add-dialog"
    ID_INPUT_NAME = "id=cic-storagetemplates-add-name"
    ID_INPUT_DESCRIPTION = "id=cic-storagetemplates-add-description"
    ID_INPUT_STORAGE_POOL = "id=cic-storagetemplates-add-pool-input"
    ID_SELECT_STORAGE_POOL = "xpath=//*[@id='cic-storagetemplates-add-form']//input[@id='cic-storagetemplates-add-pool-input']/../div[@class='hp-search-combo-spacer']/div[@class='hp-search-combo-menu']/ol/li/span[contains(text(), '%s') ]/../span[@class='hp-name' and text()='%s']"  # storage name, pool name
    ID_INPUT_SNAPSHOT_STORAGE_POOL = "id=cic-storagetemplates-add-snapshotPool-input"
    ID_SELECT_SNAPSHOT_STORAGE_POOL = "xpath=//*[@id='cic-storagetemplates-add-form']//input[@id='cic-storagetemplates-add-snapshotPool-input']/../div/div[@class='hp-search-combo-menu']/ol/li/span[contains(text(), '%s') ]/../span[@class='hp-name' and text()='%s']"  # storage name, pool name
    ID_DROPDOWN_PANEL_SELECTOR = "id=cic-storagetemplates-add-panel-selector"
    ID_SELECT_PANEL_VOLUME_PROPERTIES = "xpath=//ol[@class='hp-options']/li/a[text()='Volume Properties']"
    ID_INPUT_CAPACITY = "id=cic-storagetemplates-add-capacity"
    ID_DROPDOWN_PROVISIONING = "xpath=//li[@id='cic-storagetemplates-add-advanced']/fieldset/ol/li[descendant::label[contains(.,'Provisioning')]]//div[@class='hp-value']"
    ID_SELECT_PROVISIONING_THIN = "xpath=//li[@id='cic-storagetemplates-add-advanced']/fieldset/ol/li[descendant::label[contains(.,'Provisioning')]]//ol[@class='hp-options']//span[text()='Thin']"
    ID_SELECT_PROVISIONING_FULL = "xpath=//li[@id='cic-storagetemplates-add-advanced']/fieldset/ol/li[descendant::label[contains(.,'Provisioning')]]//ol[@class='hp-options']//span[text()='Full']"
    ID_RADIO_SHARING_PRIVATE = "id=cic-storagetemplates-add-pool-private"
    ID_RADIO_SHARING_SHARED = "id=cic-storagetemplates-add-pool-shared"
    ID_BUTTON_CREATE = "id=cic-storagetemplates-add-ok"
    ID_BUTTON_CREATE_PLUS = "id=cic-storagetemplates-addplus"
    ID_BUTTON_CANCEL = "//input[@id='cic-storagetemplates-add-cancel']"
    ID_TEXT_CREATING_VOLUME_TEMPLATE = "xpath=//*[@id='hp-form-message']/div[1]/span[contains(.,'Creating volume template')]"

    ID_DROPDOWN_DATA_PROTECTION_LEVEL = "xpath=//li[@id='cic-storagetemplates-add-advanced']/fieldset/ol/li[descendant::label[contains(.,'Data protection level')]]//div[@class='hp-value']"
    ID_SELECT_DATA_PROTECTION_LEVEL = "xpath=//li[@id='cic-storagetemplates-add-advanced']/fieldset/ol/li[descendant::label[contains(.,'Data protection level')]]//ol[@class='hp-options']//span[text()='%s']"  # data protection level
    ID_DROPDOWN_PERFORMANCE_POLICY = "xpath=//*[@id='cic-storagetemplates-add-performance-policy-form-content']/div[2]/div[2]/div"
    ID_DROPDOWN_VOLUME_SET = "xpath=//*[@id='cic-storagetemplates-add-volume-set-form-content']/div[2]/div[2]/div"
    ID_DROPDOWN_FOLDER = "xpath=//*[@id='cic-storagetemplates-add-folder-form-content']/div[2]/div[2]/div"
    ID_SELECT_PERFORMANCE_POLICY = "//*[@id='cic-storagetemplates-add-performance-policy-form-content']/div[2]/div[3]/div/ol[2]/li/span[text()='%s']"  # performance policy
    ID_SELECT_VOLUME_SET = "xpath=//*[@id='cic-storagetemplates-add-volume-set-form-content']/div[2]/div[3]/div/ol[2]/li/span[text()='%s']"  # volume set
    ID_SELECT_FOLDER = "xpath=//*[@id='cic-storagetemplates-add-folder-form-content']/div[2]/div[3]/div/ol[2]/li/span[text()='%s']"  # data protection level
    ID_TOGGLE_ADAPTIVE_OPTIMIZATION = "xpath=//*[@id='cic-storagetemplates-add-adaptive-optimization-hpToggle']"
    ID_ICON_CAPACITY_LOCKED = "xpath=//div[@id='cic-storagetemplates-add-capacity-lock' and contains(@class, 'hp-lock-clickable hp-lock')]"
    ID_ICON_CAPACITY_UNLOCKED = "xpath=//div[@id='cic-storagetemplates-add-capacity-lock' and contains(@class, 'hp-lock-clickable hp-unlock')]"
    ID_ICON_SHARING_LOCKED = "xpath=//div[@id='cic-storagetemplates-add-pool-sharing-lock' and contains(@class, 'hp-lock-clickable hp-lock')]"
    ID_ICON_SHARING_UNLOCKED = "xpath=//div[@id='cic-storagetemplates-add-pool-sharing-lock' and contains(@class, 'hp-lock-clickable hp-unlock')]"
    ID_ICON_PROVISIONING_LOCKED = "xpath=//div[@id='cic-storagetemplates-add-provisioning-lock' and contains(@class, 'hp-lock-clickable hp-lock')]"
    ID_ICON_PROVISIONING_UNLOCKED = "xpath=//div[@id='cic-storagetemplates-add-provisioning-lock' and contains(@class, 'hp-lock-clickable hp-unlock')]"
    ID_ICON_SNAPSHOT_POOL_LOCKED = "xpath=//div[@id='cic-storagetemplates-add-snapshotPool-lock' and contains(@class, 'hp-lock-clickable hp-lock')]"
    ID_ICON_SNAPSHOT_POOL_UNLOCKED = "xpath=//div[@id='cic-storagetemplates-add-snapshotPool-lock' and contains(@class, 'hp-lock-clickable hp-unlock')]"


class EditVolumeTemplateElements(object):
    """
        Elements used on the Edit Volume Templates Page
    """
    ID_SELECT_ACTION_EDIT = "id=cic-storagetemplates-edit-action"
    ID_DIALOG_EDIT = "id=cic-storagetemplates-edit-dialog"
    ID_INPUT_NAME = "id=cic-storagetemplates-edit-name"
    ID_INPUT_DESCRIPTION = "id=cic-storagetemplates-edit-description"
    ID_INPUT_STORAGE_POOL = "xpath=//input[@id='cic-storagetemplates-edit-pool-input']"
    ID_SELECT_STORAGE_POOL = "xpath=//*[@id='cic-storagetemplates-edit-form']//div[@class='hp-search-combo-menu']/ol/li/span[contains(text(), '%s') ]/../span[@class='hp-name' and text()='%s']"  # storage name, pool name
    ID_INPUT_SNAPSHOT_STORAGE_POOL = "id=cic-storagetemplates-edit-snapshotPool-input"
    ID_SELECT_SNAPSHOT_STORAGE_POOL = "xpath=//*[@id='cic-storagetemplates-edit-snapshotPool-input']/../div/div[@class='hp-search-combo-menu']/ol/li/span[contains(text(), '%s') ]/../span[@class='hp-name' and text()='%s']"  # storage name, pool name
    ID_DROPDOWN_PANEL_SELECTOR = "id=cic-storagetemplates-edit-panel-selector"
    ID_SELECT_PANEL_VOLUME_PROPERTIES = "xpath=//ol[@class='hp-options']/li/a[text()='Volume Properties']"
    ID_INPUT_CAPACITY = "id=cic-storagetemplates-edit-capacity"
    ID_DROPDOWN_PROVISIONING = "xpath=//li[@id='cic-storagetemplates-edit-advanced']/fieldset/ol/li[descendant::label[contains(.,'Provisioning')]]//div[@class='hp-value']"
    ID_SELECT_PROVISIONING_THIN = "xpath=//li[@id='cic-storagetemplates-edit-advanced']/fieldset/ol/li[descendant::label[contains(.,'Provisioning')]]//ol[@class='hp-options']//span[text()='Thin']"
    ID_SELECT_PROVISIONING_FULL = "xpath=//li[@id='cic-storagetemplates-edit-advanced']/fieldset/ol/li[descendant::label[contains(.,'Provisioning')]]//ol[@class='hp-options']//span[text()='Full']"
    ID_RADIO_SHARING_PRIVATE = "id=cic-storagetemplates-edit-pool-private"
    ID_RADIO_SHARING_SHARED = "id=cic-storagetemplates-edit-pool-shared"
    ID_BUTTON_OK = "id=cic-storagetemplates-edit-ok"
    ID_BUTTON_CANCEL = "id=cic-storagetemplates-edit-cancel"
    ID_TEXT_EDITING_VOLUME_TEMPLATE = "xpath=//*[@id='hp-form-message']/div[1]/span[contains(.,'Editing volume template')]"
    ID_DROPDOWN_DATA_PROTECTION_LEVEL = "xpath=//li[@id='cic-storagetemplates-edit-advanced']/fieldset/ol/li[descendant::label[contains(.,'Data protection level')]]//div[@class='hp-value']"
    ID_SELECT_DATA_PROTECTION_LEVEL = "xpath=//li[@id='cic-storagetemplates-edit-advanced']/fieldset/ol/li[descendant::label[contains(.,'Data protection level')]]//ol[@class='hp-options']//span[text()='%s']"
    ID_DROPDOWN_FOLDER = "xpath=//*[@id='cic-storagetemplates-edit-folder-form-content']/div[2]/div[2]/div"
    ID_SELECT_FOLDER = "xpath=//*[@id='cic-storagetemplates-edit-folder-form-content']/div[2]/div[3]/div/ol[2]/li/span[text()='%s']"
    ID_DROPDOWN_PERFORMANCE_POLICY = "xpath=//*[@id='cic-storagetemplates-edit-performance-policy-form-content']/div[2]/div[2]/div"
    ID_SELECT_PERFORMANCE_POLICY = "xpath=//*[@id='cic-storagetemplates-edit-performance-policy-form-content']/div[2]/div[3]/div/ol[2]/li[2]/span[text()='%s']"
    ID_DROPDOWN_VOLUMESET = "xpath=//*[@id='cic-storagetemplates-edit-volume-set-form-content']/div[2]/div[2]/div"
    ID_SELECT_VOLUMESET = "xpath=//*[@id='cic-storagetemplates-edit-volume-set-form-content']/div[2]/div[3]/div/ol[2]/li/span[text()='%s']"
    ID_TOGGLE_ADAPTIVE_OPTIMIZATION = "xpath=//*[@id='cic-storagetemplates-edit-adaptive-optimization-hpToggle']"
    ID_BUTTON_LOCK_SELECT = "id=cic-storagetemplates-edit-%s-lock"


class EditVolumeTemplateSettingsElements(object):
    """
        Additional Elements used on the Edit Volume Templates Page
    """
    ID_SELECT_ACTION_EDIT_SETTINGS = "id=cic-storagetemplates-edit-settings-action"
    ID_DIALOG_EDIT_SETTINGS = "id=cic-storagetemplates-edit-settings-dialog"
    ID_CHECKBOX_REQUIRE_TEMPLATE_FOR_VOLUME_CREATION = "id=cic-storagetemplates-edit-settings-require-template"
    ID_BUTTON_OK = "id=cic-storagetemplates-edit-settings-ok"
    ID_BUTTON_CANCEL = "id=cic-storagetemplates-edit-settings-cancel"


class DeleteVolumeTemplateElements(object):
    """
        Elements used on the Delete Volume Templates Page
    """
    ID_SELECT_ACTION_DELETE = "id=cic-storagetemplates-delete-action"
    ID_DIALOG_DELETE = "xpath=//div[@class='hp-dialog']/header/h1/span[text()='Delete']"
    ID_BUTTON_YES_DELETE = "id=cic-confirm-ok"
    ID_BUTTON_CANCEL = "//button[text()='Cancel']"
