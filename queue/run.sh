#!/bin/bash

if [ "$#" -ne 0 ]; then 

option="$1";
shift;
PID=pid;

case $option in
    --start)
    	if [ -s $PID ]; then
    		echo daemon is already running with $PID `cat $PID`
    	else
			nohup python run.py $@ > out.txt 2>&1 &  
			echo $! > $PID
		fi
		;;
    --stop)
    	if [ -s $PID ]; then
    		kill `cat $PID`
    		rm -f $PID
    	else
    		echo daemon is not running
    	fi
    	;;
esac


else
	echo "usage: ./run.sh [--start | --stop] [OPTIONS]"

fi
