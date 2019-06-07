@echo off
@REM This script will install using pip from your local folder.
@REM Note that it will download dependencies from the RoboGalaxyLibrary binary repository
@REM and will install in "development" mode.

@set EXPECTED=2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 20:40:30) [MSC v.1500 64 bit (AMD64)]

@for /f "tokens=*" %%f in ('python -c "import sys; print('{0}'.format(sys.version))"') do (@set ver=%%f)
@echo Python version is "%VER%"
@if NOT "%ver%"=="%EXPECTED%" (
    @echo(
    @echo *******************************************************************************
    @echo *                                   ERROR                                     *
    @echo *******************************************************************************
    @echo Your Python version is not supported by RoboGalaxyLibrary
    @echo Detected version: "%VER%"
    @echo Expected version: "%EXPECTED%"
    @echo(
    @echo Please see https://rndwiki.corp.hpecorp.net/confluence/display/RoboGalaxy/Getting+Started+With+RoboGalaxy+3.0
) else (
    set PIP_CONFIG_FILE=pip.ini
    python -m pip install -U pip
    python -m pip uninstall -y FusionLibrary RoboGalaxyLibrary
    python -m pip install -e .
)
