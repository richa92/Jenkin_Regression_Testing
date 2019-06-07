# (C) Copyright 2015 Hewlett-Packard Development Company, L.P.
"""
RoboGalaxyLibrary keywords for PMSAN

"""
from FusionLibrary.ui.pmsan import pmsanserverprofile


class FusionPMSanUiKeywords(object):
    """
    PM San Ui keywords
    """

    def fusion_ui_create_san_storage_profile(self, *profile_obj):
        """
        Creates a Server profile with San Storage
        -------------------------------------------------------------------------------------------------------------
        The profile_obj must have the following defined within the object (optional attributes have a *)
            profile
                name -- name of the profile
                server -- name of the server hardware
                profile* -- profile's description
                hardwaretype -- type of hardware for the profile
                enclgroup -- enclosure group
                affinity* --profile's affinity
                connection -- list of connections for profile
                    network -- network name for connection
                    type -- network type
                    name* -- connection name
                    portname* -- port name
                    band* -- bandwith as a number
                    boot* -- 'Not Bootable', 'Primary', 'Secondary'
                    targetwwpn* -- target wwpn
                    targetlun* -- target lun
                    wwpn* -- wwpn address
                    wwnn* -- wwnn address
                    macaddress* -- mac address
                sanstorage -- list of storage volumes for profile
                    san -- 'true' if adding the volume
                    ostype -- name of OS
                    volumetype -- 'New Volume' or "Existing Volume"
                    sanvolume -- name of volume
                    storagepool -- storage pool name
                    description* -- description of volume
                    sanlun -- lun number, empty will default to auto
                    capacity -- volume size in GiB
                    provisioning* -- 'Full' or 'Thin'. Defaults to Thin
                    permanent* -- 'true' or 'false'. Defaults to true
                    connection -- list of connections for san volume
                        name -- name of connection
                        port -- contains the storage target (fabric attach only)
                            target -- the storage target (fabric attach only)
        -------------------------------------------------------------------------------------------------------------
        Usage:
        | Fusion UI Create San Storage Profile | @{Profiles} |
        """
        return pmsanserverprofile.create_san_storage_profile(profile_obj)

    def fusion_ui_validate_invalid_san_elements_in_profile(self, *profile_obj):
        """
        Checks for invalid input, and makes sure error messages are thrown
        when an invalid input is passed
        -------------------------------------------------------------------------------------------------------------
        The profile_obj must have the following defined within the object (optional attributes listed in parentheses)
            profile
                name -- profile's name
                profile* -- profile's description
                server -- name of server hardware
                hardwaretype -- hardware type
                enclgroup -- enclosure group
                affinity* -- profile's affinity
                connection* -- list of connections (optional, no function in this test)
                    network -- network name
                    type -- network type
                    name* -- connection name
                    portname* -- port name
                    band* -- bandwith as a number
                    boot* -- 'Not Bootable', 'Primary', 'Secondary'
                    targetwwpn* -- target wwpn
                    targetlun* -- target lun
                    wwpn* -- wwpn address
                    wwnn* -- wwnn address
                    macaddress* -- mac address
                sanstorage -- list of volumes (all attributes should be configured to trigger errors)
                    san -- 'true'
                    sanvolume -- volume name
                    ostype -- name of OS
                    volumetype -- 'New Volume'
                    description -- description (should be greater than 2000 char)
                    sanlun -- lun (examples of invalid: -2, 13.4, words, 200000)
                    storagepool -- storage pool name
                    capacity -- volume size (examples of invalid: -3, 0.2, 14.5, 16001, words)
        -------------------------------------------------------------------------------------------------------------
        Usage:
        | Fusion UI Validate Invalid SAN Elements In Profile | @{Profiles} |
        """
        return pmsanserverprofile.validate_invalid_san_elements_in_profile(profile_obj)

    def fusion_ui_edit_san_storage_profile(self, *profile_obj):
        """
        Edits a profile's general, connection, and san storage section,
        by adding, deleting, or modifying existing volumes
        -------------------------------------------------------------------------------------------------------------
        The profile_obj must have the following defined within the object (optional attributes listed in parentheses)
            editprofile
                name -- name of profile to edit
                power* -- 'On' or 'Off
                newname* -- new name of profile
                newdescription* -- new description of profile
                newServerHardware* -- new hardware for profile
                connections* -- list of connections if applicable. Need a modification attribute
                    if modification == "add"
                        network -- name of network
                        type -- network type
                        name* -- connetion name
                        portname* -- port name
                        band* -- bandwith as a number
                        boot* -- 'Not Bootable', 'Primary', 'Secondary'
                        targetwwpn* -- target wwpn
                        targetlun* -- target lun
                        wwpn* -- wwpn address
                        wwnn* -- wwnn address
                        macaddress* -- mac address
                    if modification == "edit"
                        name -- name of connection
                        newname* -- new connection name
                        network* -- name of network
                        warning* -- include this and leave empty if editing the connection will cause a warning (such as with a volume)
                        portname* -- port name
                        band* -- bandwith as a number
                        boot* -- 'Not Bootable', 'Primary', 'Secondary'
                        targetwwpn* -- target wwpn
                        targetlun* -- target lun
                        wwpn* -- wwpn address
                        wwnn* -- wwnn address
                        macaddress* -- mac address
                    if modification == "delete"
                        name -- name of connection
                        warning* -- include this and leave empty if deleting the connection will cause a warning (such as with a volume)
                sanstorage* -- list of san storage volumes if applicable. Need a modification attribute
                    if modification == "add"
                        san -- 'true'
                        ostype -- name of OS
                        volumetype -- 'New Volume' or 'Existing Volume'
                        sanvolume -- name of volume
                        storagepool -- name of storage pool
                        description* -- description of volume
                        sanlun* -- lun. If empty, will default to auto
                        capacity* -- size of volume in GiB.
                        provisioning* -- 'thin' or 'full'. Defaults to 'thin'
                        permanent* -- 'true' or 'false'. Defaults to 'true'
                        connection -- list of connections for volume
                            name -- name of connection
                            port -- contains the storage target (fabric attach only)
                                target -- storage target port name (fabric attach only)
                    if modification == "edit"
                        sanvolume -- name of volume
                        sanlun* -- lun. If empty it will switch to auto
                        connection -- list of connections to modify for the volume
                            if edit == "add"
                                name -- name of connection
                                port -- contains the storage target port (fabric attach only)
                                    target -- storage target port (fabric attach only)
                            if edit == "remove"
                                name -- name of connection
                            if edit == "disable"
                                name -- name of connection
                            if edit == "enable"
                                name -- name of connection
                                port -- contains the storage target port (fabric attach only)
                                    target -- storage target port (fabric attach only)
                                    enabled* -- include if you want to enable a disabled storage target port
                                    disabled* -- include if you want to disable an enabled storage target port
                            if edit == ""
                                name -- name of connection
                                port -- contains the storage target port (fabric attach only)
                                    target -- storage target port (fabric attach only)
                                    enabled* -- include if you want to enable a disabled storage target port
                                    disabled* -- include if you want to disable an enabled storage target port
                    if modification == "delete"
                        sanvolume -- name of volume
                        permanent* -- if the volume is permanent, include this
                    if modification == "lunswap"
                        sanvolume -- name of volume
                        sanlun -- lun
        -------------------------------------------------------------------------------------------------------------
        Usage:
        | Fusion UI Edit San Storage Profile | @{Profiles} |
        """
        return pmsanserverprofile.edit_san_storage_profile(profile_obj)

    def fusion_ui_delete_pmsan_server_profile(self, *profile_obj):
        """
        Deletes a server profile, and checks for warnings based on
        permanence of volumes in the profile
        -------------------------------------------------------------------------------------------------------------
        The profile_obj must have the following defined within the object (optional attributes listed in parentheses)
            deleteprofile
            name -- name of profile
            nonpermanentvolume* -- include if the profile to delete has a non-permanent volume associated with it
        -------------------------------------------------------------------------------------------------------------
        Usage:
        | Fusion UI Delete Pmsan Server Profile | @{Profiles} |
        """
        return pmsanserverprofile.delete_pmsan_server_profile(profile_obj)

    def fusion_ui_verify_volume_configuration_for_profile(self, profile_name="", *volume_obj):
        """
        Checks both the san storage volumes table, and the edit profile volumes
        table against the correct configuration passed in. Makes sure the volume
        configuration is correct in both places
        -------------------------------------------------------------------------------------------------------------
        The volume_obj must have the following defined within the object (optional attributes listed in parentheses)
            volume
                name -- volume name
                lun -- volume lun. leave empty if it was auto-assigned
                permanent -- 'yes' or 'no'
                storagepool -- storage pool name
                size -- volume capacity in GiB
                provisioning -- 'thin' or 'full'
                sharing -- 'shared' or 'private'
                connection -- list of connections associated with the volume
                    name -- name of connection
                    type -- connection type
                    serverinitiator* -- name of server initiator
                    enabled -- 'yes' if connection is enabled, 'no' otherwise
                    port -- contains storage targets (fabric attach supported currently)
                        target -- storage target port
                        group -- storage target port group (usually 'auto')
        -------------------------------------------------------------------------------------------------------------
        Usage:
        | Fusion UI Verify Volume Configuration For Profile| profile_name | @{Volumes} |
        """
        return pmsanserverprofile.verify_volume_configuration_for_profile(profile_name, volume_obj)

    def fusion_ui_pmsan_verify_volume_section_of_fusion(self, *volume_obj):
        """
        This keyword should be used to check the volume section of fusion after a
        profile edit/delete to make sure the correct volumes are being displayed
        -------------------------------------------------------------------------------------------------------------
        The volume_obj must have the following defined within the object (optional attributes listed in parentheses)
            volume
                name -- volume name
                remain* -- if the volume should remain, include this
                deleted* -- if the volume should have been deleted, include this
        -------------------------------------------------------------------------------------------------------------
        Usage:
        | Fusion UI Pmsan Verify Volume Section Of Fusion | @{Volumes} |
        """
        return pmsanserverprofile.verify_volume_section_of_fusion(volume_obj)

    def fusion_ui_verify_render_time_for_san_storage(self, render_time, *profile_obj):
        """
        This keyword is used to check the render time for profile's sanstorage section.
        Passes if the tables load in less than render_time (passed in as milliseconds)
        -------------------------------------------------------------------------------------------------------------
        The profile_obj must have the following defined within the object (optional attributes listed in parentheses)
            profile
                name -- profile's name
        -------------------------------------------------------------------------------------------------------------
        Usage:
        | Fusion UI Verify Render Time For San Storage | render_time | @{Profiles} |
        """
        return pmsanserverprofile.verify_render_time_for_san_storage(render_time, profile_obj)

    def fusion_ui_uncheck_manage_san_storage_of_profile(self, *profile_obj):
        """
        This keyword is used to uncheck the manage san storage checkbox of a profile.
        It will also update the profile so that it no longer manages san storage
        -------------------------------------------------------------------------------------------------------------
        The profile_obj must have the following defined within the object (optional attributes listed in parentheses)
            editprofile
                name -- profile's name
        -------------------------------------------------------------------------------------------------------------
        Usage:
        | Fusion UI Uncheck Manage San Storage of Profile | @{Profiles} |
        """
        return pmsanserverprofile.uncheck_manage_san_storage_of_profile(profile_obj)
