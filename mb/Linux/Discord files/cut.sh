#!/bin/bash

cutme=false
eerste=$1
shift
optie=${eerste:0:2}
if [ $optie = "-c" ]
 then
  cutme=true
  van=${eerste#-c}
  van=${van%-*}
  van=$(($van-1))
  tot=${eerste##*-}
  lengte=$(($tot-$van))
fi

IFS=$'\n'
for lijn in $(cat "$@")
do
 if $cutme
  then 
lijn=${lijn:$van:$lengte}
 fi
  echo $lijn
done 