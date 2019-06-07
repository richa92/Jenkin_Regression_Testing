from robot.libraries.BuiltIn import BuiltIn
from performance_db_access import PerformanceDbAccess
from robot.utils import robottime
import fusion_conditions
import datetime
import re
import json
import os

ROBOT_LISTENER_API_VERSION = 2

##############################################################

# This Python module is a listener that include the listener methods
# that's use to listen into the test execution. Other functions are
# used to parsed keywords, get timing results, writing data to a file, etc
# The three lister methods used here are start_test, end_keyword, and end_test

# Usage Example:
#     pybot --listener  listener.py  -v APPLIANCE_IP:16.x.x.x  test.robot
#

##############################################################


# The below variables are all global, since we do not want these to
# reinitialized everytime the listener methods starts, made them global
write_to_db = False  # Flag to turn on/off writing to performance DB
test_case_name = ""
performance = False
kw_resource = ''
non_task_resource = ''
condition = ''
async_elapsed = ''
task_uri = ''
fw_version_id = ''
non_get_action = ''
async_resource = ''
rest_resource = ''
rest_crud = ''
resp_resource = ''
log_stash_format = {'Timestamp': ['0', ''], 'Resource': '', 'Action': '', 'Condition': '', 'Duration': 0, 'IsAsync': '',
                    'IsWithinThreshold': '', 'OVPB': '', 'GARFS': '', 'EncType': ''}
task_details = {'uri': '', 'status': '', 'created': '', 'modified': ''}
task_list = []


def write_results(file_path, results, open_action):
    """ Open file based on the open action('a','w',etc.) and write results
    Ex. write_results('c:\filepath.txt, results[], 'a')
    """
    open_action = open_action
    with open(file_path, open_action) as target:
        target.write(' '.join(results))
    target.close()


def get_crud_from_kw(string):
    """
    This function returns the crud action base on the name of the Keyword.
    Ex. get_crud_from_kw("Fusion api add network")
    return action= 'post'
    """
    action = ''
    crud = {'create': 'post',
            'delete': 'delete',
            'update': 'put',
            'edit': 'put',
            'add': 'post',
            'remove': 'delete',
            'get': 'get',
            'refresh': 'put',
            'patch': 'patch',
            'login': 'login'}
    for key in crud:
        if key in string.lower():
            action = crud[key]
            break
        else:
            action = 'none'
    print "crud action name is %s" % action
    return action


def get_resource_from_kw(string):
    """
    This function returns the Fusion resource base on the name of the Keyword.
    Ex. get_resource_from_kw("Fusion api add ethernet-network")
    return resource_name = 'ethernet-network'
    """
    resources = [
        'server profiles',
        'ethernet network',
        'fc network',
        'network set',
        'lig',
        'task',
        'appliance',
        'firmware update',
        'firmware',
        'server hardware',
        'enclosure',
        'sas interconnects'
        'interconnect',
        'users']
    resource_name = ''
    for resource in resources:
        if 'payload' not in string.lower():
            if resource in string.lower():
                if resource == 'enclosure':
                    enclosure_types = [
                        'logical enclosure',
                        'refresh enclosure',
                        'enclosure group']
                    for encl_type in enclosure_types:
                        if encl_type in string.lower():
                            resource_name = encl_type
                            break
                        else:
                            resource_name = 'enclosure'
                elif resource == 'firmware':
                    if 'firmware update' not in string.lower():
                        resource_name = 'firmware'
                    else:
                        resource_name = 'firmware update'
                else:
                    resource_name = resource
    print "keyword name is %s" % resource_name
    return resource_name


def convert_atts_to_str(attr_list):
    """
    This function removes unwanted values from robot test case tags and return a list of strings
    """
    tag_list = []
    tags = str(attr_list)
    tags = tags.replace(
        "u'",
        '').replace(
        "'",
        '').replace(
            "[",
            '').replace(
                "]",
        '')
    tags = tags.split(',')
    for tag in tags:
        tag = tag.lstrip()
        tag_list.append(tag)
    return tag_list


