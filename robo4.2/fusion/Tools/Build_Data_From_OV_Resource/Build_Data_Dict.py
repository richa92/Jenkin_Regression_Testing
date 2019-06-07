from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.utilitylib import logging as logger

import re
import json
import Build_data


def Fusion_API_Make_Pretty_Json_File(self, dataDict, fileName):

    pretty_json = json.dumps(dataDict, indent=4, sort_keys=True)

    fileName = (fileName + ".py")
    json_file = open(fileName, 'w')
    json_file.write(pretty_json)
    json_file.close()


class Build_Data_Dict(object):

    def __init__(self):
        self.fusionlib = BuiltIn().get_library_instance('FusionLibrary')

    def get(self, template, response, uriCache={}, wordy=False):
        
        dataDict = {}
        restTypeWarnings = {}

        def short_name_lookup(rest_type):

            if rest_type in Build_data.short_names:
                return Build_data.short_names[rest_type]
            else:
                return "TYPE UNKNOWN"

        def datadict_remove(item, value):
            if item not in Build_data.datadict_remove_if:
                return None
            else:
                if Build_data.datadict_remove_if[item][0] == value:
                    return Build_data.datadict_remove_if[item][1]
                else:
                    return None
            
        for key in template.keys():
            if wordy:
                logger._log_to_console_and_log_file("Key : %s" % key)

            # if the response doesn't contain the key, then ignore it from the template
            if key not in response:
                continue

            # if the response is None then the data dict should be set to None too
            if response[key] is None:
                dataDict[key] = None
                continue

            if isinstance(template[key], list):
                if key in response:
                    dataDict[key] = []
                    for i in xrange(0, len(response[key])):
                        if isinstance(response[key][i], dict):
                            sub_dict = self.get(template[key][0], response[key][i], uriCache, wordy)
                            dataDict[key].append(sub_dict)                       
                        else:
                            miniDict = {"x": response[key][i]}
                            miniTemp = {"x": "x"}  # actually could be any dict
                            miniDict = self.get(miniTemp, miniDict, uriCache, wordy)
                            dataDict[key].append(miniDict["x"])
                    continue
                else:
                    if wordy:
                        logger._log_to_console_and_log_file("Ignoring %s from template list as it is not in response." % key)
                    continue
            
            if isinstance(template[key], dict):
                if key in response:
                    sub_dict = self.get(template[key], response[key], uriCache, wordy)
                    dataDict[key] = sub_dict
                continue
                
            if key in response:
                logger._log_to_console_and_log_file("t : %s" % template[key])
                logger._log_to_console_and_log_file("r : %s" % response[key])
                logger._log_to_console_and_log_file("type: %s" % type(response[key]))
                if isinstance(response[key], str) or isinstance(response[key], unicode):
                    matchObj = re.search(r'/rest/(.*)/', response[key], re.I)
                    if matchObj:
                        uri = response[key]

                        if uri in uriCache:
                            if wordy:
                                logger._log_to_console_and_log_file("URI Cache already has %s" % uri)
                                logger._log_to_console_and_log_file("URI Cache name %s" % uriCache[uri])
                            dataDict[key] = uriCache[uri]
                            continue
                        else:
                            rest_type = matchObj.group(1)

                            if rest_type == "connection-templates":  # need special lookup for connecton-templates
                                if wordy:
                                    logger._log_to_console_and_log_file("connection-template.  Lookup bandwidth.")
                                connectionTemplate = self.fusionlib.fusion_api_get_connection_templates(response[key])
                                dataDict['bandwidth'] = connectionTemplate['bandwidth']
                                continue

                            shortname = short_name_lookup(rest_type)

                            if shortname == "TYPE UNKNOWN" and rest_type not in restTypeWarnings:
                                logger.warn("Build Data Dict WARNING: short_name{} doesn't contain rest type: %s" % rest_type)
                                logger.warn("Add to Build_data.py if this rest call should be defined for resource name lookup.")
                                logger.warn("")
                                restTypeWarnings[rest_type] = "cached"
                                continue
                          
                            if wordy:
                                logger._log_to_console_and_log_file("Need to get name from URI and build expected: %s" % uri)
                                logger._log_to_console_and_log_file("Type: %s" % rest_type)
                                logger._log_to_console_and_log_file("Short Name: %s" % shortname)
                            
                            resp = self.fusionlib.fusion_api_get_resource(uri)
                            if 'name' in resp:
                                name = resp['name']
                            else:
                                # name = "NAME NOT OBTAINED: Item to be ignored"
                                logger.warn("Build Data Dict WARNING: Name for uri not obtained, item to be ignored.  Key: %s, URI: %s" % (key, uri))
                                logger.warn("")
                                continue
                            if wordy:
                                logger._log_to_console_and_log_file("Uri name obtained: %s" % name)                       
                            
                            # add to uriCache so we don't have to call GET every time
                            uriCache[uri] = (shortname + name)

                            dataDict[key] = (shortname + name)
                            continue
                        
                # otherwise just copy
                dataDict[key] = response[key]
            else:
                if wordy:
                    logger._log_to_console_and_log_file("Ignoring %s from template as it is not in response." % key)

            # some items should be removed from the dataDict depending on another item.  For example if macType is
            # virtual, then remove mac from the dataDict.  See Build_data.datadict_remove_if
            keys_to_remove = []
            for key in dataDict.keys():
                if wordy:
                    logger._log_to_console_and_log_file("Check Key for datadict_remove_if: key=%s, value=%s." % (key, dataDict[key]))

                remove = datadict_remove(key, dataDict[key])
                if (remove is not None):
                    if (isinstance(remove, str) and remove in dataDict.keys()):
                        logger._log_to_console_and_log_file("Will remove Key from dataDict: %s" % remove)
                        keys_to_remove.append(remove)
                    else:  # it is a tuple
                        for rm in remove:
                            if rm in dataDict.keys():
                                logger._log_to_console_and_log_file("Will remove Key from dataDict: %s" % rm)
                                keys_to_remove.append(rm)

            for key in keys_to_remove:
                del dataDict[key]

        return dataDict
