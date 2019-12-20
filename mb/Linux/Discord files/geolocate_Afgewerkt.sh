#!/usr/bin/env bash

tancalc ()
{
    echo "scale=5;s($1)/c($1)" | bc -l
}


data=$(geoiplookup -f /usr/share/GeoIP/GeoLiteCity.dat 8.8.8.8)
lat=$(echo $data | cut -d',' -f7)
long=$(echo $data | cut -d',' -f8)
echo LAT : $lat
echo LONG: $long
mapWidth=2058
mapHeight=1746
x=$(echo "scale=2;($long+180)*($mapWidth/360)" | bc -l)
echo x: $x
pi=$(echo 'scale=5; 4*a(1)' | bc -l)
echo pi: $pi
latRad=$(echo "scale=5;$lat*$pi/180" | bc -l)
echo latRad: $latRad
needtan=$(echo "scale=5;(($pi/4)+($latRad/2))" | bc -l)
echo needtan: $needtan
tan=$(tancalc $needtan)
mercN=$(echo "scale=5;l($tan)" | bc -l)
echo mercN: $mercN
y=$(echo "scale=5;($mapHeight/2)-($mapWidth*$mercN/(2*$pi))" | bc -l)
echo y: $y
ycircle=$(echo "$y+10" | bc -l)
echo ycircle: $ycircle
convert -page ${mapWidth}x${mapHeight} geolocate.jpg -fill red -draw "circle ${x},${y} ${x},${ycircle}" -layers flatten geolocatenew.jpg
