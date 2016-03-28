#!/bin/bash

ANSIBLE="ansible cntk -i ~/tools/hosts"
CRAP="/home/srg/cntk/Examples/CRAP/Data"

killall run_experiment.sh
cd $CRAP && ./kill_crap.sh
