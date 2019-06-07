#!/bin/sh

# Make sure a switch hostname was supplied.
if [ -z "$*" ] ; then 
    echo "No switch hostname was supplied"
    echo "Usage:  `basename $0` <switchHostname>..."
    exit 1
fi

rval=0
for switch in $* ; do
   # Call ssh, and release Graviton.
   ssh -o "StrictHostKeyChecking no" root@$switch "killall -HUP gravd"
   if [ $? -ne 0 ] ; then
      echo "Failed for switch $switch."
      rval=1        
   else
      echo "Reset switch $switch."
   fi
done

exit $rval

