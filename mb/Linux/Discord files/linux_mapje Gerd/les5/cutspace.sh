#!/bin/bash

IFS=$'\n'
for lijn in {1..10}
do
        touch "bestand ${RANDOM} ${bestand}"
done
for bestand in $(ls)
do
        mv "${bestand}" "${bestand// /_}" 2>/dev/null
done
~              