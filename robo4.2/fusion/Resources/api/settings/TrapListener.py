#!/usr/local/bin/python2.7
import socket
import sys
import re
import argparse
from datetime import datetime


def main():
    # read the arguments
    parser = argparse.ArgumentParser(description='listen to the port for the test trap', add_help=True)
    parser.add_argument('-l', '--log_file', help='log file', default='/root/trap_forwarding/log_file', type=str)
    parser.add_argument('-s', '--status_file', help='status file', default='/root/trap_forwarding/status_file', type=str)
    parser.add_argument('-p', '--listen_port', help='listen port', default=1162, type=int)
    parser.add_argument('-b', '--buffer_size', help='buffer size', default=1024, type=int)
    parser.add_argument('-d', '--data_size', help='data size', default=300, type=int)
    parser.add_argument('-v', '--validate_string', help='validate string', type=str, required=True)
    args = parser.parse_args()
    log_file = open(args.log_file, "w")
    log_file.write("%s status file: %s\n" % (str(datetime.now()), args.status_file))
    log_file.write("%s listen port: %s\n" % (str(datetime.now()), args.listen_port))
    log_file.write("%s buffer size: %s\n" % (str(datetime.now()), args.buffer_size))
    log_file.write("%s expected data size: %s\n" % (str(datetime.now()), args.data_size))
    log_file.write("%s validate string: %s\n" % (str(datetime.now()), args.validate_string))
    # write START to the status file
    status_file = open(args.status_file, "w")
    status_file.write("START")
    status_file.close()
    # open the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = (socket.gethostname(), args.listen_port)
    s.bind(server_address)
    while True:
        data, client_address = s.recvfrom(args.buffer_size)
        log_file.write("%s actual data size: %s\n" % (str(datetime.now()), len(data)))
        if isinstance(data, (str, unicode)) and re.search(args.validate_string, data) and len(data) > args.data_size:
            # write PASS to the status file
            status_file = open(args.status_file, "w")
            status_file.write("PASS")
            status_file.close()
            log_file.close()
            sys.exit(0)

if __name__ == '__main__':
    main()
