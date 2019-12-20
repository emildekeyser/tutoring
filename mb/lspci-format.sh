#!/bin/bash
IFS=$'\n'

device_regex='^[0-9][0-9]:[0-9][0-9]\.[0-9] (.*): .*'
memory_regex='Memory at ([0-9a-f]{8}) \(.*\) \[size=([0-9]+[KMG]?)]$'

for line in $(lspci -v)
do
    if [[ $line =~ $device_regex ]]
    then
        echo "DEVICE: ${BASH_REMATCH[1]^^}"
    fi

    if [[ $line =~ $memory_regex ]]
    then
        echo "Has memory at ${BASH_REMATCH[1]} of size = ${BASH_REMATCH[2]}"
    fi
done
