#!/bin/bash

IFS=$'\n'       
counter = 0
        
for i in $(cat < "$1"); do
	counter=$(($counter+1))
done

echo "$counter $(pwd $1)"