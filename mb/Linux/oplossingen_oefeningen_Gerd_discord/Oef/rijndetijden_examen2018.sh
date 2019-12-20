#!/bin/bash

# Beschrijving:
#   Script om de namen en het gevonden totaal
#   en gemiddelde uit een gegeven file te halen.
#
# Arguments:
#   Argument 1 is een file
#
# Auteur: Gerd Goemans gerd.goemans@student.kdg.be
# Copyright: 2019 MIT Gerd Goemans
#
# Versie: 0.1
#
# Requires: Standaard shell commando's
#

#Define error function
reset='[0m'
rood='[0;31m'
function printError() {
  #foutmeldingen versturen naar stderr met >&2
  #foutmeldingen bevatten ook het naam van het script ($0 of basename $0)
  echo -e "\e$rood $0" >&2
  echo -e "$1" >&2
  echo -e "\e$reset" >&2
  #vermits dit altijd word uitgevoer als er een error is kunnen we ook hier best IFS unsetten
  unset IFS
}

IFS=$'\n'

#check op root:
if [ "$(id -u)" == "0" ]; then
  printError "Dit programma mag niet uitgevoerd worden als root"
  exit 1
fi

#check op dependencies
#Vervang "read mkdir rmdir" met de speciale commando's waarop je dependencies wil testen
for i in read test ; do
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
  echo -e "\t\tEen file met ronde tijden"

  echo -e "\nVoorbeeld:"
  echo -e "\t./rijndetijden.sh rondetijden.txt"
  exit 0
fi

#test of input een bestand is dat bestaat
#en niet leeg is (zie man test voor meer tests)
if [ -s "$1" ]; then
  echo "Script van: Goemans Gerd"
else
  printError "Argument 1 is geen bestand of is leeg"
fi


totaalUren=0
totaalMinuten=0

aantalOks=0
gemiddeldeUren=0
gemiddeldeMinuten=0

regex="^Deelnemer(.*)Uur([0-9])Minuten([0-9]{1,2})"

for line in $(cat $1) ; do
  if [[ $line =~ $regex ]] ; then
    echo "Rondo OK voor: ${BASH_REMATCH[1]}"
    totaalUren=$(($totaalUren+${BASH_REMATCH[2]}))
    totaalMinuten=$(($totaalMinuten+${BASH_REMATCH[3]}))
    aantalOks=$(($aantalOks+1))
  fi
done

while [ $totaalMinuten -ge 60 ] ; do
  totaalUren=$(($totaalUren+1))
  totaalMinuten=$(($totaalMinuten-60))
done

gemiddeldeUren=$(echo "scale=1;$totaalUren/$aantalOks" | bc -l)
gemiddeldeMinuten=$(echo "scale=1;$totaalMinuten/$aantalOks" | bc -l)

echo "Gevonden totaal: $totaalUren uren en $totaalMinuten minuten."
echo "Gemiddelde: $gemiddeldeUren uren en $gemiddeldeMinuten minuten"


unset IFS
#normal exit
exit 0
