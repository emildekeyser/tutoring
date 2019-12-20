#!/bin/bash
IFS=$'\n'

for i in `ls *.png`; do
  echo $i
done


unset IFS
