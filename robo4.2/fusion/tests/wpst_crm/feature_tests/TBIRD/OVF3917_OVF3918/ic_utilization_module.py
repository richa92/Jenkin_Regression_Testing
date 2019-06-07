from robot.libraries.BuiltIn import BuiltIn


def fetch_utilization_values(uri):
    param = '/utilization'
    fz = BuiltIn().get_library_instance('FusionLibrary')
    output = fz.fusion_api_get_interconnect(uri, param)
    print output["metricList"]
    for i in output["metricList"]:
        print i
        if i['metricName'] == 'Cpu' or 'Memory' or 'Temperature' or 'PowerAverageWatts' or 'PowerPeakWatts' or 'PowerMinimumWatts' or 'PowerAllocatedWatts':
            print "\nthe metric name obtained is:%s" % i['metricName']
            Value = i['metricSamples']
            if isinstance(Value[0][0][1], int):
                print "The Metric Value obtained is an integer:%s \n" % Value
            else:
                return False
        else:
            return False
