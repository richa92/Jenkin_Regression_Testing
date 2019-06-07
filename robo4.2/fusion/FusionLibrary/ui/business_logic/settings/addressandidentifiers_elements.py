
class GeneralIPPoolElements(object):

    ID_TABLE_IPV4_SUBNET_EDIT_ADDRESSESIDENTIFIERS_DIALOG = "id=cic-settings-edit-ipv4-table"
    ID_DIALOG_ADD_RANGE = "id=cic-settings-ipv4-add-range-form"
    ID_DIALOG_ADD_IPV4_SUBNET = "id=cic-settings-ipv4-add-form"
    ID_LINK_ADDRESSES_AND_IDENTIFIERS_PAGE_SETTINGS = "xpath=//div[@class='hp-page-label hp-preserve']//a[text()='Settings']"
    ID_HEADER_ADDRESSES_AND_IDENTIFIERS = "xpath=//div[@id='hp-settings-show']//h1[text()='Addresses and Identifiers']"
    ID_LINK_ADDRESSES_AND_IDENTIFIER = "xpath=//*[@id='cic-settings-guid-panel']//a[text()='Addresses and Identifiers']"
    ID_DIALOG_EDIT_ADDRESSES_AND_IDENTIFIERS = "id=cic-addresses-edit-form"
    ID_LINK_EDIT_ADDRESSES_AND_IDENTIFIERS = "xpath=//*[@id='cic-settings-guid-panel']//a[text()='Edit']"
    ID_TABLE_IPV4_SUBNET_ADDRESS_RANGE_NO_DATA = "xpath=//*[@id='cic-settings-edit-ipv4-table']/tbody//tr[td[contains(text(),'No subnets')]]"

    ID_BUTTON_ACTION = "id=cic-settings-guid-more-actions"
    LINK_EDIT = "link=Edit"

    ID_BUTTON_EDIT_ADDRESSES_AND_IDENTIFIERS_OK = "id=cic-settings-edit-ok"
    ID_BUTTON_EDIT_ADDRESSES_AND_IDENTIFIERS_CANCEL = "id=cic-settings-edit-cancel"
    ID_BUTTON_EDIT_ADDRESSIDENTIFIERS_PROCEED = "id=hp-form-navigate-away-proceed"
    ID_DIALOG_CHANGES_LOST_WARNING = "id=hp-form-navigate-away-dialog"

    ID_HPSTATUS_UPDATE = "xpath=//div[@class='hp-status hp-changing']/span[contains(text(), 'Update')]"
    ID_SUBNET_ERROR_MESSAGE_DETAILS = "xpath=//form[@id='cic-addresses-edit-form']//div[@class='hp-footer']//div[@class='hp-form-message-details']"
    ID_SUBNET_ERROR_MESSAGE_SUMMARY = "xpath=//form[@id='cic-addresses-edit-form']//div[@class='hp-footer']//div[@class='hp-form-message-summary']//span[@class='hp-form-message-text']"
    ID_IPV4_EDIT_ERROR_STATUS = "xpath=//form[@id='cic-addresses-edit-form']//div[@class='hp-footer']//div[@class='hp-form-message-summary']//div[@class='hp-status hp-status-error']"

    ID_CHECKBOX_EDIT_ADDRESSESIDENTIFIERS_RANGE_DISABLED = "xpath=//table[@id='cic-settings-edit-ipv4-table']//tbody//tr[td[@class='cic-settings-edit-ipv4-table-networkId' and text()='%s']]/..//tr[td[contains(@class,'cic-settings-edit-ipv4-table-name')]/div[text()='%s']]/descendant::input[@class='cic-settings-ipv4-checkbox' and @disabled]"
    ID_TABLE_ADDRESS_RANGE_OF_SUBNET = "xpath=//table[@id='{0}']//tbody//tr[td[@class='{0}-networkId' and text()='{1}']]/following-sibling::tr[@class='cic-settings-edit-ipv4-table-range-row hp-row-details-row' and position()='1']//div[@class='cic-settings-edit-ipv4-table-range-contents']//table"

    ID_RANGE_COLLAPSER = "xpath=//table[@id='{0}']//tbody//tr[td[@class='{0}-networkId' and text()='{1}']]/following-sibling::tr[@class='cic-settings-edit-ipv4-table-range-row hp-row-details-row' and position()='1']//div[contains(@class,'hp-collapsed')]"
    ID_TABLE_ADD_SUBNET_ADD_RANGE = "xpath=//table[@id='cic-settings-edit-ipv4-add-range-table']//tbody//tr[td[@class='cic-settings-edit-ipv4-add-range-table-name']/div[text()='%s']]"

    ID_DIALOG_UPDATE_IPV4_SUBNET = "id=cic-settings-ipv4update-form"
    ID_DIALOG_EDIT_ADDRESS_RANGE = "id=cic-settings-ipv4-update-range-form"
    ID_CHECKBOX_EDIT_ADDRESSESIDENTIFIERS_ADDRESS_RANGE = "xpath=//table[@id='cic-settings-edit-ipv4-table']//tbody//tr[td[@class='cic-settings-edit-ipv4-table-networkId' and text()='%s']]/..//tr[td[contains(@class,'cic-settings-edit-ipv4-table-name')]/div[text()='%s']]/descendant::input[@class='cic-settings-ipv4-checkbox']"
    ID_TABLE_EDIT_SUBNET_EDIT_RANGE = "xpath=//table[@id='cic-settings-edit-ipv4-edit-range-table']//tbody//tr[td[@class='cic-settings-edit-ipv4-add-range-table-name']/div[text()='%s']]"

    ID_COLLAPSIBLE_DELETE_SUBNET_WARNING = "xpath=//div[@id='cic-settings-ipv4delete-dialog']//div[@id='cic-settings-edit-ipv4-delete-subnet-collapsible' and @class='hp-collapsible hp-collapsed']/label"
    ID_DELETE_SUBNET_WARNING_ASSOCIATED_OBJECT = "xpath=//div[@id='cic-settings-ipv4delete-dialog']//div[@id='cic-settings-edit-ipv4-delete-subnet-collapsible']//a[translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')='%s']"
    ID_COLLAPSIBLE_DELETE_ADDRESS_RANGE_WARNING = "xpath=//div[@id='cic-settings-ipv4delete-range-dialog']//div[@id='cic-settings-edit-ipv4-delete-subnet-collapsible' and @class='hp-collapsible hp-collapsed']/label"
    ID_DELETE_RANGE_WARNING_ASSOCIATED_OBJECT = "xpath=//div[@id='cic-settings-ipv4delete-range-dialog']//div[@id='cic-settings-edit-ipv4-delete-subnet-collapsible']//a[translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')='%s']"
    ID_TABLE_IPV4_SUBNET_ADDRESSES_IDENTIFIERS_PAGE = "id=cic-settings-ipv4-table-more"
    ID_EXPANDED_RANGE_COLLAPSER = "xpath=//table[@id='{0}']//tbody//tr[td[@class='{0}-networkId' and text()='{1}']]/following-sibling::tr[@class='cic-settings-edit-ipv4-table-range-row hp-row-details-row' and position()='1']//div[@class='hp-collapsible cic-settings-edit-ipv4-table-range-collapsible']/label"

    ID_IPV4_ADDRESSES_TOTAL_COUNT = "id=cic-settings-guid-ipv4-addresses"
    ID_TABLE_IPV4_SUBNET_DATA = "xpath=//table[@id='cic-settings-ipv4-table-more']/tbody"
    ID_TABLE_IPV4_SUBNET_HEADERS = "xpath=//div[@id='cic-settings-ipv4-table-more_wrapper']//div[@class='dataTables_scrollHead']//table/thead"


