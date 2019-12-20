#!/bin/bash
IFS=$'\n'
poorten=""
echo "TCP poorten: "
for lijn in $(netstat -tulpn 2>/dev/null)
do
eerste="${lijn%% *}"
laatste="${lijn:68:6}"

if [ "$eerste" = "tcp" ] && [ "$laatste" = "LISTEN" ]
then 
lijn=${lijn#*:}
lijn=${lijn%% *}
echo $lijn
fi
done