def get_condition_from_list(tag_list):
    """
    This function checks for a -condition- with a robot test case tags and returns a list of condition
    Ex. get_condition_from_list(server_profile-condition-connectionless)
    returns condition = [server_profile, connectionless]
    """
    for tag in tag_list:
        if '-condition-' in tag.lower():
            condition = tag.split('-condition-')
            return condition
    return None


def get_elapsed_time(start_time, end_time):
    """
    This function returns the elapsed time in milliseconds from the REST call response body.
    Ex. get_elapsed_time(2016-01-25T17:24:28.144Z, 2016-01-25T17:25:08.567Z)
    returns elapsed_time = 20902
    """
    start_time = start_time.replace('-', '').replace('T', ' ').replace('Z', '')
    end_time = end_time.replace('-', '').replace('T', ' ').replace('Z', '')
    elapsed_time = robottime.get_elapsed_time(start_time, end_time)
    return elapsed_time


def get_performance_sync_results(action):
    """
    This function returns the synchronous performance results(True or False).
    All synchronous call should be under '200' milliseconds.
    Ex. get_performance_sync_results(300)
    returns False
    """
    synchronous_call = 200  # This is a 200 milliseconds, all sync API call should around this time or under
    if action < synchronous_call:
        return True
    else:
        return False


def get_performance_async_results(resource_name, total_elapsed, condition):
    """
    This function returns the asynchronous performance results(True or False) based on the resource(sever profile, enclosure,etc) and conditions.
    Ex. conditions = [{'name': 'server profile', 'connectionless': 30000, 'gen8_connections_only': 30000]
    Based on the condtions dict defined, a server profile with no connections should take about 30000 milliseconds to complete.
    get_performace_aysnc_results(server profile, 28000, connectionless)
    returns True
    """
    fusion_resources = fusion_conditions.conditions
    for resource in fusion_resources:
        # print "resource condition is %s fusion resource is %s"
        if resource['name'] in resource_name:
            for item in resource:
                if condition[1] == item:
                    crud_time = resource[item]
                    print 'total elapsed is %s, crud_time is %s' % (str(total_elapsed), str(crud_time))
                    if total_elapsed < crud_time:
                        return True
                    else:
                        return False


def get_nodes_details(task_list):
    node_list = []
    for task in task_list:
        node_details = {
            'created': '',
            'modified': '',
            'category': '',
            'name': '',
            'statusUpdate': []}
        if task['percentComplete'] == 100:
            # print"%s /n" % task
            details = ['created', 'modified', 'name', 'category']
            for detail in details:
                if task[detail]:
                    node_details[detail] = task[detail].replace(
                        "u'",
                        '').replace(
                        "'",
                        '')
            for update in task['progressUpdates']:
                if update['statusUpdate']:
                    node_details['statusUpdate'].append(
                        update['statusUpdate']).replace(
                        "u'",
                        '').replace(
                        "'",
                        '')
            node_list.append(node_details)
    return node_list


def get_task_tree_nodes(task_tree, nodes):
    # return a list of the nodes in the task tree that match taskState
    # If taskState is undefined, return all the nodes
    nodes = nodes
    nodes.append(task_tree['resource'])
    if len(task_tree['children']) != 0:
        for childtask in task_tree['children']:
            get_task_tree_nodes(childtask, nodes)
    return nodes


