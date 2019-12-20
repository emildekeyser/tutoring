#!/usr/bin/env bash
#author: Niels Palinckx

#declaratie functie
function kleursingle() {
  echo -e "\e${groen}${1} \e$reset"
}

echo "Script van: Niels Palinckx"
IFS=$'\n'
reset='[0m'
groen='[0;32m'
regex=".*(\(.*\)).*"
error_geen_strace="Het programma strace is nodig!"
command -v strace >/dev/null 2>&1 || { echo >&2 $error_geen_strace; exit 1; }

for line in  `strace ls / 2>&1` ;
do
  operand=${line%%\(*}
  [[ $line =~ $regex ]]
  commaparams=${BASH_REMATCH[1]//[^,]}
  countparams=$((${#commaparams}+ 1))
  echo "working on line $line"
  echo "Operand `kleursingle $operand` contains `kleursingle $countparams` parameters"
done


unset IFS
