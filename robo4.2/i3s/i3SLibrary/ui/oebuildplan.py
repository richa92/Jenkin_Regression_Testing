# (C) Copyright 2015 Hewlett-Packard Development Company, L.P.
"""
    Buildplan UI
"""

from i3SLibrary.ui.general.base_elements import i3SBasePage
from i3SLibrary.ui.oebuildplan_elements import i3sBuildPlanPage
from i3SLibrary.ui.general import base_page
from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.utilitylib import logging
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from time import sleep

import re
    
def navigate():
    base_page.navigate_base(i3sBuildPlanPage.ID_PAGE_LABEL, i3SBasePage.ID_MENU_LINK_BUILDPLANS, "css=span.hp-page-item-count")
    
    if not ui_lib.wait_for_element(i3sBuildPlanPage.ID_PAGE_LABEL):
        ui_lib.fail_test("Failed to navigate to OE Build page", True)
        
def return_to_create_bppage():
    ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_CANCEL_BP_BUTTON)
    if (ui_lib.wait_for_element_visible(i3sBuildPlanPage.ID_CANCEL_CONFIRM_FORM)):
        ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_CANCEL_CONFIRM_FORM_PROCEED)
    
        if not ui_lib.wait_for_element(i3sBuildPlanPage.ID_PAGE_LABEL):
            ui_lib.fail_test("Failed to navigate to OE Build page", True)
        if ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_CREATE_BP):
            ui_lib.wait_for_element_visible(i3sBuildPlanPage.ID_CREATE_BP_PAGE)
    else:        
        if not ui_lib.wait_for_element(i3sBuildPlanPage.ID_PAGE_LABEL):
            ui_lib.fail_test("Failed to navigate to OE Build page", True)
        if ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_CREATE_BP):
            ui_lib.wait_for_element_visible(i3sBuildPlanPage.ID_CREATE_BP_PAGE)        
    return
    
    
