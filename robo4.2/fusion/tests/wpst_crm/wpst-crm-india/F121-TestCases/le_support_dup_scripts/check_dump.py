import sys
import os
import subprocess

bay_number = 'bay' + sys.argv[1] + '/'
file_path = '/logical-enclosure/var/tmp/le-support-dumps/li*/*/enc*/'
file_name = 'version.txt'
# file_name = 'error.txt'
sp_path = '/logical-enclosure/var/tmp/le-support-dumps/'


os.system("date")
cwd = os.getcwd()
print cwd
file_count = 0
sdmp_file_count = os.listdir("/backup_staging/support-dumps/")
for file in sdmp_file_count:
    if "*.sdmp" in file:
        file_count = file_count + 1
if file_count > 1:
    # Abort the dump validation
    os.system("touch /var/ledump/multiple_sdmp_files")
    sys.exit()

os.system("cp /backup_staging/support-dumps/*.sdmp /var/ledump/")
# os.system("cp /tmp/*.sdmp /var/ledump/")
os.chdir("/var/ledump")
cw = os.getcwd()
os.system("./decrypt-support-dump.sh -f ./*.sdmp -k ./private.key")
os.system("gunzip *-DECRYPTED.tar.gz")
os.system("tar -xvf *-DECRYPTED.tar")

file_to_verify = cw + file_path + bay_number + file_name
ICMBAY = os.system('ls ' + file_to_verify)

if ICMBAY == 0:
    print "The support dump validation successfull"
    os.system("touch /var/ledump/validated_support_dump")
else:
    print "The support dump validation failed"
    os.system("touch /var/ledump/failed_support_dump")
