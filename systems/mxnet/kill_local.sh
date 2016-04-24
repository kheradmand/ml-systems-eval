echo "=Killing mxnet locally"
for i in `ps -aux | grep "mxnet" | grep -v "grep" | grep -v -e "kill.sh" -e "kill_local.sh" -e "ansible" -e "kill_all.sh" -e "run_experiment.sh mxnet-" | sed 's/\s\s*/ /g' | cut -d ' ' -f 2`; do
	echo $i;
	kill $i;
done
