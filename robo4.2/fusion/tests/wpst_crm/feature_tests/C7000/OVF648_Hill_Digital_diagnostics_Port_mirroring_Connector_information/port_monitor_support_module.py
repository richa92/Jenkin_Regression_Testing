'''

This module is used to include some helper function for Port Monitoring

'''


def set_networkuri_lig(data_variable, get_output):
    '''
    Build the network URI's from the network Name and form the
    LIG body
    '''
    temp = data_variable
    for i in range(len(temp['uplinkSets'])):
        for j in range(len(temp['uplinkSets'][i]['networkUris'])):
            for x in get_output['members']:
                if temp['uplinkSets'][i]['networkUris'][j] == x['name']:
                    temp['uplinkSets'][i]['networkUris'][j] = x['uri']
    return temp


def validate_port_monitor_in_icm(port_no, output):
    '''
    This method is used to validate the port monitor is configured successfully in ICM.
    '''
    try:
        flag = False
        for i in output.splitlines():
            if "Mirror" in i.split() and port_no == i.split()[0]:
                result = i.split()[0]
                flag = True
        if flag:
            return True
        else:
            return flag
    except Exception as e:
        return e


def validate_mirror_port_status_in_icm(output, state):
    '''
    This method is used to validate the mirror port status in ICM.
    '''
    try:
        flag = False
        for i in output.splitlines():
            if "Mirror Port" in i:
                result = i.split()[2]
                if result == state:
                    flag = True
        if flag:
            return True
        else:
            return flag
    except Exception as e:
        return e


def validate_flow_command_in_icm(output):
    '''
    This method is used to validate the mirror port status in ICM.
    '''
    try:
        flag = False
        for i in output.splitlines():
            if "fm_ingr" in i:
                return i
                flag = True
        if flag:
            return True
        else:
            return flag
    except Exception as e:
        return e
