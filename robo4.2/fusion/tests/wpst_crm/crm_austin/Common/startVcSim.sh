#!/bin/bash

#/usr/local/vcm/etc/init.d/rcSvcm start all
#/usr/bin/releaseprompt /proc/$PPID/fd/0
/usr/local/vcm/etc/init.d/rcSvcm start > rcSvcm-start.log 2>&1 &