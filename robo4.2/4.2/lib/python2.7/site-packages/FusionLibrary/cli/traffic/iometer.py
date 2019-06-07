import os
import sys
from robot.api import logger


class IOMeterLibrary(object):
    def __init__(self, traffic_data):
        self.traffic = traffic_data

    def start_traffic(self):
        try:
            logger.debug("start_traffic entered")

        except:
            pass

        finally:
            logger.debug("start_traffic exited")

    def stop_traffic(self):
        try:
            logger.debug("stop_traffic entered")

        except:
            pass

        finally:
            logger.debug("stop_traffic exited")

    def analyse_traffic(self):
        try:
            logger.debug("analyse_traffic entered")

        except:
            pass

        finally:
            logger.debug("analyse_traffic exited")

    def generate_commands_to_execute(self):
        try:
            logger.debug("generate_commands_to_execute entered")

        except:
            pass

        finally:
            logger.debug("generate_commands_to_execute exited")
