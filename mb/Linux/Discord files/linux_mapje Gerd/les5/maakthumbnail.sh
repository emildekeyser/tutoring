#!/bin/bash
IFS=$'\n'
maak_thumbnail () {
convert -thumbnail 50x50 -extent 50x50 -gravity center ${1} ${2} 
}

for line in $(ls)
do
extension=${line: -3}
 if [ ${extensions,,} = "jpg" ] #,, is voor lowercase
  then
  naam="thumbnail_${line//jpg/png}"
  maak_thumbnail $line $naam
  if [ $? -eq 0 ]
  then
  echo "Bestand $line omgezet naar $naam"
 fi
done



