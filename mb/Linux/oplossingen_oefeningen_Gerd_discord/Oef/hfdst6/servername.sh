#!/bin/bash

file="/etc/apache2/apache2.conf"
regex="ServerName"

#check op root:
#(het bestand dat we willen aanpassen kan alleen in worden geschreven door root)
if [ "$(id -u)" != "0" ]; then
  echo "Dit programma moet uitgevoerd worden als root"
  exit 1
fi

#zoek in het bestand voor de regex
result=$(grep -e $regex $file)

#grep geeft het gevonden resultaat terug
#als dit dus "" is hebben we het niet gevonden
#en moet het worden toegevoegd
if [[ result = "" ]]; then
    echo "ServerName mijnlaptop" >> $file
    echo "Hostname ingesteld"
else
    echo "Hostname al ingesteld"
fi
