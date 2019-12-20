#!/bin/bash

paswoord="supersecret" #definieer het ww

read -s -p "Paswoord:" mogelijkpaswoord #vraag de user voor input met een speciaal commando
echo "..." #print een lege lijn

regex="[A-Z]+.{5,}[0-9]{2}"
if [[ $mogelijkpaswoord =~ $regex ]] ; then
  echo "Passwoord geldig";
  exit 0
else
	echo "Passwoord ongeldig";
	exit 0
fi
