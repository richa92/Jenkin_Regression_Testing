import sys
import xmltodict
import json
import re
from collections import OrderedDict


class log_analysis:
    """
    The main goal of this module is to analyze the rg output file and generate a json file "json_data.txt"
    with list of failed test cases and cause of failure. In this way manual effort can be reduced to analyze huge RG log file.
    This will also support to analyze  CHO log file ( log file which has more than one suite)
    Execute: python rg_log_analysis.py <folder with output.xml>
    In this folder path itself the json_data.txt ( output result )  will be generated
    """
    def __init__(self, path):
        self.path = path
        self.input_file = path + r"\output.xml"
        self.out_file = path + r"\json_data.txt"

    def output_json(self, data):
        fout = open(self.out_file, 'w')
        fout.write(json.dumps(data, indent=4))

    def output_csv(self, data):
        import csv
        f = open(self.path + r'\mycsvfile.csv', 'wb')
        if 'total' in data:
            if 'suite' in data['total']:
                header = data['total']['suite'][0].keys()
                dat = data['total']['suite']
                print dat
                writer = csv.DictWriter(f, fieldnames=header)
                writer.writeheader()
                writer.writerows(dat)
                writer.writerows([{}, {}])
            if 'Pass' in data['total'] and 'Fail' in data['total']:
                header1 = ['Pass', 'Fail']
                writer = csv.DictWriter(f, fieldnames=header1)
                writer.writeheader()
                pf = [{k: data['total'][k] for k in data['total'] if k in header1}]
                writer.writerows(pf)

    def processing_data(self):
        output = OrderedDict()
        with open(self.input_file, "r") as f1:
            ary = f1.read()
        log_data = xmltodict.parse(ary)
        if "robot" in log_data:
            if "statistics" in log_data["robot"]:
                stat = log_data["robot"]["statistics"]
                output["total"] = self.__analyse_stats(stat)
            if "suite" in log_data['robot']:
                log_suite = log_data['robot']['suite']
                output["suite"] = OrderedDict()
                if "@source" in log_suite:
                    output["suite"]["source"] = log_suite["@source"]
                if "@name" in log_suite:
                    output["suite"]["name"] = log_suite["@name"]
                if "test" in log_suite:
                    output["suite"]["test_case"] = self.__analyse_test_case(log_suite["test"])
                else:
                    if "suite" in log_data["robot"]["suite"]:
                        log_sub_suite = log_data["robot"]["suite"]["suite"]
                        if(isinstance(log_sub_suite, list)):
                            suites = []
                            for suite in log_sub_suite:
                                suite1 = {}
                                if "@source" in suite:
                                    suite1["source"] = suite["@source"]
                                if "@name" in suite:
                                    suite1["name"] = suite["@name"]
                                if "test" in suite:
                                    suite1["test_case"] = self.__analyse_test_case(suite["test"])
                                suites.append(suite1)
                            output["suite"]["sub_suite"] = suites
                        elif(isinstance(log_sub_suite, dict)):
                            suite = {}
                            if "@source" in log_sub_suite:
                                suite["source"] = log_sub_suite["@source"]
                            if "@name" in log_sub_suite:
                                suite["name"] = log_sub_suite["@name"]
                            if "test" in log_sub_suite:
                                suite["test_case"] = self.__analyse_test_case(log_sub_suite["test"])
                            output["suite"]["sub_suite"] = suite
        self.output_json(output)

    def __analyse_stats(self, stat_data):
        total = OrderedDict()
        if "total" in stat_data:
            if "stat" in stat_data["total"]:
                for i in stat_data["total"]["stat"]:
                    if "#text" in i.keys():
                        if re.match("All Tests", i["#text"]):
                            if "@fail" in i.keys():
                                total["Fail"] = i["@fail"]
                            if "@pass" in i.keys():
                                total["Pass"] = i["@pass"]
        if "suite" in stat_data:
            if "stat" in stat_data["suite"]:
                total["suite"] = []
                if isinstance(stat_data["suite"]["stat"], list):
                    for i1 in stat_data["suite"]["stat"]:
                        suite = OrderedDict()
                        if "@name" in i1.keys():
                            suite["Name"] = i1["@name"]
                        if "@fail" in i1.keys():
                            suite["fail"] = i1["@fail"]
                        if "@pass" in i1.keys():
                            suite["pass"] = i1["@pass"]
                        total["suite"].append(suite)
                elif isinstance(stat_data["suite"]["stat"], dict):
                    i1 = stat_data["suite"]["stat"]
                    suite = {}
                    if "@fail" in i1.keys():
                        suite["fail"] = i1["@fail"]
                    if "@pass" in i1.keys():
                        suite["pass"] = i1["@pass"]
                    if "@name" in i1.keys():
                        suite["Name"] = i1["@name"]
                    total["suite"].append(suite)
        return total

    def __analyse_test_case(self, test_data):
        tests = []
        if isinstance(test_data, dict):
            test1 = OrderedDict()
            if "status" in test_data:
                if "@status" in test_data["status"]:
                    if test_data["status"]["@status"] == "FAIL":
                        if "@name" in test_data:
                            test1["name"] = test_data["@name"]
                            test1["status"] = "FAIL"
                        if "kw" in test_data:
                            kw = self.__analyse_keywords(test_data["kw"])
                            test1["keyword"] = kw
                tests.append(test1)
        elif isinstance(test_data, list):
            for tc in test_data:
                test1 = OrderedDict()
                if "status" in tc:
                    if "@status" in tc["status"]:
                        if tc["status"]["@status"] == "FAIL":
                            if "@name" in tc:
                                test1["name"] = tc["@name"]
                                test1["status"] = "FAIL"
                            if "kw" in tc:
                                kw = self.__analyse_keywords(tc["kw"])
                                test1["keyword"] = kw
                if test1:
                    tests.append(test1)
        return tests

    def __analyse_keywords(self, kw_data):
        kws = []
        if isinstance(kw_data, dict):
            kws = kws + self.__analyse_keyword_dict(kw_data)
        elif isinstance(kw_data, list):
            for kw in kw_data:
                dat = self.__analyse_keyword_dict(kw)
                if dat:
                    kws = kws + dat
        return kws

    def __analyse_keyword_dict(self, kw_data):
        kw = []
        try:
            kw_dict = OrderedDict()
            if "status" in kw_data:
                if "@status" in kw_data["status"]:
                    if kw_data["status"]["@status"] == "FAIL":
                        if "kw" in kw_data:
                            kw = self.__analyse_keywords(kw_data["kw"])
                        else:
                            if "@name" in kw_data:
                                err = []
                                if "msg" in kw_data:
                                    if isinstance(kw_data["msg"], list):
                                        msg_len = len(kw_data["msg"])
                                        for i in range(msg_len):
                                            msg = kw_data["msg"][i]
                                            if "@level" in msg:
                                                task_msg = "^Getting Task using location.*"
                                                task = "task:.*"
                                                if "#text" in msg:
                                                    if msg["@level"] == "INFO" and re.match(task, msg["#text"]):
                                                        if msg["#text"] not in err:
                                                            err.append(msg["#text"])
                                                    if msg["@level"] == "INFO" and re.match(".*taskState.*", msg["#text"]):
                                                        if msg["#text"] not in err:
                                                            err.append(msg["#text"])
                                                    if msg["@level"] == "DEBUG":
                                                        if  re.match(".*Status .*\nResponse Headers.*",msg["#text"]):
                                                            err.append(msg["#text"])
                                                    if msg["@level"] == "FAIL":
                                                        err.append(msg["#text"])
                                                        if i < msg_len-1:
                                                            j = i + 1
                                                            err.append(kw_data["msg"][j]["#text"])
                                    elif isinstance(kw_data["msg"], dict):
                                        msg = kw_data["msg"]
                                        if msg["@level"] == "FAIL":
                                            if "#text" in msg.keys():
                                                err.append(msg["#text"])
                                kw_dict[kw_data["@name"]] = err
                            kw.append(kw_dict)
            return kw
        except Exception as err1:
            import os
            if 'err1' != '0':
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno, err1)
                print "kw {0}".format(json.dumps(kw_data))


def main():
    if len(sys.argv) != 2:
        print " Please provide location of output xml file"
        print " rg_log_analysis <output.xml(input) and result(output)>"
        sys.exit(1)
    xmlFile = sys.argv[1]
    log_data = log_analysis(xmlFile)
    log_data.processing_data()


if __name__ == '__main__':
    main()
