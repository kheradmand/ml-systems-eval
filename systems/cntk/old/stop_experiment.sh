#!/bin/bash

ANSIBLE="ansible cntk -i ~/tools/hosts"
CRAP="/home/srg/cntk/Examples/CRAP/Data"
EVAL="/home/srg/eval"


cd $CRAP && ./kill_crap.sh
killall run_experiment.sh

echo "stoping monitors"
cd $EVAL && ./stop_dstat.sh
cd $EVAL && ./stop_gstat.sh
