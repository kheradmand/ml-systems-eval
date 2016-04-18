
if [ $# -ne 4 ]; then
	echo "usage generate_experiment name batch host epochs"
	exit 1;
fi

NAME=$1
BATCH=$2
HOST=$3
EPOCHS=$4

rm -rf exp/$NAME
mkdir exp/$NAME

echo $BATCH > "exp/$NAME/batch"
echo $EPOCHS > "exp/$NAME/epochs"
grep Mustang exp/base/hosts | head -n $HOST > exp/$NAME/hosts

