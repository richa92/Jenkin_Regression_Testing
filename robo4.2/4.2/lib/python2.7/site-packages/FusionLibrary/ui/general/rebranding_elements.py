# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
'''
This file contains all element ID on Fusion login page/screen
'''


class RebrandLoginPage(object):
    # Login Page
    ID_PRODUCT_NAME = "//*[@id='hp-login-page']/header//div[@class='hp-login-header' and text()='%s']"
    ID_ICON_HELP = "//*[@id='hp-help-control']/div[@class='hp-icon hp-help']"
    ID_BROWSE_HELP = "//*[@id='hp-help-documentation']/ol/li/a[@class='hp-help-index'and text()='Browse help']"
    ID_REST_HELP = "//*[@id='hp-help-documentation']/ol/li/a[@href='/doc#/cic-rest'and text()='REST API help']"
    ID_REST_REFERENCE = "//*[@id='hp-help-documentation']/ol/li/a[@href='/api-docs/current'and text()='REST API reference']"
    ID_PAGE_SETTINGS = "xpath=//div[@class='hp-page-label hp-preserve']/h1[text()='Settings']"
    ID_LINK_SETTINGS = "link=Settigns"
    ID_SETTINGS_SECURITY = "//*[@id='fs-settings-security-panel']/div/header/h2/a[@class='hp-anchor-uri' and text()='Security']"
    ID_REQUIRED_INFORMATION = "//*[@id='fs-setings-security-certificate']//legend[@data-localize='fs.settings.certificate.selfsigned.required_information' and text()='Required Information']"
    LIST_REQUIRED_INFORMATION = "//*[@id='fs-settings-security-certificate-org' and text()='%s']"  # NEC Corporation


class CertificateTypes():
    NEC_CORPORATION = "NEC Corporation"


class ProductName():
    ONEVIEW_FOR_NEC = "OneView for NEC"
