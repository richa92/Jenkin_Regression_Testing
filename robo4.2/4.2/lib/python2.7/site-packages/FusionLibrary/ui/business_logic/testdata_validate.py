# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
"""
This class holds all
"""
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.ui.common import ui_lib


class FusionUITestDataValidate(object):

    ReferenceData = {
        'Affinity': ('Device bay', 'Device bay + server hardware'),
        'Firmware_Baseline': ('managed manually',
                              'HP Service Pack for ProLiant version 2013.09.0 (c)',
                              'HP Service Pack for ProLiant version 2014.02.0',
                              'HP Service Pack for ProLiant version 2014.06.0',
                              'HP Service Pack for ProLiant version 2014.09.0',
                              'HP Service Pack for ProLiant version 2015.03.0',
                              'Service Pack for ProLiant version 2016.02.0',
                              'Service Pack for ProLiant version gen9snap6',
                              'Service Pack for ProLiant version 2016.10.0',
                              'Service Pack for ProLiant version Gen10Snap1',
                              'Not set',
                              ),
        'Connection_Function_Type': ('Ethernet', 'Fibre Channel', 'iSCSI'),
        'Connection_Requested_Bandwidth': ('Auto', '2', '4', '8'),
        'Connection_Boot': ('Not bootable', 'Primary', 'Secondary', 'PXE primary', 'PXE secondary', 'iSCSI primary',
                            'iSCSI secondary', 'FC primary', 'FC secondary'
                            ),
        'Connection_Boot_Option': ('Specify boot target', 'Use Adapter BIOS', 'Profile initiator name',
                                   'User specified'
                                   ),
        'Local_Storage_Controller_Mode': ('RAID',),
        'Logical_Drive_RAID_Level': ('RAID 0', 'RAID 1'),
        'Logical_Drive_Drive_Technology': ('not specified', 'SAS HDD', 'SATA HDD', 'SAS SSD', 'SATA SSD'),
        'SAN_Storage_Host_OS_Type': ('AIX',
                                     'Citrix Xen Server 5.x/6.x',
                                     'Egenera',
                                     'Exanet',
                                     'HP-UX (11i v1, 11i v2)',
                                     'HP-UX (11i v3)',
                                     'IBM VIO Server',
                                     'InForm',
                                     'NetApp/ONTAP',
                                     'OE Linux UEK (5.x, 6.x)',
                                     'OpenVMS',
                                     'RHE Linux (5.x, 6.x, 7.x)',
                                     'RHE Linux (Pre RHEL 5)',
                                     'RHE Virtualization (5.x, 6.x)',
                                     'Solaris 11',
                                     'Solaris 9/10',
                                     'SuSE (10.x, 11.x, 12.x)',
                                     'SuSE Linux (Pre SLES 10)',
                                     'VMware (ESXi)',
                                     'Windows 2003',
                                     'Windows 2008/2008 R2',
                                     'Windows 2012 / WS2012 R2'),
        'SAN_Storage_Volume_Type': ('Existing volume', 'New volume'),
        'SAN_Storage_Volume_Provisioning': ('Thin', 'Full'),
        'SAN_Storage_Volume_LUN': ('Auto', 'Manual'),
        'SAN_Storage_System_Type': ('StoreServ', 'StoreVirtual', 'Nimble'),
        'Boot_Mode': ('UEFI', 'UEFI optimized', 'Legacy BIOS', 'Select mode'),
    }

    @classmethod
    def check_enum(cls, val, ref_data_key):
        """

        :param val:
        :type val:
        :param ref_data_key: key of the Reference Data dictionary's item
        :type ref_data_key:
        :return:
        :rtype:
        """
        if ref_data_key not in cls.ReferenceData.keys():
            logger.warn("given key '%s' is not existing in reference data '%s'" % (ref_data_key, cls.ReferenceData.keys()))
            return False

        ref_data_value = cls.ReferenceData[ref_data_key]
        logger.debug("checking given value '%s' should be in reference enum data '%s' ..." % (val, ref_data_value))

        if val in ref_data_value:
            logger.debug("given value '%s' for '%s' is found in reference data" % (val, ref_data_key))
            return True
        else:
            if val is None or val.strip().lower() in ('undefined', 'not-defined', 'not defined'):
                logger.warn("given value '%s' for '%s' shows the attribute is not defined in test data file" % (val, ref_data_key))
            elif val.strip() == '':
                logger.warn("given value '%s' for '%s' is empty, please remove this attribute from test data file if you want to use the default option from UI" % (val, ref_data_key))
            else:
                msg = "<test data invalid>: given value '%s' for '%s' is NOT found in reference values: %s" % (val, ref_data_key, ref_data_value)
                logger.warn(msg)
                ui_lib.fail_test(msg)

            return False


# class FusionUIReferenceData(object):
#     ENUM_SERVER_PROFILE_AFFINITY = {'Affinity': ('Device bay', 'Device bay + server hardware')}
#     ENUM_SERVER_PROFILE_FIRMWARE_BASELINE = {'Firmware baseline':
#                                              ('managed manually',
#                                               'HP Service Pack for ProLiant version 2013.09.0 (c)',
#                                               'HP Service Pack for ProLiant version 2014.02.0',
#                                               'HP Service Pack for ProLiant version 2014.06.0',
#                                               'HP Service Pack for ProLiant version 2014.09.0',
#                                               'HP Service Pack for ProLiant version 2015.03.0',
#                                               )}
#     ENUM_SERVER_PROFILE_CONNECTION_FUNCTION_TYPE = {'Connection_Function_Type':
#                                                     ('Ethernet',
#                                                      'Fibre Channel',
#                                                      )}
#     ENUM_SERVER_PROFILE_CONNECTION_BOOT = {'Connection_Boot':
#                                            ('Not bootable',
#                                             'Primary',
#                                             'Secondary',
#                                             )}
