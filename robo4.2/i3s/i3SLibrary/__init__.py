#!/usr/bin/env python
# Copyright 2018 Hewlett Packard Enterprise Development Company LP
""" API Library initialization file"""
from robot import version as robot_version
from RoboGalaxyLibrary.utilitylib import logging as logger
from i3SLibrary.keywords.i3s_api import i3sAPIKeywords
from i3SLibrary.keywords.i3s_ui import i3SUIKeywords
from version import get_version
from i3SLibrary.utils import BuildDownload
import Selenium2Library as s2l

__version__ = get_version()


class i3SLibrary(i3SUIKeywords,
                 i3SUIKeywords.i3SUIgoldenimageKeywords,
                 i3SUIKeywords.i3SUIplanscriptsKeywords,
                 i3SUIKeywords.i3SUIOEBuildPlanKeywords,
                 i3SUIKeywords.i3SUIOEDeploymentPlanKeywords,
                 i3sAPIKeywords,
                 i3sAPIKeywords.LoginSessionKeywords,
                 i3sAPIKeywords.i3SAPIGetCallForArtifactKeywords,
                 i3sAPIKeywords.i3SAPIArtifactBundleKeywords,
                 i3sAPIKeywords.i3SAPIGoldenImageKeywords,
                 i3sAPIKeywords.i3SAPIBuildPlanKeywords,
                 i3sAPIKeywords.i3SAPIPlanScriptsKeywords,
                 i3sAPIKeywords.i3SAPIDeploymentPlanKeywords,
                 i3sAPIKeywords.i3SAPIBackupRestoreKeywords,
                 i3sAPIKeywords.i3SAPISupportDumpKeywords,
                 i3sAPIKeywords.i3SAPIAuditLogKeywords,
                 i3sAPIKeywords.i3SAPIDeploymentGroupKeywords,
                 i3sAPIKeywords.i3SApplianceFirmwareKeywords,
                 i3sAPIKeywords.I3sHaNodesKeywords,
                 i3sAPIKeywords.i3sAPIOSVolumes,
                 BuildDownload):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __version__

    def __init__(self):
        logger._log_to_console_and_log_file("#########################################################")
        logger._log_to_console_and_log_file("i3SLibrary version %s" % __version__)
        logger._log_to_console_and_log_file("Developed by HPE i3S QA")
        logger._log_to_console_and_log_file("Copyright 2014 Hewlett-Packard Development Company, L.P.")
        logger._log_to_console_and_log_file("#########################################################")
        logger._log_to_console_and_log_file("Robot Framework version %s" % robot_version.VERSION)
        logger._log_to_console_and_log_file("Selenium2Library version %s" % s2l.__version__)

        for base in i3SLibrary.__bases__:
            base.__init__(self)
