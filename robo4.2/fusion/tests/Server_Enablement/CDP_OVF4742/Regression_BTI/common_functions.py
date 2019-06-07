import json


def string_to_dictionary(raw_data):
    #    Author : Yogeshwar.V
    #    This Method will receive the raw data and simply convert it to dictionary format and returns the same

    return json.loads(raw_data)
