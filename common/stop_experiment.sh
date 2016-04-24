#!/bin/bash

source common.sh

cd $EVAL && ./kill_all.sh
killall run_experiment.sh

echo "==stoping monitors"
cd $MONITOR && ./stop_dstat.sh
cd $MONITOR && ./stop_gstat.sh
