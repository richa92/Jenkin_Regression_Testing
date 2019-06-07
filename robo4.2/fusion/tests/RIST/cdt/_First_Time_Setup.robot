*** Settings ***
Resource    resource.txt

*** Test Cases ***
Perform First Time Setup
    First Time Setup    password=${admin_credentials['password']}