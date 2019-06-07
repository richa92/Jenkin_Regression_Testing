#!/usr/local/bin/python
import time
import json
import os
import re
import sys
import types
import copy
from RoboGalaxyLibrary.utilitylib import logging as logger

ignoreStringList = []
ignoreStringList.append('/rest/')
ignoreStringList.append('name')


class JsonData():

    def __init__(self):
        self._replaceStringList = []
        self._replacePatternList = []
        self._replaceStringList.append(re.compile(r'\"relativeValue\"'))
        self._replaceStringList.append(re.compile(r'\"lagId\"'))
        self._replaceStringList.append(re.compile(r'\"modified\"'))
        self._replaceStringList.append(re.compile(r'\"created\"'))
        self._replaceStringList.append(re.compile(r'\"eTag\"'))
        self._replaceStringList.append(re.compile(r'\"taskUri\"'))
        self._replaceStringList.append(re.compile(r'\"uri\"'))
        self._replaceStringList.append(re.compile(r'\"timestamp\"'))

        self._replacePatternList.append(
            re.compile(r'\w{8}\W\w{4}\W\w{4}\W\w{4}\W\w{12}'))
        self._replacePatternList.append(
            re.compile(r'\d{4}\W\d+\W\d+T\d+:\d+:\d+.\d{3}Z'))
        self._replacePatternList.append(
            re.compile(r'UTC \d+\W\d+\W\d+ \d+:\d+:\d+'))
        self._replacePatternList.append(
            re.compile(self._create_regex('@', '[')))

    def write(self, data, filename, filemode='w'):
        with open(filename, filemode) as output_file:
            json.dump(
                data, output_file, sort_keys=True, indent=4, ensure_ascii=True)

    def filter(self, inputFile, outputFile):

        with open(inputFile, 'r+') as inputfp, open(outputFile, 'w+') as outputfp:
            for line in inputfp:
                for the_replaceString in self._replaceStringList:
                    if the_replaceString.search(line):
                        line = self._replace(line)
                        break
                for the_replacePattern in self._replacePatternList:
                    if the_replacePattern.search(line):
                        line = the_replacePattern.sub('IGNORE', line)
                        break

                outputfp.write(line)

    def _replace(self, line):
        new_regex = self._create_regex(':', ',')
        the_filter = re.compile(new_regex)
        line = the_filter.sub(' \"IGNORE\"', line)
        return line

    def _create_regex(self, first, second):
        new_regex = '(?<=' + first + ')[^\\' + \
            second + ']*(?=\\' + second + ')'
        return new_regex

    def compare(self, first_file, second_file):
        first_filtered_file = os.path.dirname(
            first_file) + '/filtered-' + os.path.basename(first_file)
        second_filtered_file = os.path.dirname(
            second_file) + '/filtered-' + os.path.basename(second_file)

        self.filter(first_file, first_filtered_file)
        self.filter(second_file, second_filtered_file)

        with open(first_filtered_file, 'r+') as savefp, open(second_filtered_file, 'r+') as runfp:
            try:
                saveData = json.load(savefp)
                expectData = json.load(runfp)
                if saveData == expectData:
                    return True
                else:
                    return False
            except:
                e = sys.exc_info()[0]
                errorString = "Error is %s" % e
                print errorString


