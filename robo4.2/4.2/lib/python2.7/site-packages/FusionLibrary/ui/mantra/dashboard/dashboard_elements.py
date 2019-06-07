# (C) Copyright 2014 Hewlett-Packard Development Company, L.P.


class DashboardPage(object):

    ID_PAGE_LABEL = "//*[@id='hp-page-container']/div[@class='hp-page hp-dashboard']/nav[@class='hp-sub-nav']/div[@class='hp-page-label']/h1[text()='Dashboard']"
    ID_MENU_LINK_DASHBOARD = "link=Dashboard"

    # First query looks for the div that contains a header named as System Profiles
    SYSTEM_PROFILES_CONTAINER_PATH = "//*[@id='hp-dashboard-panels']/*[descendant::*[text()='System Profiles']]/"

    # Following queries use the SYSTEM_PROFILES_CONTAINER_PATH to specify which element they need inside the container.
    SYSTEM_PROFILES_COUNTER = SYSTEM_PROFILES_CONTAINER_PATH + "descendant::header/descendant::*[@class='hp-count']"
    SYSTEM_PROFILES_DONUT_STATUS_LABEL = SYSTEM_PROFILES_CONTAINER_PATH + "descendant::*[text()='%s']"

    SYSTEM_PROFILES_SUMMARY_COUNTER = SYSTEM_PROFILES_CONTAINER_PATH + "descendant::*[@class='hp-count' and parent::*[contains(@class, 'hp-summary-%s')]]"
    SYSTEM_PROFILES_CRITICAL_COUNTER = SYSTEM_PROFILES_SUMMARY_COUNTER % "error"
    SYSTEM_PROFILES_WARNING_COUNTER = SYSTEM_PROFILES_SUMMARY_COUNTER % "warning"
    SYSTEM_PROFILES_OK_COUNTER = SYSTEM_PROFILES_SUMMARY_COUNTER % "ok"

    SYSTEM_PROFILES_SUMMARY_CRITICAL_ACTIVE = SYSTEM_PROFILES_CONTAINER_PATH + "descendant::*[@class='hp-summary-error']"
    SYSTEM_PROFILES_SUMMARY_WARNING_ACTIVE = SYSTEM_PROFILES_CONTAINER_PATH + "descendant::*[@class='hp-summary-warning']"
    SYSTEM_PROFILES_SUMMARY_OK_ACTIVE = SYSTEM_PROFILES_CONTAINER_PATH + "descendant::*[@class='hp-summary-ok']"

    SYSTEM_PROFILES_SUMMARY_CRITICAL_INACTIVE = SYSTEM_PROFILES_CONTAINER_PATH + "descendant::*[@class='hp-summary-error hp-inactive']"
    SYSTEM_PROFILES_SUMMARY_WARNING_INACTIVE = SYSTEM_PROFILES_CONTAINER_PATH + "descendant::*[@class='hp-summary-warning hp-inactive']"
    SYSTEM_PROFILES_SUMMARY_OK_INACTIVE = SYSTEM_PROFILES_CONTAINER_PATH + "descendant::*[@class='hp-summary-ok hp-inactive']"

    # Enum used for mapping system profiles status
    class Status():
        CRITICAL = 'Critical'
        WARNING = 'Warning'
        OK = 'OK'
        NONE = 'None'
        OTHER = 'Other'
