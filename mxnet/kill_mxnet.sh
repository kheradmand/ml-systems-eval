for i in `ps -aux | grep "mxnet" | grep -v "grep" | grep -v "kill_mxnet.sh" | sed 's/\s\s*/ /g' | cut -d ' ' -f 2`; do
	echo $i;
	kill $i;
done
