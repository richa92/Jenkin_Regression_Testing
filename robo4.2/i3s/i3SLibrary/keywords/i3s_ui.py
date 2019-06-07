'''
RobotGalaxyLibrary keywords

'''
from i3SLibrary.ui.general import login_page
from i3SLibrary.ui.general import base_page
from i3SLibrary.ui import goldenimageui
from i3SLibrary.ui import planscriptsui
from i3SLibrary.ui import oebuildplan
from i3SLibrary.ui import oedeploymentplan


class i3SUIKeywords(object):

    ##########################################################################
    # Login page functions
    ##########################################################################
    def i3s_ui_login_to_appliance(self, user_name):
        """ Login to the fusion appliance
        Example:
        | Fusion UI Login to Appliance | Administrator |
        """
        return login_page.login(user_name)


    def i3s_ui_logout_of_appliance(self):
        """ Log out of the Fusion appliance
        Example:
        | i3S UI |
            """
        base_page.logout()

    # #########################################################################
    # Create/Edit/Delete Golden Image functions
    # #########################################################################
    class   i3SUIgoldenimageKeywords(object):

        def i3s_ui_add_goldenImage(self, *addgoldenimageui_obj):
            """ Add GI in to the i3S appliance
            Example:
            | i3S UI Select AddGoldenImage |
            """
            return goldenimageui.add_goldenimage(self, addgoldenimageui_obj)


        def i3s_ui_edit_goldenImage(self, *editgoldenimageui_obj):
            """ Edit GI in to the i3S appliance
            Example:
            | i3S UI Select EditGoldenImage |
            """
            return goldenimageui.edit_goldenimage(self, editgoldenimageui_obj)


        def i3s_ui_delete_goldenImage(self, *deletegoldenimageui_obj):
            """ Delete GI in to the i3S appliance
            Example:
            | i3S UI Select DelGoldenImage |
            """
            return goldenimageui.delete_goldenimage(self, deletegoldenimageui_obj)

    # #########################################################################
    # Create/Edit/Delete Plan Script functions
    # #########################################################################

    class   i3SUIplanscriptsKeywords(object):

        def i3s_ui_create_planScripts(self, *createplanscript_obj):
            """ Create PS in the i3S appliance
            Example:
            | i3S UI Select CreateplanScripts |
            """
            return planscriptsui.create_planscript(self, createplanscript_obj)

        def i3s_ui_edit_planScripts(self, *editplanscript_obj):
            """ Edit PS in the i3S appliance
            Example:
            | i3S UI Select EditplanScripts |
            """
            return planscriptsui.edit_planscript(self, editplanscript_obj)

        def i3s_ui_copy_planScripts(self, *copyplanscript_obj):
            """ Copy PS in the i3S appliance
            Example:
            | i3S UI Select CopyplanScripts |
            """
            return planscriptsui.copy_planscript(self, copyplanscript_obj)

        def i3s_ui_delete_planScripts(self, *deleteplanscript_obj):
            """ Delete PS in the i3S appliance
            Example:
            | i3S UI Select delplanScripts |
            """
            return planscriptsui.delete_planscript(self, deleteplanscript_obj)


    # #########################################################################
    # Create/Edit/Delete Deploymentplan functions
    # #########################################################################

    class   i3SUIOEDeploymentPlanKeywords(object):

        def i3s_ui_create_oedeploymentplan(self, *createoedeploymentplan_obj):
            """ Create OEDP in the i3S appliance
            Example:
            | i3S UI Createdeploymentplans |
            """
            return oedeploymentplan.create_oedeploymentplan(self, createoedeploymentplan_obj)

        def i3s_ui_edit_oedeploymentplan(self, *editoedeploymentplan_obj):
            """ Edit PS in the i3S appliance
            Example:
            | i3S UI Select EditplanScripts |
            """
            return oedeploymentplan.edit_oedeploymentplan(self, editoedeploymentplan_obj)

        def i3s_ui_delete_oedeploymentplan(self, *deleteoedeploymentplan_obj):
            """ Delete PS in the i3S appliance
            Example:
            | i3S UI Select delplanScripts |
            """
            return oedeploymentplan.delete_oedeploymentplan(self, deleteoedeploymentplan_obj)
    # #########################################################################
    # Create/Edit/Delete/copy Buildplan functions
    # #########################################################################

    class   i3SUIOEBuildPlanKeywords(object):

        def i3s_ui_create_oebuildplan(self, *createoebuildplan_obj):
            """ Create OEBP in the i3S appliance
            Example:
            | i3S UI Create Buildplans |
            """
            return oebuildplan.create_oebuildplan(self, createoebuildplan_obj)

        def i3s_ui_edit_oebuildplan(self, *editoebuildplan_obj):
            """ Edit OEBP in the i3S appliance
            Example:
            | i3S UI Select Edit Buildplans |
            """
            return oebuildplan.edit_oebuildplan(self, editoebuildplan_obj)

        def i3s_ui_delete_oebuildplan(self, *deleteoebuildplan_obj):
            """ Delete OEBP in the i3S appliance
            Example:
            | i3S UI Select Delete Buildplans|
            """
            return oebuildplan.delete_oebuildplan(self, deleteoebuildplan_obj)

        def i3s_ui_copy_oebuildplan(self, *copyoebuildplan_obj):
            """ Copy OEBP in the i3S appliance
            Example:
            | i3S UI Select copy Buidlplans |
            """
            return oebuildplan.copy_oebuildplan(self, copyoebuildplan_obj)