class selectDataDiff():

    def __init__(self):
        self.difference = []
        self.diff_key_list = []
        self._counter = 0
        self._hits = {}

    def diff_data(self, saved, new, path='', parentKey=None, ignoreListOrder=True):

        # print 'DEBUG: saved: %s' % saved
        # print 'DEBUG: new: %s' % new
        if (isinstance(saved, dict) and isinstance(new, dict)):
            # print 'DEBUG: both dictionary'
            newKeys = set(new.keys())
            savedKeys = set(saved.keys())
            newExclusiveKeys = newKeys - savedKeys
            newKV = set(k for k in newKeys if saved.get(k) == new.get(k))
            diffKeySet = newKeys - newKV

            if len(diffKeySet) > 0:
                for key in diffKeySet:
                    newPath = "%s.%s" % (path, key)
                    self.diff_data(saved[key], new[key],
                                   newPath, parentKey=key,
                                   ignoreListOrder=ignoreListOrder)

            if len(newExclusiveKeys) > 0:
                for key in newExclusiveKeys:
                    newPath = "%s.%s" % (path, key)
                    self.save_diff('Not expected attribute ',
                                   '%s  at ' % key,
                                   path)
                self.diff_key_list.extend(list(newExclusiveKeys))

        # compare list
        elif (isinstance(saved, list) and isinstance(new, list)):
            # print 'DEBUG: both list'
            if len(saved) != len(new):
                if parentKey:
                    self.save_diff('Differ in List length of ',
                                   ' %s :  %s | %s    at ' % (parentKey, len(saved), len(new)),
                                   path)
                    self.diff_key_list.append(parentKey)
                else:
                    self.save_diff('?? ', '  -  %s | %s' % (saved, new), path)
                    self.diff_key_list.append("Lists differ in length")
            else:
                if ignoreListOrder:
                    saved = self.sortList(saved)
                    new = self.sortList(new)
                for i in xrange(len(saved)):
                    newPath = "%s[%s]" % (path, i)
                    self.diff_data(saved[i], new[i],
                                   newPath, parentKey=saved[i],
                                   ignoreListOrder=ignoreListOrder)

        elif (type(saved) != type(new) and
              ((type(saved).__name__ != 'str' and
                type(saved).__name__ != 'unicode') or
               (type(new).__name__ != 'str' and
                type(new).__name__ != 'unicode'))):

            # print 'DEBUG: saved and new not the same type: parentKey: %s' % parentKey
            self.save_diff('Type mismatch', ' %s -  %s | %s    at ' % (parentKey, type(saved).__name__, type(new).__name__), path)
            self.diff_key_list.append(parentKey)

        elif saved != new:
            # print 'DEBUG: saved and new not the equal: parentKey: %s' % parentKey
            if parentKey:
                if not self.containStrPattern(ignoreStringList, saved) or not self.containStrPattern(ignoreStringList, new):
                    self.save_diff('Differ in key value of ',
                                   ' %s :  %s | %s     at ' % (parentKey, saved, new),
                                   path) if parentKey else None
                    self.diff_key_list.append(parentKey) if parentKey else None

            else:
                self.save_diff('GENERAL', 'Structs are not equal', path)
                self.diff_key_list.append("Structs are not equal")

        return

    def save_diff(self, diff_type, diff_message, diff_path):
        self.difference.append((diff_type, diff_message, diff_path))
        # print 'DEBUG: save_diff: difference: %s' % self.difference

    def containStrPattern(self, stringList, destStr):
        if isinstance(destStr, basestring):
            if any(s in destStr for s in stringList):
                return True
        return False

    def sortList(self, beforeList, sortDict=True):
        # sort keys for list of dictionaries
        if not beforeList:
            return beforeList

        if isinstance(beforeList[0], dict) and sortDict:
            if 'name' in beforeList[0]:
                afterList = sorted(beforeList, key=lambda k: k['name'])
            elif 'type' in beforeList[0]:
                afterList = sorted(beforeList, key=lambda k: k['type'])
            elif 'logicalLocation_ADD' in beforeList[0]:
                afterList = sorted(beforeList, key=lambda k: k['logicalLocation_ADD'])
            elif 'Location_ADD' in beforeList[0]:
                afterList = sorted(beforeList, key=lambda k: k['Location_ADD'])
            elif 'qosTrafficClass' in beforeList[0]:
                afterList = sorted(beforeList, key=lambda k: k['qosTrafficClass']['className'])
            elif 'portName' in beforeList[0]:
                afterList = sorted(beforeList, key=lambda k: k['portName'])
            elif 'interconnects_ADD_name' in beforeList[0]:
                afterList = sorted(beforeList, key=lambda k: k['interconnects_ADD_name'])
            elif 'location_ADD' in beforeList[0]:
                afterList = sorted(beforeList, key=lambda k: k['location_ADD'])
            elif 'bayNumber' in beforeList[0]:
                afterList = sorted(beforeList, key=lambda k: k['bayNumber'])
            elif 'description' in beforeList[0]:
                afterList = sorted(beforeList, key=lambda k: k['description'])
            else:
                afterList = beforeList
            return afterList
        else:
            return sorted(beforeList)


