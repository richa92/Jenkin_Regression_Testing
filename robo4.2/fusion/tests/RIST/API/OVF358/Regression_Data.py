
ADMIN_CREDENTIALS = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
FILES = ["/etc/pki/tls/certs/cachains/all-certificates.bks", "/etc/pki/tls/certs/cachains/all-certificates.crt"]
FUSION_SSH_USERNAME = "root"
FUSION_SSH_PASSWORD = "hpvse1"
FUSION_PROMPT = "#"
FUSION_TIMEOUT = '20'

USER_NAME = "admin"
USER_PASSWORD = "admin"
USER_PASSWORD_WRONG = "wrong_password"
IPDU_SERVER_SELF_SIGN = "16.125.33.182"
IPDU_SERVER_FORCE = "16.125.33.197"
POWER_DEVICE_BODY = [{"hostname": IPDU_SERVER_SELF_SIGN, "username": USER_NAME, "password": USER_PASSWORD, "force": False}]
POWER_DEVICE_BODY_FORCE = [{"hostname": IPDU_SERVER_FORCE, "username": USER_NAME, "password": USER_PASSWORD, "force": True}]
POWER_DEVICE_BODY_WRONG_PWD = [{"hostname": IPDU_SERVER_SELF_SIGN, "username": USER_NAME, "password": USER_PASSWORD_WRONG, "force": False}]
POWER_DEVICE_REFRESH_BODY = [{"refreshState": "RefreshPending"}]

CERTIFICATE = {"aliasName": "", "base64SSLCertData": "", "status": None, "type": "SSLCertificateDTO"}
CERTIFICATE_CHAIN = [{"aliasName": "", "base64SSLCertData": "", "status": None, "type": "SSLCertificateDTO"}, {"aliasName": "", "base64SSLCertData": "", "status": None, "type": "SSLCertificateDTO"}]
