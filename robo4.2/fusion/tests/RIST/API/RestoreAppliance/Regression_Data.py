ADMIN_CREDENTIALS = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

backup_file = "OneViewBackup.bkp"

# Enclosures
ENC1 = 'CN75440444'
# Interconnects
ENC1ICBAY3 = '%s, interconnect 3' % ENC1
ENC1ICBAY6 = '%s, interconnect 6' % ENC1
# Server Hardware
ENC1SHBAY4 = '%s, bay 4' % ENC1
ENC1SHBAY6 = '%s, bay 6' % ENC1
ENC1SHBAY7 = '%s, bay 7' % ENC1
ENC1SHBAY8 = '%s, bay 8' % ENC1
ENC1SHBAY9 = '%s, bay 9' % ENC1
# Logical Enclosure
le_name = "LE_SYNERGY"
# Logical Interconnect Groups
lig_name = "LIG_POTASH"
# Sas Interconect Groups
sas_name = "LIG_SAS"
# Server Profiles
sp_name = "SP1"
# storage systems
ssys_name1 = "wpst3par-7200-7-srv"
ssys_name2 = "fvt3par-8400-1-srv"

resources_names = ["LE:%s" % le_name,
                   "LI:%s-%s" % (le_name, lig_name),
                   "SASLI:%s-%s-1" % (le_name, sas_name),
                   "IC:%s" % ENC1ICBAY3,
                   "IC:%s" % ENC1ICBAY6,
                   # "ENC:%s" % ENC1,
                   "SH:%s" % ENC1SHBAY4,
                   "SH:%s" % ENC1SHBAY6,
                   "SH:%s" % ENC1SHBAY7,
                   "SH:%s" % ENC1SHBAY8,
                   "SH:%s" % ENC1SHBAY9,
                   "SP:%s" % sp_name,
                   "SSYS:%s" % ssys_name1,
                   "SSYS:%s" % ssys_name2,
                   ]
