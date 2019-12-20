#!/bin/bash

# Beschrijving:
#   Best practices template
#
# Arguments:
#   Arg1 is een getal
#   Arg2 is een file
#
# Auteur: Voornaam Naam Email
# Copyright: 2019 MIT Email
#
# Versie: 0.1
#
# Requires: Standaard shell commando's
#

#eigen variable: kleine letters en _ geen camle case
#omgevingsvariable: hoofdletters

#Define error function
reset='[0m'
rood='[0;31m'
function printError() {
  #foutmeldingen versturen naar stderr met >&2
  #foutmeldingen bevatten ook het naam van het script ($0 of basename $0)
  echo -e "\e$rood $0" >&2
  echo -e "$1" >&2
  echo -e "\e$reset" >&2
}

#check op root:
if [ "$(id -u)" != "0" ]; then
  printError "Dit programma moet uitgevoerd worden als root"
  exit 1
fi

#check op dependencies
#Vervang "read mkdir rmdir" met de speciale commando's waarop je dependencies wil testen
for i in read mkdir rmdir ; do
  command -v $i >/dev/null

  if [ $? != 0 ] ; then
    printError "Het programma $i is niet geïnstalleerd"
    exit 1
  fi
done

#help argument
if [ "$1" = "--help" ] ; then
  echo "Help `basename $0`:"
  echo -e "\nBeschrijving: "
  echo -e "\tVervang dit door de beschrijving"

  echo -e "\nArgumenten: "

  echo -e "\n\tArgument 1: "
  echo -e "\t\tBeschrijving van argument 1"
  echo -e "\n\tArgument 2: "
  echo -e "\t\tBeschrijving van argument 2"

  echo -e "\nVoorbeeld:"
  echo -e "\tvoorbeeld hier"
  exit 0
fi

# Test of de input een integer getal is
echo "Geef een getal: "
read getal
if [ "$getal" -eq "$getal" ] 2>/dev/null; then
  echo $getal is een getal
else
  echo "$(basename $0):">&2
  echo $getal is geen getal >&2
  exit 1
fi

#test of input een bestand is dat bestaat en niet leeg is (zie man test voor meer tests)
echo "Geef de bestandsnaam: "
read bestandsnaam
if [ -s "$bestandsnaam" ]; then
  cat $bestandsnaam
else
  echo "$0:">&2
  echo $bestandsnaam werd niet gevonden >&2
fi

#kijk of het verige commando gelukt is
directory="test"
mkdir $directory
if [ $? != 0 ] ; then
  echo "$0:">&2
  echo "$directory aanmaken niet gelukt" >&2
  exit 1
else
  rmdir $directory
  echo "$directory aanmaken gelukt (en terug verwijderd)"
fi


#normal exit
exit 0
