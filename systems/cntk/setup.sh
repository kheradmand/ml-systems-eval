#!/bin/bash

source ../../common/common.sh

EXP=$1;
RES=$2;

RUN="$RUNNABLE/cntk/`cat $EXP/data`";

echo "==Setting config"
$ANSIBLE_COPY "src=$EXP/config.cntk dest=$RUN/config.cntk"

