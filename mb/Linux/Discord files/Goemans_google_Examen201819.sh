#!/bin/bash

# Beschrijving:
#   Best practices template
#
# Arguments:
#   Arg1 het OS waarop je wil zoeken
#
#   of
#
#   Arg1 het file waarin gezocht moet worden
#   Arg2 het OS waarop je wil zoeken
#
# Auteur: Gerd Goemans gerd.goemans@student.kdg.be
# Copyright: 2019 MIT Gerd Goemans
#
# Versie: 0.1
#
# Requires: Standaard shell commando's
#

#variable declareren
reset='[0m'
rood='[0;31m'
IFS=$'\n'
os=""
input_file="./imagelist.txt"
regex="$os-.*-V([0-9]{8}).*READY"
linecounter=0

#error functie
function printError() {
  # error bevat de naam van het script en het bericht dat meegegeven is aan deze functie
  echo -e "\e${rood}ERROR: $(basename $0)" >&2
  echo -e "$1" >&2
  echo -e "\e$reset" >&2

  #unset IFS because this will be executed every time something goes wrong
  unset IFS
}

echo "Dit is het script van Goemans Gerd"

#check op root:
if [ "$(id -u)" = "0" ]; then
  printError "Dit programma mag niet uitgevoerd worden als root"
  exit 1
fi

#check op dependencies (niet nodig, geen speciale commando's)
#for i in read mkdir rmdir ; do
#  command -v $i >/dev/null
#
#  if [ $? != 0 ] ; then
#    printError "Het programma $i is niet geïnstalleerd"
#    exit 1
#  fi
#done

#help argument
if [ "$1" = "--help" ] ; then
  echo "Help `basename $0`:"
  echo -e "\nBeschrijving: "
  echo -e "\tVervang dit door de beschrijving"

  echo -e "\nArgumenten: "

  echo -e "\n\tArgument 1: "
  echo -e "\t\tHet OS waarop je wil zoeken"
  echo -e "\nOf: "
  echo -e "\n\tArgument 1: "
  echo -e "\t\tHet bestand waarin je wil zoeken"
  echo -e "\n\tArgument 2: "
  echo -e "\t\tHet OS waarop je wil zoeken"

  echo -e "\nVoorbeeld:"
  echo -e "\tvoorbeeld hier"
  exit 0
fi

if [[ "$#" = "0" ]]; then
  printError "Script kan niet starten zonder parameters"
  exit 1
fi

if [[ $# -ge 3 ]]; then
  printError "Script mag maximum 2 parameters krijgen"
  exit 1
fi

if [[ "$#" = "1" ]]; then
  os=$1
else
  os=$2
  if [[ -s "$1" ]]; then
    input_file=$1
  else
    printError "$1 is geen bestaand en niet leeg inputfile"
    exit 1
  fi
fi

#OS naar upper case
os=${os^^}
#voor het geval os geupdate is
regex="$os-.*-V([0-9]{8}).*READY"

for line in $(cat $input_file) ; do
  #line naar upper case
  line=${line^^}

  if [[ $line =~ $regex ]] ; then
    echo "Found for $os with date ${BASH_REMATCH[1]}"
    linecounter=$(($linecounter+1))
  fi
done

if [[ "$linecounter" = "0" ]]; then
  echo "$os has not been found with any dates"
else
  echo "Number of lines found: $linecounter"
fi

#normal exit
unset IFS
exit 0
