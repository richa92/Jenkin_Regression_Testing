#!/usr/bin/python

import string
import re
import paramiko
import json

ssh = ''
prompt = '-view>'

def read_until_prompt():

    out = ''
    stdOut = ''
    while out.find(prompt) < 0:
        try:
            out = ssh.recv(999)
            if len(out) < 1:
                return
           
        except:
            print "socket timed out"
            exit
        stdOut += out

    # Remove graphic characters
    printable = stdOut.replace('\x1b[?1h\x1b=',"")
    printable = printable.replace('\x1b[K\x1b[?1l\x1b',"")
    printable = re.sub("^help\s+([\w\-]*)\s+\n","",printable )	# Remove command echo
    printable = re.sub(">\w+-view>","",printable )		# Remove prompt        
    return printable
    
def parse_help( help_msg ):

    cmds = re.findall('^\s+([\w\-]+)\s+\w',help_msg,re.M)
    return cmds

def get_command_help( cmd ):

    ssh.send( 'help ' + cmd + "\n" )
    stdout = read_until_prompt()
    print stdout

    return stdout
    
def get_view_help( view_json ):

    response = get_command_help('')
    commands = parse_help(response)
    
    view_json['view-help'] = response
    view_json['commands'] = commands

    if len(commands) > 0:
        for cmd in commands:
            if cmd.find('-view') > -1:
               # cmd_json = {}
                cmd_help = get_command_help( cmd ) 
                cmd_json = { 'cmd-help':cmd_help }

                ssh.send( cmd + "\n" )
                stdOut = read_until_prompt()

                get_view_help( cmd_json )
                view_json[cmd] = cmd_json 
            else:
                cmd_help = get_command_help( cmd ) 
                view_json[cmd]= { 'cmd-help':cmd_help, 'commands': [] }
    else:
        ssh.send( 'exit\n' )
        stdOut = read_until_prompt()
        return


fusion_ip = 'tesla-cim1.rsn.hp.com'
user = 'Administrator'
pw = 'hpvse123'
client = paramiko.client.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(fusion_ip, username=user, password=pw, timeout=60.0 )
except paramiko.BadHostKeyException:
    print "Not able to connect because of BadKeyException.  Need to clean up .ssh directory?"
except paramiko.AuthenticationException:
    print "Not able to connect because of Authentication"
except paramiko.SSHException:
    print "Not able to connect because of SSHException"
except:
    print "Not able to connect to client %s" % client
    exit

ssh = client.invoke_shell()
ssh.settimeout(30.)
output = read_until_prompt()

main_json = {}
get_view_help(main_json)
string_json = json.dumps( main_json )
string_json = string_json.replace("\\n"," ")
string_json = string_json.replace("\\r"," ")
string_json = string_json.replace('\\"','\\\\"')
string_json = re.sub("\s+(\S)"," \g<1>",string_json)
string_json = re.sub("\s+"," ",string_json)

file = open('cli_help_oracle.json','w+')
file.write( string_json )
