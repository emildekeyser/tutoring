#!/bin/bash
a="[[:alpha:]]"
d="[[:digit:]]"
u="[[:upper:]]"
p="[[:print:]]"

regex="$a{3} | [0-9]$d $d{2}:$d{2}:$d{2} $HOSTNAME (.*)\[$d+\]: (.*)"
content 'jan 31 20:02:14 kdguntu ntpd_intres[1024]: host name not'
for content in cat $logfile
do
[[ content =~ $regex]]
echo
 "${BASH_REMATCH[1]} ${BASH_REMATCH[2]}" >> "$0.tmp"
done
cat $0.tmp | sort | uniq -c | sort -g | grep -v info
rm -f "$tmpfile" 2>/dev/null
#regex="$a{3} | [0-9]$d $d$d:$d$d:$d$d $a+ (.*)(\[$d+\]){0,1}: (.*)"