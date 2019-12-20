#!/bin/bash
IFS=$'\n'

function maak_thumbnail(){
convert -thumbnail 50x50 -extent 50x50 -gravity center ${1} ${2}
}

for i in $(ls *.jpg); do
	thumbnailname="thumbnail${i}"
	juisteThumbnailname=${thumbnailname/.jpg/}
	echo "maak_thumbnail $i ${juisteThumbnailname}.png"
	
done


unset IFS
