import paramiko
import re

class OACommand:
	def __init__(self):
	
		pass
	
	def get_trap_from_interconnects(self, ip, username, password, cmd, regex):
		'''
		Execute commands in the Hill Interconnect modules
		'''
		try:
			self._ssh_obj = paramiko.SSHClient()
			self._ssh_obj.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			self._ssh_obj.connect(ip,username = username,
								  password = password)
			stdin, stdout, stderr = self._ssh_obj.exec_command(cmd)
			x = stdout.read()
			matches = re.findall(regex,x)
			return matches
			
		except Exception as e:
			print e

if __name__ == '__main__':
	obj = OACommand()
	r = obj.executeOACommand('15.186.21.107', 'root','D4SNKXF9', \
	'snmpconfig --show snmpv1', r"Trap recipient: \d+.\d+.\d+.\d+")
	print r
	