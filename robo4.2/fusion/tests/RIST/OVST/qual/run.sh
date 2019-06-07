#!/bin/bash

export PATH=/home/jenkins/robogalaxy/tools/Python27:/home/jenkins/robogalaxy/tools/Python27/Scripts:/home/jenkins/robogalaxy/tools/Python27/Lib/site-packages:/home/jenkins/robogalaxy/Tools/exe:$PATH
export PYTHONPATH=C:/cygwin/home/jenkins/robogalaxy

cd /home/jenkins/robogalaxy/tests/fusion/qual 

mkdir -p log
python -m robot.run --outputdir log OVAQual.txt 
