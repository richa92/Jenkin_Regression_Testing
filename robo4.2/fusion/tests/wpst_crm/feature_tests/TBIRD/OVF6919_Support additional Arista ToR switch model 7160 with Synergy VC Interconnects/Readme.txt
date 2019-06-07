1. It is single script for both potash and nitro module and there are tags used for potash and nitro module.
2. While executing the script with respect to potash module comment the tags with nitro and use below command:
      pybot -i Potash Suite.txt
3. While executing the script with respect to nitro module comment the tags with potash and use below command:
      pybot -i Nitro Suite.txt
4. IP series variable used should be changed according to valid ip we get in servers.
5. switch command : if we use speed 'auto' in LIG then we need to use command
   "speed auto 10g full" (speed can be seen inside switch or in interconnects page i.e the speed of uplink port to which switch port is connected)
6. If we use specific speed in LIG then command should be:
   "speed forced 10g full"