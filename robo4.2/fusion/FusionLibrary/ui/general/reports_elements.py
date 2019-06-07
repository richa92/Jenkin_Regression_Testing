# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
'''

This file contains all element ID on Fusion Reports Page
'''


class FusionReportsPage(object):
    ID_PAGE_LABEL = "//div[@class='hp-page-label']/h1[text()='Reports']"
    ID_MENU_ACTION_BTN = "xpath=//*[@id='hp-report-actions']/label"
    ID_MENU_ACTION_SAVE_AS = "xpath=//*[@id='hp-report-save-action']"
    ID_BTN_SAVE_AS_OK = "xpath=//*[@id='hp-report-save-form']//button[contains(text(),'OK')]"
    ID_SELECT_INVENTORY_NAME = "xpath=//*[@id='hp-report-master-table']//td[contains(text(),'%s')]"
    ID_ELEMENT_ALERTS_TITLE = "xpath = //h1[@id='hp-report-details-title' and contains(text(),'Active alerts')]"
    ID_ELEMENT_ACTIVE_ALERTS = "xpath = //table[@id='hp-report-master-table']//td[contains(text(), 'Active alerts')]"
    ID_TABLE_REPORT_RESOURCES = "xpath = //table[@id='hp-report-resources']"
    ID_ACTIVE_ALERTS_LIST = "xpath = //table[@id='hp-report-resources']/tbody/tr"
    ID_ACTIVE_ALERT_DETAILS = ID_ACTIVE_ALERTS_LIST + "[%s]"  # row number
    ID_ELEMENT_CORRECTIVEACTION = "xpath = //span[text()='correctiveAction']/following-sibling::div"
    ID_ELEMENT_EVENT_DETAILS = "xpath = //label[text()='Event details']"
    ID_ELEMENT_RESOLUTION = "xpath = //span[text()='correctiveAction']/following-sibling::div"
    ID_LINK_LOCAL_USERS = "xpath=.//*[@id='hp-report-master-table']/tbody//td[contains(text(),'Local users')]"
    ID_TABLE_USERS = "xpath=.//*[@id='hp-report-resources']"
    ID_USERS_COUNT = "xpath=.//*[@id='hp-report-table-title']/span[@class='hp-count']"
    ID_BTN_XLS_DROPDOWN = "xpath=.//*[@id='hp-report-save-form']/div[@class='hp-form-contents']//div[@class='hp-value']"
    ID_BTN_CSV_DROPDOWN = "xpath=.//*[@id='hp-report-save-form']/div[@class='hp-form-contents']/div//ol//span[contains(text(),'CSV MS-DOS')]"
