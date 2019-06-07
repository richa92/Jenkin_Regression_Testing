# (C) Copyright 2014 Hewlett-Packard Development Company, L.P.


class enclosuresPage(object):
    ID_BLADE = "xpath=//ol[@class='hp-bays cic-enclosure-blade-row']/li[%s]/div[@class='hp-device hp-blade hp-flyout-wrapper']"
    ID_BLADE_OK = ID_BLADE + "/div[@class='hp-status hp-status-ok']"
