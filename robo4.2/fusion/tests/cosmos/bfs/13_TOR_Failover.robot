*** Settings ***
Documentation                   TOR Switch Failover
Resource                        resource.txt
Suite Setup                     BFS OV Suite Setup   ${admin_credentials}
Suite Teardown                  BFS OV Suite Teardown

*** Test Cases ***
TOR Switch Port Failover for Interconnect A-Side
    [Tags]  Switch  F-SW-ASide
    [Documentation]  TOR port Failover for interconnect a side
    :FOR  ${switch_failover}  IN  @{tor_failover_a_side}
    \  TOR Switch Port Should Be  ${switch_failover['switchIP']}  ${switch_failover['switchport']}  ${switch_failover['switchUsername']}  ${switch_failover['switchPassword']}  ${switch_failover['PortName']}  0  ${switch_failover['interconnect_port']}  ${switch_failover['interconnect_name']}  Unlinked

TOR Switch Port Enable for Interconnect A-Side
    [Tags]  Switch  E-SW-ASide
    [Documentation]  TOR port Enable for interconnect a side
    :FOR  ${switch_failover}  IN  @{tor_failover_a_side}
    \  TOR Switch Port Should Be  ${switch_failover['switchIP']}  ${switch_failover['switchport']}  ${switch_failover['switchUsername']}  ${switch_failover['switchPassword']}  ${switch_failover['PortName']}  1  ${switch_failover['interconnect_port']}  ${switch_failover['interconnect_name']}  Linked

TOR Switch Port Failover for Interconnect B-Side
    [Tags]  Switch  F-SW-BSide
    [Documentation]  TOR port Failover for interconnect b side
    :FOR  ${switch_failover}  IN  @{tor_failover_b_side}
    \  TOR Switch Port Should Be  ${switch_failover['switchIP']}  ${switch_failover['switchport']}  ${switch_failover['switchUsername']}  ${switch_failover['switchPassword']}  ${switch_failover['PortName']}  0  ${switch_failover['interconnect_port']}  ${switch_failover['interconnect_name']}  Unlinked

TOR Switch Port Enable for Interconnect B-Side
    [Tags]  Switch  E-SW-BSide
    [Documentation]  TOR port Enable for interconnect b side
    :FOR  ${switch_failover}  IN  @{tor_failover_b_side}
    \  TOR Switch Port Should Be  ${switch_failover['switchIP']}  ${switch_failover['switchport']}  ${switch_failover['switchUsername']}  ${switch_failover['switchPassword']}  ${switch_failover['PortName']}  1  ${switch_failover['interconnect_port']}  ${switch_failover['interconnect_name']}  Linked