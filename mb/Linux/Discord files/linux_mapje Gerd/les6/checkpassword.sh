#!/bin/bash
echo "Geef u paswoord"
read -s content
a="[[:alpha:]]"; d="[[:digit:]]"
u="[[:upper:]]"; p="[[:print:]]"
regex="^($u$p{5,}$d{2,})$"

[[ "$content" =~ $regex ]]
match="${BASH_REMATCH[1]}"

if [ -n "$match" ]
then
 echo Paswoord geldig
else
 echo Paswoord ongeldig
fi