def create_oebuildplan(self, *createoebuildplan_obj):
    """ Select Create OEBuildplans
        Example:
        | Select Create-OEBuildtplans     |     |
    """
    s2l = ui_lib.get_s2l()
    """ Navigate to Buildplan Page """    
        
    if not s2l._is_element_present(i3sBuildPlanPage.ID_PAGE_LABEL):
        navigate()
        
    if ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_CREATE_BP):
        ui_lib.wait_for_element_visible(i3sBuildPlanPage.ID_CREATE_BP_PAGE)      
       
    """ Retrieve data from datasheet """
    if type(createoebuildplan_obj) is test_data.DataObj:
        createoebuildplan_obj = [createoebuildplan_obj]
    elif type(createoebuildplan_obj) is tuple:
        createoebuildplan_obj = list(createoebuildplan_obj[0])
    for oebp in createoebuildplan_obj:
        logger._log_to_console_and_log_file("inside for loop")
        ''' Below are flags to track invalid inputs'''
        name_flag=1
        desc_flag=1       
        dup_name_flag=0
        special_char_flag=1
        
        ''' In the below code, flags are set/unset based on the validity of the input parameters'''
        if (oebp.name == "" ):
            name_flag=0
        if (oebp.description == "" ):
            desc_flag=0        
        if re.search('^[a-zA-Z_]', oebp.name):
            special_char_flag=0
          
        """ Before Adding check for the BuildPlan exists """        
        if name_flag:           
            if s2l._is_element_present(i3sBuildPlanPage.ID_ELEMENT_BUILDPLAN % oebp.name):   
                '''set dup_name_flag to true if name already exists'''
                dup_name_flag=1         
            ui_lib.wait_for_element_and_input_text(i3sBuildPlanPage.ID_INPUT_NAME, oebp.name)  
                              
        if desc_flag:      
            ui_lib.wait_for_element_and_input_text(i3sBuildPlanPage.ID_INPUT_DESCRIPTION, oebp.description)  
              
        ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_INPUT_PLANTYPE_DROPDOWN)        
        sleep(5)            
        ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_INPUT_PLANTYPE)                       
        
        ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_INPUT_OSTYPE_DROPDOWN)  
        sleep(5)      
        ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_INPUT_OSTYPE)                                                  
        ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_INPUT_ARCHITECTURE)    
        
        if (oebp.button != 'cancel'):
            if (oebp.button=='create'):              
                ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_CREATE_BP_BUTTON)
            elif (oebp.button=='create+'):              
                ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_CREATEPLUS_BP_BUTTON)               
                    
                '''checking for blank name error message'''
            if (name_flag==0 ):      
                if not ui_lib.wait_for_element(i3sBuildPlanPage.ID_BLANK_NAME):                    
                    logger._warn("ID_BLANK_NAME not found")
                return_to_create_bppage()
                continue
            
            if (len(oebp.name) > 255):
                logger._log_to_console_and_log_file("inside name greater than 256 chars")
                if not ui_lib.wait_for_element(i3sBuildPlanPage.OEBP_INVALID_NAME_MESSAGE):                   
                    logger._warn("OEBP_INVALID_NAME_MESSAGE not found")
                if not ui_lib.wait_for_element(i3sBuildPlanPage.OEBP_INVALID_NAME_RESOLUTION):                    
                    logger._warn("OEBP_INVALID_NAME_RESOLUTION not found")
                if not ui_lib.wait_for_element(i3sBuildPlanPage.OEBP_INVALID_NAME_DETAILS):                    
                    logger._warn("OEBP_INVALID_NAME_DETAILS not found")
                return_to_create_bppage()
                continue
            if (desc_flag ==0):      
                if not ui_lib.wait_for_element(i3sBuildPlanPage.ID_BLANK_DESCRIPTION):
                    logger._warn("ID_BLANK_DESCRIPTION not found")
                return_to_create_bppage()
                continue
            if (len(oebp.description) > 1000):
                logger._log_to_console_and_log_file("inside desc greater than 1000 chars")
                if not ui_lib.wait_for_element(i3sBuildPlanPage.OEBP_INVALID_DESCRIPTION_MESSAGE):                   
                    logger._warn("OEBP_INVALID_DESCRIPTION_MESSAGE not found ")
                if not ui_lib.wait_for_element(i3sBuildPlanPage.OEBP_INVALID_DESCRIPTION_RESOLUTION):                    
                    logger._warn("OEBP_INVALID_DESCRIPTION_RESOLUTION not found ")
                if not ui_lib.wait_for_element(i3sBuildPlanPage.OEBP_INVALID_DESCRIPTION_DETAILS):                    
                    logger._warn("OEBP_INVALID_DESCRIPTION_DETAILS not found ")
                return_to_create_bppage()
                continue           
            if dup_name_flag:               
                if not ui_lib.wait_for_element(i3sBuildPlanPage.OEBP_DUPLICATE_NAME_MESSAGE):                                        
                    logger._warn("OEBP_DUPLICATE_NAME_MESSAGE not found")
                if not ui_lib.wait_for_element(i3sBuildPlanPage.OEBP_DUPLICATE_NAME_RESOLUTION):                    
                    logger._warn("OEBP_DUPLICATE_NAME_RESOLUTION not found")   
                if not ui_lib.wait_for_element(i3sBuildPlanPage.OEBP_DUPLICATE_NAME_DETAILS):                    
                    logger._warn("OEBP_DUPLICATE_NAME_DETAILS not found")
                return_to_create_bppage()                
                continue              
            if special_char_flag:
                logger._log_to_console_and_log_file("inside special char flag loop")
                if not ui_lib.wait_for_element(i3sBuildPlanPage.OEBP_INVALID_NAME_MESSAGE):                    
                    logger._warn("OEBP_INVALID_NAME_MESSAGE not found ")
                if not ui_lib.wait_for_element(i3sBuildPlanPage.OEBP_INVALID_NAME_RESOLUTION):                     
                    logger._warn("OEBP_INVALID_NAME_RESOLUTION not found ")                    
                if not ui_lib.wait_for_element_visible(i3sBuildPlanPage.OEBP_INVALID_NAME_DETAILS):                    
                    logger._warn("OEBP_INVALID_NAME_DETAILS not found ")                
                return_to_create_bppage()
                continue                    
                  
            logging._log_to_console_and_log_file("\nCreating Buildplan please wait ...\n")
                    
            if (oebp.button=='create'):                
                if ui_lib.wait_for_element(i3sBuildPlanPage.ID_ELEMENT_BUILDPLAN % oebp.name):                    
                    ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_CREATE_BP)
                    if (ui_lib.wait_for_element_visible(i3sBuildPlanPage.ID_CREATE_BP_PAGE)):                    
                        logger._log_to_console_and_log_file("Opened OEBP UI create")
                    continue                    
                else:
                    logger._log_to_console_and_log_file("Creating Buildplan %s failed" % oebp.name)
                    continue
            if (oebp.button=='create+'):               
                ''' for create+ the page goes back remains in OEBP create page after success of OEBP creation'''
                if ui_lib.wait_for_element_visible(i3sBuildPlanPage.ID_CREATE_BP_PAGE):
                    logger._log_to_console_and_log_file("In OEBP Create UI")                    
                    continue
                else:
                    logger._warn("Failed to return to OEBP Create UI")                            
                    continue          
        elif (oebp.button=='cancel'):            
            return_to_create_bppage()
            if not ui_lib.wait_for_element(i3sBuildPlanPage.ID_PAGE_LABEL):                   
                logger._warn("Failed to navigate to OE BuildPlan page")
            else:
                if not ui_lib.wait_for_element_visible(i3sBuildPlanPage.ID_ELEMENT_BUILDPLAN % oebp.name):
                    logger._warn("BuildPlan '%s' not created " % oebp.name)
                else:
                    logger._warn("Test failed, BuildPlan '%s' created " % oebp.name)
                if ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_CREATE_BP):
                    ui_lib.wait_for_element_visible(i3sBuildPlanPage.ID_CREATE_BP_PAGE)                    
            continue                  
    return                          
                        
  
