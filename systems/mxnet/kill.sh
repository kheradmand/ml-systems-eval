source ../../common/common.sh

./kill_local.sh

sleep 2;

$ANSIBLE_SHELL "cd $ROOT/systems/mxnet && ./kill_local.sh"

sleep 2;

echo "=running ps"
$ANSIBLE_SHELL  "ps -axjf | grep mxnet | grep -v grep "
