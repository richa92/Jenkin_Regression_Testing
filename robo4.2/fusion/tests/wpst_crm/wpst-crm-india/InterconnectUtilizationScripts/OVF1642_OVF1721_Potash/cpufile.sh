#!/bin/bash
while [ 1 ] ; do
    # Force some computation even if it is useless to actually work the CPU
    echo $((13**999))
done
