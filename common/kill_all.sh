source common.sh

echo "===Killing all systems"

for i in `ls $ROOT/systems`; do 
	echo "==Killing $i";
	cd $ROOT/systems/$i && ./kill.sh;
	sleep 2;
done
