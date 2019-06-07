*** Settings ***
Resource                        resource.txt
Suite Setup                     Scale Suite Setup     ${scaleuser_credentials}
Suite Teardown                  Scale Suite Teardown

*** Test Cases ***
Add LIG
    [Tags]    LIG   ADDLIG    ALT1
    [Documentation]        Add LIG to OneView
    Run Keyword If    ${ligs} is not ${null}      Add LIG    ${ligs}
    Verify Scale Resources  ${expected_ligs}

Add SAS LIG
    [Tags]    LIG   ADDSASLIG   ALT1
    [Documentation]        Add Natasha LIG to OneView
    Run Keyword If  ${sas_ligs} is not ${null}          Add SAS LIG from variable async        ${sas_ligs}
    Verify Scale Resources  ${expected_sasligs}

ADD EG
    [Tags]    ADDEG     ALT1
    Run Keyword If  ${enc_groups} is not ${null}    Add Enclosure Group from variable sync    ${enc_groups}
    Verify Scale Resources   ${expected_encgroup}

Verify Server Hardware
    [Tags]      VERIFYHARDWARE   ALT1
    Verify Monitored Server Hardware

Verify All Interconnect's Health before LE Creation
    [Tags]      INTERCONNECTHEALTH   ALT1
    Verify All Interconnects

Add Logical Enclosures
    [Tags]      ADDLE   ALT1
    Run Keyword If  '${PREV TEST STATUS}'=='FAIL'     Pause Execution    message=Verify Interconnect failed. Press OK to continue
    Add Logical Enclosure from lists    ${logical_enclosure}
    Verify Scale Resources  ${expected_logical_enclosure}

Verify Logical Interconnects
    [Tags]      VERIFYLOGICINTERCONNECTS   ALT1
    Verify All Logical Interconnects

Verify Managed Server Hardware
    [Tags]      VERIFYMANAGEDHARDWARE   ALT1
    Verify Managed Server Hardware

