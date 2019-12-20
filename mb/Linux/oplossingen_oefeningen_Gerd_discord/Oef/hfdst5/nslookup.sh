#maak eerst een file met IPs
inputfile="ips.txt"
echo "109.74.196.225" > ips.txt
echo "91.189.90.40" >> ips.txt
echo "173.194.34.168" >> ips.txt

#set IFS to newline, gewoon voor de zekerheid
IFS=$'\n'

#definieer de functie de we moeten gebruiken
function fun_nslookup() {
    #de rauwe output van dat comonade steken we in de nsLookUpReturn var
    nsLookUpReturn=`nslookup $1`
    #knip alles van de voorkant af tot de eerste (en enigne in dit geval) string "name = "
    hostname=${nsLookUpReturn#*name = }
    #knip alles van het uitinde na het laatste .
    hostname=${hostname%.*}
    #echo de naam de we nu alleen nog maar hebben
    echo $hostname
}

for ip in `cat $inputfile ` ; do
  fun_nslookup $ip
done

unset IFS
