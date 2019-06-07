# (C) Copyright 2014 Hewlett-Packard Development Company, L.P.


class activityPage(object):
    ID_ADD_STATUS = "xpath=//table[@id='hp-activities']/tbody/tr[8]/td[2]/div[@class='hp-status hp-status-ok']"
    ID_ADD_NAME = "xpath=//table[@id='hp-activities']/tbody/tr[8]/td[@class='hp-name']/p/span[text()='Add']"
    ID_ADD_STATUS2 = "xpath=//table[@id='hp-activities']/tbody/tr[2]/td[2]/div[@class='hp-status hp-status-ok']"
    ID_ADD_NAME2 = "xpath=//table[@id='hp-activities']/tbody/tr[2]/td[@class='hp-name']/p/span[text()='Add']"
    ID_HEALTH_MESSAGE = "xpath=//table[@id='hp-activities']/tbody/tr[1]/td[@class='hp-name']/p/span[text()='A change in the health status of the server has occurred, the status is now OK']"
    ID_HEALTH_STATUS = "xpath=//table[@id='hp-activities']/tbody/tr[1]/td[2]/div[@class='hp-status hp-status-ok']"