def log_results(time,
                kw_resource,
                crud_action,
                condition,
                elapsedtime,
                fw_version_id,
                is_asynchronous,
                within_threshold,
                asynchronous_time,
                test_case_name,
                dbresults,
                fusionDB):
    if elapsedtime == '':
        elapsedtime = '0'
    # Log results to datafile
    dbresults.append(
        '(kw_resource--%s, crud_action--%s, condition[1]--%s, elapsedtime--%s, asynchronous--%s, sync_results--%s, asynchronous_time--%s, test_case_name--%s)\n' %
        (kw_resource, crud_action, condition, elapsedtime, is_asynchronous, within_threshold, asynchronous_time,
         test_case_name))

    # log_stash_results.append('%s  %s  %s  %s  %s  %s  %s  %s %s %s \n' % log_stash_format['Timestamp'], log_stash_format['Resource'],
    # log_stash_format['Condition'], log_stash_format['Duration'], log_stash_format['IsAsync'], log_stash_format['IsWithinThreshold'], log_stash_format['OVPB'],
    # log_stash_format['OVPB'], log_stash_format['GARFS'],
    # log_stash_format['EncType'])

    # Log results to database
    if write_to_db:
        # Usage: add_complete_record(time, resource, action, condition,
        # duration, fw_version_id, asynchronous=None, within_threshold=None,
        # asynchronous_time=0, test_case=""):
        fusionDB.add_complete_record(time, kw_resource, crud_action, condition, elapsedtime, fw_version_id,
                                     is_asynchronous, within_threshold, asynchronous_time, test_case_name)


def logstash_results(log_stash_format, log_stash_results):
    # Time Action Resource Condition Duration f/w GARFS Async WithinThreshold
    # EncType

    log_stash_results.append('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s \n' % (
        log_stash_format['Timestamp'][0], log_stash_format[
            'Action'], log_stash_format['Resource'],
        log_stash_format['Condition'], log_stash_format[
            'Duration'], log_stash_format['OVPB'], log_stash_format['GARFS'],
        log_stash_format['IsAsync'], log_stash_format['IsWithinThreshold'], log_stash_format['EncType']))


def start_test(name, attrs):
    """
    This function is part of the listener's interface, that listens into when the test case execution starts.
    It has access to the name of the test case, and certain attributes(attrs["id,tags,starttime,etc."] as a dictionary via arguments.
    Please refer to the robotframework user guide on listener interface for more information on the method and arguments.
    At the beginning of each test case execution, it gets tags from the test case and check if it has a 'performance' tag, if it does.
    It'll set the global variable "performance = true". This is needed in end_keyword function also part of the listener's interface, whether to start listening into the keywords execution.
    This is declared as a global variable for other listener's functions to have access during test execution.
    It also set the global variable 'condition' with the conditions from the tags, which will be use other listener's functions(end_keyword).
    """
    tag_list = attrs['tags']
    global performance
    global condition
    global output
    global filename
    global keywordfile
    global dbfile
    global logstash_file
    output = BuiltIn().get_variable_value("${OUTPUTDIR}")
    filename = os.path.join(output, 'log_message.txt')
    keywordfile = os.path.join(output, 'keywordresults.txt')
    dbfile = os.path.join(output, 'dbfile.txt')
    logstash_file = os.path.join(output, 'logstash.txt')
    for tag in tag_list:
        if 'performance' in tag.lower():
            performance = True
    condition = get_condition_from_list(tag_list)
    # print condition
    global test_case_name
    test_case_name = attrs['longname']


