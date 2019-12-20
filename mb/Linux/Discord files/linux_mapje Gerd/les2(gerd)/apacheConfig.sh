#!/bin/bash 

#instaleer apache2 als dat nog niet gebeurd is
sudo apt-get install apache2

#definieer een aantal variablen
adir="/etc/apache2"
confs="$adir/apache2.conf $adir/ports.conf"

#controleer of we minstens 1 parameter binnen krijgen
if [ $# -eq 0  ] ; then 
	echo "geen argument"
	exit 1
fi

#loop over the bestanden gedefinieerd in de bovenstaande variablen
for i in $(ls $confs) ; do
	#als het bestand (i) uit de loop bestaat	
	if [ -e $i ] ; then 
		#zoek naar het woord dat als parameter word megeven in het bestand
		grep -iHn $1 $i
	fi	
done