class CreateIPPoolElements(object):

    ID_DIALOG_ADD_IPV4_SUBNET = "id=cic-settings-ipv4-add-dialog"
    # add subnet elements
    ID_BUTTON_ADD_IPV4_SUBNET_AND_RANGE = "id=cic-settings-ipv4-add"
    ID_INPUT_IPV4_SUBNETID = "id=cic-settings-ipv4-networkid-custom-input"
    ID_INPUT_IPV4_SUBNET_MASK = "id=cic-settings-ipv4-subnet-custom-input"
    ID_INPUT_IPV4_GATEWAY = "id=cic-settings-ipv4-gateway-custom-input"
    ID_INPUT_IPV4_DOMAIN_NAME = "id=cic-settings-ipv4-domain-custom-input"
    ID_INPUT_IPV4_DNS1 = "id=cic-settings-ipv4-dns1-custom-input"
    ID_INPUT_IPV4_DNS2 = "id=cic-settings-ipv4-dns2-custom-input"
    ID_INPUT_IPV4_DNS3 = "id=cic-settings-ipv4-dns3-custom-input"
    ID_BUTTON_ADD_ADDRESS_RANGE = "id=cic-settings-ipv4-add-range"

    ID_BUTTON_SUBNET_ADD = "id=cic-settings-ipv4-add-subnet"
    ID_BUTTON_SUBNET_ADD_PLUS = "id=cic-settings-ipv4-add-again"
    ID_BUTTON_SUBNET_CANCEL = "id=cic-settings-ipv4-cancel"

    # add range elements
    ID_DIALOG_ADD_IPV4_RANGE = "id=cic-settings-ipv4-add-range-dialog"
    ID_INPUT_ADD_RANGE_NAME = "id=cic-settings-ipv4-name-custom-input"
    ID_INPUT_ADD_RANGE_STARTIP = "id=cic-settings-ipv4-start-custom-input"
    ID_INPUT_ADD_RANGE_ENDIP = "id=cic-settings-ipv4-end-custom-input"

    ID_BUTTON_RANGE_ADD = "id=cic-settings-ipv4-create-range"
    ID_BUTTON_RANGE_ADD_PLUS = "id=cic-settings-ipv4-create-range-add-again"
    ID_BUTTON_RANGE_CANCEL = "id=cic-settings-ipv4-create-range-cancel"

    ID_ADD_RANGE_DIALOG_NOTIFICATION = "id=cic-settings-ipv4add-range-warning-dialog-notification"
    ID_TEXT_ADD_RANGE_WARNING = "id=cic-settings-ipv4add-range-warning-dialog-warning"
    ID_ADD_RANGE_WARNING_CLOSE = "id=cic-settings-pv4add-range-warning-close"


