# (C) Copyright 2014 Hewlett-Packard Development Company, L.P.


class systemprofilesPage(object):
    ID_PAGE_LABEL = "xpath=//*[@class='hp-page-label']/*[text()='System Profiles']"
    ID_ONEVIEW_TAB = "//*[@id='hp-main-menu-label']"
    ID_LINK_SYSTEM_PROFILE = "link=System Profiles"
    ID_LABEL_SYSTEM_PROFILE_NAME = "id=cic-systemprofiles-details-title"
    ID_DROPDOWN_VIEW_SELECTOR = "id=cic-systemprofiles-panel-selector"

    # Actions
    ID_DROPDOWN_ACTIONS = "id=cic-systemprofiles-actions"
    ID_DROPDONW_OPTION_REFRESH_ACTION = "id=cic-systemprofiles-refresh-action"
    ID_DROPDONW_OPTION_EDIT_ACTION = "id=cic-systemprofiles-edit-action"
    ID_REFRESH_POPUP_ERROR_CLOSE_BUTTON = "id='cic-systemprofiles-refresh-close"

    # View
    ID_DROPDOWN_OPTION_OVERVIEW = "xpath=//*[@data-localize='systemprofiles.show.overview' and text()='Overview']"
    ID_DROPDOWN_OPTION_GENERAL_VIEW = "xpath=//*[@data-panel-id='cic-systemprofiles-general']"
    ID_DROPDOWN_OPTION_ACTIVITY_VIEW = "xpath=//*[@data-localize='core.menu.activity']"
    ID_BUTTON_MAP = "//*[@id='cic-systemprofiles-show']/descendant::*[@tooltip='Map']"
    ID_LABEL_GENERAL = "//*[@id='cic-systemprofiles-more-general']"
    ID_LABEL_MAP = "//*[@class='hp-value'][text()='Map']"

    # Activities
    ID_ACTIVITY_TABLE = "id=hp-activity-resource-view"
    ID_ICON_ACTIVITY = "id=hp-activity-control"
    ID_ACTIVITY_FLYOUT_TASK_BRIEF = "//*[@id='hp-flyout-activities']/descendant::*[@class='hp-brief']"
    ID_ICON_ACTIVITY_FLYOUT_TASK_BRIEF_STATUS_OK = ID_ACTIVITY_FLYOUT_TASK_BRIEF + "/*[@class='hp-status hp-status-ok']"
    ID_ACTIVITY_FLYOUT_TASK_FULL = "//*[@id='hp-activity-flyout']/descendant::*[@class='hp-full']"

    # Compliance notification
    ID_SYSTEM_PROFILE_NOTIFICATION = "//*[@id='hp-page-notifications' and @class='hp-available']"
    ID_SYSTEM_PROFILE_NOTIFICATION_TASK_NAME = ID_SYSTEM_PROFILE_NOTIFICATION + "/descendant::*[@class='hp-message']/descendant::span"
    ID_EXPANDED_TASK = "//*[contains(@class, 'hp-task hp-expanded')]"
    ID_EXPANDED_TASK_STATE = ID_EXPANDED_TASK + "/descendant::*[@class='hp-duration']/preceding-sibling::*"
    ID_BUTTON_TASK_DETAILS = "//*[@id='hp-page-notifications']/descendant::*[@class='hp-activity-details']"

    # System Profiles' Map View
    ID_MAP_COMPONENT = ".//*[@class='hp-bucket'][label='%s']"  # replace %s with the desired map component type (e.g. System Types)
    ID_LABEL_MAP_TYPE = ID_MAP_COMPONENT + "/label"  # to get the label name when needed
    ID_MAP_COMPONENT_ITEM = ID_MAP_COMPONENT + "/descendant::*[@class='hp-name']"  # gets the component content
    # TODO: Remove these specific elements for map components when creating new methods to validate the Map page
    ID_MAP_SYSTEM_PROFILE = "xpath=//ol[@class='hp-buckets']/li[1]/ol/li"
    ID_MAP_SYSTEMS = "xpath=//ol[@class='hp-buckets']/li[2]/ol/li"

    # Overview >> General items
    ID_PRODUCT_NUMBER_LABEL = "//*[@rel='localize[systemprofiles.general.product_number]']"
    ID_PRODUCT_NUMBER_CONTENT = "id=cic-systems-product-number"
    ID_SERIAL_NUMBER_LABEL = "//*[@rel='localize[systemprofiles.general.serial_number]']"
    ID_SERIAL_NUMBER_CONTENT = "id=cic-systems-serial-number"
    ID_SYSTEM_TYPE_LABEL = "//*[@class='hp-form-item']/label[@rel='localize[systemprofiles.general.system_type]']"
    ID_SYSTEM_TYPE_CONTENT = "id=cic-systemtypes-system-type"
    ID_SYSTEM_TYPE_VERSION_LABEL = "//*[@class='hp-form-item']/label[@rel='localize[systemprofiles.general.system_type_version]']"
    ID_SYSTEM_TYPE_VERSION_CONTENT = "id=cic-systemtypes-version"
    ID_MODEL_LABEL = "//*[@class='hp-form-item']/label[@rel='localize[systemprofiles.general.model]']"
    ID_MODEL_CONTENT = "id=cic-systemtypes-model"
    ID_LAST_REFRESH_LABEL = "//*[@class='hp-form-item']/label[@data-localize='systemprofiles.general.last_refresh']"
    ID_LAST_REFRESH_CONTENT = "//*[@id='cic-systemprofiles-last-refresh']/span[@class='hp-value']"

    # System Profiles page status
    ID_ICON_SYSTEM_PROFILE_HEALH_STATUS = "xpath=.//*[@id='cic-systemprofiles-details-status'][contains(@class,'hp-status-%s')]"  # replace %s with the status to be verified

    # System profile's list
    ID_SYSTEM_PROFILES_TABLE = "//*[@id='cic-systemprofiles-master-table']/"
    # Next element is the status of a specific system profile in the list of system profiles
    ID_SYSTEM_PROFILE_NAME_IN_TABLE = ID_SYSTEM_PROFILES_TABLE + "descendant::*[text()='%s']"
    ID_ICON_SYSTEM_PROFILE_LEFT_FRAME_HEALTH_STATUS = ID_SYSTEM_PROFILES_TABLE + "descendant::*[contains(@class,'hp-status-%s') and parent::*[following-sibling::*[text()='%s']]]"
    # TODO: remove this element when checkElements method is changed
    ID_HEALTH_ICON = ID_SYSTEM_PROFILES_TABLE + "descendant::*[@class='hp-status hp-status-ok']"

    # Accessing content items
    ID_LABEL_CONTENTS = "xpath=//label[@data-localize='systemprofiles.show.contents']"
    OVERVIEW_CONTENTS = "xpath=//*[@id='cic-systemprofiles-contents']"
    OVERVIEW_CONTENT_CATEGORY_LABEL = OVERVIEW_CONTENTS + "/li[label[text() = '%s']]"
    # accessing further components' elements
    MAP_CONTENT_RESOURCE_ITEM = OVERVIEW_CONTENT_CATEGORY_LABEL + "/div[span[@id='cic-systemprofiles-resource-link']/a[contains(@href, '%s')]]"
    MAP_CONTENT_ITEM_RED_STATUS = MAP_CONTENT_RESOURCE_ITEM + "/span[@class='hp-status hp-status-error' and @id='cic-systemprofiles-contents-status']"
    MAP_CONTENT_ITEM_YELLOW_STATUS = MAP_CONTENT_RESOURCE_ITEM + "/span[@class='hp-status hp-status-warning' and @id='cic-systemprofiles-contents-status']"
    MAP_CONTENT_ITEM_GREEN_STATUS = MAP_CONTENT_RESOURCE_ITEM + "/span[@class='hp-status hp-status-ok' and @id='cic-systemprofiles-contents-status']"
    MAP_CONTENT_ITEM_STATUS = MAP_CONTENT_RESOURCE_ITEM + "/span[@id='cic-systemprofiles-contents-status']"

    # Edit system profile page
    ID_PAGE_TITLE_EDIT_SYSTEM_PROFILE = "id=cic-systemprofiles-edit-details-title"
    ID_PAGE_TITLE_EDIT_SYSTEM_PROFILE_NAME = "id=cic-systemprofiles-details-title"
    # View
    ID_DROPDOWN_EDIT_SYSTEM_PROFILE_PANEL_SELECTOR = "id=cic-systemprofiles-panel-edit-selector"
    ID_DROPDOWN_OPTION_EDIT_SYSTEM_PROFILE_GENERAL = "data-panel-id=cic-systemprofiles-panel-edit-basic"
    ID_DROPDOWN_OPTION_EDIT_SYSTEM_PROFILE_RACKS = "data-panel-id=cic-systemprofiles-panel-edit-racks"
    ID_BUTTON_EDIT_SYSTEM_PROFILE = "id=cic-systemprofiles-update"
    ID_BUTTON_CANCEL_EDIT_SYSTEM_PROFILE = "id=cic-systemprofiles-edit-cancel"
    # General section
    ID_INPUT_SYSTEM_PROFILE_NAME = "id=cic-systemprofiles-edit-name"
    # Racks section
    ID_TABLE_EDIT_SYSTEM_PROFILE_RACKS = "xpath=//*[@id='cic-systemprofiles-edit-rack-table']"
    ID_LABEL_RACK_NAME = ID_TABLE_EDIT_SYSTEM_PROFILE_RACKS + "//*[text()='%s']"  # replace %s by the rack name
    ID_BUTTON_REMOVE_RACK = ID_LABEL_RACK_NAME + "/../..//*[@class='hp-close']"

    ID_EDIT_SYSTEM_PROFILE_ERROR_NOTIFICATION = "xpath =//*[contains(text(),'Unable to update system profile')]"

    # Add Rack
    ID_BUTTON_ADD_RACK_FROM_EDIT_PAGE = "id=cic-systemprofiles-add-rack"
    ID_LABEL_ADD_RACK = "xpath=//header/h1[text()='Add rack']"
    ID_BUTTON_ADD_RACK_AND_CLOSE_PAGE = "xpath=//button[@data-localize='core.details.add']"
    ID_BUTTON_ADD_RACK_PLUS = "xpath=//button[@data-localize='core.details.addAgain']"
    ID_CANCEL_ADD_RACK = "xpath=//button[@data-localize='core.details.cancel']"
    ID_SEARCH_RACK_TO_ADD = "xpath=//input[@class='hp-search']"
    ID_ITEM_RACK_TO_BE_ADDED = "xpath=//table//*[text()='%s']"  # replace %s with the rack name

    # Enum that maps the exact string on the UI. CASE SENSITIVE!
    class ContentItems():
        CLUSTERS = 'Clusters'
        INTERCONNECTS = 'Interconnects'
        MANAGEMENT_HOSTS = 'Management Hosts'
        POWER_DEVICES = 'Power Devices'
        ENCLOSURES = 'Enclosures'
        RACKS = 'Racks'
        STORAGE = 'Storage'
        EMPTY = ''

    # Enum that maps part of the contents href.
    class HardwareTypesCS700():
        server_hw = '#/server-hardware/show'
        server_profile = '#/profiles/show'
        server_profile_templates = '#/profile-templates/show'
        rack = '#/rack/show'
        storage_system = '#/storage-systems/show'
        interconnect = '#/interconnect/show'
        logical_interconnect = '#/logicalswitch/show'
        logical_enclosure = '#/logicalenclosures/show'
        enclosure = '#/enclosure/show'
        power_devices = '#/power-device/show'

    # Enum used for mapping system profiles status
    class Status():
        ERROR = 'error'
        WARNING = 'warning'
        OK = 'ok'

        status_list = [ERROR, WARNING, OK]

        def is_valid(self, expected_status):
            expected_status = expected_status.lower()
            return (expected_status in self.status_list)