def end_keyword(name, attrs):
    """
    This function is part of the listener's interface, that listens into when the keyword ends execution.
    It has access to the name of the keyword, and certain attributes(attrs["elapsed_time,starttime,etc."] as a dictionary via arguments.
    Please refer to the robotframework user guide on listener interface for more information on the method and arguments.
    There are some global attributes that are used to set when a keyword ends or were set prior to this end_keyword function, such performance and condition.
    Performance will be check, right even before it decides to start listening into the keywords, if "performance" is false, it'll won't listen into the keyword.
    Performance is set at the beginning of the start_test and end_test, and so is condition. Other global variables(task_uri, async_elapsed, non_task_resource, kw_resource)
    are used because at the end of  each keyword, the variable needs to be declared and set with certain data from specific keywords, by using global variable,
    we pass certain attributes from the previous executed keywords to the next executed keyword. In this function, it listen into the any keywords that has "fusion api" in the name,
    for each of those keyword, we extract the resource and the crud action from it. If the crud action is not a 'get', it'll get the response body from the assigned variable(${resp}),
    and set that task's uri to the variable task_uri. This task uri is used to ensure it matches with the task uri from "fusion api get task" keyword executed, if it does, and the task state is complete,
    we can get the elapsed time for asynchronous call from the time stamps for the resource in this get task call. All other fusion api keywords without a task's uri associated with it, are synchronous calls
    and this funcitons uses the elapsedtime attribute for the end_keyword to determine the performance results. Any synchronous call under 200 milliseconds is consider a performance failure.
    In the case of asynchronous performance measurements, it listens into the "wait for task" keyword, determine if the keyword pass, if it does, async_elapsed from the get task uri will be used to determine the results.
    The results are written to a database via fusiondb class, it passes arguments like, kw_resource, crud_action, condition[1], attrs['elapsedtime'], 2, False, sync_results.
    Results are also written to a keyword log with the attributes, the arguments for the DB call are also written to dbfile.txt for debugging purposes.
    The files path are written to the pybot execution path.
    Ex. "Fusion api create server profile", keyword will return a task uri, resource, and timestamps that will be needed by Wait for task keyword to gets the performance results.
    """
    fusion_lib = BuiltIn().get_library_instance('FusionLibrary')
    fusionDB = PerformanceDbAccess()
    # print 'output dir is %s' % keywordfile
    global performance
    global kw_resource
    global non_task_resource
    global condition
    global task_uri
    global async_elapsed
    global fw_version_id
    global test_case_name
    global non_get_action
    global log_stash_format
    global async_resource
    global rest_resource
    global rest_crud
    global resp_resource
    global task_details
    global task_list
    crud_action = ''
    status = str(attrs['status']).lower()
    kwname = str(attrs['kwname']).lower()
    current_time = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    fw_version_id = str(1)
    attributes = [
        'kwname',
        'status',
        'assign',
        'elapsedtime',
        'starttime',
        'endtime']
    GARFS = BuiltIn().get_variable_value("${GARFS}")
    OV_PB = BuiltIn().get_variable_value("${OV_PB}")
    EncType = BuiltIn().get_variable_value("${EncType}")
    log_stash_format['EncType'] = EncType
    log_stash_format['OVPB'] = OV_PB
    log_stash_format['GARFS'] = GARFS
    assign_var = None

    if performance:
        results = []
        dbresults = []
        log_stash_results = []
        # Listens into only keywords that has fusion api and if the status is
        # passing
        if 'fusion api' in kwname:
            if 'pass' in status:  #
                # gets the crud action and type of resource from the keyword's
                # name
                print "keyword message crud %s" % rest_crud
                print "keyword message resource %s" % rest_resource
                for arg in attrs['args']:
                    results.append('argument is  %s \n' % (arg))
                crud_action = get_crud_from_kw(kwname)
                kw_resource = get_resource_from_kw(kwname)
                dbresults.append('*** **** **** ***\n')
                dbresults.append('crud_action %s \n' % crud_action)
                dbresults.append('kw_resource %s \n' % kw_resource)

                dbresults.append('Executing Keyword %s \n' % name)
                results.append('*** **** **** ***\n')
                results.append('Executing Keyword %s \n' % name)
                print 'fusion api keyword started'
                # Start writing out the keyword attributes
                for attrib in attributes:
                    print 'writing attributes to file'
                    results.append('%s  %s \n' % (attrib, attrs[attrib]))
                # If the crud action is not a "get", it'll get response body,
                # if it has a uri key, get the uri.
                if crud_action is not 'get' and crud_action is not 'none':
                    print 'crud action is not get'
                    non_get_action = crud_action
                    results.append('not get call')
                    if attrs['assign']:
                        assign_var = attrs['assign'][0]
                        results.append('assign variable is -- %s' % assign_var)
                    if assign_var:
                        post_resp = BuiltIn().get_variable_value(assign_var)
                        if post_resp:
                            results.append('post resp = %s' % post_resp)
                            if 'uri' in post_resp:
                                try:
                                    task_uri = post_resp['uri']
                                    results.append(
                                        'results_path %s \n' %
                                        task_uri)
                                except KeyError:
                                    results.append(
                                        'results_path -- not task uri')
                                    pass
                            elif 'location' in post_resp:
                                try:
                                    task_uri = post_resp['location']
                                    results.append(
                                        'results_path %s \n' %
                                        task_uri)
                                except KeyError:
                                    results.append(
                                        'results_path -- not task uri')
                                    pass
                            elif 'headers' in post_resp:
                                header_dict = post_resp['headers']
                                try:
                                    task_uri = header_dict['Location']
                                    results.append(
                                        'results_path %s \n' %
                                        task_uri)
                                except KeyError:
                                    results.append(
                                        'results_path -- not task uri')
                                    pass
                            results.append('task_uri %s \n' % task_uri)
                            if task_uri:
                                task_details['uri'] = task_uri
                                task_list.append(task_details)
                    if condition is not None:
                        condition_resource = condition[0].replace('_', ' ')
                        if rest_resource == condition_resource:
                            print " kw resource %s match condition resource %s" % (kw_resource, condition_resource)
                            async_resource = rest_resource
                            log_stash_format['Resource'] = rest_resource
                            log_stash_format['Action'] = non_get_action
                            log_stash_format['Timestamp'][0] = str(
                                attrs['starttime'])
                            log_stash_format['Timestamp'][
                                1] = str(attrs['endtime'])
                            log_stash_format['Duration'] = str(
                                attrs['elapsedtime'])
                            log_stash_format['Condition'] = condition[1]
                dbresults.append('duration (%s) \n' % attrs['elapsedtime'])
                # Get synchronous results from keyword's elapsed time
                sync_results = get_performance_sync_results(
                    int(attrs['elapsedtime']))
                log_stash_format['IsWithinThreshold'] = sync_results
                log_stash_format['IsAsync'] = 'False'
                if sync_results:
                    results.append('Performance Pass \n')
                else:
                    results.append('Performance Fail \n')
                dbresults.append('within_threshold (%s) \n' % sync_results)
                # Checks for task not in the resource
                if crud_action is not 'get' and crud_action is not 'none' and 'task' not in kw_resource:
                    print 'no task in keywords'
                    non_task_resource = kw_resource
                    # log_stash_format['Resource'] = non_task_resource
                    print 'non task is %s' % non_task_resource
                    if condition is not None:
                        condition_resource = condition[0].replace('_', ' ')
                        log_stash_format['Condition'] = condition[1]
                        print 'condition resource is %s' % condition_resource
                        if (rest_resource == condition_resource):
                            print 'log result for condition found'
                            log_results(current_time, kw_resource, crud_action, condition[1], attrs['elapsedtime'],
                                        fw_version_id, "0", sync_results, "0", test_case_name, dbresults, fusionDB)
                            logstash_results(
                                log_stash_format,
                                log_stash_results)

                        else:
                            print 'log result for condition not found'
                            if kw_resource:
                                log_results(current_time, kw_resource, crud_action, condition[1], attrs['elapsedtime'],
                                            fw_version_id, "0", sync_results, "0", test_case_name, dbresults, fusionDB)
                    else:
                        print 'log result for None in condition'
                        if kw_resource:
                            log_results(current_time, kw_resource, crud_action, 'None', attrs['elapsedtime'],
                                        fw_version_id, "0", sync_results, "0", test_case_name, dbresults, fusionDB)

                            # Write saved logs to files
                write_results(dbfile, dbresults, 'a')
                write_results(keywordfile, results, 'a')
                write_results(logstash_file, log_stash_results, 'a')

        elif ('wait for task' or 'wait For task_enc' or 'wait for task2') in kwname:
            task_results = []
            if 'pass' in status:
                print 'wait for task passed'
                task_tree = fusion_lib.fusion_api_get_task(
                    uri=task_uri,
                    param='?view=tree')
                nodes = []
                results.append(
                    'non_task_resource---> %s \n' %
                    non_task_resource)
                task_results.append('*** **** **** ***\n')
                task_results.append(
                    'Executing Keyword %s on Fusion resource %s \n' %
                    (name, non_task_resource))
                print 'loggin results and attributes'
                for attrib in attributes:
                    task_results.append('%s  %s \n' % (attrib, attrs[attrib]))
                write_results(keywordfile, results, 'a')
                write_results(dbfile, dbresults, 'a')
                write_results(logstash_file, log_stash_results, 'a')
                task_list = []


