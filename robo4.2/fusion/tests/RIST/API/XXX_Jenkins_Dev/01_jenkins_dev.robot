*** Settings ***
Documentation                   JenkinsDev
...                             This is a dummy test for Developing Jenkins Jobs.
...                             Used to run something without fear of disturbing or breaking a real Jenkins Job
...                             All it reall does is a login / logout into the passed in APPLIANCE_IP
...                             And one simple GET call

Library                         FusionLibrary
Library                         RoboGalaxyLibrary

Suite Setup               	    Run Keywords    Should Not Be Equal As Strings    ${APPLIANCE_IP}    APPLIANCE_IP
...                             AND    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}
Suite Teardown                  Fusion Api Logout Appliance

Resource                        ./../../../../Resources/api/fusion_api_resource.txt
Resource                        ../global_variables.robot

Variables 		                ${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}                 APPLIANCE_IP

*** Test Cases ***
Jenkins Dev
    Set Log Level	DEBUG
    Log Variables
    
    ${encs} =  Fusion Api Get Enclosures

    ${enc} =    Get Enclosure    CN754404R6

    ${validate_status} =    Fusion api validate response follow    ${encR6}    ${enc}    wordy=${true}
    Should Be Equal As Strings    ${validate_status}    True

