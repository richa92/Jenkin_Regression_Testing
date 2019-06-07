commands = ['rpm -ivh http://pyramid.vse.rdlabs.hpecorp.net/CentOS/6.7/os/x86_64/Packages/ppp-2.4.5-10.el6.x86_64.rpm',
            'rpm -ivh http://pyramid.vse.rdlabs.hpecorp.net/CentOS/6.7/os/x86_64/Packages/pptp-1.7.2-8.1.el6.x86_64.rpm',
            'echo "cvpn PPTP Cosmos7 *" >> /etc/ppp/chap-secrets',
            'rm -f /etc/ppp/peers/tbvpn',
            'echo "pty \\"pptp 16.84.100.8 --nolaunchpppd\\"" >> /etc/ppp/peers/tbvpn',
            'echo "name cvpn" >> /etc/ppp/peers/tbvpn',
            'echo "remotename PPTP" >> /etc/ppp/peers/tbvpn',
            'echo "require-mppe-128" >> /etc/ppp/peers/tbvpn',
            'echo "file /etc/ppp/options.pptp" >> /etc/ppp/peers/tbvpn',
            'echo "ipparam tbvpn" >> /etc/ppp/peers/tbvpn',
            'sed -i "s/#require-mppe-128/require-mppe-128/g" /etc/ppp/options.pptp',
            'service iptables stop',
            'pppd call tbvpn',
            'ip a | grep ppp',
            'route add default gw 10.0.6.2',
            'ip route add 10.0.0.0/8 dev ppp0'
            ]
verify_cmd = ['ping 10.101.101.205 -c 5']
verify_output = '5 received'
ssh_username = 'root'
ssh_password = 'hpvse1'
