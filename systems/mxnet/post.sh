#!/bin/bash

source ../../common/common.sh

EXP=$1
RES=$2

echo "==Moving result"
mv $EVAL/result.txt $RES
