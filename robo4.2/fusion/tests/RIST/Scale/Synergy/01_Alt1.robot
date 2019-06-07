*** Settings ***
Resource                        resource.txt
Suite Setup                     Scale Suite Setup     ${admin_credentials}
Suite Teardown                  Scale Suite Teardown

*** Test Cases ***
Add Proxy Server
    [Tags]    ADDPROXY      ALT1
    [Documentation]        Add Proxy Server to OV
    Set Log Level    TRACE
    ${responses}=  Add Proxy Server to OV    ${proxy_server}
    Run Keyword for List with kwargs  ${responses}  Wait For Task2   timeout=60

Rename All Enclosures
    [Tags]    RENAME    ALT1
    [Documentation]        Rename Enclosure
    Set Log Level    TRACE
    ${responses}=  Edit Enclosure from List    ${encl_update}
    Run Keyword for List with kwargs  ${responses}  Wait For Task2   timeout=500
    Verify Resources for List  ${expected_enclosure}

Add Potash FC Licenses
    [Tags]      ADDLICENSE
    Run Keyword If  ${licenses} is not ${null}    Add Licenses from variable    ${licenses}     ${VERIFY}

Add Firmware Bundle
    [Tags]    ADDSPP
    Log to console and logfile  Connecting to FTP Site ${ftp_site}
    Ftp Connect     ${ftp_site}
    Log to console and logfile  Downloading SPP File ${spp_name}
    FtpLibrary.Download File    ${spp_ftp_path}  ${spp_local_path}
    Log to console and logfile  Uploading ${spp_name} to OV
    Upload SPP to Fusion    ${APPLIANCE_IP}    ${admin_credentials['userName']}     ${admin_credentials['password']}      ${spp_local_path}
    Verify Resources for List  ${expected_spp}

Add Local Users
    [Tags]    ADDUSER
    ${responses} =  Add Users from variable    ${users}
    Run Keyword for List  ${responses}  Wait For Task2
    Verify Users    ${expected_users}

Add Active Directory
    [Tags]    ADDAD
    ${responses} =  Add Active Directory    ${active_directory_server}
    Run Keyword for List with kwargs  ${responses}  Wait For Task2

Enable Remote support
    [Tags]    REM
    [Documentation]    Edit file /ci/data/sarm/config/rshpe.xml
    ...  Modify the xml node <entry key="HpAdapter.Address.EndPoint">
    ...  http://10.0.0.61:8444/RsdcMock/</entry> to reference your appliance IP address
    ...  Execute the PSQL on appliance and reference your appliance IP address in the SQL statement.
    ...    a.psql -U postgres fusiondb
    ...    b.UPDATE sarm.sttngs SET valu = 'http://10.0.0.61:8444/RsdcMock/' WHERE ky_nm = 'HpAdapter.Address.EndPoint';
    ...  Reboot appliance
    ...  Initiate remote support registration
    #Update XML Node
    #Execute PSQL command On Appliance
    #Restart the appliance
    Initiate Remote Support Registration