def edit_oebuildplan(self, *editoebuildplan_obj):
    """ Select Edit BuildPalns 
        Example:
        | Edit Buildplans     |     |
    """
    s2l = ui_lib.get_s2l()
    """ Navigate to BuildPlan Page """   
        
    if not s2l._is_element_present(i3sBuildPlanPage.ID_PAGE_LABEL):
        navigate()
        
    """ Retrieve data from datasheet """
    if type(editoebuildplan_obj) is test_data.DataObj:
            editoebuildplan_obj = [editoebuildplan_obj]
    elif type(editoebuildplan_obj) is tuple:
        editoebuildplan_obj = list(editoebuildplan_obj[0])
            
    for oebp in editoebuildplan_obj:  
        if s2l._page_contains(oebp.name):
            oedp_Obj = i3sBuildPlanPage.ID_ELEMENT_BUILDPLAN % oebp.name
            s2l.mouse_over(oedp_Obj)
            ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_ELEMENT_BUILDPLAN % oebp.name)
            ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_BUTTON_ACTION)         
            ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_BUTTON_EDIT)  
        
            ''' Below are flags to track invalid inputs'''
            name_flag=1
            desc_flag=1            
            dup_name_flag=0
            special_char_flag=1
                        
            ''' In the below code, flags are set/unset based on the validity of the input parameters'''            
            if (hasattr(oebp, "newName")):               
                if re.search('^[a-zA-Z_]', oebp.newName):
                    special_char_flag=0   
                if (oebp.newName == "" ):
                    name_flag=0  
                    
                """ Before Adding check for the Buildplan exists """
                if name_flag:
                    if s2l._is_element_present(i3sBuildPlanPage.ID_ELEMENT_BUILDPLAN % oebp.newName):   
                        ''' set dup_name_flag to true if name already exists'''
                        dup_name_flag=1                
                ui_lib.wait_for_element_and_input_text(i3sBuildPlanPage.ID_EDIT_NAME, oebp.newName)   
                        
            if (hasattr(oebp, "description")):
                if (oebp.description == "" ):
                    desc_flag=0                   
                ui_lib.wait_for_element_and_input_text(i3sBuildPlanPage.ID_EDIT_DESCRIPTION, oebp.description)       
            if (hasattr(oebp, "ostype")):
                ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_EDIT_OSTYPE_DROPDOWN)               
                ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_EDIT_OSTYPE)             
            
            if (oebp.button == 'edit'):
                if (hasattr(oebp, "step")):
                        logger._log_to_console_and_log_file("Buildstep to be specified before clicking edit button")
                else:
                    ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_EDIT_OK_BUTTON)         
                       
                if (name_flag == 0 or desc_flag ==0):                    
                    if (name_flag == 0):  
                        if not ui_lib.wait_for_element(i3sBuildPlanPage.ID_BLANK_NAME):                            
                            logger._warn("ID_BLANK_NAME not found")                        
                    if (desc_flag == 0):                          
                        if not ui_lib.wait_for_element(i3sBuildPlanPage.ID_BLANK_DESCRIPTION):
                            logger._warn("ID_BLANK_DESCRIPTION not found")                                             
                    ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_EDIT_CANCEL_BUTTON)
                    ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_CANCEL_CONFIRM_FORM_PROCEED)  
                    continue
                elif (hasattr(oebp, "newName") or hasattr(oebp, "description") or hasattr(oebp, "ostype")):    
                    if (hasattr(oebp, "description")):                    
                        if (desc_flag == 0):                                               
                            if not ui_lib.wait_for_element(i3sBuildPlanPage.ID_BLANK_DESCRIPTION):
                                logger._warn("ID_BLANK_DESCRIPTION not found")
                                ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_EDIT_CANCEL_BUTTON)
                                ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_CANCEL_CONFIRM_FORM_PROCEED)
                                continue                         
                        elif (len(oebp.description) > 1000):                            
                            if not ui_lib.wait_for_element(i3sBuildPlanPage.OEBP_INVALID_UPDATE_DESCRIPTION_MESSAGE):                            
                                logger._warn("OEBP_INVALID_DESCRIPTION_MESSAGE not found ")
                            if not ui_lib.wait_for_element(i3sBuildPlanPage.OEBP_INVALID_DESCRIPTION_RESOLUTION):                            
                                logger._warn("OEBP_INVALID_DESCRIPTION_RESOLUTION not found ")
                            if not ui_lib.wait_for_element(i3sBuildPlanPage.OEBP_INVALID_DESCRIPTION_DETAILS):                            
                                logger._warn("OEBP_INVALID_DESCRIPTION_DETAILS not found ")
                            ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_EDIT_CANCEL_BUTTON)
                            ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_CANCEL_CONFIRM_FORM_PROCEED)
                            continue                                                     
                        else:
                            logger._log_to_console_and_log_file("Updated Description to '%s'" % oebp.description)                
                            if not ui_lib.wait_for_element(i3sBuildPlanPage.ID_EDIT_DESC_CHECK %oebp.description):
                                logger._warn("Failed to update oebp %s description: %s" % (oebp.name, oebp.description))                                                            
                            else:
                                logger._log_to_console_and_log_file("Updated Description to '%s'" % oebp.description)
                            continue 
                
                    if (hasattr(oebp, "newName")):
                        if (name_flag==0):                
                            if not ui_lib.wait_for_element(i3sBuildPlanPage.ID_BLANK_NAME):                           
                                logger._warn("ID_BLANK_NAME not found")
                            ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_EDIT_CANCEL_BUTTON)                  
                            ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_CANCEL_CONFIRM_FORM_PROCEED)
                            continue 
                        elif dup_name_flag:                            
                            if not ui_lib.wait_for_element(i3sBuildPlanPage.OEBP_DUPLICATE_NAME_UPDATE_MESSAGE):                                
                                logger._warn("OEBP_DUPLICATE_NAME_UPDATE_MESSAGE not found")
                            if not ui_lib.wait_for_element(i3sBuildPlanPage.OEBP_DUPLICATE_NAME_RESOLUTION):
                                logger._warn("OEBP_DUPLICATE_NAME_MESSAGE not found")   
                            if not ui_lib.wait_for_element(i3sBuildPlanPage.OEBP_DUPLICATE_NAME_DETAILS):
                                logger._log_to_console_and_log_file("OEBP_DUPLICATE_NAME_MESSAGE not found")
                            ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_EDIT_CANCEL_BUTTON)
                            ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_CANCEL_CONFIRM_FORM_PROCEED)
                            continue 
                        elif special_char_flag:                            
                            if not ui_lib.wait_for_element(i3sBuildPlanPage.OEBP_INVALID_UPDATE_NAME_MESSAGE):
                                logger._warn("OEBP_INVALID_UPDATE_NAME_MESSAGE not found ")
                            if not ui_lib.wait_for_element(i3sBuildPlanPage.OEBP_INVALID_NAME_RESOLUTION):
                                logger._warn("OEBP_INVALID_NAME_RESOLUTION not found ")
                            if not ui_lib.wait_for_element(i3sBuildPlanPage.OEBP_INVALID_NAME_DETAILS): 
                                logger._warn("OEBP_INVALID_NAME_DETAILS not found ")
                            ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_EDIT_CANCEL_BUTTON)
                            ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_CANCEL_CONFIRM_FORM_PROCEED)
                            continue 
                        elif (len(oebp.newName) > 255):                            
                            if not ui_lib.wait_for_element(i3sBuildPlanPage.OEBP_INVALID_UPDATE_NAME_MESSAGE):                                
                                logger._warn("OEBP_INVALID_UPDATE_NAME_MESSAGE not found")
                            if not ui_lib.wait_for_element(i3sBuildPlanPage.OEBP_INVALID_NAME_RESOLUTION):                                
                                logger._warn("OEBP_INVALID_NAME_RESOLUTION not found")
                            if not ui_lib.wait_for_element(i3sBuildPlanPage.OEBP_INVALID_NAME_DETAILS):                               
                                logger._warn("OEBP_INVALID_NAME_DETAILS not found")
                            ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_EDIT_CANCEL_BUTTON)
                            ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_CANCEL_CONFIRM_FORM_PROCEED)
                            continue      
                        else:                            
                            if not ui_lib.wait_for_element_visible(i3sBuildPlanPage.ID_ELEMENT_BUILDPLAN % oebp.newName, PerfConstants.SUCCESS_TIME):
                                logger._warn("Failed to update with newName: %s" % oebp.newName)
                            else:
                                logger._log_to_console_and_log_file("Updated Name to '%s'" % oebp.newName)
                            continue 
                    if (hasattr(oebp, "ostype")):                     
                        if not ui_lib.wait_for_element(i3sBuildPlanPage.ID_EDIT_OSTYPE_CHECK %oebp.ostype):
                            logger._warn("Failed to update oebp %s ostype: %s" % (oebp.name, oebp.ostype))
                                
                        else:
                            logger._log_to_console_and_log_file("Updated Ostype to '%s'" % oebp.ostype)
                        continue 
                        
                elif (hasattr(oebp, "step")):                    
                    if not ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_EDIT_BUILDSTEP):
                            logger._warn("Failed to click on Add Step") 
                            continue                    
                    if not ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_EDIT_BUILDSTEP_DROPDOWN):
                        logger._warn("Failed to get the buildstep dropdown \n")                    
                    if not ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_INPUT_BUILDSTEP % oebp.step):
                            logger._warn("Failed to select the buildstep")   
                    if (oebp.step_button == "cancel"):
                        ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_EDIT_BUILDSTEP_CANCEL)
                    elif (oebp.step_button == "ok"):
                        ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_EDIT_BUILDSTEP_OK)
                    if ui_lib.wait_for_element_visible(i3sBuildPlanPage.ID_EDIT_FORM):  # Wait for form to visible
                        if (oebp.edit_button == "cancel"):
                            ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_EDIT_CANCEL_BUTTON)
                            logger._warn("Cancel clicked, buildstep should not be added")
                        elif (oebp.edit_button == "ok"):
                            ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_EDIT_OK_BUTTON) 
                    else:
                        logger._warn("Form is not visible")
                        continue 
                  
                    if (oebp.step_button == "ok" and oebp.edit_button == "ok"):
                        if (s2l._is_element_present(i3sBuildPlanPage.ID_ELEMENT_BUILDPLAN % oebp.step)):
                            logger._log_to_console_and_log_file("Buildstep added successfully \n")
                    if (oebp.step_button == "ok" and oebp.edit_button == "cancel"):
                        if (s2l._is_element_present(i3sBuildPlanPage.ID_ELEMENT_BUILDPLAN % oebp.step)):
                            logger._log_to_console_and_log_file("Test failed, Buildstep successfully added with Cancel button \n")
                    if (oebp.step_button == "cancel" and oebp.edit_button == "cancel" or oebp.edit_button == "ok"):
                        if (s2l._is_element_present(i3sBuildPlanPage.ID_ELEMENT_BUILDPLAN % oebp.step)):
                            logger._log_to_console_and_log_file("Test failed, Buildstep successfully added with Cancel button \n")
                    continue
                          
            if (oebp.button=='cancel'):                
                ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_EDIT_CANCEL_BUTTON)
                ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_CANCEL_CONFIRM_FORM_PROCEED)   
                if ui_lib.wait_for_element(i3sBuildPlanPage.ID_PAGE_LABEL):               
                    logger._log_to_console_and_log_file("returned successfully to OEBP UI") 
                else:
                    logger._warn("Failed to return to OEBP UI post clicking cancel in Edit OEBP UI")               
           
                continue    
                                    
        else:
            logger._warn("Failed to edit the deployment plan as the name provided does not exist on the OEBP UI page")
            continue
            
    return                 

