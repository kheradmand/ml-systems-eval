#!/bin/bash

ANSIBLE="ansible cntk -i ~/tools/hosts"
EVAL="/home/srg/eval/mxnet"
STAT="/home/srg/eval"

cd $EVAL && ./stop_mxnet.sh
killall run_experiment.sh

echo "stoping monitors"
cd $STAT && ./stop_dstat.sh
cd $STAT && ./stop_gstat.sh
