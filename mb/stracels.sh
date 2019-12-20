#!/bin/bash

echo "Dit is het script van Goemans Gerd"

#variable declareren
reset='[0m'
rood='[0;31m'
groen='[1;32m'
IFS=$'\n'

#error functie
function printError() {
  # error bevat de naam van het script en het bericht dat meegegeven is aan deze functie
  echo -e "\e$rood $0" >&2
  echo -e "$1" >&2
  echo -e "\e$reset" >&2

  #unset IFS because this will be executed every time something goes wrong
  unset IFS
}

command -v strace >/dev/null
if [ $? != 0 ] ; then
  printError "Het programma strace is niet geïnstalleerd"
  exit 1
fi

regex="^(.*)\((.*,.*)\) *="

for line in $(strace ls / 2>&1); do

  if [[ $line =~ $regex ]] ; then
    echo "Working on line: $line"
    count=$(echo "${BASH_REMATCH[2]}" | wc -w)
    echo -e "Operand\e$groen ${BASH_REMATCH[1]}\e$reset contains $count parameters."
  fi
done
