#!/bin/bash
source ../../common/common.sh

if [ $# -ne 8 ]; then
	echo "usage generate_experiment name data batch host worker gpu bits limit"
	exit 1;
fi

NAME=$1
DATA=$2
BATCH=$3
HOST=$4
WORKER=$5
GPU=$6
BITS=$7
LIMIT=$8

EXP=$EXPS/$NAME

rm -rf $EXP
mkdir $EXP


echo cntk > $EXP/system
echo $DATA > $EXP/data
echo $GPU > $EXP/gpu
echo $WORKER > $EXP/workers
echo $LIMIT > $EXP/limit
grep Mustang $HOSTS | head -n $HOST > $EXP/hosts

cp $RUNNABLE/cntk/$DATA/config.cntk.backup $EXP/config.cntk

sed -i "0,/minibatchSize = 32/s//minibatchSize = $BATCH/" $EXP/config.cntk   
sed -i "0,/gradientBits = 32/s//gradientBits = $BITS/" $EXP/config.cntk 

