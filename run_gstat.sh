ANSIBLE="ansible cntk -i ~/tools/hosts"


$ANSIBLE -m shell -a "cd eval && rm -f gstat.txt  && ./bcgstat.sh"