class JsonDiff():
    __slots__ = ['conditionalExcL', 'taggedKeys_pathDataDict']

    def __init__(self, conditionalExcL, taggedKeys_pathDataDict):
        self.difference = []
        self.diff_key_list = []
        self._counter = 0
        self._hits = {}
        self.conditionalExcL = conditionalExcL
        self.taggedKeys_pathDataDict = taggedKeys_pathDataDict

    def _searchKeyValue(self, myDict, otherDict, hitsKey=None):
        retvalList = []
        for k, v in myDict.items():
            if not isinstance(v, int) and v.endswith('*'):
                retvalList.append(True if re.search(v, otherDict[k]) and self._validateHit(hitsKey) else False)
            else:
                retvalList.append(True if v == otherDict[k] and self._validateHit(hitsKey) else False)

        return retvalList

    def _validateHit(self, hitsKey):
        return (True if hitsKey is None or self._counter not in self._hits[hitsKey] else False)

    def _freeDataType(self, var):
        if isinstance(var, list):
            del var[:]
            del var
        elif isinstance(var, dict):
            var = {}
        else:
            var = ''

    def _findBoolInList(self, myOp, myList, hitsKey=None, data=[], freeData=True):
        if myOp is 'AND' and False not in myList:
            if freeData:
                self._freeDataType(data)
            if hitsKey is not None:
                self._hits[hitsKey].append(self._counter)
            return True
        elif myOp is 'OR' and True in myList:
            if freeData:
                self._freeDataType(data)
            if hitsKey is not None:
                self._hits[hitsKey].append(self._counter)
            return True
        else:
            return False

    def checkConditionalExclusion(self, conditionalExcL, path, parent_key):
        """
        :param conditionalExcL: a dictionary of pre-defined conditional exclusion usually set in defaults.py
        :param path: the same path variable we see in diff_structs which is the immediate path to the key/parent_key
        :param parent_key: struct dictionary key
        :return: True or False. The former if it matched the conditional exclusion criteria.
        """
        retval = False
        for exclDict in conditionalExcL:
            exclPath = exclDict.get('path')
            taggedKeys = copy.deepcopy(exclDict.get('taggedKeys'))

            if exclPath is not None:
                if path == '%s.%s' % (exclPath, parent_key) and any(parent_key == k for k in exclDict.get('excList') if k):
                    retval = True
            elif taggedKeys is not None and any(parent_key == k for k in exclDict.get('excList') if k):
                # now, check if it matched to the conditional exclusion using tagged key
                taggedKeys_path = exclDict.get('taggedKeys_path')
                try:
                    if taggedKeys_path is None or not re.search('.', taggedKeys_path):
                        errMsg = '[%s] Conditional exclusion "taggedKeys_path" attribute is %s: set it to valid "path"' % (__file__, taggedKeys_path)
                        raise RuntimeError(errMsg)
                    else:
                        # iterate over taggedKeys and check if value match our conditional exception
                        taggedKeys_operator = exclDict.get('taggedKeys_operator')
                        if taggedKeys_operator != 'AND' and taggedKeys_operator != 'OR':
                            errMsg = 'Conditional exclusion has invalid "taggedKeys_operator" attribute value %s' % taggedKeys_operator
                            raise RuntimeError(errMsg)

                        taggedKeys_pathData = copy.deepcopy(self.taggedKeys_pathDataDict.get(taggedKeys_path))

                        retvalList = []
                        if isinstance(taggedKeys_pathData, list):
                            # chop off path list up to the first wildcard list
                            taggedKeys_pathList = taggedKeys_path.split('.')
                            if taggedKeys_pathList[1] != '':
                                taggedKeys_pathList.remove(taggedKeys_pathList[0])
                                taggedKeys_pathList.remove(taggedKeys_pathList[0])
                                for i in taggedKeys_pathList:
                                    if re.search('.*\[\*\]', i):
                                        taggedKeys_pathList.remove(taggedKeys_pathList[0])

                            self._counter = 0
                            if self._hits.get(taggedKeys_path) is None:
                                self._hits[taggedKeys_path] = []

                            while len(taggedKeys_pathData) > 0:
                                for pristine_data in taggedKeys_pathData[0]:
                                    self._counter += 1
                                    if self._counter in self._hits[taggedKeys_path]:
                                        continue
                                    if taggedKeys_pathList:
                                        for t in taggedKeys_pathList:
                                            if re.search('.*\[\*\]', t):
                                                # remove wildcard tag in list ([*])
                                                t = re.sub('\[\*\]', '', t)
                                            for pristine_subdata in pristine_data[t]:
                                                self._counter += 1
                                                if self._counter in self._hits[taggedKeys_path]:
                                                    continue
                                                # check if taggedKeys are there
                                                retvalList = self._searchKeyValue(taggedKeys, pristine_subdata, taggedKeys_path)
                                                if self._findBoolInList(taggedKeys_operator, retvalList, taggedKeys_path, data=taggedKeys_pathData, freeData=True):
                                                    return True
                                    else:
                                        retvalList = self._searchKeyValue(taggedKeys, pristine_data, taggedKeys_path)
                                        if self._findBoolInList(taggedKeys_operator, retvalList, taggedKeys_path, data=taggedKeys_pathData, freeData=True):
                                            return True

                                del taggedKeys_pathData[0]
                        elif isinstance(taggedKeys_pathData, dict):
                            retvalList = self._searchKeyValue(taggedKeys, taggedKeys_pathData)
                            return self._findBoolInList(taggedKeys_operator, retvalList, freeData=False)
                        else:
                            print 'WARNING: Unexpected data type found for tagged keys path data in %s' % __file__

                        if not retvalList:
                            retvalList.append(False)

                        # check for taggedKeys_operator and decide what the appropriate retval is
                        return self._findBoolInList(taggedKeys_operator, retvalList, taggedKeys_path, freeData=False)
                except Exception as e:
                    raise Exception(e)

        return retval

    def diff_structs(self, struct_a, struct_b, excList, path='', parent_key=None, ignore_list_order=True, resolve_name=False):

        if (isinstance(struct_a, dict) and isinstance(struct_b, dict) and parent_key not in excList):
            a_keys = set(struct_a.keys())
            b_keys = set(struct_b.keys())
            a_exclusive_keys = a_keys - b_keys - set(excList)
            b_exclusive_keys = b_keys - a_keys - set(excList)
            common_keys = a_keys & b_keys
            common_pairs = set(k for k in common_keys if struct_a[k] == struct_b[k])
            diff_key_set = common_keys - common_pairs

            if len(diff_key_set) > 0:
                for key in diff_key_set:
                    new_path = "%s.%s" % (path, key)
                    self.diff_structs(struct_a[key], struct_b[key], excList,
                                      new_path, parent_key=key,
                                      ignore_list_order=ignore_list_order,
                                      resolve_name=resolve_name)
            # if any key not in either a or b
            if len(a_exclusive_keys) > 0:
                for dict_key in a_exclusive_keys:
                    new_path = "%s.%s" % (path, dict_key)
                    self.save_diff('Missing attribute ',
                                   '%s  at ' % dict_key,
                                   path)
                self.diff_key_list.extend(list(a_exclusive_keys))
            if len(b_exclusive_keys) > 0:
                for dict_key in b_exclusive_keys:
                    new_path = "%s.%s" % (path, dict_key)
                    self.save_diff('Not expected attribute ',
                                   '%s  at ' % dict_key,
                                   path)
                self.diff_key_list.extend(list(b_exclusive_keys))

        # compare list
        elif (isinstance(struct_a, list) and isinstance(struct_b, list) and parent_key not in excList):
            if len(struct_a) != len(struct_b):
                if parent_key:
                    self.save_diff('Differ in List length of ',
                                   ' %s :  %s | %s    at ' % (parent_key, len(struct_a), len(struct_b)),
                                   path)
                    self.diff_key_list.append(parent_key)
                else:
                    self.save_diff('?? ', '  -  %s | %s' % (struct_a, struct_b), path)
                    self.diff_key_list.append("Lists differ in length")
            else:
                if ignore_list_order:
                    struct_a = self.sortList(struct_a)
                    struct_b = self.sortList(struct_b)
                for i in xrange(len(struct_a)):
                    new_path = "%s[%s]" % (path, i)
                    if resolve_name:
                        if (isinstance(struct_a[i], dict)):
                            if struct_a[i].get('name'):
                                new_path = new_path.rsplit('.', 1)[0]
                                new_path = new_path + ".%s" % (struct_a[i]['name'])
                    self.diff_structs(struct_a[i], struct_b[i], excList,
                                      new_path, parent_key=struct_a[i],
                                      ignore_list_order=ignore_list_order,
                                      resolve_name=resolve_name)

        elif (type(struct_a) != type(struct_b) and
              ((type(struct_a).__name__ != 'str' and
                type(struct_a).__name__ != 'unicode') or
               (type(struct_b).__name__ != 'str' and
                type(struct_b).__name__ != 'unicode'))):

            if parent_key:
                if parent_key not in excList:
                    self.save_diff('Type mismatch', ' %s -  %s | %s    at ' % (parent_key, type(struct_a).__name__, type(struct_b).__name__), path)
                    self.diff_key_list.append(parent_key)

        elif struct_a != struct_b:
            if parent_key:

                if parent_key not in excList:
                    if not self.containStrPattern(ignoreStringList, struct_a) or not self.containStrPattern(ignoreStringList, struct_b):
                        if not self.checkConditionalExclusion(self.conditionalExcL, path, parent_key):

                            self.save_diff('Differ in key value of ',
                                           ' %s :  %s | %s     at ' % (parent_key, struct_a, struct_b),
                                           path) if parent_key else None
                            self.diff_key_list.append(parent_key) if parent_key else None

            else:
                self.save_diff('GENERAL', 'Structs are not equal', path)
                self.diff_key_list.append("Structs are not equal")

        return

    def save_diff(self, diff_type, diff_message, diff_path):
        self.difference.append((diff_type, diff_message, diff_path))

    def containStrPattern(self, stringList, destStr):
        if isinstance(destStr, basestring):
            if any(s in destStr for s in stringList):
                return True
        return False

    def sortList(self, beforeList, sortDict=True):
        # sort keys for list of dictionaries
        if isinstance(beforeList[0], dict) and sortDict:
            if 'name' in beforeList[0]:
                afterList = sorted(beforeList, key=lambda k: k['name'])
            elif 'type' in beforeList[0]:
                afterList = sorted(beforeList, key=lambda k: k['type'])
            elif 'logicalLocation_ADD' in beforeList[0]:
                afterList = sorted(beforeList, key=lambda k: k['logicalLocation_ADD'])
            elif 'Location_ADD' in beforeList[0]:
                afterList = sorted(beforeList, key=lambda k: k['Location_ADD'])
            elif 'qosTrafficClass' in beforeList[0]:
                afterList = sorted(beforeList, key=lambda k: k['qosTrafficClass']['className'])
            elif 'portName' in beforeList[0]:
                afterList = sorted(beforeList, key=lambda k: k['portName'])
            elif 'interconnects_ADD_name' in beforeList[0]:
                afterList = sorted(beforeList, key=lambda k: k['interconnects_ADD_name'])
            elif 'location_ADD' in beforeList[0]:
                afterList = sorted(beforeList, key=lambda k: k['location_ADD'])
            elif 'bayNumber' in beforeList[0]:
                afterList = sorted(beforeList, key=lambda k: k['bayNumber'])
            elif 'description' in beforeList[0]:
                afterList = sorted(beforeList, key=lambda k: k['description'])
            else:
                afterList = beforeList
            return afterList
        else:
            return sorted(beforeList)


class Timeout(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Timer:

    def __init__(self, Name=None, time_out=0, func=time.clock):
        self.elapsed = 0.0
        self._func = func
        self._start = None
        self._name = Name
        self._timeout = time_out
        self._logger = logger

    def start(self):
        if self._start is None:
            # raise RuntimeError('Already started')
            self._start = self._func()
            if self._timeout > 0:
                self._timeout = float(self._timeout + self._start)

    def stop(self):
        if self._start is not None:
            #    raise RuntimeError('Not started')
            end = self._func()
            self.elapsed += end - self._start
            self._start = None

    def reset(self):
        self.elapsed = 0.0

    def elapse(self):
        end = self._func()
        self.elapsed = end - self._start
        msg = "elapsed time %ds" % (self.elapsed)
        if self.elapsed > self._timeout:
            msg = "timer %s start %d timeout %d elapsed %d" % (
                self._name, self._start, self._timeout, self.elapsed)
            self._logger._log_to_console_and_log_file(msg)
            raise Timeout(msg)
        return self.elapsed

    @property
    def running(self):
        return self._start is not None

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.stop()


class switch(object):

    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args:  # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False
