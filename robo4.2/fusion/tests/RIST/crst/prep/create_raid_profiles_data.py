"""
data needed to create server profiles with local storage options
to initialize RAID LVM.
"""


def mk_profile(name,
               drives,
               raidLevel,
               serverHardwareUri):
    """
    :param name:    The name of the desired profile
    :param drives:  The number of drives to include in the array
    :param raidLevel:  The RAID level.  Valid values: RAID0, RAID1
    :param serverHardwareUri:   The uri of the server hardware for the profile
    :return:
    """
    return {'type': 'ServerProfileV10',
            'serverHardwareUri': serverHardwareUri,
            'name': name,
            'connectionSettings': {'connections': []},
            'bootMode': {'manageMode': True,
                         'mode': 'BIOS',
                         'pxeBootPolicy': None,
                         'secureBoot': 'Disabled'},
            'boot': {'manageBoot': True,
                     'order': ['CD', 'USB', 'HardDisk', 'PXE']},
            'localStorage': {'controllers': [{'deviceSlot': 'Embedded',
                                              'driveWriteCache': 'Unmanaged',
                                              'initialize': True,
                                              'logicalDrives': [
                                                  {
                                                      'accelerator': 'Unmanaged',
                                                      'bootable': True,
                                                      'driveTechnology': None,
                                                      'name': '{} - LVM'.format(raidLevel),
                                                      'numPhysicalDrives': drives,
                                                      'raidLevel': raidLevel,
                                                  }
                                              ],
                                              'mode': 'Mixed'
                                              }]}
            }
