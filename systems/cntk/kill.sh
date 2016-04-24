source ../../common/common.sh

$ANSIBLE_SHELL "killall cntk"

sleep 2;

$ANSIBLE_SHELL "$SYSS/cntk/kill_local.sh"

