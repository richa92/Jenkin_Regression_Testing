import logging
import sys
import os
import pdb


class Logger(object):

    def __init__(self, filename, loggername, tloggername, libloggername):
        self.logfile = filename
        self.lname = loggername
        self.tname = tloggername
        self.libname = libloggername

        try:
            self.log = logging.getLogger(self.lname)
            self.log.setLevel(logging.DEBUG)

            self.term = logging.getLogger(self.tname)
            self.term.setLevel(logging.INFO)

            self.liblog = logging.getLogger(self.libname)
            self.liblog.setLevel(logging.DEBUG)

            format = logging.Formatter("%(levelname)-10s %(asctime)s %(message)-10s")

            stderr_hand = logging.StreamHandler(sys.stderr)
            stderr_hand.setLevel(logging.INFO)
            stderr_hand.setFormatter(format)

            logfile_hand = logging.FileHandler(self.logfile)
            logfile_hand.setLevel(logging.DEBUG)
            logfile_hand.setFormatter(format)

            self.log.addHandler(stderr_hand)
            self.log.addHandler(logfile_hand)
            self.term.addHandler(stderr_hand)
            self.liblog.addHandler(logfile_hand)

        except Exception as e:
            msg = "Failed to create logger for %s" % (self.logfile)
            raise Exception(msg, e)

        return


class LogFile(object):

    def __init__(self, baseLogDir, name):
        self.baseLogDir = baseLogDir
        self.name = name
        self.logfile = self.baseLogDir + "/" + self.name + "/" + self.name + ".log"

    def createLogFile(self):
        try:
            self.log = logging.getLogger(self.name)
            self.log.setLevel(logging.INFO)
            logfile_hand = logging.FileHandler(self.logfile)
            self.log.addHandler(logfile_hand)

        except Exception as e:
            msg = "Failed to create logger for %s" % (self.name)
            raise Exception(msg, e)

        return

    def removeLogFile(self):
        try:
            logFile = self.baseLogDir + "/" + self.name + "/" + self.name + ".log"
            os.remove(logFile)

        except Exception as e:
            msg = "Failed to delete log file for %s" % (self.name)
            raise Exception(msg, e)

        return
