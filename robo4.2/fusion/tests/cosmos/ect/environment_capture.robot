*** Settings ***
Library    environment_collector

*** Variables ***
${oneview_ip}
${oneview_username}
${oneview_password}
${oneview_version}
${operating_systems}
${use_case}

*** Test Cases ***
First Test Case
    log    ${oneview_ip}
    log    ${oneview_username}
    log    ${oneview_password}
    log    ${oneview_version}
    log    ${operating_systems}
    log    ${use_case}

Validate Variables
    ${ret} =    validate_parameters    oneview_ip=${oneview_ip}    oneview_username=${oneview_username}    oneview_password=${oneview_password}    oneview_version=${oneview_version}    operating_systems=${operating_systems}    use_case=${use_case}
    Should Be Equal As Strings    True    ${ret}
