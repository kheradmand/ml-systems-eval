#!/bin/bash

source ../../common/common.sh

EXP=$1
RES=$2
RUN="$RUN/cntk/`cat $EXP/data`";


echo "==Running experiment";
cd $RUN && ./run.sh `cat $EXP/gpu` `cat $EXP/workers` $EXP/hosts  > $EVAL/mapping.txt  2> $EVAL/result.txt 

