#!/bin/bash

IFS=$'\n'

#create 10 files
for (( i = 0; i < 10; i++ )); do
    touch "test $RANDOM.txt"
done

#remove spaces
for i in `ls *.txt`; do
  orgName=$(basename $i)
  newName=${orgName// /_}
  mv $orgName $newName
done

unset IFS
