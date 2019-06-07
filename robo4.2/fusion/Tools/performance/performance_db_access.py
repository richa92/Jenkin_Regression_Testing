#!/usr/bin/env python
import requests
import json

##############################################################

# This class implements python functions which interact with the
# OneViewPerformanceDB. This allows the Performance Listener to
# retrieve and insert data into the database via REST API calls.

# Database: http://oneviewperformance.rsn.rdlabs.hpecorp.net:8080/

# Usage Example:
#     from performance_db_access import PerformanceDbAccess
#     import datetime;
#     db = PerformanceDbAccess()
#
#     response = db.get_performance_records();
#
#     timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S");
#     resp = db.add_performance_record(timestamp, "1", 506, "1");

##############################################################


class PerformanceDbAccess():

    def __init__(self):
        self.username = 'admin'
        self.password = 'hpvse123'
        self.url = 'http://16.114.189.182:8080/'
        self.performance_url = self.url + 'performance_records/'
        self.resource_url = self.url + 'fusion_resources/'
        self.firmware_url = self.url + 'firmware_versions/'

    def update_url(self, url):
        self.url = url

    #####################################################
    # Performance Results
    #####################################################

    def get_performance_records(self):
        response = requests.get(self.performance_url, auth=(self.username, self.password))
        return response

    def get_performance_record(self, id):
        response = requests.get(self.performance_url + str(id) + '/', auth=(self.username, self.password))
        return response

    # curl -H 'Content-Type: application/json; Accept: application/json; indent=4' -X POST -u admin:hpvse123 --data '{"resource_id":"http://16.114.187.221:8080/fusion_resources/1/","duration":200,"fw_version_id":"http://16.114.187.221:8080/firmware_versions/1/"}' http://16.114.187.221:8080/performance_records/
    def add_performance_record(self, time, resource_id, duration, fw_version_id, asynchronous=None, within_threshold=None):
        # TODO: Validate input
        data = {"time": str(time),
                "resource_id": self.resource_url + str(resource_id) + '/',
                "duration": int(duration),
                "fw_version_id": self.firmware_url + str(fw_version_id) + '/',
                "is_asynchronous": asynchronous,
                "within_threshold": within_threshold,
                }
        print "Adding PerformanceRecord: " + json.dumps(data)
        response = requests.post(self.performance_url, auth=(self.username, self.password), data=data)
        if response.status_code != 201:
            print "[ PERFORMANCE ] Failed to add performance record"
            print response.content
        else:
            print "[ PERFORMANCE ] Successfully added performance record."
        return response

    # UTILITY FUNCTIONS
    # This is the primary function used by the listener to insert data into the db.
    def add_complete_record(self, time, resource, action, condition, duration, fw_version_id, asynchronous=None, within_threshold=None, asynchronous_time=0, test_case=""):
        resource_id = self.get_resource_id(resource, action, condition, test_case)
        if resource_id is None:
            resource_id = self.add_fusion_resource(resource, action, condition, asynchronous_time, test_case)
        response = self.add_performance_record(time, resource_id, duration, fw_version_id, asynchronous, within_threshold)
        return response

    #####################################################
    # Performance Requrements/Resources
    #####################################################

    def get_fusion_resources(self, url=None):
        if url is None:
            url = self.resource_url
        response = requests.get(url, auth=(self.username, self.password))
        return response

    def get_fusion_resource(self, id):
        response = requests.get(self.resource_url + str(id) + '/', auth=(self.username, self.password))
        return response

    def add_fusion_resource(self, resource, action, condition, asynchronous_time=0, test_case=""):
        print "Add_Fusion_Resource"
        data = {"resource": resource,
                "action": action,
                "condition": condition,
                "asynchronous_time": asynchronous_time,
                "test_case": test_case
                }
        print "Adding Resource: " + json.dumps(data)
        response = requests.post(self.resource_url, auth=(self.username, self.password), data=data)
        content = json.loads(response.content)
        if response.status_code != 201:
            print "Failed to add new resource"
            print content
            return None
        print "Added new resource! (%s)" % content['id']
        return content['id']

    # UTILITY FUNCTIONS

    def get_all_fusion_resources(self):
        resources = []
        response = self.get_fusion_resources()
        content = json.loads(response.content)
        resources.extend(content['results'])
        print "NEXT: '" + str(content['next']) + "'"
        while (str(content['next']) != 'None'):
            response = self.get_fusion_resources(content['next'])
            content = json.loads(response.content)
            resources.extend(content['results'])
            print "NEXT: '" + str(content['next']) + "'"
        return resources

    def get_resource_id(self, resource, action, condition, test_case):
        # response = self.get_fusion_resources();
        # content = json.loads(response.content)
        content = self.get_all_fusion_resources()
        if len(content) == 0:
            print "No Fusion Resources found."
            return None
        for result in content:
            if 'detail' in result:
                continue
            print "Considering: " + json.dumps(result)
            if (result['resource'].lower() == resource.lower() and
                    result['action'].lower() == action.lower() and
                    result['condition'].lower() == condition.lower() and
                    result['test_case'].lower() == test_case.lower()):
                print "Found Resource! (%s)" % result['id']
                return result['id']
        print "Failed to find matching records"
        return None

    #####################################################
    # Firmware Versions
    #####################################################

    # curl -H 'Content-Type: application/json; Accept: application/json; indent=4' -X POST -u admin:hpvse123
    # --data '{"fusion_release":"3.00", "feature_set":"GARFS1", "Platform":"C7000", "Delta":""}'
    # http://16.114.189.182:8080/firmware_versions/
    # To be implemented in the future.
    def add_firmware_version(self, fusion_release, feature_set, platform=None, delta=None):
        pass

    def get_firmware_versions(self):
        response = requests.get(self.firmware_url, auth=(self.username, self.password))
        return response

    def get_firmware_version(self, id):
        response = requests.get(self.firmware_url + str(id) + '/', auth=(self.username, self.password))
        return response
