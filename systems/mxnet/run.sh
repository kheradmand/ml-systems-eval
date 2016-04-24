#!/bin/bash

source ../../common/common.sh

EXP=$1
RES=$2
RUN="$RUNNABLE/mxnet/`cat $EXP/data`";



cd $RUN && ./run.sh `cat $EXP/batch` $EXP/hosts  > $EVAL/result.txt  2>&1  
