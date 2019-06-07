***Settings***
Documentation      Network Sets Page Test suite
Resource           ../resource.txt
Suite Setup        Suite Setup
Suite Teardown     Logout And Close Browser
Force Tags         smoke  networksets  tbird  c7000
Test Timeout       ${TEST_TIMEOUT}


***Test Case***
'Create Network Set' Dialog Elements Should Appear As Expected
    [Documentation]   Network Sets Page Dialog 'Create Network Set' Elements Should Appear As Expected
    ...   \n Navigate to Network Sets page
    ...   \n Click "Create Network Sets"
    ...   \n Create Network Sets Dialog Should be visible
    ...   \n Verify text can be input into the Network name field
    ...   \n Ensure Networks pane is displayed in Create Network Sets Dialog box
    ...   \n Create button should be visible and primary in Create Network Sets Dialog box
    ...   \n Create+ button should be visible in Create Network Sets Dialog box
    ...   \n Click Cancel button in Create Network Sets Dialog box
    ...   \n Create Network Sets Dialog should not be visible

    Open Sub Menu   Networking   Network Sets
    Navigate To Page          Network Sets
    Click Link                Link=Create network set
    Dialog Should Be Visible  Create Network Set
    ${networkset_name}=  Generate Random String  8  chars=[LETTERS][NUMBERS]
    Input Text           id=cic-networkset-add-name  ${networkset_name}
    ${panels}=  Create List From Action or Panel Drop Menu  cic-networkset-panel-add-selector
    :FOR  ${panel}  in  @{panels}
    \    Select Dialog Panel          cic-networkset-panel-add-selector  ${panel}
    Dialog Element Should Be Visible  css=#cic-networkset-add.hp-primary
    Dialog Element Should Be Visible  id=cic-networkset-add-again
    Click Element                     id=cic-networkset-add-close
    Dialog Should Not Be Visible      Create Network Set