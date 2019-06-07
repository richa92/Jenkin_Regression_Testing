from robot.api import logger


def list_of_devices(response, device_type):
    logger.console('Generating list of devices.')
    instances = response['List'][0]['EntityInstance']
    instance_names = []
    for instance in instances:
        if instance['type'] == device_type:
            instance_names.append(instance['name'])
    return instance_names


def list_of_types(response):
    instances = response['List'][0]['SchematicType']
    instance_types = []
    for instance in instances:
        if instance['type'] not in instance_types:
            instance_types.append(instance['type'])
    return instance_types


def list_of_verbs(response):
    verbs = []
    if len(response['List'][0]) is not 0:
        verbs = response['List'][0]['String']
    return verbs


def list_of_attributes(response):
    attributes = []
    if len(response['List'][0]) is not 0:
        attributes = response['List'][0]['Attribute']
    for entry in attributes:
        logger.console('     ' + entry['type'] + ' ' + entry['name'])
    return attributes


def list_of_one_hack(verbs):
    verb_list = verbs
    if type(verbs) is not list:
        verb_list = []
        verb_list.append(verbs)
    return verb_list
