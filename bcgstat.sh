nohup ./gpustat.sh  > gstat.txt 2> /dev/null &
echo $! > gstat.pid