class EditIPPoolElements(object):

    ID_BUTTON_UPDATE_SUBNET_ADD_RANGE = "id=cic-settings-ipv4-edit-create-range"

    ID_DIALOG_EDIT_SUBNET = "id=cic-settings-ipv4update-dialog"
    ID_ICON_EDIT_SUBNET = "xpath=//table[@id='cic-settings-edit-ipv4-table']//tbody//tr[td[@class='cic-settings-edit-ipv4-table-networkId' and text()='%s']]/descendant::div[@class='hp-edit hp-icon crm-ipv4-edit']"

    # edit subnet elements
    ID_INPUT_UPDATE_SUBNET_ID = "id=cic-settings-ipv4-networkid-update"
    ID_INPUT_UPDATE_SUBNET_MASK = "id=cic-settings-ipv4-subnet-update"
    ID_INPUT_UPDATE_GATEWAY = "id=cic-settings-ipv4-gateway-update"
    ID_INPUT_UPDATE_DOMAIN_NAME = "id=cic-settings-ipv4-domain-update"
    ID_INPUT_UPDATE_DNS1 = "id=cic-settings-ipv4-dns1-update"
    ID_INPUT_UPDATE_DNS2 = "id=cic-settings-ipv4-dns2-update"
    ID_INPUT_UPDATE_DNS3 = "id=cic-settings-ipv4-dns3-update"

    ID_BUTTON_UPDATE_SUBNET = "id=cic-settings-ipv4update"
    ID_BUTTON_EDIT_SUBNET_CANCEL = "id=cic-settings-guid-update-cancel"

    ID_UPDATE_SUBNET_WARNING = "id=cic-settings-ipv4-update-warning"
    ID_TEXT_UPDATE_SUBNET_WARNING = "xpath=//div[@id='cic-settings-ipv4-update-warning']/div[@class='hp-message']"

    # edit address range elements
    ID_ICON_UPDATE_SUBNET_EDIT_RANGE = "xpath=//table[@id='cic-settings-edit-ipv4-edit-range-table']/tbody/tr[td[@class='cic-settings-edit-ipv4-add-range-table-name']/div[text()='%s']]/descendant::td/div[@class='hp-edit crm-ipv4-edit']"
    ID_DIALOG_UPDATE_RANGE = "id=cic-settings-ipv4-update-range-dialog"
    ID_INPUT_UPDATE_RANGE_NAME = "id=cic-settings-ipv4-name-update"
    ID_INPUT_UPDATE_RANGE_STARTIP = "id=cic-settings-from-update-input"
    ID_LABEL_RANGE_STARTIP = "id=cic-settings-from-update"
    ID_LABEL_RANGE_STARTIP_HELP = "id=cic-settings-from-update-help"
    ID_INPUT_UPDATE_RANGE_ENDIP = "id=cic-settings-to-update"

    ID_BUTTON_UPDATE_RANGE_OK = "id=cic-settings-ipv4-update-range"
    ID_BUTTON_UPDATE_RANGE_CANCEL = "id=cic-settings-ipv4-update-range-cancel"


