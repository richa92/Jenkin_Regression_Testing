from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.utilitylib import logging as logger
import re

verbose = False

# Method to obtain a Server Hardware Type uri not just by name but also using Mezz Slot and Model.
# If multiple Servers are added to OneView a SHT is create for each one with different Mezz card configuration


def block_no_keyword_warn():
    # this provides a keyword so RoboGalaxy doesn't issue a warning stating "No Keyword found"
    # this is a no-op keyword
    pass


class SHTByMezz(object):

    def __init__(self):
        self.fusionlib = BuiltIn().get_library_instance('FusionLibrary')

    # Calling keyword must pass in:
    # shts: list of SHT that match the expected name
    # mezz: dict of Slot=Model
    def get(self, shts, mezz):
        logger._log_to_console_and_log_file("There are %s matching SHTs to scan from OneView." % len(shts))

        logger._log_to_console_and_log_file("These are the expected Slots and Models:")
        adapters = {}
        for slot, model in mezz.items():
            if re.match('(Flb|Lom)', slot, re.I):
                logger._log_to_console_and_log_file("\t%s expects a %s" % (slot, model))
                adapters[str(slot)] = model
            else:
                adapters['Mezz' + str(slot)] = model
                logger._log_to_console_and_log_file("\tMezz slot %s expects a %s" % (slot, model))

        for sht in shts:
            if len(mezz) == len(sht['adapters']):
                logger._log_to_console_and_log_file("Adapter count match, will check for Slot and Model match.")
                found = 1  # until a non match
                for adapter in sht['adapters']:
                    thisSlot = adapter['slot']
                    thisModel = adapter['model']
                    thisLocation = adapter['location']

                    locationSlot = thisLocation + str(thisSlot)
                    logger._log_to_console_and_log_file("Location and Slot: %s" % locationSlot)

                    if (locationSlot in adapters.keys()) and (adapters[locationSlot] == thisModel):
                        logger._log_to_console_and_log_file("Slot %s matches model %s" % (thisSlot, thisModel))
                        continue
                    else:
                        logger._log_to_console_and_log_file("Slot %s does Not match model %s, onto next adapter." % (thisSlot, thisModel))
                        found = 0
                        break

                if found:
                    return sht['uri']
            else:
                 logger._log_to_console_and_log_file("Adapter count miss match.")

        return "/BadUri"

