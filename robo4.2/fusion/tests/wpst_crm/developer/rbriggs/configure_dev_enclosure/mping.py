import argparse
from clint.textui import colored, puts
from subprocess import Popen, PIPE
import sys


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-ips', '--iplist', help='comma separated list of IPs\hosts to ping', required=True)
    parser.add_argument('-args', help='Ping args', nargs=argparse.REMAINDER)

    args = parser.parse_args()
    #sys.argv = ["-ips", "16.114.208.62, 16.114.208.60, 16.114.208.61", "-args", "-c", "4"]
    #args = parser.parse_args(sys.argv)

    ips = list(args.iplist.split(','))
    procs = {}
    for ip in ips:
        cmd = "ping %s " % ip
        if args.args:
            cmd += " ".join(args.args)
        procs[ip] = Popen(cmd, shell=True, stdout=PIPE)

    while procs.keys():
        x = 1
        for proc in procs.keys():
            x += 1
            if procs[proc].poll() is None:
                if procs[proc].stdout.readline() is None:
                    print "%s: no output" % proc
                    continue

                if 'TTL' in str.upper(procs[proc].stdout.readline()):
                    puts(colored.green("%s%s: %s" % ("  " * x, proc, procs[proc].stdout.readline())))
                else:
                    puts(colored.red("%s%s: %s" % ("  " * x, proc, procs[proc].stdout.readline())))
            else:
                # proc terminated
                puts(colored.green("%s%s: completed with rc:%s" % ("  " * x, proc, str(procs[proc].returncode))))
                del procs[proc]

if __name__ == '__main__':
    main()


