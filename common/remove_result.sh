source common.sh
if [ $# != 1 ]; then
	echo "usage remove_result <result name>"
	exit 1
fi

if [ ! -s $RESS/$1 ]; then
	echo "$1 does not exist"
	exit 1
fi

$ANSIBLE_SHELL "rm -r $RESS/$1"

