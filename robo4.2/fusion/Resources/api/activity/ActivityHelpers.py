"""
Validates the errors from the Oneview Tasks
"""
from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.utilitylib import logging as logger

import re
import time

fusion_lib = BuiltIn().get_library_instance('FusionLibrary')


def get_task_tree(uri):
    """
    :param uri: task uri
    :return response: task tree
    """
    response = fusion_lib.fusion_api_get_task(uri=uri, param='?view=tree')
    logger._debug("The task tree for %s is %s" % (uri, response))
    return response


def get_task_tree_nodes(task_tree, nodes, taskState=''):
    """
    :param task_tree:
    :param nodes: nodes in the task tree that match taskState
    :param taskState: default to empty string
    :return nodes:
    """
    nodes = nodes

    if taskState != '':
        if re.search(task_tree['resource']['taskState'], taskState):
            nodes.append(task_tree['resource'])
    else:
        nodes.append(task_tree['resource'])

    if len(task_tree['children']) != 0:
        for childtask in task_tree['children']:
            get_task_tree_nodes(childtask, nodes, taskState=taskState)

    return nodes


def check_task_error_message(task_list, taskState='Error', errorMessage=''):
    """
    :param task_list: list of tasks
    :param taskState: default to 'Error'
    :param errorMessage:
    :return found: True or False
    """
    found = False
    for task in task_list:
        if re.search(task['taskState'], taskState):
            for taskError in task['taskErrors']:
                if len(taskError['nestedErrors']) != 0:
                    for nestedError in taskError['nestedErrors']:
                        if re.search(errorMessage, nestedError['message']):
                            found = True
                else:
                    if re.search(errorMessage, taskError['message']):
                        found = True

    return found


def get_task_error_message(task_list, taskState='Error'):
    """
    :param task_list: list of tasks
    :param taskState: default to 'Error'
    :return errorMessage
    """
    errorMessage = None
    for task in task_list:
        if re.search(task['taskState'], taskState):
            for taskError in task['taskErrors']:
                if 'message' in taskError.keys():
                    errorMessage = taskError['message']
    return errorMessage


