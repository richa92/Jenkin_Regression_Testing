#from FusionLibrary.api.common.request import HttpVerbs
#from FusionLibrary.api.networking.logical_interconnect_groups import LogicalInterconnectGroup
import sys
import re
#sys.path.append('c:/rg-fusion/fusion/tests/wpst_crm/resources')

#from voluptuous import *


class Users(object):
    def __init__(self, *args, **kwargs):
        self.version = '3.00'
        self.users = [{'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin',
                       'roles': ['Server administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003',
                       'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
                      {'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin',
                       'roles': ['Network administrator'], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003',
                       'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
                      {'userName': 'Backupadmin', 'password': 'Backupadmin', 'fullName': 'Backupadmin',
                       'roles': ['Backup administrator'], 'emailAddress': 'backup@hp.com',
                       'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
                      {'userName': 'Noprivledge', 'password': 'Noprivledge', 'fullName': 'Noprivledge',
                       'roles': ['Read only'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003',
                       'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'}
                      ]
        if kwargs:
            if kwargs['x'] == 1:
                return 'some ui version'
        else:
            return self.users

users = Users(x=1)

x = [{'bay': 3, 'type': 'VC Flex-10/10D Module'}]


def _make_interconnect_map_template_dict(interconnectMapTemplate):
    template = {'interconnectMapEntryTemplates':
               [{'logicalLocation':
                    {'locationEntries':
                       [{'type': 'Bay', 'relativeValue': v['bay']},
                        {'type': 'Enclosure', 'relativeValue': v.get('enclosure', 1)}]},
                      'permittedInterconnectTypeUri': v['type'],
                      'enclosureIndex': v.get('enclosureIndex', 1)
                      } for i, v in enumerate(interconnectMapTemplate)],
                    }
    return template

y = _make_interconnect_map_template_dict(x)

print y




def cmpr(exp, act):
    pattern = re.compile(str(exp))
    result = re.match(pattern, act)
    return result

exp = {'CRM_INVALID_UPLINK_SET_PORT':
                      {'type': 'regex',
                       'taskErrors':
                           [{"data": {},
                             "details": "",
                             "errorCode": "CRM_INVALID_UPLINK_SET_PORT",
                             "errorSource": "logical-interconnect-groups",
                             "message": 'Invalid uplink-set: Port: \\d+ for interconnect-type: .* is not an uplink port.',
                             "nestedErrors": [],
                             "recommendedActions": ["Please retry the operation with a valid port.", "other"]}
                            ]},
                  }
act = {'CRM_INVALID_UPLINK_SET_PORT':
                      {'type': 'regex',
                       'taskErrors':
                           [{"data": {},
                             "details": "",
                             "errorCode": "CRM_INVALID_UPLINK_SET_PORT",
                             "errorSource": "logical-interconnect-groups",
                             "message": 'Invalid uplink-set: Port: A for interconnect-type: 9 is not an uplink port.',
                             "nestedErrors": [],
                             "recommendedActions": ["Please retry the operation with a valid port.", "other"]}
                            ]},
                  }


def drill(d, e):
    if isinstance(d, dict):
        # check type
        if type(d) != type(e):
            message = 'Type mismatch: \nExpected: %s \n  Actual: %s' % (type(d), type(e))
            raise Exception(message)
        # check keys in both
        elif d.keys() != e.keys():
            message = 'key mismatch: %s' % (list(set(d.keys()) - set(e.keys())))
            raise Exception(message)
        for (k, v), (k1, v1) in zip(d.items(), e.items()):
            if isinstance(v, dict):
                print "a {0} : {1} : {2}".format(k, 'dict', v)
                print "b {0} : {1} : {2}".format(k1, 'dict', v1)
                drill(v, v1)
            elif isinstance(v, list):
                print "a {0} : {1} : {2}".format(k, 'list', v)
                print "b {0} : {1} : {2}".format(k1, 'list', v1)
                drill(v, v1)
            if isinstance(v, str):
                print "a {0} : {1} : {2}".format(k, 'str', v)
                print "b {0} : {1} : {2}".format(k1, 'str', v1)
                result = cmpr(v, v1)
                if result is None:
                    message = "Regex Mismatch: \nExpected:{0} \n  Actual:{1}".format(v, v1)
                    raise Exception(message)

    elif isinstance(d, list):
        if type(d) != type(e):
            message = 'Type mismatch: \nExpected: %s \n  Actual: %s' % (type(d), type(e))
            raise Exception(message)
        # check length in both
        if len(d) != len(e):
            message = 'key mismatch: %s' % (list(set(d) - set(e)))
            raise Exception(message)
        for (i, v), (i1, v1) in zip(enumerate(d), enumerate(e)):
            if isinstance(v, dict):
                print "a {0} : {1}".format(v, 'dict')
                print "b {0} : {1}".format(v1, 'dict')
                drill(v, v1)
            elif isinstance(v, list):
                print "a {0} : {1}".format(v, 'list')
                print "b {0} : {1}".format(v1, 'list')
                drill(v, v1)
            else:
                print "[%i] %s" % (i, v)
                print "[%i] %s" % (i1, v1)
                result = cmpr(v, v1)
                if result is None:
                    message = "Regex Mismatch: \nExpected:{0} \nActual:{1}".format(v, v1)
                    raise Exception(message)

if isinstance(exp, dict):
    if type(act) == type(exp):
        print "they match"
        drill(exp, act)
    else:
        print "wrong data types, can't compare"
else:
    print "Error"

print 'wait'

"""
def drill(d):
    x = ''
    if isinstance(d, dict):
        for k, v in d.iteritems():
            #print "{0} : {1}".format(k, v)
            #print "{0}:".format(k)
            if isinstance(v, dict):
                print "{0} : {1}".format(k, 'dict')
                drill(v)
            elif isinstance(v, list):
                print "{0} : {1}".format(k, 'list')
                drill(v)
            if isinstance(v, str):
                print "{0} : {1}".format(k, v)
                # TODO: compare with regex
    elif isinstance(d, list):
        for i, v in enumerate(d):
            if isinstance(v, dict):
                print "{0} : {1}".format(v, 'dict')
                drill(v)
            elif isinstance(v, list):
                print "{0} : {1}".format(v, 'list')
                drill(v)
            else:
                print "[%i] %s" % (i, v)
                # TODO: compare with regex



#for (k1, v1), (k2, v2) in act.iteritems(), exp.iteritems():
#    print k1, v1, k2, v2

def drill(d):
    if isinstance(d, dict):
        drill_dict(d)
    elif isinstance(d, list):
        drill_list(d)

def drill_dict(d):
    if isinstance(d, dict):
        for k, v in d.iteritems():
            print k
            if isinstance(v, dict):
                drill_dict(v)
            elif isinstance(v, list):
                drill_list(v)
            elif isinstance(v, str):
                exp = v
                print "{0} : {1}".format(k, v)

def drill_list(d):
    if isinstance(d, list):
        for i in d:
            if isinstance(i, dict):
                drill_dict(i)
            elif isinstance(i, list):
                drill_list(i)
            else:
                print "- %s" % i






for key in valDict:
    if not valDict[key]:
        continue
    # logger._log_to_console_and_log_file('key: %s' % (key))
    keyDict = {'key': key, 'expected': valDict[
        key], 'actual': respDict[key], 'success': True}
    if key in respDict:
        pattern = re.compile(str(valDict[key]))
        # if not re.search(str(valDict[key]), str(respDict[key])):
        # t = re.compile('(?i)Warning|Unknown|Terminated|Killed|Error|Completed')

        if not re.search(pattern, str(respDict[key])):

            success = False
            keyDict['success'] = False
    else:
        success = False
        keyDict['success'] = False
    keys.append(keyDict)


fcoe_ranges = {'fcoe-range32a': {'prefix': 'fcoe-', 'suffix': 'a', 'start': 1001, 'end': 1032},
               'fcoe-range32b': {'prefix': 'fcoe-', 'suffix': 'b', 'start': 1001, 'end': 1032},
               'fcoe-range32c': {'prefix': 'fcoe-', 'suffix': 'c', 'start': 1001, 'end': 1032},
               'fcoe-range32d': {'prefix': 'fcoe-', 'suffix': 'd', 'start': 1001, 'end': 1032},
               'fcoe-range33': {'prefix': 'fcoe-', 'suffix': '', 'start': 1001, 'end': 1033},
               'fcoe-range30a': {'prefix': 'fcoe-', 'suffix': 'a', 'start': 1001, 'end': 1030},
               'fcoe-range128': {'prefix': 'fcoe-', 'suffix': '', 'start': 1001, 'end': 1128},
               'fcoe-range-delete-20': {'prefix': 'fcoe-', 'suffix': '', 'start': 1109, 'end': 1128}
               }

def rlist(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist

x = rlist(**fcoe_ranges['fcoe-range32a'])
y = rlist(1,20)

icmap = [{'bay': 3, 'type': 'HP FlexFabric 40GbE Module - EdgeSafe/Virtual Connect version', 'enclosureIndex': 1},
         {'bay': 6, 'type': 'HP FlexFabric 40GbE Module - EdgeSafe/Virtual Connect version', 'enclosureIndex': 1},
         ]

for i, v in enumerate(icmap):
    if 'bay' in v: print v



#fc = HttpVerbs()

#LIG = LogicalInterconnectGroup(fc)
#x = LIG.make_body(name='x', interconnectMapTemplate=icmap)







x = {v['bay'] for i, v in enumerate(icmap)}
y = {v['enclosure'] for i, v in enumerate(icmap)}

for i, v in enumerate(icmap):
    print v['bay']
    print v['enclosure']


template = {'interconnectMapEntryTemplates':
            [{'logicalLocation':
              {'locationEntries':
               [{'type': 'Bay', 'relativeValue': v['bay']},
                {'type': 'Enclosure', 'relativeValue': v['enclosure']}]},
              'permittedInterconnectTypeUri': v['type'],
              } for i, v in enumerate(icmap)],
            }


print template

"""
