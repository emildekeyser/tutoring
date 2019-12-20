#!/bin/bash

if [ -x /bin/df ] ; then #controleer of het gegeven pad uitvoerbaar is
	df -h #voer het uit
else
	echo "Niet uitvoerbaard"
fi

