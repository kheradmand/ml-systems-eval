#Configure this stuff!
ROOT="/home/srg/eval"
ANSIBLE_HOSTS="/home/srg/tools/hosts"
RUNNABLE="/home/srg/exp"

ANSIBLE="ansible all -i $ANSIBLE_HOSTS"
ANSIBLE_SHELL="$ANSIBLE -m shell -a"
ANSIBLE_COPY="$ANSIBLE -m copy -a"

EVAL="$ROOT/common"
EXPS="$ROOT/experiments"
RESS="$ROOT/results"
SYSS="$ROOT/systems"
MONITOR="$ROOT/monitor"
