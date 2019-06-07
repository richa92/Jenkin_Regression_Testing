def getFusionDirPath():
    import os
    import FusionLibrary

    return os.path.dirname(os.path.dirname(FusionLibrary.__file__))

FUSION_DIRPATH = getFusionDirPath()

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}