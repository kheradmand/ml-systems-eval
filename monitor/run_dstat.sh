source ../common/common.sh;

$ANSIBLE_SHELL  "rm -f $MONITOR/dstat.csv && nohup dstat -tcmnrd --socket  --output $MONITOR/dstat.csv > /dev/null 2> /dev/null &"
