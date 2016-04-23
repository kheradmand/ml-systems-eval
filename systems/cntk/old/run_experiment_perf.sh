#!/bin/bash

ANSIBLE="ansible cntk -i ~/tools/hosts"
CRAP="/home/srg/cntk/Examples/CRAP/Data"
EVAL="/home/srg/eval"
P=10 #sleep between two checks
CONFIG=""
EXP=""
RES=""
if [ $# == 0 ]; then
	echo "no experiment name provided using default experiment config"
	EXP="base";
else
	EXP=$1;
fi

CONFIG=$EVAL/exp/$EXP/Config;
if [ ! -e $CONFIG ]; then
	echo "$CONFIG does not exists";
	exit 1;
fi

echo "config: $CONFIG"
	
n=0;
while true; do
	if [ ! -e $EVAL/res/$EXP-$n ]; then
		break;
	fi
	n=$((n+1));
done
RES=$EVAL/res/$EXP-$n;
	
echo "result: $RES"

echo "Killing any running experiment"
cd $CRAP && ./kill_crap.sh;

sleep 1;

echo "Removing output"
cd $CRAP && ./remove_crap.sh;

sleep 1;

echo "setting the config"
rm -r $CRAP/../Config;
cp -r $CONFIG $CRAP/../;


echo "distributing config"
cd $CRAP && ./copy_crap.sh;

sleep 1;

echo "capturing process state"
$ANSIBLE -m shell -a "ps -ajxf" > $EVAL/ps.txt

echo "starting monitors"
cd $EVAL && ./run_dstat.sh;
cd $EVAL && ./run_gstat.sh;

sleep 1;

rm -f $EVAL/result.txt;

echo "running experiment";
cd $CRAP && nohup ./run_crap_perf.sh `cat $CONFIG/../gpu` `cat $CONFIG/../workers` $CONFIG/../hosts `cat "$CONFIG/../command"` > $EVAL/mapping.txt  2> $EVAL/result.txt &
echo "experiment started";

i=0;

while true; do
	i=$((i+1));
	sleep $P;
	date;
	echo -n "check $i: ";
	t=`tail -n 30 $EVAL/result.txt | grep COMPLETED | wc -l`
	y=`tail -n 30  $EVAL/result.txt | grep "seconds time elapsed" | wc -l`
	if [ $t == 0 ] || [ $y == 0 ]; then 
		echo "NOT DONE YET";	
		tail -n 1 $EVAL/result.txt;
	else
		echo "DONE";
		grep SamplesSeen $EVAL/result.txt | tail -n 1;
		tail -n 20 $EVAL/result.txt;
		break;
	fi
done	

echo "=============="
echo "stoping monitors"
cd $EVAL && ./stop_dstat.sh
cd $EVAL && ./stop_gstat.sh	

echo "moving results to proper place ($EXP-$n)"
$ANSIBLE -m shell -a "mkdir $RES && mv eval/dstat.csv $RES && mv eval/gstat.txt $RES";
mv $EVAL/result.txt $RES
mv $EVAL/mapping.txt $RES
mv $EVAL/ps.txt $RES
