@echo off
REM Get the commit hash
FOR /F "delims=" %%i IN ('git rev-parse HEAD') DO set COMMIT=%%i
echo Commit hash is %COMMIT%

REM PyLint Check
for /f "delims==" %%i in ('git diff-tree --no-commit-id --name-only --diff-filter=ACM -r %COMMIT%') do (
    echo Running pylint for %%i
    pylint --rcfile=.pylintrc %%i
)
