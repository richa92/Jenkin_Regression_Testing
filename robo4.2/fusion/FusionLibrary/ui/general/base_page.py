# (C) Copyright 2013-2015 Hewlett-Packard Development Company, L.P.
"""
    Base Page
"""
from RoboGalaxyLibrary.data import test_data

from FusionLibrary.ui.business_logic.base import FusionUIBaseElements
from FusionLibrary.ui.general.login_elements import FusionLoginPage
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.utilitylib import logging as logger
from robot.libraries.BuiltIn import BuiltIn
from FusionLibrary.ui.business_logic.base import FusionUIBase


class MyNonFatalError(RuntimeError):
    ROBOT_EXIT_ON_FAILURE = False


def logout():
    # check the existing login status
    if FusionUIBase.logged_in():
        logger._log_to_console_and_log_file("Logging out of Fusion..")
        ui_lib.wait_for_element(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
        ui_lib.wait_for_element_visible(FusionUIBaseElements.ID_SESSION_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
        ui_lib.wait_for_element_and_click(FusionUIBaseElements.ID_SESSION_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
        ui_lib.wait_for_element_visible(FusionUIBaseElements.ID_SESSION_LOGOUT)
        ui_lib.wait_for_element_and_click(FusionUIBaseElements.ID_SESSION_LOGOUT, PerfConstants.DEFAULT_SYNC_TIME)
        ui_lib.wait_for_element_visible(FusionLoginPage.ID_INPUT_LOGIN_USER, PerfConstants.FUSION_LOGOUT_TIME)
        FusionUIBase.set_login_status(False)

        return True
    return False


def navigate_base(currentpage, menulink, itemcount):
    s2l = ui_lib.get_s2l()
    logger._log_to_console_and_log_file('Navigating to "{0}"'.format(currentpage))
    if not s2l._is_element_present(currentpage):
        # open the menu and wait for it to be active
        if not s2l._is_element_present(FusionUIBaseElements.ID_MENU_ACTIVE):
            ui_lib.wait_for_element_and_click(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME, fail_if_false=True)
            ui_lib.wait_for_element(FusionUIBaseElements.ID_MENU_ACTIVE, PerfConstants.DEFAULT_SYNC_TIME, fail_if_false=True)

        # if the new menu style is active, the link may lie under a collapsed section
        if not ui_lib.is_visible(menulink):
            ui_lib.wait_for_element_and_click(menulink + '/parent::li/parent::ul/parent::li')

        # click the menu link and wait for the page title
        ui_lib.wait_for_element_and_click(menulink, PerfConstants.DEFAULT_SYNC_TIME, fail_if_false=True)
        s2l.wait_until_page_contains_element(currentpage, PerfConstants.DEFAULT_SYNC_TIME)

        # if the menu is still opened, close it
        if ui_lib.is_visible(FusionUIBaseElements.ID_MENU_ACTIVE):
            ui_lib.wait_for_element_and_click(FusionUIBaseElements.ID_MAIN_MENU_CONTROL)
            ui_lib.wait_for_element_remove(FusionUIBaseElements.ID_MENU_ACTIVE)

    # wait for the page items to be displayed
    s2l.wait_until_page_contains_element(itemcount, PerfConstants.DEFAULT_SYNC_TIME)

    # added wait to remove int Base 10 conversion error while running with Selenium speed 0.0
    BuiltIn().sleep(1)
    for x in range(1, 5):
        try:
            el = int(s2l.get_text(itemcount))
            break
        except ValueError:
            BuiltIn().sleep(1)
            pass
    while el >= 0:
        BuiltIn().sleep(0.1)
        tmp_el = int(s2l.get_text(itemcount))
        if el == tmp_el:
            break
    # wait for page controls to complete expanding
    # ui_lib.wait_for_element_expand(FusionUIBaseElements.ID_MASTER_PANE)


def get_page_name():
    # get a reference to the selenium lib
    s2l = ui_lib.get_s2l()

    # get the current page
    s2l.wait_until_page_contains_element(FusionUIBaseElements.ID_PAGE_LABEL)
    page_name = s2l.get_text(FusionUIBaseElements.ID_PAGE_LABEL)
    return page_name


def navigate_help_page(help_page_type):
    """
    Using this function we can browse to help using "help on this page"
    or "Browse help link available on every page.
    """

    # get a reference to the selenium lib
    s2l = ui_lib.get_s2l()
    # Click on Help on this page link after making sure link exist.
    if not s2l._is_element_present(help_page_type):
        s2l.click_element(FusionUIBaseElements.ID_HELP)

    # launch help page on click "Help on this page"\ "Browse help" link
    s2l.click_element(help_page_type)

    # Select frame inside window to interact with help page
    s2l.select_window(FusionUIBaseElements.HELP_PAGE_TITLE)
    s2l.select_frame(FusionUIBaseElements.HELP_PAGE_FRAME_NAME)


def help_on_this_page_header():
    """
    This function compare between header with respective sub menu page
    """
    # get a reference to the selenium lib
    s2l = ui_lib.get_s2l()

    # get current page_name using FusionUIBaseElements.ID_PAGE_LABEL
    page_name = get_page_name()

    # capture the title to come back
    prev_title = s2l.get_title()

    # get header of help page after clicking on "Help on this page"
    navigate_help_page(FusionUIBaseElements.ID_HELP_ON_THIS_PAGE)

    # replace white space by _, creating header string to find xpath from repository
    header = page_name.replace(" ", "_") + "_header"

    # get help file header using xpath in repos
    page_header = s2l.get_text("xpath=//h1[@class='firsttitle']")

    # return control back to main browser
    s2l.select_window(prev_title)

    # verify header of help file matched with page name
    if page_name == page_header:
        logger._log_to_console_and_log_file(' Passed: Page name ("%s") and header of Help page ("%s")' % (page_name, page_header))
    else:
        ui_lib.fail_test('Failed: Page name ("%s") and header of Help page ("%s")' % (page_name, page_header))


def browse_help_page_header():
    """
        This function compare between header with respective sub menu page
    """
    # get a reference to the selenium lib
    s2l = ui_lib.get_s2l()

    # capture the title to come back
    prev_title = s2l.get_title()

    # get current page_name using FusionUIBaseElements.ID_PAGE_LABEL
    page_name = get_page_name()

    # get header of help page after clicking on "Browse help"
    navigate_help_page(FusionUIBaseElements.ID_BROWSE_HELP)

    page_header = s2l.get_text("xpath=//h1[@class='firsttitle']")

    # return control back to main browser
    s2l.select_window(prev_title)

    # verify header of help file matched with page name
    if page_name == page_header:
        logger._log_to_console_and_log_file(' Passed: Page name ("%s") and header of Browse Help page ("%s")' % (page_name, page_header))
    else:
        ui_lib.fail_test('Failed: Page name ("%s") and header of  Browse Help page ("%s")' % (page_name, page_header))


def help_page_should_not_contain_string(help_page_type, *keys):

    # get a reference to the selenium lib
    s2l = ui_lib.get_s2l()

    # Navigate to help page
    navigate_help_page(help_page_type)

    # Flag is used to continue test in case of failure
    Flag = True

    # Using List to store all the observation and print them in Last""
    lst = list()
    lst.append("                                       ")
    lst.append("Key => Link of the page where key found")
    lst.append("                                       ")
    # Make sure frame selected before processing links
    s2l.select_window(FusionUIBaseElements.HELP_PAGE_TITLE)
    s2l.select_frame("contentspane")
    s2l.select_frame("nav-main")

    # get the count of links available on page.
    count = int(s2l.get_matching_xpath_count("//a"))
    logger._log_to_console_and_log_file('Total links available on this Page = ("%s") ' % (count))

    # iterate over links
    for i in range(1, 5 + 1):

        # Select frame inside window to interact with help page
        s2l.select_window(FusionUIBaseElements.HELP_PAGE_TITLE)
        s2l.select_frame("contentspane")
        s2l.select_frame("nav-main")

        # Get the href value and report in log and file for further analysis
        href = s2l.get_element_attribute("xpath=(//a)[%s]@href" % (str(i)))
        logger._log_to_console_and_log_file('Link # "%s" HREF value = "%s"' % (i, href))

        # Make sure that element is visible and click on element
        if s2l._is_visible("xpath=(//a)[%s]" % (str(i))):
            s2l.wait_until_page_contains_element("xpath=(//a)[%s]" % (str(i)))
            s2l.click_element("xpath=(//a)[%s]" % (str(i)))
        else:
            continue

        # Make sure that target page is selected for text verification
        s2l.select_window(FusionUIBaseElements.HELP_PAGE_TITLE)
        s2l.select_frame("mainhelp_pane")

        # Look for all KEY STRING provided in test file
        for key in keys:
            if s2l._is_text_present(key):
                # raise Exception is exiting test so using List to record message and display at the end of test
                raise MyNonFatalError('Search key ("%s") found at ("%s") link' % (key, href))
                lst.append(key + " => " + href)
                Flag = False

    if not Flag:
        # print the list data to show key found and name of the page
        for item in lst:
            logger._log_to_console_and_log_file('Failed:  "%s"' % item)
        ui_lib.fail_test('Failed: Search key found in help pages')


def search(search_fusion_page, search_keyword):
    """ Search a keyword on fusion Page specified

        Example :
                ***Variables***
                ${SearchFusionPage}        Enclosures
                ${SearchKeyword}           CS_MAT
                ***Keyword***
                Fusion UI search  ${SearchFusionPage}  ${SearchKeyword}

                ${SearchFusionPage} will have the page name where search need to be initiated.
                ${SearchKeyword} is the keyword searched.

        NOTE :
            >> Fusion Pages covered -Server Profiles, Enclosures, Server Hardware,Server Hardware Types
                                     Logical Interconnect Groups, Logical Interconnects, Networks, Network Sets
                                     Interconnects, Data Centers, Racks,Power Delivery Devices, Users and Groups
               (Fusion UI Page which are having table can be searched for the keywords.)
                                    -Enclosure Group, Server Hardware Type and Firmware Bundles
                (Above stated pages will have <div> containing the keywords.)

            >> function will not work on     -   Settings and Activity Page

    """
    s2l = ui_lib.get_s2l()
    navigate_base(FusionUIBaseElements.ID_PAGE_LABEL_BASE % search_fusion_page, FusionUIBaseElements.ID_MENU_LINK_BASE % search_fusion_page, "css=span.hp-page-item-count")

    # CODE TO TYPE IN SEARCH FIELD
    ui_lib.wait_for_element_and_click(FusionUIBaseElements.ID_SEARCH_BAR)
    if s2l.get_text(FusionUIBaseElements.ID_SEARCH_BAR) != "Search":
        ui_lib.wait_for_element_and_click(FusionUIBaseElements.ID_SEARCH_CLEAR)
        logger._log_to_console_and_log_file("Search Bar is not EMPTY, Cleared Search Bar")

    logger._log_to_console_and_log_file("Text to be Searched is - '%s'" % search_keyword)
    s2l.input_text(FusionUIBaseElements.ID_INPUT_SEARCH, str('"' + search_keyword + '"'))
    s2l.press_key(FusionUIBaseElements.ID_INPUT_SEARCH, chr(13))

    # Wait required to overcome change in DOM object error for Keyword's Master Table
    BuiltIn().sleep(2)
    logger._log_to_console_and_log_file(" ===Search on %s Page,=== " % search_fusion_page)
    # Searching for the keyword. As these Fusion pages are having data formatted in Table, so covering them together.
    page_list = ['server profiles', 'enclosures', 'server hardware', 'logical interconnect groups', 'logical interconnects', 'networks', 'network sets', 'interconnects', 'data centers', 'racks', 'power delivery devices', 'users and groups']
    if search_fusion_page.lower() in page_list:
        # Checking for keyword in the table, and returns FALSE if fail
        element = s2l._table_element_finder.find_by_content(s2l._current_browser(), FusionUIBaseElements.ID_TABLE_MASTER_BASE, search_keyword)
        if element is None:
            logger._warn("Search for Keyword %s Failed" % search_keyword)
            s2l.capture_page_screenshot()
            return False

        # This code will match the exact keyword in UI table.
        table = s2l._table_element_finder.find(s2l._current_browser(), FusionUIBaseElements.ID_TABLE_MASTER_BASE)
        if table is not None:
            rows = table.find_elements_by_xpath("./tbody/tr")
            for row_index in range(len(rows)):
                logger._log_to_console_and_log_file("checking for data in Row no. - %s" % row_index)
                columns = rows[row_index].find_elements_by_tag_name('th')
                columns.extend(rows[row_index].find_elements_by_tag_name('td'))
                for col_index in range(len(columns)):
                    if columns[col_index].text.lower().strip() == search_keyword.lower().strip():
                        logger._log_to_console_and_log_file("SUCCESS : Found on  %s Page " % search_fusion_page)
                        logger._log_to_console_and_log_file("kEYWORD %s Searched" % search_keyword)
                        return True
        logger._warn("Search for Keyword '%s' Failed" % search_keyword)
        s2l.capture_page_screenshot()
        return False

    # Code to search on Enclosure Group
    elif search_fusion_page.lower() == "enclosure groups":
        if ui_lib.wait_for_element(FusionUIBaseElements.ID_LABEL_ENCLOSURE_GROUPS_BASE % search_keyword, PerfConstants.DEFAULT_SYNC_TIME):
            logger._log_to_console_and_log_file("SUCCESS: KEYWORD '%s' Searched" % search_keyword)
            return True
        else:
            logger._warn("Search for Keyword %s Failed" % search_keyword)
            s2l.capture_page_screenshot()
            return False

    # Code to search on Server Hardware
    elif search_fusion_page.lower() == "server hardware types":
        if ui_lib.wait_for_element(FusionUIBaseElements.ID_LABEL_SERVER_HARDWARE_TYPE_BASE % search_keyword, PerfConstants.DEFAULT_SYNC_TIME):
            logger._log_to_console_and_log_file("SUCCESS: KEYWORD '%s' Searched" % search_keyword)
            return True
        else:
            logger._warn("Search for Keyword %s Failed" % search_keyword)
            s2l.capture_page_screenshot()
            return False

    # Code to search on firmware bundles
    elif search_fusion_page.lower() == "firmware bundles":
        if ui_lib.wait_for_element(FusionUIBaseElements.ID_LABEL_FIRMWARE_BUNDLE_BASE % search_keyword, PerfConstants.DEFAULT_SYNC_TIME):
            logger._log_to_console_and_log_file("SUCCESS: KEYWORD '%s' Searched" % search_keyword)
            return True
        else:
            logger._warn("Search for Keyword %s Failed" % search_keyword)
            s2l.capture_page_screenshot()
            return False
    else:
        logger._warn(" ERROR : === %s Page is not Present in FUSION Appliance or not covered by SEARCH function === " % search_fusion_page)
        s2l.capture_page_screenshot()
        return False


def set_logged_user(user):
    """ set_logged_user
        Description : Function used for setting the logged user, set user name once you are logged in to the applicance
    """
    test_data.set_variable(test_data.GlobalProperty.UiLoggedIn, user)


def get_logged_user():
    """ get_logged_user
        Description : Function used for retrieving the logged in user. If no user is logged in, it will return None.
    """
    return test_data.get_variable(test_data.GlobalProperty.UiLoggedIn)


def logged_in():
    """ logged_in
        Description : Function used for retrieving the login status (True of False). Returns true if test_data.GlobalProperty.UiLoggedIn is not None
    """
    return get_logged_user() is not None


def get_errors_on_form(form_id):
    '''
    Function to get all the errors seen on the form - Common for Create and edit operations
    Return error string separated by '\t' if errors are present else returns None
    '''

    # if errors are seen then return a string of errors separated by \t else None
    error_elements = []
    error_string = ''
    selenium2libObj = ui_lib.get_s2l()
    try:
        error_elements = selenium2libObj._current_browser().find_element_by_id(form_id).find_elements_by_class_name("hp-error")
    except:
        error_elements = []
    if error_elements:
        logger._warn("Displaying Following errors : ...")
        for errorelement in error_elements:
            if errorelement.text is not None and errorelement.text != "":
                logger._warn("Error - '{}' for element : '{}'".format(errorelement.text, errorelement.get_attribute("for")))
                error_string += errorelement.text + '\t'
        return error_string
    else:
        return None


def open_guided_setup_panel():
    """ display the guided setup panel """
    if not logged_in():
        raise AssertionError("Not logged in")

    # if the panel is already visible, do nothing
    if not ui_lib.is_visible(FusionUIBaseElements.ID_GUIDED_SETUP_PANEL):
        ui_lib.wait_for_element_and_click(FusionUIBaseElements.ID_GUIDED_SETUP_BUTTON)
        ui_lib.wait_for_element_visible(FusionUIBaseElements.ID_GUIDED_SETUP_PANEL, fail_if_false=True)


def close_guided_setup_panel():
    """ hide the guided setup panel """
    if not logged_in():
        raise AssertionError("Not logged in")

    # if the panel not already hidden, close it
    if ui_lib.is_visible(FusionUIBaseElements.ID_GUIDED_SETUP_PANEL):
        ui_lib.wait_for_element_and_click(FusionUIBaseElements.ID_GUIDED_SETUP_BUTTON)
        ui_lib.wait_for_element_notvisible(FusionUIBaseElements.ID_GUIDED_SETUP_PANEL, fail_if_false=True)
