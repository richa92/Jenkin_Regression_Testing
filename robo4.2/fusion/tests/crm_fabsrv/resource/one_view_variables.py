"""Variables for working with the One View instance

    = Usage =
    | *** Settings ***      |
    | variables | ../resource/one_view_variables.py |
    | pybot --variablefile ../resource/one_view_variables.py |
"""

#  One View Connectivity
API_USER = 'Administrator'
API_PASSWORD = 'skyline!'
SSH_USER = 'root'
SSH_PASSWORD = 'hpvse1'
ADMIN_CREDENTIALS = {'userName': API_USER, 'password': API_PASSWORD}

ONE_VIEW_IP = '172.17.209.72'
REST_BASE_URL = 'https://' + ONE_VIEW_IP

FUSION_PROMPT = '#'
FUSION_TIMEOUT = 300


