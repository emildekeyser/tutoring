#!/bin/bash

startTime=$(date +"%s%N")

zenity --warning --title "Hallo" --text"`date`" 2> /dev/null

endTime=$(date +"%s%N")


difTime=$(($endTime-$startTime))

seconds=$(($difTime/1000000000))
difTime=$(($difTime-$(($seconds*1000000000))))
mils=$(($difTime/1000000))
nans=$(($difTime-$(($mils*1000000))))

echo "Time taken: ${seconds}s ${mils}ms ${nans}ns"

