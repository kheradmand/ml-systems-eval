#!/bin/bash

source ../../common/common.sh

EXP=$1
RES=$2


seg=`cat $EVAL/result.txt | grep "Signal: Segmentation fault (11)" | wc -l`
exc=`cat $EVAL/result.txt | grep "EXCEPTION occurred" | wc -l`;
if [ $seg -gt 0 ] || [ $exc -gt 0 ]; then
	echo 1;
else
	echo 0;
fi
