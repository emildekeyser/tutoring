#!/bin/bash

#print al da ding
echo "Gewone gebruiker op het systeem: "

#loop over alle nummers in dat pwd bestand
for i in `cut -d: -f3 cat /etc/passwd 2> /dev/null` ; do

	#controleer of i grooter dan of gelijk aan 1000 is
    if [ $i -gt 999 ] ; then
	#als het groter dan of gelijk aan 1000 is doen we hetvolgende:
	#Lees heel het bestand terug in, 
	#cut alleen de velden met de nummers en de namen (3 en 1 respectievelijk), 
	#zoek naar de lijn waar $i (onze nummer) in voorkomt,
	#cut daaruit het eerste veld met de naam en print die
        echo $(cat /etc/passwd | cut -d: -f1,3 | grep $i | cut -d: -f1 )
    fi    
done
 
