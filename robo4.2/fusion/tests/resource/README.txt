*******************************************************************************
*   README - v1.0
*
*   Fusion test resource folder
*
*   The purpose of this folder is to contain globally defined resource files
*   and keywords for all teams to share across Fusion testing (not data files).
*   Since these are shared files used for testing the product, they should
*   strive for good readability, clarity, and most importantly, robustness and
*   test accuracy.
*
*   If you are unclear about something, these resources can help:
*   http://robotframework.org/robotframework/#user-guide
*   http://robotframework.org/#test-libraries
*   https://code.google.com/p/robotframework/wiki/HowToWriteGoodTestCases
*   https://blog.codecentric.de/en/2012/03/robot-framework-tutorial-overview/
*   https://blog.codecentric.de/en/2013/05/robot-framework-tutorial-loops-conditional-execution-and-more/
*
*******************************************************************************


Please observe the following guidelines with this folder:

*   Restrict it to keywords that are useful to everyone.  Use your local
    resource folders for keywords specific to your cause.

*   Use for resource keywords, not test cases.

*   Keep keywords categorized in files with meaningful titles, such as
    storage_api.txt, network_ui.txt, etc.

*   Remember that these are shared resources so please take the time to code
    and document clearly, concisely, and consistently.

*   Document keywords appropriately so libdoc can parse them.  Also, be sure
    to document what you're returning.

*   Please limit your use of Tags to indicate the keyword control surface
    (UI/API/etc.).  Also please utilize "Default Tags" and "Force Tags" in the
    Settings where possible for simplicity and clarity.

*   Sample Documentation for resource file:
    *** Settings ***
    Documentation    Resource file for demo purposes.
    ...              This resource is only used in an example and it doesn't do anything useful.
    Default Tags      UI

    *** Keywords ***
    My Keyword
        [Documentation]   Does nothing and returns nothing
        No Operation

    Your Keyword
        [Arguments]  ${arg}
        [Documentation]   Takes one argument and *does nothing* with it.
        ...
        ...    Examples:
        ...    | Your Keyword | xxx |
        ...    | Your Keyword | yyy |
        No Operation

*   Please don’t use tab characters in text files.   This makes the reviews
    easier to read because tab characters show up as green arrows which clutters
    the text.

*   Fail your keyword where appropriate and let the test writer handle it.
    Use "Run Keyword and Continue on Failure" when necessary.

*   IMPORTANT:  DO NOT IGNORE, WARN, LOG, OR OTHERWISE DISMISS FAILURES.

*   Don't expect the test writer to know what to do with your return value.
    This creates ambiguity, inconsistency, and the possibility for missed
    defects.  Just fail the keyword.
    A keyword that returns nothing implicitly passes.

*   Don't reinvent usage patterns.  Keep it simple.

*   Look for existing keywords before creating a new one.

*   Robot library keywords are your friend - chances are it's been done before.
    http://robotframework.org/#test-libraries

*   Keywords naming should be clear and observe the following pattern when
    possible in order to maintain clarity and avoid namespace collisions:
        Fusion <UI/API> <action> <target>
        Example:
            Fusion API Create User  ${user}

*   Avoid abbreviating when possible.  Using the full word takes more keystrokes
    but is easy to read for everyone.

*   Provide validation keywords following the Robot Framework keyword model
    when possible.
        Fusion <UI/API> <Resource> Should <be/have/etc.> <condition>
        Example:
            Fusion API Ethernet Network Should Exist    enet-001
            Fusion UI User Should Exist     NetAdmin

*   If you refuse to use "Should" and wish to use "Verify" or "Validate" in
    your keyword name, please observe the following definitions and name
    appropriately and make sure you're doing it:

    * Validation: The assurance that a product, service, or system meets the
        needs of the customer and other identified stakeholders.

    * Verification: The evaluation of whether or not a product, service, or
        system complies with a regulation, requirement, specification, or
        imposed condition.
