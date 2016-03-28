ANSIBLE="ansible cntk -i ~/tools/hosts"


$ANSIBLE -m shell -a "rm -f eval/dstat.csv && nohup dstat --output eval/dstat.csv > /dev/null 2> /dev/null &"
