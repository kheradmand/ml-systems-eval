#!/bin/bash

ANSIBLE="ansible cntk -i ~/tools/hosts"
EVAL="/home/srg/eval"
if [ $# != 1 ]; then
	echo "usage: analyze_result resname"
	exit  1;
fi
RESNAME=$1
RES=$EVAL/res/$1
if [ ! -e $RES ]; then
        echo "$RES does not exists";
        exit 1;
fi  

echo "running dpeak"
$ANSIBLE -m shell -a "cd $EVAL/analyze && python dpeak.py $RESNAME > $RES/peak.txt"

echo "running gpeak"
$ANSIBLE -m shell -a "cd $EVAL/analyze && python gpeak.py $RESNAME >> $RES/peak.txt"

echo "running time"
cd $EVAL/analyze && python time.py $RESNAME > $RES/time.txt

echo "genrating final result"
cp $RES/time.txt $RES/final_result.txt
echo " " >> $RES/final_result.txt
$ANSIBLE -m shell -a "cat $RES/peak.txt" >> $RES/final_result.txt

cat $RES/final_result.txt
