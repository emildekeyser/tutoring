#!/bin/bash

paswoord="supersecret" #definieer het ww

read -s -p "Paswoord:" mogelijkpaswoord #vraag de user voor input met een speciaal commando

echo "" #print een lege lijn

#controleer of het ww juist is
if [ $paswoord = $mogelijkpaswoord ] ; then
	echo "Toegelaten"
else
	echo "Verboden!"
fi
