#!/bin/bash

# Functie:
#   Zoekt naar grote bestanden In een bepaalde directory
#
# Arguments:
#   Arg1 is een directory
#
# Auteur: Voornaam Naam Email
# Copyright: 2019 MIT Email
#
# Versie: 0.1
#
# Requires: Standaard shell find commando

#help argument
if [ "$1" = "--help" ] ; then
  echo "Usage: `basename $0` arg1 "
  echo "Example: `basename $0` Hallo "
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

#eigen variable: kleine letters en _ geen camle case
#omgevingsvariable: hoofdletters

#check op root:
if [ "$(id -u)" != "0" ]; then
  echo "$0:">&2
  echo "Dit script moet je als root uitvoeren">&2
  exit 1
fi

#foutmeldingen versturen naar stderr met >&2
#foutmeldingen bevatten ook het naam van het script ($0 of basename $0)

#check op dependencies
error_geen_ab="Het programma ab is niet geïnstalleerd"
command -v ab >/dev/null || (echo -e "$0 \n$error_geen_ab" >&2 && exit 1);
which ab >/dev/null || (echo -e "$0 \n$error_geen_ab" >&2 && exit 1);

#normal exit
exit 0
