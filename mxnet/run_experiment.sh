#!/bin/bash
MXNET="/home/srg/exp/exp_mxnet"
ANSIBLE="ansible cntk -i ~/tools/hosts"
EVAL="/home/srg/eval/mxnet"
STAT="/home/srg/eval"
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

CONFIG=$EVAL/exp/$EXP;
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
cd $EVAL && ./stop_mxnet.sh;

sleep 1;


echo "capturing process state"
$ANSIBLE -m shell -a "ps -ajxf" > $EVAL/ps.txt

echo "starting monitors"
cd $STAT && ./run_dstat.sh;
cd $STAT && ./run_gstat.sh;

sleep 1;

rm -f $EVAL/result.txt;

EPOCHS=`cat $CONFIG/epochs`;

echo "running experiment";
cd $MXNET && nohup ./run.sh `cat $CONFIG/batch` $CONFIG/hosts $EPOCHS  > $EVAL/result.txt  2>&1  &
echo "experiment started";

i=0;



while true; do
	i=$((i+1));
	sleep $P;
	date;
	echo -n "check $i: ";
	t=`tail -n 50 $EVAL/result.txt | grep "Epoch\[$((EPOCHS-1))\]" | wc -l`
	y=`tail -n 50  $EVAL/result.txt | grep elapsed | wc -l`
	if [ $t == 0 ] || [ $y == 0 ]; then 
		echo "NOT DONE YET";	
		tail -n 1 $EVAL/result.txt;
	else
		echo "DONE";
		#grep SamplesSeen $EVAL/result.txt | tail -n 1;
		tail -n 55 $EVAL/result.txt;
		break;
	fi
done	

echo "=============="
echo "stoping monitors"
cd $STAT && ./stop_dstat.sh
cd $STAT && ./stop_gstat.sh	

echo "moving results to proper place ($EXP-$n)"
$ANSIBLE -m shell -a "mkdir $RES && mv eval/dstat.csv $RES && mv eval/gstat.txt $RES";
mv $EVAL/result.txt $RES
mv $EVAL/ps.txt $RES
