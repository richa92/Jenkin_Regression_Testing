*** Settings ***
Documentation               takes a fresh VM appliance by name and creates a snapshot, then powers on the VM.
...                         usage: pybot -v VM:<vmname> vmsetup.txt
Resource                     ../../../resources/resource.txt
Library                      Collections
*** Test Cases ***
VM Setup
    VM Setup    ${VM}