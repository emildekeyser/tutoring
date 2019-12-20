#!/bin/bash

if [ -e /bin/df ] ; then  #controleer of het pad bestaat
	
	if [ -r /bin/df ] ; then #controleer of het pad leesbaar is
		if [ -x /bin/df ] ; then #controleer of het pad uitvoerbaar is
			df -h #voer het uit
		else
			echo "Niet uitvoerbaard"
			exit 1
		fi
	else 
		echo "Niet leesbaar"
		exit 1
	fi
	
else
	echo "/bin/def bestaat niet"
	exit 1
fi 