def delete_oebuildplan(self, *deleteoebuildplan_obj):
    """ Delete BuildPlan
     Example:
        | remove buildplan      | ${oebpName}    |
    """
    s2l = ui_lib.get_s2l()
    """ Navigate to BuildPlan Page """
    if not s2l._is_element_present(i3sBuildPlanPage.ID_PAGE_LABEL):
        navigate()
    ui_lib.wait_for_element(i3sBuildPlanPage.ID_BP_VISIBLE)

    """ Retrieve data from datasheet """
    if type(deleteoebuildplan_obj) is test_data.DataObj:
        deleteoebuildplan_obj = [deleteoebuildplan_obj]
    elif type(deleteoebuildplan_obj) is tuple:
        deleteoebuildplan_obj = list(deleteoebuildplan_obj[0])
        
    for oebp in deleteoebuildplan_obj:
        if s2l._page_contains(oebp.name):
            oebp_Obj = i3sBuildPlanPage.ID_ELEMENT_BUILDPLAN % oebp.name
            s2l.mouse_over(oebp_Obj)
            ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_ELEMENT_BUILDPLAN % oebp.name)
            ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_BUTTON_ACTION)
            if s2l._is_visible(i3sBuildPlanPage.ID_BUTTON_DELETE):                
                ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_BUTTON_DELETE)
                if ui_lib.wait_for_element_visible(i3sBuildPlanPage.ID_DELETE_FORM):  # Wait for form to visible
                    if (oebp.button == "delete"):
                        ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_YES_DELETE_BUTTON)
                    elif (oebp.button == "cancel"):
                        ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_CANCEL_DELETE_BUTTON)
                        logger._log_to_console_and_log_file(" BuildPlan '%s' not deleted as Cancel was chosen" % oebp.name) 
                        continue
                else:
                    logger._warn("Form is not visible")
                    continue                 
                '''Validating BuildPlan removal'''
                if ui_lib.wait_for_element_remove(i3sBuildPlanPage.ID_ELEMENT_BUILDPLAN % str(oebp.name), PerfConstants.REMOVE_SERVER):
                    logger._log_to_console_and_log_file("Removed BuildPlan '%s'" % oebp.name)                    
                else:
                    logger._warn("FAILED :: BuildPlan can't be removed - '%s'" % oebp.name)          
                  
            else:
                logger._warn("'%s' BuildPlan can't be deleted, delete option is not visible on page." % oebp.name)                
        else:
            logger._warn("'%s' BuildPlan not found in Buildplan page" % oebp.name)
            continue 
    return          
                               
       
