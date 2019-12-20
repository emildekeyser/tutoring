#!/bin/bash

lat=$(geoiplookup -f /usr/share/GeoIP/GeoLiteCity.dat 8.8.8.8 | cut -f7 -d",")
long=$(geoiplookup -f /usr/share/GeoIP/GeoLiteCity.dat 8.8.8.8 | cut -f8 -d",")

mapWidth=2058
mapHeight=1746

x=$(echo"($long+180)*(mapWidth/360)" | bc: )

echo $x

#Niet af!
