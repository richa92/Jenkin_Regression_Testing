# (C) Copyright 2014 Hewlett-Packard Development Company, L.P.


class systemtypesPage(object):
    ID_PAGE_LABEL = "xpath=//div[@class='hp-page-label']/h1[text()='System Types']"
    ID_MENU_LINK_SYSTEMTYPES = "link=System Types"
    ID_CS = "xpath=//tr[@class='odd hp-selected hp-scroll-first']/td[2]"
    ID_CS_VERSION = "xpath=//tr[@class='odd hp-selected hp-scroll-first']/td[3]"
    ID_VERSION = "//*[@class='hp-form-item']/label[@data-localize='systemtypes.show.version']"
    ID_VERSION_CONTENT = "//*[@id='cic-systemtypes-version']/span[@class='hp-value']"
    ID_AUTHOR = "//*[@data-localize='systemtypes.show.author']"
    ID_AUTHOR_CONTENT = "//*[@id='cic-systemtypes-author']"
    ID_DESCRIPTION = "//*[@data-localize='systemtypes.show.description']"
    ID_DESCRIPTION_CONTENT = "//*[@id='cic-systemtypes-description']"
    ID_CONTENTS_TABLE = "//*[@id='cic-systemtypes-purposes-table']"
    ID_BUTTON_MAP = "//*[@class='hp-map-control hp-anchor-uri hp-tooltipped']"
    ID_MAP_CS = "//*[@class='hp-details-contents hp-map']/ol/li[1]/ol/li"
    ID_MAP_SYSTEMS = "//*[@class='hp-details-contents hp-map']/ol/li[2]/ol/li"
    ID_MAP_SYSTEM_TYPES = "//*[@class='hp-details-contents hp-map']/ol/li[3]/ol/li"
