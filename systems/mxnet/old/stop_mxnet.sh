./kill_mxnet.sh

sleep 2;

ansible cntk -i ~/tools/hosts -m shell -a "cd eval/mxnet && ./kill_mxnet.sh"

sleep 2;

ansible cntk -i ~/tools/hosts -m shell -a "ps -axjf | grep mxnet | grep -v grep "
