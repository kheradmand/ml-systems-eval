#!/bin/bash

source ../../common/common.sh

EXP=$1
RES=$2

echo "==Moving result and mapping"
mv $EVAL/result.txt $RES
mv $EVAL/mapping.txt $RES
