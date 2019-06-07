class Errors(object):
    taskErrors = {'CRM_INVALID_UPLINK_SET_PORT':
                      {'type': 'regex',
                       'taskErrors':
                           [{"data": {},
                             "details": "",
                             "errorCode": "CRM_INVALID_UPLINK_SET_PORT",
                             "errorSource": "logical-interconnect-groups",
                             "message": "Invalid uplink-set: Port: \\d+ for interconnect-type: .* is not an uplink port.",
                             "nestedErrors": [],
                             "recommendedActions": ["Please retry the operation with a valid port.", "other"]}
                            ]},
                  }
