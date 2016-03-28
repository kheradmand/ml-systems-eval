ANSIBLE="ansible cntk -i ~/tools/hosts"


$ANSIBLE -m shell -a "kill \`cat eval/gstat.pid\`"
$ANSIBLE -m shell -a "rm eval/gstat.pid"
