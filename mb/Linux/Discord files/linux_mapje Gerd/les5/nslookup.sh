#!/bin/bash

function fun_nslookup () {
ip=$1
lookup=$(nslookup $ip)
var1=${lookup#*=}
echo ${var1%.*}
}

inputfile="ips.txt"
echo "109.74.196.225" > ips.txt
echo "91.189.90.40" >> ips.txt
echo "173.194.34.168" >> ips.txt
filename='ips.txt'
while read line; do
        fun_nslookup $line
done < ${filename}
