import json
from OVS11171_Regression_Data import *

Rack_compare_Types = ['Basic', 'Full']
BL_compare_types = ['Basic', 'Full']
Syn_compare_types = ['Basic', 'Full']


def ordered(obj):
    #    Author : Yogeshwar.V
    #    This Method will sort a given dictionary when called.
    #    The argument "obj" should obtain a dictionary object when called
    #    This Method returns an object in sorted manner

    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj


def get_json_from_raw_data(rawdata):
    #    Author : Yogeshwar.V
    #    This Method will remove the unwanted header details and collect only the dictionary object from the raw data.

    return rawdata[rawdata.index('{'):]


def find_registry_details(rawdata):
    #    Author : Yogeshwar.V
    #    This Method will receive the raw data and convert it to dictionary format, returns attribute_Registry, cpu_Family and version

    substring = get_json_from_raw_data(rawdata)
    diction = json.loads(substring)
    attribute_Reg = diction.get("AttributeRegistry")
    # length of the string Biosattribute_Registry is 21
    cpu_Family = attribute_Reg[21:attribute_Reg.index('.')]
    version_Info = attribute_Reg[attribute_Reg.index('.') + 1:]
    return attribute_Reg, cpu_Family, version_Info


def string_to_dictionary(raw_Data):
    #    Author : Yogeshwar.V
    #    This Method will receive the raw data and simply convert it to dictionary format and returns the same

    return json.loads(raw_Data)


def update_to_dictionary(dictionx, keyx, valx):
    #    Author : Yogeshwar.V
    #    This Method will receive the dictionary object, key name and value as input.
    #    updates the given dictionary for the given key with the given value, where the values is set as a List object in the dict.

        dictionx[keyx] = [valx]


def rack_compare(compare_Type, diction1, diction2):
    #    Author : Yogeshwar.V
    #    This Method will receive the three arguments --> "comparison type", dictionary1 and dictionary2 object
    #    This returns boolean value as true if the comparison of rack data resulted in equality otherwise returns false.

    if compare_Type == Rack_compare_Types[0]:
        if any(diction1[i] != diction2[i] for i in Rack_basic_compare_fields):
            return False
        else:
            return True
    elif compare_Type == Rack_compare_Types[1]:
        return ordered(diction1) == ordered(diction2)


def bl_compare(compare_Type, diction1, diction2):
    #    Author : Yogeshwar.V
    #    This Method will receive the three arguments --> "comparison type", dictionary1 and dictionary2 object
    #    This returns boolean value as true if the comparison of BL data resulted in equality otherwise returns false.

    if compare_Type == BL_compare_types[0]:
        if any(diction1[i] != diction2[i] for i in BL_basic_compare_fields):
            return False
        else:
            return True
    elif compare_Type == BL_compare_types[1]:
        return ordered(diction1) == ordered(diction2)


def syn_compare(compare_Type, diction1, diction2):
    #    Author : Yogeshwar.V
    #    This Method will receive the three arguments --> "comparison type", dictionary1 and dictionary2 object
    #    This returns boolean value as true if the comparison of Syn data resulted in equality otherwise returns false.

    if compare_Type == Syn_compare_types[0]:
        if any(diction1[i] != diction2[i] for i in Syn_basic_compare_fields):
            return False
        else:
            return True
    elif compare_Type == Syn_compare_types[1]:
        return ordered(diction1) == ordered(diction2)


def compare_dictionary(server_Type, compare_Type, diction1, diction2):
    #    Author : Yogeshwar.V
    #    This Method will receive the four arguments --> "server_type", "comparison type", dictionary1 and dictionary2 objects
    #    This returns boolean value as true if the comparison resulted in equality otherwise returns false.

    server_types = {'Rack': rack_compare,
                    'BL': bl_compare,
                    'Syn': syn_compare}
    return server_types[server_Type](compare_Type, diction1, diction2)
