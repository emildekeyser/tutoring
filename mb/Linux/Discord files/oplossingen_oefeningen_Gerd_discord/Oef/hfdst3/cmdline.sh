#!/bin/bash

#loop over al de bestanden
for i in `ls /proc/*/cmdline` ; do 

	#controleer of het bestand bestaat en de size > 0
	if [ -s $i ] ; then 
		
		#zoek naar sbin in het bestand
		grepReturn=$(grep "sbin" "$i")
		
		#als het niet leeg is 
		if [ "$grepReturn" != "" ] ; then

			#en als het bestand nog bestaat print dan
			if [ -e $i ] ; then 
				echo "$grepReturn"
			fi
		fi
	fi 
done