class DeleteIPPoolElements(object):

    ID_BUTTON_DELETE_WARNING_CLOSE = "id=cic-settings-guid-delete-close"
    ID_UPDATE_SUBNET_RANGE_DELETE = "xpath=//table[@id='cic-settings-edit-ipv4-edit-range-table']/tbody/tr[td[@class='cic-settings-edit-ipv4-add-range-table-name']/div[text()='%s']]/descendant::td/div[@class='hp-close crm-ipv4-close']"
    ID_DIALOG_DELETE_RANGE_WARNING = "id=cic-settings-ipv4delete-range-dialog"
    ID_TEXT_DELETE_RANGE_WARNING = "id=cic-settings-ipv4delete-range-dialog-warning"

    ID_SUBNET_DELETE = "xpath=//table[@id='cic-settings-edit-ipv4-table']//tbody//tr[td[@class='cic-settings-edit-ipv4-table-networkId' and text()='%s']]//div[@class='hp-close crm-guid-close']"
    ID_DIALOG_SUBNET_DELETE_WARNING = "id=cic-settings-ipv4delete-dialog"

    ID_TEXT_SUBNET_DELETE_WARNING = "id=cic-settings-ipv4-delete-dialog-warning"
    ID_BUTTON_EDIT_ADDRESSESIDENTIFIERS_DELETE_RANGE = "xpath=//div[@class='cic-settings-edit-ipv4-table-range-contents']//tbody/tr[td[contains(@class,'cic-settings-edit-ipv4-table-name')]/div[text()='%s']]//descendant::td/div[@class='hp-close crm-ipv4-address-close']"


class VerifyIPPoolsElements(object):

    ID_GENERIC_ADDRESSRANGE_IN_TABLE = "xpath=//table[@id='{0}']//div[@class='cic-settings-edit-ipv4-table-range-details']//table/tbody/tr[td[contains(@class,'{0}-name')]/div[text()='{1}']]"
    ID_GENERIC_SUBNET_IN_TABLE = "xpath=//table[@id='{0}']/tbody/tr[td[@class='{0}-networkId' and text()='{1}']]"

    ID_TABLE_EDIT_SUBNET_ADDRESS_RANGE_NODATA = "xpath=//table[@id='cic-settings-edit-ipv4-edit-range-table']/tbody//tr[td[contains(text(),'No address ranges')]]"
    ID_TABLE_EDIT_ADDRESSIDENTIFIERS_SUBNET_NODATA = "xpath=//form[@id='cic-addresses-edit-form']//table[@id='cic-settings-edit-ipv4-table']/tbody/tr[td[contains(text(),'No subnets')]]"
    ID_INPUT_SUBNET_ID_EDITABLE = "xpath=//input[@id='cic-settings-ipv4-networkid-update' and @style='display: inline;']"
    ID_INPUT_SUBNET_MASK_EDITABLE = "xpath=//input[@id='cic-settings-ipv4-subnet-update' and @style='display: inline;']"
    ID_TEXT_UPDATE_SUBNET_HEADER = "xpath=//div[@id='cic-settings-ipv4update-dialog']/header//span[text()='%s']"

    ID_CHECKBOX_ADDRESSRANGE = "//table[@id='cic-settings-edit-ipv4-table']//div[@class='cic-settings-edit-ipv4-table-range-details']//table/tbody/tr[td[contains(@class,'cic-settings-edit-ipv4-table-name')]/div[text()='%s']]/descendant::input[@class='cic-settings-ipv4-checkbox']"
    ID_SUBNET_IN_ADDRESSIDENTIFIERS_PAGE = "xpath=//table[@id='cic-settings-ipv4-table-more']/tbody/tr[td[@class='cic-settings-ipv4-table-more-networkId' and text()='%s']]"
    ID_UNSET_ASSOCIATED_NETWORKS_IN_ADDRESSIDENTIFIERS_PAGE = ID_SUBNET_IN_ADDRESSIDENTIFIERS_PAGE + "/descendant::td[@class='cic-settings-ipv4-table-more-associatedNetwork hp-unset']"
    ID_ASSOCIATED_NETWORKS_IN_ADDRESSIDENTIFIERS_PAGE = ID_SUBNET_IN_ADDRESSIDENTIFIERS_PAGE + "/descendant::td[@class='cic-settings-ipv4-table-more-associatedNetwork']/a[translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')='%s']"
    ID_SUBNET_DELETE_ASSOCIATED_OBJECT = "xpath=//div[@id='cic-settings-ipv4delete-dialog']//div[@id='cic-settings-edit-ipv4-delete-subnet-collapsible']//a[translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')='%s']"
    ID_RANGE_DELETE_ASSOCIATED_OBJECT = "xpath=//div[@id='cic-settings-ipv4delete-range-dialog']//div[@id='cic-settings-edit-ipv4-delete-subnet-collapsible']//a[translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')='%s']"

    ID_TABLE_ADDRESSESIDENTIFIERS_PAGE_SUBNET_NODATA = "xpath=//form[@id='cic-addresses-show-form']//li[@id='cic-settings_ipv4-selector']//table[@id='cic-settings-ipv4-table-more']/tbody/tr[td[contains(text(),'No subnets')]]"
    ID_LABEL_IPV4_SUBNET_ADDRESSRANGES = "xpath=//li[@id='cic-settings_ipv4-selector']/label[text()='IPv4 Subnets and Address Ranges']"
    ID_GENERIC_DNS_UNSET = ID_GENERIC_SUBNET_IN_TABLE + "/descendant::td[@class='{0}-dnsServers hp-unset']"


