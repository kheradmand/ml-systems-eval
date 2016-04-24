#!/bin/bash
source ../../common/common.sh

if [ $# -ne 5 ]; then
	echo "usage generate_experiment name data batch host limit"
	exit 1;
fi

NAME=$1
DATA=$2
BATCH=$3
HOST=$4
LIMIT=$5

EXP=$EXPS/$NAME

rm -rf $EXP
mkdir $EXP

echo mxnet > $EXP/system
echo $DATA > $EXP/data
echo $BATCH > $EXP/batch
echo $LIMIT > $EXP/limit
grep Mustang $HOSTS | head -n $HOST > $EXP/hosts

