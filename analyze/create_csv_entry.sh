VALS="cpup memc recv send iord iowt dski dsko gpup memg";

if [ $# -ne 1 ]; then
	echo "usage csv_entry resname";
	exit 1;
fi

NAME=$1

if [ ! -s ../res/$NAME ]; then
	echo "does not exists"
	exit 1;
fi
	EXPNAME=`python exp_extractor.py $NAME`;
	TRY=`python try_extractor.py $NAME`;
	BIT=$(grep "gradientBits" ../exp/$EXPNAME/Config/CRAP.cntk | cut  -d '=' -f 2 | tr -d ' ' | tr -d '\n')
	DATA=$(grep "epochSize" ../exp/$EXPNAME/Config/CRAP.cntk | cut  -d '=' -f 2 | tr -d ' ' | tr -d '\n')
	BATCH=$(grep "minibatchSize" ../exp/$EXPNAME/Config/CRAP.cntk | head -n 1 |  cut  -d '=' -f 2 | tr -d ' ' | tr -d '\n')
	HOST=$(grep Mustang ../exp/$EXPNAME/hosts | wc -l)
	WORKER=$(cat ../exp/$EXPNAME/workers) 
	GPU=$(cat ../exp/$EXPNAME/gpu)

        echo -n "$EXPNAME,$TRY,$BIT,$DATA,$BATCH,$HOST,$WORKER,$GPU," 
        #./analyze_result.sh $i-1 > /dev/null 2> /dev/null;
        RES=../res/$NAME/final_result.txt
        cat $RES | grep "time" | cut -d ':' -f 2 | tr -d '\t'  | tr -d '\n'
        for j in `cat ~/iplist`; do
                for k in $VALS; do
                        echo -n ","
                        grep "$j" $RES -A 10 | grep "$k" | cut -d ':' -f 2 | tr -d '\t'  | tr -d '\n'
                done
        done
        echo ""
               