def copy_oebuildplan(self, *copyoebuildplan_obj):
    """ Copy  BuildPlan
     Example:
        | Copy buildplan      | ${copyName}    |
    """
    s2l = ui_lib.get_s2l()
    """ Navigate to DeploymentPlan Page """
    if not s2l._is_element_present(i3sBuildPlanPage.ID_PAGE_LABEL):
        navigate()
    ui_lib.wait_for_element(i3sBuildPlanPage.ID_BP_VISIBLE)

    """ Retrieve data from datasheet """
    if type(copyoebuildplan_obj) is test_data.DataObj:
        copyoebuildplan_obj = [copyoebuildplan_obj]
    elif type(copyoebuildplan_obj) is tuple:
        copyoebuildplan_obj = list(copyoebuildplan_obj[0]) 
                
    for oebp in copyoebuildplan_obj:
        if s2l._page_contains(oebp.name):
            oedp_Obj = i3sBuildPlanPage.ID_ELEMENT_BUILDPLAN % oebp.name
            s2l.mouse_over(oedp_Obj)
            ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_ELEMENT_BUILDPLAN % oebp.name)
            ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_BUTTON_ACTION)
            if s2l._is_visible(i3sBuildPlanPage.ID_BUTTON_COPY):
                logger._log_to_console_and_log_file("Copy Buidlplan '%s'" % oebp.name)
                ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_BUTTON_COPY)
                
                ''' Below are flags to track invalid inputs'''
            name_flag=1                       
            dup_name_flag=0
            special_char_flag=1
                            
            ''' In the below code, flags are set/unset based on the validity of the input parameters'''
            
            if (hasattr(oebp, "copyName")):               
                if re.search('^[a-zA-Z_]', oebp.copyName):
                    special_char_flag=0   
                if (oebp.copyName == "" ):
                    name_flag=0  
                    
                """ Before Adding check for the Buildplan exists """
                if name_flag:
                    if s2l._is_element_present(i3sBuildPlanPage.ID_ELEMENT_BUILDPLAN % oebp.copyName):   
                        ''' set dup_name_flag to true if name already exists'''
                        dup_name_flag=1                
            
                if (oebp.button == "copy"):
                    ui_lib.wait_for_element_visible(i3sBuildPlanPage.ID_COPY_FORM)
                    ui_lib.wait_for_element_and_input_text(i3sBuildPlanPage.ID_EDIT_COPY_NAME, oebp.copyName)
                    ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_COPY_OK_BUTTON)
                        
                    '''checking for only blank name error message'''
                    if (name_flag==0): 
                        if not ui_lib.wait_for_element(i3sBuildPlanPage.ID_BLANK_NAME):                           
                            logger._warn("ID_BLANK_NAME not found")
                        ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_COPY_CANCEL_BUTTON)                  
               
                    elif dup_name_flag:                        
                        if not ui_lib.wait_for_element(i3sBuildPlanPage.OEBP_DUPLICATE_NAME_COPY_MESSAGE):
                            logger._warn("OEBP_DUPLICATE_NAME_COPY_MESSAGE not found")
                        if not ui_lib.wait_for_element(i3sBuildPlanPage.OEBP_DUPLICATE_NAME_RESOLUTION):
                            logger._warn("OEBP_DUPLICATE_NAME_MESSAGE not found") 
                        ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_COPY_CANCEL_BUTTON)
                    elif special_char_flag:                        
                        if not ui_lib.wait_for_element(i3sBuildPlanPage.OEBP_INVALID_NAME_COPY_MESSAGE):
                            logger._warn("OEBP_INVALID_NAME_COPY_MESSAGE not found ")
                        if not ui_lib.wait_for_element(i3sBuildPlanPage.OEBP_INVALID_NAME_RESOLUTION):
                            logger._warn("OEBP_INVALID_NAME_RESOLUTION not found ")
                        ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_COPY_CANCEL_BUTTON)
                    elif (len(oebp.copyName) > 255):                        
                        if not ui_lib.wait_for_element(i3sBuildPlanPage.OEBP_INVALID_NAME_COPY_MESSAGE):                                
                            logger._warn("OEBP_INVALID_UPDATE_NAME_MESSAGE not found")
                        if not ui_lib.wait_for_element(i3sBuildPlanPage.OEBP_INVALID_NAME_RESOLUTION):                                
                            logger._warn("OEBP_INVALID_NAME_RESOLUTION not found")                    
                        ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_COPY_CANCEL_BUTTON)          
                    
                    else:                        
                        if not ui_lib.wait_for_element_visible(i3sBuildPlanPage.ID_ELEMENT_BUILDPLAN % oebp.copyName, PerfConstants.SUCCESS_TIME):
                            logger._warn("Failed to copy with copyName: %s" % oebp.copyName)
                        else:
                            logger._log_to_console_and_log_file("Copy Name to '%s' successfull " % oebp.copyName)
                        continue   
                elif (oebp.button == "cancel"):
                    ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_COPY_CANCEL_BUTTON)
                    logger._log_to_console_and_log_file(" BuildPlan '%s' not copied as Cancel was chosen" % oebp.name) 
                    continue
            else:
                ui_lib.wait_for_element_and_click(i3sBuildPlanPage.ID_COPY_OK_BUTTON)                
                copy_name=oebp.name+str('_copy')
                if not ui_lib.wait_for_element_visible(i3sBuildPlanPage.ID_ELEMENT_BUILDPLAN % copy_name, PerfConstants.SUCCESS_TIME):
                    logger._warn("Failed to copy with copyName: %s" % copy_name)
                else:
                    logger._log_to_console_and_log_file("Copy Name to '%s' successful" % copy_name)
                continue                
        
        else:
            logger._warn("'%s' BuildPlan not found in Buildplan page" % oebp.name)
            continue 
    return    

        
 