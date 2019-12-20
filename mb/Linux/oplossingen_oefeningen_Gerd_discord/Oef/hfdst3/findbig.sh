#!/bin/bash

#check if we're asked for version or help
if [ "$1" = "--help" ] ; then
	echo "This script searches for files of a given size in a given directory"
	echo ""
	echo "arguments: "
	echo "1: dir: the directory in which you want to search for files (default /)"
	echo "2: number: the size (in MB) of the file you want to search for (default 10)"
	exit 0	
fi
if [ "$1" = "--version" ] ; then
	echo "`basename $0` version 0.1"
	exit 0		
fi

#check if argument 1 is a directory
if [ "$1" = "" ] ; then 
	path="/"
else
	if [ ! -d $1 ] ; then
		echo "$1 is not a directory" >&2
		exit 1
	fi
	path=$1
fi


#check if argument 2 is not nothing
if [ "$2" = "" ] ; then 
	size=10
else 
	#check if it is a number
	if [ ! "$2" -eq "$2" ] 2> /dev/null ; then
		echo "$2 is not a nuber" >&2
		exit 1
	fi
	size=$2
fi

#do what we're here for, search for big files and print them to the stdout
find $path -type f -size "+${size}M" -exec stat -c '%s %n' {} \;



