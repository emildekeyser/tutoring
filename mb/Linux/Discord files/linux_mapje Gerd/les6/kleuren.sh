#!/bin/bash

regex="($d{1,5}) (.*)"
function tooninkleur(){
	reset='\e[0m'
	rood='\e[0;31m'
	blauw='\e[0;34m'
	echo -e "$rood $1 $blauw $2 $reset"
}

for proces in $(ps -eo pid,args)
do
	if [[ $proces =~ $regex ]]; then
	tooninkleur {$BASH_REMATCH[1]} "${BASH_REMATCH[2]}"
	fi
done
