#!/bin/bash

source ../common/common.sh

if [ $# == 0 ]; then
        echo "usage: stat <res name>"
        exit 1;
else
        RESNAME=$1;
fi


TRY=`python helper/try_extractor.py $RESNAME`;
EXPNAME=`python helper/exp_extractor.py $RESNAME`;
 
EXP=$EXPS/$EXPNAME;
RES=$RESS/$RESNAME
if [ ! -e $RES ]; then
        echo "$RES does not exists";
        exit 1;
fi

echo "=== analysing dstat results"
$ANSIBLE_SHELL "cd $ANALYZE && python dstat.py $RESNAME"
echo "=== analysing gpu status results"
$ANSIBLE_SHELL "cd $ANALYZE && python gpustat.py $RESNAME"

echo "=== analysing system output results"
SYSTEM=`cat $EXP/system`
cd $SYSS/$SYSTEM && python analyze.py $RESNAME

