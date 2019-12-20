#!/bin/bash
# Functie: velden uit syslog halen met regex 

logfile="/var/log/syslog"
tmpfile="`basename $0`.tmp"

#rm -f "$tmpfile" 2>/dev/null
OLD_IFS="$IFS"
IFS=$'\n'
#content='Jan  1 20:02:36 kdguntu ntpd_intres[10245]: host name not found'
regex="[[:alpha:]]{3} .*[0-9]{2}:[0-9]{2}:[0-9]{2} `hostname` (.*)"
regex="[[:alpha:]]{3} [ 0-9][0-9] [0-9]{2}:[0-9]{2}:[0-9]{2} `hostname` (.*)"
#regex="[[:alpha:]]{3}(.*)"
#content='Jan 31 20:02:36 kdguntu ntpd_intres[10245]: host name not found'

for content in `cat $logfile` 
do
  # Omzetten \d naar [0-9] (bash ondersteunt geen \d
 # substring='\\d'
 # replacement='[0-9]'
 # regex=${regex//$substring/$replacement}
if [[ $content =~ $regex ]]
then 
  #echo "${BASH_REMATCH[1]} " #>> "$0.tmp"
  echo "${BASH_REMATCH[1]} ${BASH_REMATCH[2]}" >> "$0.tmp"
fi
done

cat "$tmpfile" | sort | uniq -c | sort -g | grep -v info

#rm -f "$tmpfile" 2>/dev/null
IFS="$OLD_IFS"

