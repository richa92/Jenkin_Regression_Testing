''' User Input begins here...'''
fusion_ip = "16.83.10.14"
fusion_admin_credentials_username = "Administrator"
fusion_admin_credentials_password = "hpvse123"
backup_file = "OneViewBackup.bkp"
''' User Input Ends here... '''

admin_credentials = {'userName': fusion_admin_credentials_username, 'password': fusion_admin_credentials_password}

# Enclosures
ENC1 = 'CN744502CH'

# Interconnects
ENC1ICBAY1 = '%s, interconnect 1' % ENC1
ENC1ICBAY3 = '%s, interconnect 3' % ENC1
ENC1ICBAY4 = '%s, interconnect 4' % ENC1
# ENC1ICBAY4 = '%s, interconnect 4' % ENC1
ENC1ICBAY6 = '%s, interconnect 6' % ENC1

# Server Hardware
ENC1SHBAY1 = '%s, bay 1' % ENC1
ENC1SHBAY3 = '%s, bay 3' % ENC1
ENC1SHBAY5 = '%s, bay 5' % ENC1


# Server Profiles
sp_name1 = "SP"
# sp_name2 = "SP_ML350"
# sp_name3 = "SP_Bay3_BL460"

resources_names = ["IC:%s" % ENC1ICBAY1,
                   "IC:%s" % ENC1ICBAY3,
                   "IC:%s" % ENC1ICBAY4,
                   # "IC:%s" % ENC1ICBAY4,
                   "IC:%s" % ENC1ICBAY6,
                   # "ENC:%s" % ENC1,
                   "SH:%s" % ENC1SHBAY1,
                   "SH:%s" % ENC1SHBAY3,
                   "SH:%s" % ENC1SHBAY5,
                   # "SP:%s" % sp_name1,
                   # "SP:%s" % sp_name2,
                   "SP:%s" % sp_name1
                   ]