def WFT2_Python_Helper(tasks,
                       timeout=60,
                       interval=2,
                       errorMessage="None Expected",
                       PASS="((?i)Completed|Warning)",
                       BREAK_LOOP_IF="((?i)Error|Terminated)",
                       VERBOSE=False,
                       **kwargs):
    """
    #   Argument ${tasks} can be a TaskResource dict or a dict that contains a ['headers']['location'] value to a task uri,
    #   or a list of such.  If a list and any task fails, the keyword will fail and remaining tasks are not verified.
    #
    #   Supports BREAK_LOOP_IF and Error Message override of failure for negative testing.  BREAK_LOOP_IF is used to
    #    terminate the wait loop prior to timeout.
    #
    #   This keyword also evaluates ${tasks} to see if an error occurred and thus ${tasks} isn't a task resource.
    #
    #   Defaults: ${timeout}=60  ${interval}=2  ${errorMessage}=None Expected  ${PASS}=((?i)Completed|Warning)  ${BREAK_LOOP_IF}=((?i)Error|Terminated)  ${VERBOSE}=False
    #
    #   Timeout and interval are in seconds, though both can be entered in minutes as in 10m.
    #
    #   If ${errorMessage} is not passed in, error messages will not be be validated for Negative testing.
    #   If ${errorMessage} is passed in and the actual errorMessage value contains ${variables}, then you must supply those variables values.
    #   See errorMessages.py for additional information regarding errorMessages.
    #
    #   Usage examples:
    #   Wait For Task2	${tasks}	   timeout=60	interval=5    pass=Error  errorMessage=ethernet_exists    name=Net777
    #   Wait For Task2    ${tasks}    ${PASS}=((?i)Running|Starting)    ${BREAK_LOOP_IF}=((?i)Error|Terminated)   ${VERBOSE}=True
    #   Wait For Task2    ${tasks}    ${PASS}=((?i)Running|Starting)    ${BREAK_LOOP_IF}=((?i)Error|Terminated)   ${VERBOSE}=True
    #
    #  Note:  By default this WFT2 helper aborts on task failure (if not expected with correct errorMessage).
    # To ignore errors and process all tasks supply a command line switch:
    # pybot -v APPLIANCE_IP:16.114.221:186 -v WFT2_CONTINUE_ON_ERROR:True
    # someTest.robot
    """

    if BuiltIn().get_variable_value("${WFT2_CONTINUE_ON_ERROR}"):
        WFT2_CONTINUE_ON_ERROR = BuiltIn().replace_variables(
            "${WFT2_CONTINUE_ON_ERROR}")
    else:
        WFT2_CONTINUE_ON_ERROR = False

    failingTasks = []
    if WFT2_CONTINUE_ON_ERROR:
        logger._log_to_console_and_log_file(
            "Will process all tasks and continue on errors.")

    # Convert timeout to seconds if passed in as minutes: 10m.
    if re.search(r'm', timeout, re.I):
        logger._log_to_console_and_log_file(
            "Timeout in minutes.  Convert to seconds.")
        timeout = int(float(re.sub('m.*$', '', timeout, re.I)) * 60)

    if re.search(r'm', interval, re.I):
        logger._log_to_console_and_log_file(
            "Interval in minutes.  Convert to seconds.")
        interval = int(float(re.sub('m.*$', '', interval, re.I)) * 60)

    # verify that tasks is a dict or list of dict.  If not, fail and inform
    # user of this requirement.
    if isinstance(tasks, dict):
        logger._log_to_console_and_log_file(
            "tasks is a dict.  Convert to list of this task.")
        tasks = [tasks]
    elif isinstance(tasks, list) and isinstance(tasks[0], dict):
        logger._log_to_console_and_log_file(
            "tasks is a list with %d tasks." %
            len(tasks))
    else:
        raise AssertionError(
            "You must pass in a dict or list of dict.  Should WFT2 be called?.")

    if VERBOSE:
        logger._log_to_console_and_log_file("task: %s" % tasks)

    # Set up expected error for negative tests.
    if errorMessage == "None Expected":
        expected_error_message = "None Expected"
    else:
        # Get extrapolated expected error message.  Use RG Keyword for now
        expected_error_message = BuiltIn().run_keyword(
            "Get Expected Error",
            errorMessage,
            kwargs)

    logger._log_to_console_and_log_file("errorMessage: %s" % errorMessage)
    logger._log_to_console_and_log_file(
        "timeout (seconds): %s interval: %s" %
        (timeout, interval))
    logger._log_to_console_and_log_file(
        "PASS: %s, BREAK_LOOP_IF: %s" %
        (PASS, BREAK_LOOP_IF))
    logger._log_to_console_and_log_file("kwargs: %s" % kwargs)
    logger._log_to_console_and_log_file(
        "expected_error_message: %s" %
        expected_error_message)
    logger._log_to_console_and_log_file(
        "WFT2_CONTINUE_ON_ERROR: %s" %
        WFT2_CONTINUE_ON_ERROR)

    # if location header available use that, else get the task uri and do Get of that task.
    # This way user can pass in a taskResouce or dict with headers and a
    # location header
    for task in tasks:
        location = None
        task_uri = None
        taskData = {}
        if ('headers' in task) and ('location' in task['headers']):
            location = task['headers']['location']
        if 'uri' in task:
            task_uri = task['uri']

        if location is not None:
            logger._log_to_console_and_log_file(
                "Getting Task using location: %s" %
                location)
            task = fusion_lib.fusion_api_get_task(uri=location)
        elif task_uri is not None:
            logger._log_to_console_and_log_file(
                "Getting Task using task_uri: %s" %
                task_uri)
            task = fusion_lib.fusion_api_get_task(uri=task_uri)

        # Determine if ${task} contains taskState thus is a taskResource.
        # If not, check the error message and either fail or pass if it was an
        # expected error.
        resourceName = None
        resourceType = None
        if 'associatedResource' in task:
            resourceName = task['associatedResource']['resourceName']
            resourceType = task['associatedResource']['resourceCategory']
        else:
            print "NO ASSOCIATED RESOURCE"
        if 'taskState' in task:
            taskState = task['taskState']
            logger._log_to_console_and_log_file("taskState: %s" % taskState)
            task_uri = task['uri']
        else:
            logger._log_to_console_and_log_file(
                "taskState not obtained, will check error message")

            if 'message' in task:
                actMessage = task['message']
                logger._log_to_console_and_log_file(
                    "actMessage: %s" %
                    actMessage)

                if re.search(expected_error_message, actMessage):
                    logger.warn(
                        "actMessage message matches expected error message.")
                    continue
                else:
                    if WFT2_CONTINUE_ON_ERROR:
                        # failingTasks.append(task['uri'])
                        taskData['uri'] = task['uri']
                        taskData['name'] = resourceName
                        failingTasks.append(taskData)
                        logger.warn(
                            "actMessage not matching expected error message.")
                    else:
                        logger.warn("{0} '{1}' Failed: actMessage not matching expected error message." .format(resourceType, resourceName))
                        out_string = "Task Message:{0} \nRecommendedActions:{1} \nerrorCode:{2} ".format(
                            task['message'], task['recommendedActions'], task['errorCode'])
                        raise AssertionError("actMessage not matching expected error message.\n{}".format(out_string))
            else:
                if WFT2_CONTINUE_ON_ERROR:
                    taskData['uri'] = task['uri']
                    taskData['name'] = resourceName
                    failingTasks.append(taskData)
                    logger.warn(
                        "Unable to obtain taskState and no error message.  Should WFT2 be called?.")
                else:
                    raise AssertionError(
                        "Unable to obtain taskState and no error message.  Should WFT2 be called?.")

        # setup up timer
        countDownTo = 0
        countDownFrom = int(timeout)
        logger._log_to_console_and_log_file(
            "Countdown from %s to %s by interval of %s seconds." %
            (countDownFrom, countDownTo, interval))
        interval = int(interval)

        # spin on the task, checking taskState each pass
        passed = False
        break_loop = False
        timed_out = False
        while True:
            # Exit loop if taskState PASS
            if re.search(PASS, taskState):
                logger._log_to_console_and_log_file(
                    "taskState reached expected argument 'PASS' state: %s." %
                    taskState)
                passed = True
                break

            # Exit loop if taskState BREAK_LOOP_IF
            if re.search(BREAK_LOOP_IF, taskState):
                logger._log_to_console_and_log_file(
                    "Break Loop, taskState failed: %s." %
                    taskState)
                break_loop = True
                break

            # Exit loop if timedout
            if countDownFrom <= countDownTo:
                logger._log_to_console_and_log_file(
                    "Task loop timed out after %s seconds" %
                    timeout)
                timed_out = True
                break
            time.sleep(interval)
            countDownFrom -= interval

            # get the task again
            task = fusion_lib.fusion_api_get_task(uri=task_uri)
            if 'taskState' in task:
                taskState = task['taskState']
            else:
                if WFT2_CONTINUE_ON_ERROR:
                    logger.warn(
                        "taskState not found in last GET on task uri: %s" %
                        task_uri)
                else:
                    logger.warn("{0} '{1}' Failed: taskState not found in last GET taskUri" .format(resourceType, resourceName))
                    raise AssertionError(
                        "taskState not found in last GET on task uri: %s" %
                        task_uri)

            logger._log_to_console_and_log_file(
                "Now at %s, taskState: %s" %
                (countDownFrom, taskState))

        # if taskState reached expected taskState: PASS (could be Complete could be Error) then evaluate taskErrors
        # If there are taskErrors and user didn't specify an errorMessage then fail.
        # if there are not taskErrors and the user did specify an error message then fail
        # otherwise pass
        check_expected_error = False
        if passed:
            if ('taskErrors' in task) and (len(task['taskErrors']) > 0):
                if expected_error_message is 'None Expected':
                    if taskState is 'Completed':
                        actMessage = task['taskErrors'][0]['message']
                        if WFT2_CONTINUE_ON_ERROR:
                            # failingTasks.append(task['uri'])
                            taskData['uri'] = task['uri']
                            taskData['name'] = resourceName
                            failingTasks.append(taskData)
                            logger.warn(
                                "Task reached expected state but didn't expect taskError: %s" %
                                actMessage)
                        else:
                            raise AssertionError(
                                "{0} '{1}' Failed: Task reached expected state but didn't expect taskError- '{2}'".format(resourceType, resourceName, actMessage))
                    else:
                        logger._log_to_console_and_log_file(
                            "taskError ignored as taskState is not 'Completed' and user did not specify an errorMessage.")
                else:
                    check_expected_error = True

            elif ('taskErrors' not in task) and (expected_error_message is not 'None Expected'):
                if WFT2_CONTINUE_ON_ERROR:
                    # failingTasks.append(task['uri'])
                    taskData['uri'] = task['uri']
                    taskData['name'] = resourceName
                    failingTasks.append(taskData)
                    logger.warn(
                        "Task reached expected state but no expected taskError returned.  Expected: %s" %
                        expected_error_message)
                else:
                    logger.warn("{0} '{1}' Failed: No expected errorMessage returned".format(resourceType, resourceName))
                    raise AssertionError(
                        "Task reached expected state but no expected taskError returned.  Expected: %s" %
                        expected_error_message)
            else:
                if taskState != 'Completed':
                    logger._log_to_console_and_log_file(
                        "Unexpected taskErrors are ignored for non 'Completed' taskState.")
                continue

        if timed_out:
            if WFT2_CONTINUE_ON_ERROR:
                # failingTasks.append(task['uri'])
                taskData['uri'] = task['uri']
                taskData['name'] = resourceName
                failingTasks.append(taskData)
                logger.warn("{0} '{1}' Failed: Task timed out.".format(resourceType, resourceName))
            else:
                logger.warn("{0} '{1}' Failed: Task timed out".format(resourceType, resourceName))
                raise AssertionError("Task timed out.")

        #  user the supplied taskState was met (Error for example) and the passed in a errorMessage then we'll
        #  get to here.  Use this same code to test the error message.
        if break_loop or check_expected_error:
            if 'taskErrors' in task:
                task_tree = get_task_tree(task_uri)
                nodes = []
                task_nodes = get_task_tree_nodes(
                    task_tree,
                    nodes,
                    taskState=PASS)
                logger._debug("The nodes returned are %s" % task_nodes)
                if check_expected_error:
                    found = check_task_error_message(
                        task_nodes,
                        taskState=PASS,
                        errorMessage=expected_error_message)
                    if found:
                        logger._log_to_console_and_log_file(
                            "Error message '%s' found" %
                            expected_error_message)
                    else:
                        if WFT2_CONTINUE_ON_ERROR:
                            # failingTasks.append(task['uri'])
                            taskData['uri'] = task['uri']
                            taskData['name'] = resourceName
                            failingTasks.append(taskData)
                            logger.warn(
                                "{0} '{1}' Failed: Error message '{2}' not found".format(resourceType, resourceName, expected_error_message))
                        else:
                            logger.warn("{0} '{1}' Failed: Error message is not found".format(resourceType, resourceName))
                            task_msg = get_task_error_message(task_nodes)
                            out_str = "{0} not found.\nActual message is : {1}".format(expected_error_message, task_msg)
                            raise AssertionError("Error message : {}".format(out_str))
                else:
                    if 'message' in task:
                        actMessage = task['message']
                        logger._log_to_console_and_log_file(
                            "actMessage: %s" %
                            actMessage)

                    if ('taskErrors' in task) and (
                            'message' in task['taskErrors'][0]):
                        actMessage = task['taskErrors'][0]['message']
                        logger._log_to_console_and_log_file(
                            "actMessage: %s" %
                            actMessage)

                    if WFT2_CONTINUE_ON_ERROR:
                        # failingTasks.append(task['uri'])
                        taskData['uri'] = task['uri']
                        taskData['name'] = resourceName
                        failingTasks.append(taskData)
                        logger.warn(
                            "{0} '{1}' Failed: Task Error but no expected error was specified.".format(resourceType, resourceName))
                    else:
                        logger.warn("{0} '{1}' Failed: Task Error but no expected error was specified.".format(resourceType, resourceName))
                        logger.warn("Actual error message: {}".format(actMessage))
                        raise AssertionError(
                            "Task Error but no expected error was specified.")
            else:
                if WFT2_CONTINUE_ON_ERROR:
                    # failingTasks.append(task['uri'])
                    taskData['uri'] = task['uri']
                    taskData['name'] = resourceName
                    failingTasks.append(taskData)
                    logger.warn(
                        "Task broke loop, but no taskError was returned.")
                else:
                    raise AssertionError(
                        "{0} '{1}' Failed: Task broke loop, but no taskError was returned.".format(resourceType, resourceName))

    if WFT2_CONTINUE_ON_ERROR and len(failingTasks):
        logger._log_to_console_and_log_file(failingTasks)
        for task in failingTasks:
            logger._log_to_console_and_log_file("Failed {0} name: {1}".format(resourceType, task['name']))
        raise AssertionError("There were %s failing tasks." % len(failingTasks))
    return True


