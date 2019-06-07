#
#  This Test Suite requires these command line variables for execution:
#    -v APPLIANCE_IP:#.#.#.# -v DATA_FILE:ring.py -v CFM:cfm_hostname.domain
#  At Qual dev time these where the created data files: plexxi-r1-cfm.py, plexxi-r2-cfm.py, plexxi-r3-cfm.py and
#  plexxi-r4-cfm.py
#
#  APPLIANCE_IP is the IP address of the deployed OneView Appliance
#
#  DATA_FILE is the data file specific to the ring being used.  For example: -v DATA_FILE:plexxi-r1-cfm.py
#
#  CFM is used to specify the CFM hostname.
#
#  ${PAUSE_BEFORE_SUITE_SETUP} (within resource.txt) is used to Pause the run prior to each Test Suite (.robot file).
#  Default is ${False}, not pause.
#  Set to ${True} in resource.txt or via: -v PAUSE_BEFORE_SUITE_SETUP:True to enable.
#  The purpose of this is for manual verification of the environment prior to next Test Suite (a debug thing) or to
#  inject faults to verify the tests catch things (such as Critical Alerts between Test Suites).
#
#  ${PAUSE_BEFORE_TEST_CASE} (within resource.txt) is used to Pause the run prior to Test Cases with support for the
#  pause.  Currently only implemented in 44_Server_Profiles_ONE.robot and 54_Edit_Profiles.robot.
#  Set to ${True} in resource.txt or via: -v PAUSE_BEFORE_TEST_CASE:True to enable.
#
#  Each new .robot file executed will check to see if any Critical Alerts were left over from the previous test.
#  In resource.txt, ${ALERT_COUNT_CHANGE_ACTION} defines what action to do.  The default is: Continue.  The Test Suite
#  will continue.  If set to Fail, then the about to start .robot file will call Fatal Error to abort the Test Suite.
#
#  By default log messages are also sent to the console.  To disable this set ${CONSOLE} (in resource.txt) to ${False}
#  or -v CONSOLE:False
#
# ${CONFIRM_SWITCHES} is created by simply executing a GET on /rest/switches and saving to ${OV_SWITCHES_FILE}
# Plexxi-r1-switces_master.txt.   That file is read at run-time to create ${CONFIRM_SWITCHES}.  This was an idea
# so as to not have to manually create the data but use what is in OneView and when confirmed to be accurate can then
# be used in subsequent tests to ensure the environment has not changed.  If this proves a maintenace nightmare then
# another approach will be needed.
#