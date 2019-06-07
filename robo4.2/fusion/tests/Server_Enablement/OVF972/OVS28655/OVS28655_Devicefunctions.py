import json


"""Method: purpose is to take raw data from ris call and Converts the raw data to Jason format and returns json format dictionary
input: Raw data from ris call output data is given as input to this method
returns: returns the dictionary format for comparing the data with ilo and OV
"""


def get_json_data_from_ilo_output(rawdata):
    json_string = rawdata[rawdata.index('{'):]
    json_acceptable_string = json_string.replace("'", "\"")
    json_dict = json.loads(json_acceptable_string)
    return json_dict

"""Methad: purpose is to slice the unwanted data from RIS call and take the data which can be used for futher consumption to fetch the required data and process
Input:raw data from ris call
Returns :the data in the dictionary format"""


def get_json_data_from_ov_output(rawdata):
    rawdata[rawdata.index('{'):]


"""Method: purpose is to slice the unwanted data from RIS call and take the data which can be used for futher consumption to fetch the required data and process
Input:raw data from ris call
Returns :the data in the dictionary format for data processing """


def getjsonovfromrawdata1(rawdata):
    rawdata[rawdata.index('['):]
