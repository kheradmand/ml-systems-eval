
if [ $# -ne 1 ]; then
	echo "usage create_csv res_list_file"
	exit 1
fi

cat result-template.csv

for i in `cat $1`; do 
	./create_csv_entry.sh $i; 
done
