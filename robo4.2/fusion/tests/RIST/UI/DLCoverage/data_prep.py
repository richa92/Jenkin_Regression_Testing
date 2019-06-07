#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is to generate a new test data file based on user's selection of server list:
    In the source data file (DLCoverage_data.xml) all servers' data is presented,
    so based on user's input 'wpstdl2,wpstdl9,wpstdl16' this script will delete all other servers'
    data than data of 'wpstdl2,wpstdl9,wpstdl16' and make the target data file is only used for these 3 selected servers.

Usage: python data_prep.py [source data file] [server name list to keep, like 'wpstdl2,wpstdl8,wpstdl9,wpstdl16'] [target file name, optional]

"""
import re
import sys
import os


class PrepServerData(object):
    def __init__(self, source_file, server_selected, target_file='Server_Data_Runtime.xml'):
        self.server_all = []
        self.source_file = source_file
        self.server_selected = server_selected.split(',')
        self.target_file = target_file
        assert len(source_file) > 0, 'source_file not defined!'
        assert len(server_selected) > 0, 'server_list not defined!'

    def generate(self):
        if os.path.exists(self.source_file):
            path_source = os.path.dirname(self.source_file)
            path_target = os.path.dirname(self.target_file)
            file_name = os.path.basename(self.source_file)
            source_file_full_path = os.path.join(path_source, file_name)
            target_file_full_path = os.path.join(path_target, os.path.basename(self.target_file))
            print "source file path is: '%s'" % source_file_full_path
            print "target file path is: '%s'" % target_file_full_path
        else:
            print "'%s' not exists" % self.source_file
            sys.exit()

        fp_source_file = open(source_file_full_path, 'r')
        fp_target_file = open(target_file_full_path, "w")

        file_str = fp_source_file.read()

        server_all = list(set(re.findall(r"wpstdl\d*", file_str)))
        server_not_selected = list(set(server_all).difference(set(self.server_selected)))
        print "Removing data for these servers: %s ..." % server_not_selected

        for server in server_not_selected:
            file_str = re.sub(r"<server name=\"%s-ilo.*?([\s\S]*?)/>" % server, '', file_str)
            file_str = re.sub(r"<profile([^/]*)name=\".*_%s\".*?[^/]>([\s\S]*?)</profile>|<profile([^/]*)name=\".*_%s\".*?([^<\s\S]*?)/>" % (server, server), '', file_str)

        fp_source_file.close()
        fp_target_file.write(file_str)
        fp_target_file.close()


if __name__ == '__main__':
    print sys.argv
    p1 = sys.argv[1]
    p2 = sys.argv[2]
    p3 = sys.argv[3] if len(sys.argv) > 3 else '%s_runtime.xml' % p1.replace('.xml', '')
    PrepServerData(source_file=p1, server_selected=p2, target_file=p3).generate()
