#!/bin/bash
sec=60
while [ $sec -ge 0 ] ; do
	if [ $sec -ge 10 ] ; then
		echo -n "$sec" 
	else
		echo -n "0$sec" 
	fi
	
	echo -en "\b\b"
	let "sec=$sec-1"
	sleep 1
done

echo
echo "ready!"