class GetIPPoolsElements(object):

    ID_TEXT_GENERIC_SUBNETMASK_IN_TABLE = VerifyIPPoolsElements.ID_GENERIC_SUBNET_IN_TABLE + "/descendant::td[@class='{0}-subnetmask']"
    ID_TEXT_GENERIC_GATEWAY_IN_TABLE = VerifyIPPoolsElements.ID_GENERIC_SUBNET_IN_TABLE + "/descendant::td[@class='{0}-gateway']"
    ID_TEXT_GENERIC_DOMAIN_IN_TABLE = VerifyIPPoolsElements.ID_GENERIC_SUBNET_IN_TABLE + "/descendant::td[@class='{0}-domain']/div"
    ID_TEXT_GENERIC_GATEWAY_UNSET_IN_TABLE = VerifyIPPoolsElements.ID_GENERIC_SUBNET_IN_TABLE + "/descendant::td[@class='{0}-gateway hp-unset']"
    ID_TEXT_GENERIC_DOMAIN_UNSET_IN_TABLE = VerifyIPPoolsElements.ID_GENERIC_SUBNET_IN_TABLE + "/descendant::td[@class='{0}-domain hp-unset']"
    ID_TEXT_GENERIC_DNS_IN_TABLE = VerifyIPPoolsElements.ID_GENERIC_SUBNET_IN_TABLE + "/descendant::td[@class='{0}-dnsServers']"
    ID_TEXT_GENERIC_RANGE_STARTIP = VerifyIPPoolsElements.ID_GENERIC_ADDRESSRANGE_IN_TABLE + "/descendant::td[contains(@class,'{0}-start')]"
    ID_TEXT_GENERIC_RANGE_ENDIP = VerifyIPPoolsElements.ID_GENERIC_ADDRESSRANGE_IN_TABLE + "/descendant::td[contains(@class,'{0}-end')]"
    ID_TEXT_GENERIC_RANGE_COUNT = VerifyIPPoolsElements.ID_GENERIC_ADDRESSRANGE_IN_TABLE + "/descendant::td[contains(@class,'{0}-count')]"
    ID_TEXT_GENERIC_RANGE_AVAILABLE = VerifyIPPoolsElements.ID_GENERIC_ADDRESSRANGE_IN_TABLE + "/descendant::td[contains(@class,'{0}-available')]"

    ID_TEXT_GENERIC_RANGE_ALLOCATED = VerifyIPPoolsElements.ID_GENERIC_ADDRESSRANGE_IN_TABLE + "/descendant::td[contains(@class,'{0}-allocated')]"
    ID_TEXT_RANGE_AVAILABLE_DISABLED = VerifyIPPoolsElements.ID_GENERIC_ADDRESSRANGE_IN_TABLE + "/descendant::td[@class='{0}-available hp-unset']"
