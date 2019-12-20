#============================================================
#          FILE:  autologin.sh
#         USAGE:  ./autologin.sh hostname username password
#   DESCRIPTION: automatic ssh login with username/password
#
#       OPTIONS:  ---
#  REQUIREMENTS:  openssh-client, expect
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Jan Celis (jan.celis@kdg.be)
#       COMPANY:  KdG
#       VERSION:  1.0
#       CREATED:  01/21/13 15:42:08 CET
#      REVISION:  ---
#============================================================
host="127.0.0.1"
port="22"
tmpexpect="expect.sh"

error_geen_ssh="Het programma ssh is nodig. Installeren kan met sudo apt-get install openssh-client"
error_geen_expect="Het programma expect is nodig. Installeren kan met sudo apt-get install expect"
error_usage="Usage: `basename $0` hostname username password"
error_url="De host is niet bereikbaar"

# Nakijken of alle argumenten werden meegegeven
if [ -z "$3" ]; then echo $error_usage ; exit 1;
else
   echo Automatic login at $host
fi 

# Kijk met nc na of ssh draait -> ok => tekst, kan ook met $?
nc -w 1 $host $port 2>/dev/null >/dev/null
if [ $? -ne 0 ]; then
echo $error_url && exit 1  
fi


# Nakijken of ssh en expect geinstalleerd zijn
command -v ssh >/dev/null 2>&1 || { echo >&2 $error_geen_ssh; exit 1; }
command -v expect >/dev/null 2>&1 || { echo >&2 $error_geen_expect; exit 1; }

# Schrijven van een expect script
echo '#!/usr/bin/expect -f' > $tmpexpect
echo 'set timeout 20' >> $tmpexpect
echo "spawn ssh -o \"StrictHostKeyChecking no\" $2@$1" >> $tmpexpect 
echo 'expect "*assword:*"'  >> $tmpexpect	
echo "send $3\r">> $tmpexpect
echo "interact" >> $tmpexpect
echo "exit" >> $tmpexpect
chmod +x $tmpexpect

# Opstarten expect script en daarna verwijderen 
./$tmpexpect
rm -f $tmpexpect
