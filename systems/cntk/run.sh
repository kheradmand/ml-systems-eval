#!/bin/bash

source ../../common/common.sh

EXP=$1
RES=$2
RUN="$RUNNABLE/cntk/`cat $EXP/data`";


cd $RUN && ./run.sh `cat $EXP/gpu` `cat $EXP/workers` $EXP/hosts  > $EVAL/mapping.txt  2> $EVAL/result.txt 

