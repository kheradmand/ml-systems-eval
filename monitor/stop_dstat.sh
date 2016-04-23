ANSIBLE="ansible cntk -i ~/tools/hosts"


$ANSIBLE -m shell -a "killall dstat"
