*** Settings ***
Library      RoboGalaxyLibrary
Library      FusionLibrary
Resource     ../resource/dcs_keywords.robot

*** Variables ***
${DCS_IP}                 172.17.4.137:9990
${FUSION_IP}              172.17.4.137
${FUSION_SSH_USERNAME}    root
${FUSION_SSH_PASSWORD}    hponeview
${FUSION_PROMPT}          \#
${FUSION_TIMEOUT}         500

*** Test Cases ***
Test DCS Schematic Management
    Restart DCS With New Schematic  demo
    ...                             ${FUSION_IP}
    ...                             ${FUSION_SSH_USERNAME}
    ...                             ${FUSION_SSH_PASSWORD}
    ...                             ${FUSION_PROMPT}
    ...                             ${FUSION_TIMEOUT}

    Verify DCS Status Running  ${FUSION_IP}
    ...                        ${FUSION_SSH_USERNAME}
    ...                        ${FUSION_SSH_PASSWORD}
    ...                        ${FUSION_PROMPT}
    ...                        ${FUSION_TIMEOUT}

    Verify DCS Schematic  demo
    ...                 ${FUSION_IP}
    ...                 ${FUSION_SSH_USERNAME}
    ...                 ${FUSION_SSH_PASSWORD}
    ...                 ${FUSION_PROMPT}
    ...                 ${FUSION_TIMEOUT}
