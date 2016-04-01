
if [ $# -ne 6 ]; then
	echo "usage generate_experiment name data batch host worker gpu"
	exit 1;
fi

NAME=$1
DATA=$2
BATCH=$3
HOST=$4
WORKER=$5
GPU=$6

rm -rf exp/$NAME
cp -r exp/base exp/$NAME

echo $GPU > exp/$NAME/gpu
echo $WORKER > exp/$NAME/workers
grep Mustang exp/base/hosts | head -n $HOST > exp/$NAME/hosts
sed -i "0,/epochSize = 100000/s//epochSize = $DATA/" exp/$NAME/Config/CRAP.cntk   
sed -i "0,/minibatchSize = 10/s//minibatchSize = $BATCH/" exp/$NAME/Config/CRAP.cntk   