def end_test(name, attrs):
    """
    This function is part of the listener's interface, that listens into when the test case ends execution.
    It has access to the name of the keyword, and certain attributes(attrs["id,tags,starttime,etc."] as a dictionary via arguments.
    Please refer to the robotframework user guide on listener interface for more information on the method and arguments.
    The function will set the global variable performance to false and condition back to empty at the end of every test and also write the results to a testcaseresults.txt for debugging purposes.
    """
    test_results = []
    global performance
    global condition
    test_results.append('Test %s completed executing \n' % name)
    attributes = [
        'longname',
        'status',
        'elapsedtime',
        'starttime',
        'endtime',
        'tags']
    if performance:
        for attrib in attributes:
            test_results.append('%s  %s \n' % (attrib, attrs[attrib]))
        test_results.append(
            'Test Elapsed time keyword is %s \n' %
            attrs['elapsedtime'])
        write_results(filename, test_results, 'a')
    performance = False
    condition = ''


def log_message(message):
    test_results = []
    results = []
    log_stash_results = []
    global rest_resource
    global rest_crud
    global resp_resource
    global log_stash_format
    global condition
    global performance
    global kw_resource
    global non_task_resource
    global task_uri
    global async_elapsed
    global fw_version_id
    global test_case_name
    global non_get_action
    global async_resource
    global task_details
    global task_list
    crud_action = ''
    current_time = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    fw_version_id = str(1)
    if performance:
        if message:
            mess = message['message']
            if 'URL' in mess:
                match = re.findall(
                    'URL\s([A-Z]+)\s\https:\/\/([^\s\.]+\.[^\s]{2,}|www\.[^\s]+\.[^\s]{2,})',
                    mess)
                try:
                    test_results.append('Crud is %s \n' % match[0][0])
                    rest_crud = match[0][0]
                    rest_resource = match[0][1].split('/')
                    rest_resource = rest_resource[2].split('?')
                    rest_resource = rest_resource[0].replace('-', ' ')
                    test_results.append(
                        'rest_resource---- is %s \t' %
                        rest_resource)
                    test_results.append('mess---- is %s \t' % mess)
                except IndexError:
                    pass
            if 'Request Body' in mess:
                request_body = json.loads(mess.split('Request Body')[1])
            if 'Response Body' in mess:
                resp_headers = json.loads(
                    mess.split('Response Headers')[1].split('Response Body')[0])
                for header in resp_headers:
                    test_results.append('resp_headers is %s \n' % header)
                response_body = json.loads(
                    mess.split('Response Headers')[1].split('Response Body')[1])
                for body in response_body:
                    test_results.append('response_body is %s \n' % body)
                location = re.search(
                    '"location": "(\/[a-z,0-9,/]+[A-Z,0-9,-]+)',
                    mess)
                created = re.search(
                    '"created": "([0-9+,0-9,-]+T[0-9,0-9,:]+.[0-9]+Z)',
                    mess)
                modified = re.search(
                    '"modified": "([0-9+,0-9,-]+T[0-9,0-9,:]+.[0-9]+Z)',
                    mess)
                category = re.search('"category":\s"([a-z]+)"', mess)
                if 'category' in response_body and response_body[
                        'category'] == 'tasks':
                    test_results.append(
                        'computedPercentComplete is %s \n' %
                        response_body['computedPercentComplete'])
                    test_results.append(
                        'category is %s \n' %
                        response_body['category'])
                    if response_body['computedPercentComplete'] == 100:
                        async_elapsed = get_elapsed_time(
                            response_body['created'].replace(
                                '-',
                                '').replace(
                                'T',
                                ' ').replace(
                                'Z',
                                ''),
                            response_body['modified'].replace('-', '').replace('T', ' ').replace('Z', ''))
                        associated_resource = response_body[
                            'associatedResource']
                        test_results.append(
                            'computedPercentComplete is %s \n' % response_body['computedPercentComplete'])
                        test_results.append(
                            'resource type is %s \n' %
                            associated_resource['resourceCategory'])
                        test_results.append(
                            'resource name is %s \n' %
                            associated_resource['resourceName'])
                        test_results.append(
                            'task uri is %s \n' %
                            response_body['uri'])
                        test_results.append(
                            'async_elapsed is %s \n' %
                            async_elapsed)
                        results.append(
                            'computedPercentComplete is %s \n' %
                            response_body['computedPercentComplete'])
                        results.append(
                            'resource type is %s \n' %
                            associated_resource['resourceCategory'])
                        results.append(
                            'resource name is %s \n' %
                            associated_resource['resourceName'])
                        results.append(
                            'task uri is %s \n' %
                            response_body['uri'])
                        results.append(
                            'async_elapsed is %s \n' %
                            async_elapsed)
                        log_stash_format['Timestamp'][0] = response_body['created'].replace('-', '').replace('T',
                                                                                                             ' ').replace(
                            'Z', '')
                        log_stash_format['Timestamp'][1] = response_body['modified'].replace('-', '').replace('T',
                                                                                                              ' ').replace(
                            'Z', '')
                        log_stash_format['Duration'] = async_elapsed
                        async_resource = associated_resource[
                            'resourceCategory'].replace('-', ' ')
                        log_stash_format['Resource'] = async_resource
                        log_stash_format['Action'] = rest_crud
                        log_stash_format['IsAsync'] = 'True'
                        if condition is not None:
                            condition_resource = condition[0].replace('_', ' ')
                            async_results = get_performance_async_results(
                                async_resource,
                                async_elapsed,
                                condition)
                            log_stash_format[
                                'IsWithinThreshold'] = async_results
                            log_stash_format['Condition'] = condition[1]
                            if async_results:
                                results.append('Performance Pass \n')
                            else:
                                results.append('Performance Fail \n')
                        if async_resource == condition_resource:
                            print " async_resource %s match with task_resp %s condition_resource" % (
                                async_resource, condition_resource)
                            logstash_results(
                                log_stash_format,
                                log_stash_results)
                if category:
                    resp_resource = category.group(1)
                    print "log message resource %s" % resp_resource
                if location:
                    location = location.group(1)
                    # test_results.append('location is %s \n' % location)
                if created:
                    created = created.group(1)
                    # test_results.append('non-task created is %s \n' % created)
                if modified:
                    modified = modified.group(1)
                    # test_results.append('non-task modified is %s \n' % modified)

                task_percent = re.search(
                    '"computedPercentComplete":\s([0-9]+)',
                    mess)
                if task_percent:
                    task_percent = task_percent.group(1)
                    # test_results.append('computedPercentComplete is %s \n' % task_percent)
                    # test_results.append('task created is %s \n' % created)
                    # test_results.append('task modified is %s \n' % modified)
                    # test_results.append('category is %s \n' % resp_resource)
            write_results(filename, test_results, 'a')
            write_results(keywordfile, results, 'a')
            write_results(logstash_file, log_stash_results, 'a')
