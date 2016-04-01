ANSIBLE="ansible cntk -i ~/tools/hosts"
RES="/home/srg/eval/res"
if [ $# != 1 ]; then
	echo "usage remove_result resname"
	exit 1
fi

if [ ! -s $RES/$1 ]; then
	echo "$1 does not exists"
	exit 1
fi

$ANSIBLE -m shell -a "rm -r $RES/$1"

