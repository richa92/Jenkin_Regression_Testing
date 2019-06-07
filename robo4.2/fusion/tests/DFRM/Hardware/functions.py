import variables
import itertools
from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
import logging
from robot.api import logger
import logging as _logging
    
def Combinations(List,repeat_val):
    #print  type(repeat_val)
    LIG_Combinations = itertools.product(List,repeat=repeat_val)
    LIG_LIST = list(LIG_Combinations)
    return LIG_LIST

def CreateEgXML(EgName,Ligs_List_xml,Bay_list):

    enclosures = str(len(Ligs_List_xml))
    enclosuregroup=Element('enclosuregroup',name=EgName,enclosure_count = enclosures,ipv4_addresses = "use dhcp")
    for eachLigIndex in range(0,len(Ligs_List_xml)):
        enclosure=SubElement(enclosuregroup, 'enclosure',no=str(eachLigIndex+1))
        for eachBay in Bay_list[eachLigIndex]:
            SubElement(enclosure, 'switch',bay=str(eachBay),lig=Ligs_List_xml[eachLigIndex])
    #print (ElementTree.tostring(enclosuregroup))        
    return (ElementTree.tostring(enclosuregroup))

    