set http_proxy=http://web-proxy.houston.hpecorp.net:8080
set https_proxy=https://web-proxy.houston.hpecorp.net:8080

set HOST1=robogalaxy.us.rdlabs.hpecorp.net
set HOST2=wpstwork4.vse.rdlabs.hpecorp.net

set repo=RoboGalaxyLibrary-300-cp27-win_amd64

virtualenv py27
call py27\scripts\activate
python -m pip wheel -w dist --trusted-host %HOST1% --trusted-host %HOST2% -f https://%HOST1%/repo/%REPO% -f http://%HOST2%/robogalaxy/%REPO% .
