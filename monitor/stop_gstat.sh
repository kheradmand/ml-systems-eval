source ../common/common.sh

$ANSIBLE -m shell -a "kill \`cat $MONITOR/gstat.pid\`"
$ANSIBLE -m shell -a "rm $MONITOR/gstat.pid"
#
$ANSIBLE -m shell -a "cd $MONITOR && ./kill_gpustat.sh"
$ANSIBLE -m shell -a "killall nvidia-smi"