def check_event_item(event, eventItemName, eventItemValue):
    """
    :param event:
    :param eventItemName: ipv4Address, ContextEngineID, PduTrapType etc.
    :param eventItemValue: expected value.
    """
    if isinstance(event, dict) and re.search('Event', event['type']):
        check = 'FAIL'
        event_details = event['eventDetails']
        if len(event_details) != 0:
            for event_detail in event_details:
                logger._debug(
                    "eventItemName %s eventItemValue %s" %
                    (event_detail['eventItemName'], event_detail['eventItemValue']))
                if event_detail['eventItemName'] == 'ContextEngineID':
                    event_detail['eventItemValue'] = event_detail[
                        'eventItemValue'].replace(':', '')
                if event_detail['eventItemName'] == eventItemName and event_detail[
                        'eventItemValue'] == eventItemValue:
                    check = 'PASS'
                    break
        else:
            logger._debug("Event %s has no eventDetails" % event['uri'])
    else:
        raise AssertionError("The argument event %s is not event DTO" % event)

    BuiltIn().should_match(
        check,
        'PASS',
        msg='check event item should match PASS')
    BuiltIn().log(
        'PASS: Check event %s eventItemName %s eventItemValue %s' %
        (event['uri'], eventItemName, eventItemValue), console=True)
