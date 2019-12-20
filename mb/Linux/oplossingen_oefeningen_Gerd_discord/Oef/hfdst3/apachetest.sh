#!/bin/bash

if [ "$1" = "--help" ] ; then 
	echo "Doel: Benchmark test voor apache webserver oproepen"
	echo "Ref: man ab man curl"
	echo "Nodig: sudo apt-get install apache2 apache2-utils curl"
	echo "Usage: ./apachetest [url]"
	echo "Params: [url] een url van een website"
	echo "Return: stdout van ab"
	exit 0
fi

#start the apache service op om zeker te zijn, output intereseert ons niet
sudo service apache2 start > /dev/null

#controleer of ab bestaat
if [ $(which ab) = "" ] ; then
	echo "Het programma ab is nodig. Installeren kan met sudo apt-get install apache2-utils" >&2
	exit 1
fi

#controleer of we een argument mee hebben gekregen, indien niet gebruik localhost
if [ $# -lt 1 ] ; then 
	url="127.0.0.1/"
else 
	url="$1"
fi

#controleer of de URL eindigd op een "/"
tailChar=$(printf "$url" | tail -c 1)
if [ "$tailChar" != "/" ] ; then
	echo "$url moet eindigen op een /"
	exit 1
fi

#controleer of we de URL kunnen bereiken
curlReturn=$(curl $url 2> /dev/null)
if [ "$curlReturn" = "" ] ; then 
	echo "$url is niet bereikbaar"
	exit 2
fi

#doe de benchmark
ab -n 100 -kc 10 ${url}
