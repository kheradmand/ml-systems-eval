source ../common/common.sh

$ANSIBLE_SHELL "cd $MONITOR && rm -f gstat.txt &&  ./bcgstat.sh"
