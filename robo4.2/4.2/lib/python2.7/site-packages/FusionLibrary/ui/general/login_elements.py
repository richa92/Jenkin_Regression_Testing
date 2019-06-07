# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
'''

This file contains all element ID on Fusion login page/screen
'''


class FusionLoginPage(object):
    # Login Page
    ID_INPUT_LOGIN_USER = "hp-login-user"
    ID_INPUT_LOGIN_PASSWORD = "hp-login-password"
    ID_BTN_LOGIN_BUTTON = "hp-login-button"
    ID_LABEL_LOGIN_STATUS = "hp-login-status"
    ID_ONEVIEW_TUTORIAL_DIALOG = "id=hp-tutorial-step"
    ID_ONEVIEW_TUTORIAL_CLOSE = "id=hp-tutorial-close"

    # EULA
    ID_BTN_EULA_AGREE = "id=hp-eula-agree-button"
    ID_BTN_EULA_DISAGREE = "id=hp-eula-disagree-button"
    ID_BTN_EULA_OK = "id=hp-eula-ok-button"
    ID_BTN_EULA_CONFIRM_DISAGREE = "id=eula-confirmation-disagree-button"
    ID_BTN_EULA_CANCEL_DISAGREE = "id=eula-confirmation-cancel-button"
    ID_TOGGLE_HP_SUPPORT_ACCESS_ENABLE = "css=li.hp-on"
    ID_TOGGLE_HP_SUPPORT_ACCESS_DISABLE = "css=li.hp-off"
    ID_BTN_OK_CONVERGED_INFRA_SUPPORT = "id=hp-eula-ok-button"
    # First time wizard password
    ID_INPUT_NEW_PASSWORD = "id=hp-initial-password-new1"
    ID_INPUT_CONFIRM_PASSWORD = "id=hp-initial-password-new2"
    ID_BTN_OK_PASSWORD_SCREEN = "id=hp-initial-password-button-element"

    # Appliance Networking Page
    ID_INPUT_APPLIANCE_HOSTNAME = "id=cic-network-hostname"
    ID_RADIO_IPV4_MANUAL = "id=cic-network-ipv4-static"
    ID_RADIO_IPV4_DHCP = "id=cic-network-ipv4-dhcp"
    ID_APPLIANCE_OK = "xpath=//*[@id='cic-network-ok']"
    ID_APPLIANCE_APPLYING_SETTINGS = "xpath=//*[@id='cic-network-splash-dialog-init']/p[1]"

    ID_INPUT_IPV4_IPADDRESS = "id=cic-network-ip-ipv4"
    ID_INPUT_IPV4_MASK = "id=cic-network-mask-ipv4"
    ID_INPUT_IPV4_GATEWAY = "id=cic-network-gateway-ipv4"
    ID_INPUT_PREFFERED_DNS = "id=cic-network-preferred-dns"
    ID_INPUT_ALTERNATE_DNS = "id=cic-network-alternate-dns"

    # IPV6
    ID_RADIO_IPV6_UNASSIGN = "id=cic-network-ipv6-unassign"
    ID_RADIO_IPV6_MANUAL = "id=cic-network-ipv6-static"
    ID_RADIO_IPV6_DHCP = "id=cic-network-ipv6-dhcp"
    ID_INPUT_IPV6_IPADDRESS = "id=cic-network-ip-ipv6"
    ID_INPUT_IPV6_MASK = "id=cic-network-mask-ipv6"
    ID_INPUT_IPV6_GATEWAY = "id=cic-network-gateway-ipv6"
    ID_BTN_LOGOUT = "id=fs-settings-logout"
    ID_BTN_OK_NETWORK_ASSIGNMENT = "id=cic-network-ok"

    # TIME AND LANGUAGE
    ID_RADIO_SET_TIME_MANUALLY = "id=cic-network-manualdatetime"
    ID_RADIO_SYNC_WITH_TIME_SERVER = "id=cic-network-syncwithserver"

    ID_ELEMENT_CURRENT_DATE_TIME = "id=cic-network-currentdatetimeText"
    ID_BTN_TIME_NOW = "xpath=//button[@type='button']"
    ID_BTN_TIME_DONE = "xpath=//button[text()='Done']"
    ID_INPUT_NETWORK_NTP_SERVER1 = "id=cic-network-ntpserver1"
    ID_INPUT_NETWORK_NTP_SERVER2 = "id=cic-network-ntpserver2"
    ID_INPUT_NETWORK_NTP_SERVER3 = "id=cic-network-ntpserver3"

    ID_COMBO_DEFAULT_LANGUAGE = "css=div.hp-search-combo-control"
    ID_LINK_SEARCH_FOR_ANOTHER = "link=Search for another"
    ID_ELEMENT_DEFAULT_LANGUAGE_BASE = "xpath=//span[@class='hp-name' and contains(text(),'%s')]"  # replace %s with Language

    ID_DLG_APPLY_SETTINGS = "id=cic-network-splash-estimate-init"
    ID_DLG_APPLY_SETTINGS_COMPLETE_MESSAGE = "Configuration saved"

    ID_ELEMENT_DATE_YEAR = "class=ui-datepicker-year"
    ID_ELEMENT_DATE_MONTH = "class=ui-datepicker-month"

    ID_ELEMENT_SELECT_DATE = "xpath=//a[@class='ui-state-default' and text()='%s']"  # replace with date you want to select
    ID_ELEMENT_NEXT_NAVIGATION = "xpath=//a[@title='Next']"
    ID_ELEMENT_PREV_NAVIGATION = "xpath=//a[@title='Prev']"

    ID_ELEMENT_DAY_BASE = "xpath=//a[@class='ui-state-default' and text()='%s']"  # replace %s with day

    # VIEW
    ID_COMBO_MENU_VIEW = "css=div.hp-value"
    ID_LINK_GENERAL = "link=General"
    ID_LINK_IPV4 = "link=IPv4"
    ID_LINK_IPV6 = "link=IPV6"
    ID_LINK_DNS = "link=DNS"
    ID_LINK_TIME_LANGUAGE = "link=Time and Language"
    ID_ELEMENT_ERROR_MESSAGE = "xpath=//div[@class='hp-status hp-status-error']"
    ID_ALL_ERROR_FIELDS = "xpath=//label[@class='hp-error']"

    # for acive directory users login
    ID_ELEMENT_AUTHN_PROVIDER = "xpath=//select[@id='hp-authn-provider-select']/../div/div"
    ID_COMBO_AUTHN_PROVIDER = "xpath=//*[@id='hp-authn-provider-list-item']//div[@class='hp-value']"
    ID_ELEMENT_DIR = "xpath=//select[@id='hp-authn-provider-select']/../div/ol/li/span[.='%s']"
