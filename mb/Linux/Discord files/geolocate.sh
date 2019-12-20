#!/bin/bash
# Author:     jan celis
# Arguments:  ip adres of naam
# Requires:   apt-get install imagemagick geoip-bin bc
#             mercatormap of the world
# Remark:     bc needs a scale ! (after comma) or option -l for default scale
color="yellow"
worldmap="geolocate.jpg"  # mercator world map
locationtag=4         # radius of location tag

if ! [ -s "$worldmap" ]; then 
	echo " Kan $worldmap niet vinden">&2
	exit 1
fi
pi=3.1415 
ipinfo=`geoiplookup -f /usr/share/GeoIP/GeoLiteCity.dat $1`

latitude=`echo $ipinfo|cut -d, -f7`
longitude=`echo $ipinfo|cut -d, -f8`
#latitude=37.384499 #longitude=-122.088097

mapWidth=`convert -ping $worldmap -format %W info:`
mapHeight=`convert -ping $worldmap -format %H info:`

x=`echo "scale=4;($longitude+180)*($mapWidth/360)" | bc`
# convert from degrees to radians
latRad=`echo "scale=4;$latitude*$pi/180"| bc;`
# tan bestaat niet in bc en is dus s(x)/c(x) , log is l(x)
# optie bc -l laadt math libs in en zet default scale op 20
mercN=`echo "scale=4;l(s(($pi/4)+($latRad/2))/c(($pi/4)+($latRad/2)))" | bc -l`
y=`echo "scale=4;($mapHeight/2)-($mapWidth*$mercN/(2*$pi))"|bc`

x=`echo $x|cut -d. -f1` #>> xcoords.txt
y=`echo $y|cut -d. -f1` #>> xcoords.txt

ycircle=`echo "scale=4;$y+$locationtag" | bc`
#1052-1060
#528-535
if [ $x -lt 1052 -o $x -gt 1060 -o $y -lt 528 -o $y -gt 535 ]; then
  color="red" 
  echo $1 >> badguys.txt
fi
echo x $x y $y

convert -page ${mapWidth}x${mapHeight} $worldmap -fill $color -draw "circle $x,$y $x,$ycircle" -layers flatten geolocatenew.jpg 
