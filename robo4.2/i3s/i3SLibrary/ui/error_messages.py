# (C) Copyright 2015 Hewlett-Packard Development Company, L.P.
"""
    Deploymentplan UI Error messages
"""
OEDP_INVALID_NAME_MESSAGE = "Unable to create deployment plan. Check the validity of the input parameters\
                            The value specified for the parameter (Name) is not valid or not supported.\
                            OE Deployment Plan Name cannot be empty and should be unique and less than 256 characters. Verify parameters and try again.\
                            The value specified for the parameter is not valid or not supported."

OEDP_DUPLICATE_NAME_MESSAGE = "Unable to create deployment plan. Check the validity of the input parameters\
                              Deployment Plan with same name exists already.\
                              Deployment Plan with duplicate name cannot be added to the Appliance."

OEDP_INVALID_INPUT_MESSAGE = "Unable to create deployment plan. Check the validity of the input parameters\
                            Invalid characters in input.Input can have alphabets numbers and underscore only in any combination. Verify parameters and try again.\
                            The value specified for the parameter is not valid or not supported."

OEDP_INVALID_GI_URL_MESSAGE = "Unable to create deployment plan. Check the validity of the input parameters\
                              The value specified for the parameter (Golden Image) is not valid or not supported\
                              Golden Image parameter cannot be null or contain white space/TAB characters. Verify parameters and try again."

OEDP_INVALID_OEBP_URL_MESSAGE = "Unable to create deployment plan. Check the validity of the input parameters\
                                The value specified for the parameter (Oe Build Plan) is not valid or not supported.\
                                Oe Build Plan parameter cannot be null or contain white space/TAB characters. Verify parameters and try again."

OEDP_INVALID_INPUT_EDIT_MESSAGE = "Unable to edit deployment plan. Check the validity of the input parameters\
                              Invalid characters in input.\
                              Input can have alphabets numbers and underscore only in any combination."

OEDP_DUPLICATE_NAME_EDIT_MESSAGE = "Unable to edit deployment plan. Check the validity of the input parameters\
                              Deployment Plan with same name exists already.\
                              Deployment Plan with duplicate name cannot be added to the Appliance."

OEDP_INVALID_GI_URL_EDIT_MESSAGE = "Unable to edit deployment plan. Check the validity of the input parameters\
                              The value specified for the parameter (Golden Image) is not valid or not supported\
                              Golden Image parameter cannot be null or contain white space/TAB characters. Verify parameters and try again."

OEDP_INVALID_OEBP_URL_EDIT_MESSAGE = "Unable to edit deployment plan. Check the validity of the input parameters\
                                The value specified for the parameter (Oe Build Plan) is not valid or not supported.\
                                Oe Build Plan parameter cannot be null or contain white space/TAB characters. Verify parameters and try again."

OEDP_INVALID_INPUT_EDIT_MESSAGE = "Unable to edit deployment plan. Check the validity of the input parameters\
                              Invalid characters in input.\
                              Input can have alphabets numbers and underscore only in any combination."
							 
							 
"""
    GoldenImage UI Error messages
"""

GI_ADD_INVALID_NAME_MESSAGE = "Unable to add golden image. Check the validity for the input parameters\
                               The value specified for the parameter is not valid or not supported.\
                               The Name parameter cannot be null or contain special characters. Name should be unique and less than 256 characters. Verify parameters and try again."

GI_ADD_DUPLICATE_NAME_MESSAGE = "Unable to add golden image. Check the validity for the input parameters\
                                 Golden Image with same name already exists\
                                 Provide a different name for the new Golden Image."

GI_ADD_EMPTY_NAME_MESSAGE = "Enter a valid and unique name for golden image"
GI_ADD_EMPTY_DESCRIPTION_MESSAGE = "Provide description for the golden image"
GI_ADD_EMPTY_URL_MESSAGE = "Provide URL for the golden image"


GI_ADD_INVALID_URL_MESSAGE = "Unable to add golden image. Check the validity for the input parameters\
                              The value specified for the parameter source is not valid or not supported.\
                              Source URL parameter cannot be null or contain white space/TAB characters. Verify parameters and try again."

GI_EDIT_INVALID_NAME_MESSAGE = "Unable to update golden image.\
                                The value specified for the parameter is not valid or not supported.\
                                The Name parameter cannot be null or contain special characters. Name should be unique and less than 256 characters. Verify parameters and try again."
								
GI_EDIT_DUPLICATE_NAME_MESSAGE = "Unable to update golden image.\
                                 Golden Image with same name already exists.\
                                 Provide a different name for the new Golden Image."
