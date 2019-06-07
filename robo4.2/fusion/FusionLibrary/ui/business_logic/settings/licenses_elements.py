from FusionLibrary.ui.business_logic.base import FusionUIConst


class GeneralLicensesElements(object):

    ID_PAGE_LICENSES = "xpath=//h1[@id='hp-settings-details-title' and .='Licenses']"
    # ID_LINK_LICENSES = "xpath=//*[@href='#/settings/show/license/general']"
    ID_LINK_LICENSES = "xpath=//*[@id='fs-settings-license-panel']//a[text()='Licenses']"

    ID_BUTTON_ACTIONS = "xpath=//label[text()='Actions']"
    ID_OPTION_ACTIONS_ADD = "id=hp-add-license"

    ID_TEXT_ONEVIEW_WO_ILO_LICENSE = "xpath=//h2[.='%s']" % FusionUIConst.CONST_LICENSE_ONEVIEW_ADVANCED_WITHOUT_ILO
    ID_TEXT_ONEVIEW_LICENSE = "xpath=//h2[.='%s']" % FusionUIConst.CONST_LICENSE_ONEVIEW_ADVANCED

    ID_TEXT_ONEVIEW_WO_ILO_LICENSE_REQUIRED = "xpath=//h2[.='%s']/../..//div[@id='fs-settings-license-summary-licensedRequired']" % FusionUIConst.CONST_LICENSE_ONEVIEW_ADVANCED_WITHOUT_ILO
    ID_TEXT_ONEVIEW_LICENSE_REQUIRED = "xpath=//h2[.='%s']/../..//div[@id='fs-settings-license-summary-licensedRequired']" % FusionUIConst.CONST_LICENSE_ONEVIEW_ADVANCED
    ID_TEXT_ONEVIEW_WO_ILO_LICENSE_LICENSED = "xpath=//h2[.='%s']/../..//div[@id='fs-settings-license-summary-licensedNodes']" % FusionUIConst.CONST_LICENSE_ONEVIEW_ADVANCED_WITHOUT_ILO
    ID_TEXT_ONEVIEW_LICENSE_LICENSED = "xpath=//h2[.='%s']/../..//div[@id='fs-settings-license-summary-licensedNodes']" % FusionUIConst.CONST_LICENSE_ONEVIEW_ADVANCED

    ID_TEXT_ONEVIEW_FCLICENSE = "xpath=//h2[.='Synergy 8Gb FC Upgrade']"
    ID_TEXT_ONEVIEW_FCLICENSE_REQUIRED = "xpath=//h2[.='Synergy 8Gb FC Upgrade']/../..//div[@id='fs-settings-license-summary-licensedRequired']"
    ID_TEXT_ONEVIEW_FCLICENSE_LICENSED = "xpath=//h2[.='Synergy 8Gb FC Upgrade']/../..//div[@id='fs-settings-license-summary-licensedNodes']"
    ID_TEXT_ONEVIEW_FCLICENSE_AVAILABLE = "xpath=//h2[.='Synergy 8Gb FC Upgrade']/../..//div[@id='fs-settings-license-summary-availableLicenses']"

    ID_BUTTON_ADD = "//div[@id='hp-settings-show']//a[text()='Add']"


class AddLicensesElements(object):

    ID_DIALOG_ADD_LICENSE = "id=fs-addLicense-form"
    ID_INPUT_LICENSE_KEY = "id=fs-license-licenseKeyValue"
    ID_BUTTON_ADD = "id=fs-license-add"
    ID_BUTTON_ADD_PLUS = "id=fs-license-add-again"
    ID_BUTTON_CANCEL = "id=fs-addLicense-cancel"
    ID_TEXT_ADD_INVALID_ERROR = "xpath=//div[@id='hp-form-message']/div[@class='hp-form-message-details' and contains(text(), 'Invalid license key')]"
    ID_TEXT_ADD_DUPLICATED_ERROR = "xpath=//div[@id='hp-form-message']/div[@class='hp-form-message-details' and contains(text(), 'License key already exists')]"
