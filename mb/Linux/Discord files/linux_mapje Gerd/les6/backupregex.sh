#!/bin/bash

regex="-h$|--help$|-h[[:space:]]"
if [[ $@ =~ $regex ]]
 then
  echo Usage $(basename $0) [directory]
 exit 0
fi

#get de searchdir van de params
searchDir=$1

#als er geen is megegeven gebruik home als default
if [ "$searchDir" = "" ] ; then
	searchDir="/home"
fi

#2 env variablen
errorlog="/var/log/error_`basename $0`.log"
backuplog="/var/log/backup_`basename $0`.log"

#als searchdir geen dir is print dan een message naar het file dat we hierboven hebben gedefinieerd
if [ ! -d $searchDir ] ; then
	echo "Opstarten met een directory als eerste argument: bv. sudo ./`basename $0` /home" >> $errorlog
	exit 1
fi

#als we geen root zijn printen we ook een message naar het file dat hierboven gedifineerd werd
if [ "$(id -u)" != "0" ]; then
	echo "Dit script moet je als root uitvoeren" >> $errorlog
	exit 1
fi

#doe de backup
dateString=$(date '+%Y_%m_%d_%H_%M_%S')
find $searchDir -type f -cmin -500 -print0 | tar -czvf "backup_${dateString}.tar.gz" --null -T -
#werkt nog niet helemaal, stdout van het vorige commando zou nog naar backuplog moeten gestuurd worden en stderror naar errorlog
