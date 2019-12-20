#!/bin/bash
IFS=$'\n'
watermerk="Logo_V.png"
getWaterMark(){
if [ ! -e $watermerk ]
then
wget https://www.kdg.be/doc/huisstijl/Logo_V.png
convert $watermerk -brightness-contrast 92x20 $watermerk
fi
}
maakwatermerk(){
composite -compose bumpmap -tile ${watermerk} ${1} ${2} 
}


for line in $(ls)
do
extension=${line: -3}
 if [ ${extensions,,} = "jpg" ] #,, is voor lowercase
  then
  naam="${line//jpg/png}"
  maakwatermerk $line $naam
  if [ $? -eq 0 ]
  then
  echo "Bestand $line omgezet naar $naam"
 fi
done

