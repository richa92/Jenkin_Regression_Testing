# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
'''

This file contains all element ID on oebuildplan page/screen
'''

class i3sBuildPlanPage(object):
    ID_PAGE_LABEL = "xpath=//*[@id='oebuildplans-page']/*/*/*[text()='OE Build Plans']"   
    ID_BP_VISIBLE= "xpath=//*[@id='DataTables_Table_0_wrapper']/div/div[2]"    
    
    ID_CREATE_BP = "xpath=//*[@id='oebuildplans-page']//a[text()='Create OE Build Plan']"    
    ID_CREATE_BP_PAGE = "xpath=//span[@class='hp-action hp-ellipsised' and text()='Create OE Build Plan']"
    ID_ELEMENT_BUILDPLAN = "xpath=//td[text()='%s']"  # Replace %s with buildplan
    
    ID_INPUT_NAME = "xpath=//*[@id='oebuildplans-create-name']"
    ID_INPUT_DESCRIPTION = "xpath=//*[@id='oebuildplans-create-description']"
    ID_INPUT_OSTYPE_DROPDOWN = "xpath=//*[@id= 'oebuildplans-create-ostype']" 
    ID_INPUT_OSTYPE = "xpath=//*[@id= 'oebuildplans-create-ostype']/option[text()='%s']"
    #ID_INPUT_OSTYPE_ESXI = "xpath=//*[@id='oebuildplans-create-ostype']/option[1]"
    #ID_INPUT_OSTYPE_HYPERV = "xpath=//*[@id='oebuildplans-create-ostype']/option[2]"
    #ID_INPUT_OSTYPE_KVM = "xpath=//*[@id='oebuildplans-create-ostype']/option[3]"    
    ID_INPUT_PLANTYPE_DROPDOWN = "xpath=//*[@id= 'oebuildplans-create-plantype']"   
    ID_INPUT_PLANTYPE = "xpath=//*[@id ='oebuildplans-create-plantype']//option[text()='%s']"
    #ID_INPUT_PLANTYPE_DEPLOY = "xpath=//*[@id ='oebuildplans-create-plantype']//option[2]"
    #ID_INPUT_PLANTYPE_CAPTURE = "xpath=//*[@id ='oebuildplans-create-plantype']//option[1]"        
    ID_INPUT_ARCHITECTURE = "xpath=//*[@id = 'oebuildplans-create-architecture']"
    
    
    ID_CREATE_BP_BUTTON = "xpath=//*[@id='oebuildplans-create']"
    #ID_CREATE_BP_BUTTON = "xpath=//*[@class='hp-button hp-secondary' and text()='Create OE Build Plan']"
    ID_CREATEPLUS_BP_BUTTON = "xpath=//*[@id='oebuildplans-create-again']"
    ID_CANCEL_BP_BUTTON = "xpath=//*[@id='oebuildplans-create-close']"
    ID_CANCEL_CONFIRM_FORM="xpath=//*[@id='hp-form-navigate-away-dialog']"
    ID_CANCEL_CONFIRM_FORM_PROCEED="xpath=//button[contains(text(),'Yes, proceed')]"
    ID_CANCEL_CONFIRM_FORM_CANCEL="xpath=//button[contains(text(),'Cancel')]"
    
    
    ID_BUTTON_ACTION = "xpath=//*[@id='oebuildplans-actions']/label"
    ID_BUTTON_DELETE = "xpath=//*[@id='oebuildplans-delete-action']"
    ID_BUTTON_EDIT = "xpath=//*[@id='oebuildplans-edit-action']"
    ID_BUTTON_CREATE = "xpath=//*[@id='oebuildplans-create-action']" 
    ID_BUTTON_COPY = "xpath=//*[@id='oebuildplans-saveas-action']"  
     
    ID_DELETE_FORM= "xpath= //*[@class='hp-action hp-ellipsised' and text()='Delete']"   
    ID_YES_DELETE_BUTTON = "//button[contains(text(),'Yes, delete')]"    
    ID_CANCEL_DELETE_BUTTON = "//button[contains(text(),'Cancel')]"
    
    ID_COPY_FORM= "xpath= //*[@class='hp-action hp-ellipsised' and text()='Save As']"   
    ID_EDIT_COPY_NAME="xpath=//*[@id='oebuildplans-saveas-name']"
    ID_COPY_OK_BUTTON = "xpath=//button[@data-localize='core.common.ok' and contains(text(),'OK')]"    
    ID_COPY_CANCEL_BUTTON = "xpath=//button[contains(text(),'Cancel')]"
        
    ID_EDIT_FORM= "xpath= //*[@class='hp-action hp-ellipsised' and text()='Edit']" 
    ID_EDIT_NAME = "xpath=//*[@id='oebuildplans-edit-name']"
    ID_EDIT_DESCRIPTION = "xpath=//*[@id='oebuildplans-edit-description']"
    ID_EDIT_OSTYPE_DROPDOWN = "xpath=//*[@id='oebuildplans-edit-ostype']"
    ID_EDIT_OSTYPE = "xpath=//*[@id='oebuildplans-edit-ostype']/x:option[text()='%s']"
    #ID_EDIT_OSTYPE_ESXI = "xpath=//*[@id='oebuildplans-edit-ostype']/x:option[1]"
    #ID_EDIT_OSTYPE_HYPERV = "xpath=//*[@id='oebuildplans-edit-ostype']/x:option[2]"
    #ID_EDIT_OSTYPE_KVM = "xpath=//*[@id='oebuildplans-edit-ostype']/x:option[3]"   
    ID_EDIT_OK_BUTTON = "xpath=//*[@id='oebuildplans-edit-ok']"
    ID_EDIT_CANCEL_BUTTON = "xpath=//*[@id='oebuildplans-edit-close']"
    
    
    ID_BP_VISIBLE= "xpath=//*[@id='DataTables_Table_0_wrapper']/div/div[2]"
        
    ID_EDIT_DESC_CHECK = "xpath=//*[@id='oebuildplans-show-description' and text()='%s']"
    ID_EDIT_OSTYPE_CHECK = "xpath=//*[@id='oebuildplans-show-ostype' and text()='%s']"
    
    ID_EDIT_BUILDSTEP="xpath=//*[@id='oebuildplans-edit-addstep' and text()='Add Step']"
    ID_EDIT_BUILDSTEP_DROPDOWN="xpath=html/body/div[2]/div[9]/div/div/div/form/div/fieldset/ol/li/div/div/div/div[2]"   
    ID_EDIT_BUILDSTEP_OK= "xpath=//button[@data-localize='core.common.ok' and contains(text(),'OK')]"    
    ID_EDIT_BUILDSTEP_CANCEL= "xpath=//button[@data-localize='core.common.cancel' and contains(text(), 'Cancel')]"
    ID_INPUT_BUILDSTEP = "//span[@class='hp-name' and text()='%s']"
    
    ID_BLANK_NAME= "xpath=//label[@for='buildplan-create-name' and text()='This field is required.']"
    ID_BLANK_DESCRIPTION= "xpath=//label[@for='buildplan-create-desc' and text()='This field is required.']"   
    
    
    OEBP_INVALID_NAME_MESSAGE = "xpath=//*[@id='hp-form-message']//span[text()='Unable to add OE Build Plan.']"     
    OEBP_INVALID_NAME_DETAILS = "xpath=//*[@id='hp-form-message']//span[text()='The value specified for the parameter name is not valid or not supported.']"
    OEBP_INVALID_NAME_RESOLUTION = "xpath=//*[@id='hp-form-message']//span[text()='The Name parameter cannot be null, can not be duplicate and  more than 255 characters. Verify parameters and try again']"
    OEBP_INVALID_UPDATE_NAME_MESSAGE = "xpath=//*[@id='hp-form-message']//span[text()='Unable to update OE Build Plan.']"
    OEBP_INVALID_NAME_COPY_MESSAGE = "xpath=//*[@id='hp-form-message']//span[text()='The value specified for the parameter name is not valid or not supported.']"
    OEBP_INVALID_DESCRIPTION_MESSAGE = "xpath=//*[@id='hp-form-message']//span[text()='Unable to add OE Build Plan.']"
    OEBP_INVALID_DESCRIPTION_DETAILS = "xpath=//*[@id='hp-form-message']//span[text()='The value specified for the parameter description is not valid or not supported.']"
    OEBP_INVALID_DESCRIPTION_RESOLUTION = "xpath=//*[@id='hp-form-message']//span[text()='Description cannot be null and can not be more than 1000 characters. Verify parameters and try again.']"    
    OEBP_INVALID_UPDATE_DESCRIPTION_MESSAGE = "xpath=//*[@id='hp-form-message']//span[text()='Unable to update OE Build Plan.']"
    
    OEBP_DUPLICATE_NAME_MESSAGE= "xpath=//*[@id='hp-form-message']//span[text()='Unable to add OE Build Plan.']"
    OEBP_DUPLICATE_NAME_DETAILS= "xpath=//*[@id='hp-form-message']//span[text()='Duplicate OE Build Plan Name']"
    OEBP_DUPLICATE_NAME_RESOLUTION= "xpath=//*[@id='hp-form-message']//span[text()='OE Build Plan name can not be duplicate. Verify parameters and try again.']"
    OEBP_DUPLICATE_NAME_COPY_MESSAGE= "xpath=//*[@id='hp-form-message']//span[text()='An OE Build Plan resource with the specified name already exists']"  
    OEBP_DUPLICATE_NAME_UPDATE_MESSAGE = "xpath=//*[@id='hp-form-message']//span[text()='Unable to update OE Build Plan.']"
    
    OEBP_INVALID_OSTYPE_MESSAGE= "xpath=//*[@id='hp-form-message']//span[text()='Unable to add OE Build Plan.']"
    OEBP_INVALID_OSTYPE_DETAILS= "xpath=//*[@id='hp-form-message']//span[text()='The value specified for the parameter ostype is not valid or not supported.']"
    OEBP_INVALID_OSTYPE_RESOLUTION= "xpath=//*[@id='hp-form-message']//span[text()=Input can have alphabets numbers and underscore only in any combination.']"    
    OEBP_INVALID_OSTYPE_UPDATE_MESSAGE = "xpath=//*[@id='hp-form-message']//span[text()='Unable to update OE Build Plan.']"    
    
    OEBP_INVALID_OEBUILDPLAN_TYPE_MESSAGE= "xpath=//*[@id='hp-form-message']//span[text()='Unable to add OE Build Plan.']"
    OEBP_INVALID_OEBUILDPLAN_TYPE_DETAILS= "xpath=//*[@id='hp-form-message']//span[text()='Only Deploy and Capture are valid values for OE Build Plan Type.']"
    OEBP_INVALID_OEBUILDPLAN_TYPE_RESOLUTION= "xpath=//*[@id='hp-form-message']//span[text()=Verify the parameters and try again.']"
    
        
    OEBP_INVALID_ARCH_MESSAGE= "xpath=//*[@id='hp-form-message']//span[text()='Unable to add OE Build Plan.']"
    OEBP_INVALID_ARCH_DETAILS= "xpath=//*[@id='hp-form-message']//span[text()='The value specified for the parameter architecture is not valid or not supported.']"
    OEBP_INVALID_ARCH_RESOLUTION= "xpath=//*[@id='hp-form-message']//span[text()=Input can have alphabets numbers and underscore only in any combination.']"
    
    OEBP_INVALID_BUILDSTEP_PARAMETER_MESSAGE="xpath=//*[@id='hp-form-message']//span[text()='Invalid Build Step Parameter.']"
    OEBP_INVALID_BUILDSTEP_PARAMETER_RESOLUTION="xpath=//*[@id='hp-form-message']//span[text()='Verify the parameters and try again. If the problem persists, contact your authorized support representative with a support dump.']"
    OEBP_INVALID_BUILDSTEP_PARAMETER_DETAILS="xpath=//*[@id='hp-form-message']//span[text()='Invalid value for Build Step Parameter.']"

    OEBP_INVALID_BUILDSTEP_SCRIPT_NAME_MESSAGE="xpath=//*[@id='hp-form-message']//span[text()='Invalid Build Step script.']"
    OEBP_INVALID_BUILDSTEP_SCRIPT_NAME_RESOLUTION="xpath=//*[@id='hp-form-message']//span[text()='Verify the parameters and try again. If the problem persists, contact your authorized support representative with a support dump.']"
    OEBP_INVALID_BUILDSTEP_SCRIPT_NAME_DETAILS="xpath=//*[@id='hp-form-message']//span[text()='Invalid value for  Build Step script uri.']"
       
    OEBP_INVALID_BUILDSTEP_SERIAL_NUMBER_MESSAGE="xpath=//*[@id='hp-form-message']//span[text()='Invalid Build Step serial number']"
    OEBP_INVALID_BUILDSTEP_SERIAL_NUMBER_RESOLUTION="xpath=//*[@id='hp-form-message']//span[text()='Verify the parameters and try again. If the problem persists, contact your authorized support representative with a support dump.']"
    OEBP_INVALID_BUILDSTEP_SERIAL_NUMBER_DETAILS="xpath=//*[@id='hp-form-message']//span[text()='Invalid value for Build Step serial number']"
    
    
    OEBP_INVALID_BUILDPLAN_MESSAGE="xpath=//*[@id='hp-form-message']//span[text()='Invalid OE Build Plan']" 
    OEBP_INVALID_BUILDPLAN_RESOLUTION="xpath=//*[@id='hp-form-message']//span[text()='Add Build Step. If the problem persists, contact your authorized support representative with a support dump.']"
    OEBP_INVALID_BUILDPLAN_DETAILS="xpath=//*[@id='hp-form-message']//span[text()='BuildPlan must contain atleast one Build step.']"
    
    OEBP_DUPLICATE_SCRIPT_URI_MESSAGE="xpath=//*[@id='hp-form-message']//span[text()='Duplicate Scripts found in the BuildPlan']"
    OEBP_DUPLICATE_SCRIPT_URI_RESOLUTION="xpath=//*[@id='hp-form-message']//span[text()='Remove duplicate scripts from BuildPlan. If the problem persists, contact your authorized support representative with a support dump.']"
    OEBP_DUPLICATE_SCRIPT_URI_DETAILS="xpath=//*[@id='hp-form-message']//span[text()='BuildPlan must not contain duplicate scripts.']"


    OEBP_DUPLICATE_SEQUENCE_NO_MESSAGE="xpath=//*[@id='hp-form-message']//span[text()='Duplicate sequence number found in the BuildPlan']"
    OEBP_DUPLICATE_SEQUENCE_NO_RESOLUTION="xpath=//*[@id='hp-form-message']//span[text()='Remove duplicate sequence no from BuildPlan. If the problem persists, contact your authorized support representative with a support dump.']"
    OEBP_DUPLICATE_SEQUENCE_NO_DETAILS="xpath=//*[@id='hp-form-message']//span[text()='BuildPlan must not contain duplicate sequence no.']"

    OEBP_PS_NOT_FOUND_ERROR_MESSAGE="xpath=//*[@id='hp-form-message']//span[text()='Could not find the specified PlanScript.']"
    OEBP_PS_NOT_FOUND_ERROR_RESOLUTION="xpath=//*[@id='hp-form-message']//span[text()='Specify valid Planscript and try again. If the problem persists, contact your authorized support representative with a support dump.']"
    OEBP_PS_NOT_FOUND_ERROR_DETAILS="xpath=//*[@id='hp-form-message']//span[text()='The PlanScript specified in OeBuildPlan does not exist']"

    OEBP_INCONSISTENT_OSTYPE_IN_PS_MESSAGE="xpath=//*[@id='hp-form-message']//span[text()='Specified PlanScript has inconsisten value of OS Type.']"
    OEBP_INCONSISTENT_OSTYPE_IN_PS_RESOLUTION="xpath=//*[@id='hp-form-message']//span[text()='Resolve the inconsistency between OS Type value of Plan Script and OeBuildPlan and Try again.If the problem persists, contact your authorized support representative with a support dump.']"
    OEBP_INCONSISTENT_OSTYPE_IN_PS_DETAILS="xpath=//*[@id='hp-form-message']//span[text()='The OS Type value of the specified PlanScript does not match with the OS Type value of OeBuildPlan.']"

    OEBP_INCONSISTENT_PLANTYPE_IN_PS_MESSAGE="xpath=//*[@id='hp-form-message']//span[text()='Specified PlanScript has inconsistent value of Plan Type.']"
    OEBP_INCONSISTENT_PLANTYPE_IN_PS_RESOLUTION="xpath=//*[@id='hp-form-message']//span[text()='Resolve the inconsistency between Plan Type value of Plan Script and OeBuildPlan and Try again.If the problem persists, contact your authorized support representative with a support dump.']"
    OEBP_INCONSISTENT_PLANTYPE_IN_PS_DETAILS="xpath=//*[@id='hp-form-message']//span[text()='The Plan Type value of the specified PlanScript does not match with the Plan Type value of  OeBuildPlan.']"
    
    OEBP_CANT_BE_DELETED_MESSAGE="xpath=//*[@id='hp-form-message']//span[text()='This BuildPlan can not be deleted']"
    OEBP_CANT_BE_DELETED_RESOLUTION="xpath=//*[@id='hp-form-message']//span[text()='Delete the OeDeploymentPlan which contains this BuildPlan and proceed with the deletion of this BuildPlan']"
    OEBP_CANT_BE_DELETED_DETAILS="xpath=//*[@id='hp-form-message']//span[text()='This BuildPlan is being used by a OeDeploymentPlan so it can not be deleted']"

    OEBP_CANT_BE_UPDATED_MESSAGE="xpath=//*[@id='hp-form-message']//span[text()='This BuildPlan can not be updated']"
    OEBP_CANT_BE_UPDATED_RESOLUTION="xpath=//*[@id='hp-form-message']//span[text()='Delete the OeDeploymentPlan which contains this BuildPlan and proceed with the updation of this BuildPlan']"
    OEBP_CANT_BE_UPDATED_DETAILS="xpath=//*[@id='hp-form-message']//span[text()='This BuildPlan is being used by a OeDeploymentPlan so it can not be updated']"  
    