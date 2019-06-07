*** Settings ***
Documentation
...     This Test Suite uses administrator credentials to create multiple sessions and make them invalid session, then validate whether those invalid session are invalid.
...     Test Data is defined in Python Data Variable file.
Resource                       ../resource.txt

*** Test Cases ***
Expired Sessions Should Not Be Able to Login
    [Tags]    MULTIPLE-SESSION  C7000  T-BIRD
    [Documentation]     Generate multiple expired sessions and make sure it is invalid.
    ${sessions}=   Generate Bulk Expired Sessions   ${admin_credentials}    number_of_session=${number_of_session}
    Sessions Should Not Be Found     ${sessions}