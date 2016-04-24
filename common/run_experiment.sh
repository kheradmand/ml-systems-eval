#!/bin/bash

source common.sh

P=10 #sleep between two checks
EXPNAME=""
RES=""
EXP=""
if [ $# == 0 ]; then
	echo "usage: run_experiment <exp name>"
	exit 1;
else
	EXPNAME=$1;
fi

EXP=$EXPS/$EXPNAME;
if [ ! -e $EXP ]; then
	echo "$EXP does not exists";
	exit 1;
fi

echo "config: $EXP"
SYSTEM=$SYSS/`cat $EXP/system`
	
n=0;
while true; do
	if [ ! -e $RESS/$EXPNAME-$n ]; then
		break;
	fi
	n=$((n+1));
done
RES=$RESS/$EXPNAME-$n;
	
echo "result: $RES"

echo "===Killing any running experiment"
cd $EVAL && ./kill_all.sh;

sleep 1;

echo "===Preprocessing"
cd $SYSTEM && ./setup.sh $EXP $RES

sleep 1;

echo "==Capturing process state"
$ANSIBLE_SHELL "ps -ajxf" > $EVAL/ps.txt


echo "===Starting monitors"
cd $MONITOR && ./run_dstat.sh;
cd $MONITOR && ./run_gstat.sh;

sleep 1;


echo "===Running experiment";
cd $SYSTEM && nohup time ./run.sh $EXP $RES > $EVAL/system_run_log.txt 2>&1 &
PID=$!;
echo "==Experiment started ($PID)";


i=0;
total=0;

while true; do
        sleep $P;
        i=$((i+1));
        total=$((total+P));
        date;
        echo -n "Check $i (time = $total): ";
        tail -n 1 $EVAL/result.txt;
        if [ $total -gt `cat $EXP/limit` ]; then
                break;
        fi
done

echo "=================="
echo "===Stoping monitors"
cd $MONITOR && ./stop_dstat.sh
cd $MONITOR && ./stop_gstat.sh	

sleep 2;

echo "===Killing experiment"
kill $PID
sleep 2;
kill -9 $PID
sleep 2;
cd $SYSTEM && ./kill.sh

sleep 2;

echo "===Moving results to proper place ($RES)"
$ANSIBLE_SHELL "mkdir $RES && mv $MONITOR/dstat.csv $RES && mv $MONITOR/gstat.txt $RES";
mv $EVAL/ps.txt $RES
mv $EVAL/system_run_log.txt $RES
cd $SYSTEM && ./post.sh $EXP $RES
