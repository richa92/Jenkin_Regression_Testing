# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
'''

This file contains all element ID on Fusion Alert Page

'''


class FusionActivityPage(object):
    ID_PAGE_LABEL = "xpath=//div[@class='hp-page-label']/h1[text()='Activity']"
    ID_LATEST_ACTIVITY_LABEL = "xpath=//*[@id='hp-activities']/tbody/tr[position()=1]//td[count(//table//td[.='Name']/preceding-sibling::td)+1]//span"
    ID_ACTIVITY_STATUS = "xpath = //td[@date-timestamp and contains(text(),'%s')]/preceding-sibling::td[@class='hp-source' and a[contains(text(),'%s')]]/preceding-sibling::td[@class='hp-name' and p/span[contains(text(),'%s')]]/preceding-sibling::td/div[@class='hp-status hp-status-ok']"  # %s replace with time stamp, server name and message
    ID_ACTIVITY_TABLE = "xpath=//div[@id='hp-activities_wrapper']//div[@class='dataTables_scrollBody']"
    ID_ACTIVITY_SELECT = "xpath=//td[p/span[contains(text(),'%s')]]/following-sibling::td[a[@href and contains(text(),'%s')]]/following-sibling::td[@date-timestamp and contains(text(),'%s')]"
    ID_ACTIVITY_SELECT_OWNER = "%s/../td/dev[class='hp-owner hp-select']/div[class='hp-value']"   # %s is ID_ACTIVITY_SELECT
    ID_ACTIVITY_GET_OWNER = "%s/../td/div[@class='hp-owner hp-select']"  # %s is ID_ACTIVITY_SELECT
    ID_ACTIVITY_STATE = "%s/../td/div[@class='hp-state hp-select']/div[@class='hp-value hp-selected']"    # %s IS ID_ACTIVITY_SELECT
    ID_ACTION_DROPDOWN = "//*[@id='hp-activity-actions']/label"
    ID_ACTION_DROPDOWN_ASSIGN = "//*[@id='hp-activity-assign']"
    ID_ACTION_DROPDOWN_CLEAR = "//*[@id='hp-activity-clear']"
    ID_ACTION_DROPDOWN_RESTORE = "//*[@id='hp-activity-restore']"
    ID_ASSIGN_UN_INPUT_BOX = "//*[@id='hp-assign-username-input']"
    ID_ASSIGN_OK = "//*[@id='hp-alert-assign-ok']"
    ID_ASSIGN_ERROR_MSG = "//*[@id='hp-alert-assign-dialog']/div/div[@class='hp-message']"
    ID_CLEAR_ERROR_MSG = "//*[@id='hp-alert-clear-dialog']/div/div[@class='hp-message']"
    ID_RESTORE_ERROR_MSG = "//*[@id='hp-alert-restore-dialog']/div/div[@class='hp-message']"
    ID_ASSIGN_ERROR_OK = "//*[@id='hp-alert-assign-cancel']"
    ID_CLEAR_ERROR_OK = "//*[@id='hp-alert-clear-cancel']"
    ID_RESTORE_ERROR_OK = "//*[@id='hp-alert-restore-cancel']"
    ID_ACTIVITY_SPIN_IMAGE = "//*[@id='hp-activities']//td[@align='center']/div[@class='hp-spinner-small']/div[@class='hp-spinner-image']"
    ID_FILTER_ALL_TYPES = "//*[@id='hp-activity-category-filter']/div[@class='hp-value' and contains(text(),'All types')]"
    ID_FILTER_ALERTS = "//*[@id='hp-activity-category-filter']//li[@data-localize and contains(text(),'Alerts')]"
    ID_MSG_AVAILABLE = "xpath =//tbody/tr[td[@class='hp-name']/p/span[text()='%s']/following::td[@class='hp-source']/a[text()='%s']][1]"
    ID_TIMESTAMP = "xpath =//table[@id='hp-activities']/tbody/tr[td[p/span[text()='%s']] and td[a[text()='%s']]][1]/td[5]"
    ID_ASSIGNED_OWNER = "xpath =//tbody/tr[td[p/span[text()='%s']] and td[a[text()='%s']]][1]/td[text()='%s']/following::td/div/div[@class='hp-value']"
    ID_SELECT_ACTIVITY_OWNER = "xpath=//tbody/tr[td[@class='hp-name']/p/span[text()='%s']/following::td[@class='hp-source']/a[text()='%s']/following::td[text()='%s']/following::td/div/div[@class='hp-value']]"
    ID_RESET_FILTER = "xpath = //div[@id='hp-activity-filters']/a"
    ID_FILTER_TASKS = "//*[@id='hp-activity-category-filter']//li[@data-localize and contains(text(),'Tasks')]"
    ID_ACTIVITY_DETAILS = "xpath = .//*[@id='hp-activities']/tbody/tr[1]/td[%s]"
    ID_FILTER_ALL_STATES = "xpath = //div[@id='hp-activity-state-filter']/div[@class='hp-value' and contains(text(),'All states')]"
    ID_FILTER_STATES = "xpath = //div[@id='hp-activity-state-filter']/div[@data-localize='fs.activity.filter.state.all']"
    ID_FILTER_STATES_ALL = "xpath = //div[@id='hp-activity-state-filter']/ol/li[text()='All']"
    ID_ACTIVITY_FILTER_COUNT = "xpath = //div[@id='hp-activity-page']/nav/div[@class='hp-page-label']/span"
    ID_ACTIVITY_STATE_DETAILS = "xpath = //table[@id='hp-activities']/tbody/tr[%s]/td[6]"
    ID_FILTER_BY_STATE = "xpath = //div[@id='hp-activity-state-filter']/ol/li[text()='%s']"
    ID_SELECT_ACTIVITY_BY_ID = "xpath = //table[@id='hp-activities']//tbody/tr[%s]/td[@class='hp-name']"
    ID_ELEMENT_ALERT = "xpath = //tr[td[div//text()='%s']/following-sibling::td[p//span[contains(text(), '%s')]]/following-sibling::td[a/text()='%s']][1]"  # (severity, name, resource)
    ID_ACTIVITY_ITME_SPAN = "%s/p/span/span"
    ID_ACTIVITY_ITME_SPAN_S1 = "%s/p/span/span[1]"
    ID_ACTIVITY_ITEM_SPAN_A = "%s/p/span/a"
    ID_ACTIVITY_ITEM_SPAN_S2 = "%s/p/span/span[2]"
    ID_ACTIVITY_ITEM_P1 = "%s/p/span[1]"
    ID_FILTER_ON_TYPE = "//*[@id='hp-activity-category-filter']/ol/li[@data-localize and contains(text(),'Alerts')]"
    ID_ACTIVITY_NAME_DETAILS = "xpath = //*[@id='hp-activities']/tbody/tr[%s]/td[@class='hp-name']"
    ID_ACTIVITY_SOURCE_DETAILS = "xpath = //*[@id='hp-activities']/tbody/tr[%s]/td[@class='hp-source']"
    ID_ACTIVITY_OWNER_DETAILS = "xpath = //*[@id='hp-activities']/tbody/tr[%s]/td/div[@class='hp-owner hp-select']"
    ID_LABEL_PAGE_CLICK_ERROR = "xpath = //*[@id='hp-activities']/tbody/tr[%s]/td/div[@class='hp-collapser']"
    ID_LABEL_PAGE_UNCLICK_ERROR = "xpath = //*[@id='hp-activities']/tbody/tr[%s]/td/div[@class='hp-collapser hp-active']"
    ID_LABEL_PAGE_ERROR = "xpath = //*[@id='hp-activities']/tbody/tr[%s]/td[@class='hp-name']"
    ID_LABEL_PAGE_ERROR_FULL = "xpath=//*[@id='hp-activities']/tbody/tr[%s]/td//span[@class='hp-resolution']"
    ID_LABEL_EVENT_CLICK_ERROR = "//*[@id='hp-activities']/tbody/tr[%s]/td//div/label[@data-localize and contains(text(),'Event details')]"
    ID_EVENT_MESSAGE = "//*[@id='hp-activities']/tbody/tr[%s]//div[@class='hp-alert-events hp-collapsible']"
    ID_FILTER_ALL_STATUS = "xpath = //*[@id='hp-activity-status-filter']/div"
    ID_FILTER_ON_STATUSTYPE = "xpath=//*[@id='hp-activity-status-filter']/ol/li[@data-localize and contains(text(),'Critical')]"
