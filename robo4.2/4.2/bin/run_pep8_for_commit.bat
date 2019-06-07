@echo off
REM Get the commit hash
FOR /F "delims=" %%i IN ('git rev-parse HEAD') DO set COMMIT=%%i
echo Commit hash is %COMMIT%

REM PEP8 Check
for /f "delims==" %%i in ('git diff-tree --no-commit-id --name-only --diff-filter=ACM -r %COMMIT%') do (
    echo Running pep8 for %%i
    pep8 --config=.pep8 %%i
)
