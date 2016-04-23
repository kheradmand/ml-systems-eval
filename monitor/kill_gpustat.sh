for i in `ps -aux | grep "/bin/sh ./gpustat.sh" | grep -v "grep" | sed 's/\s\s*/ /g' | cut -d ' ' -f 2`; do
	echo $i;
	kill $i;
done
