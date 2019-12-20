#!/bin/bash

#Week 1: Inleiding scripting
#Eerste lijn! : #!/bin/bash
#Om script te draaien: chmod +x naam.sh
#Script starten met ./naam.sh

#Output commando naar bestand: >
#Output error naar bestand: 2>
#Error in prullenbak gooien: 2> /dev/null
#2 = standaarderror
#>&2 = output commando wegstoppen (exception) in standaarderror, zelfde als 1>&2
#Output commando als input ander commando: |

#Voorbeeld:
cut -d: -f7 </etc/passwd | sort
# gaat het 7de veld nemen uit /etc/passwd, cut doen op de : en dan sorteren

#Variabelen
mijnvar="hallo"
#Gebruiken in commando:
echo $mijnvar #Oproepen
#Of
echo "${mijnvar} gebruiker" #Gebruiken in commando

#Backquote: voeren het commando uit en vullen de output in
#`` (ALTGR + µ)
echo "Er zijn `cat /etc/passwd | wc -l` users"
#Gaat /etc/passwd openen en aantal lijnen weergeven (-l)
#Backquotes doen hetzelfde als $()
echo "Er zijn $(cat /etc/passwd | wc -l) users"

#echo:  textoutput tonen op scherm
#cat:   tonen inhoud van een bestand
#cut:   knippen, ook met velden en separators
#       goed om lijnen van een bestand te doorlopen
#sort:  sorteren bestand
#uniq:  tonen dubbele of niet dubbele lijnen
#wc:    tellen van lijnen, woorden, karakters
#head:  eerste n lijnen tonen
#tail:  laatste n lijnen tonen
#grep:  zoeken op patronen in bestand (ook regex),
#       kan gebruikt worden of een bestand een argument bevat
#       --text om een tekst te zoeken in een bestand
#find:  zoeken naar bepaalde bestanden cat: tonen inhoud van een bestand

#bash parameters
# $0 : bestandsnaam
# $1 : eerste parameter
# $2 : tweede parameter
# $3 : derde parameter

#Debuggen: -x gebruiken bij opstarten
#Of #!/bin/bash -x op eerste lijn


#Week 1: Herhaling loops
#if-structuur
if test -f "/etc/passwd"
then
  cat /etc/passwd
fi
#Als de file bestaat en regular is (-f) wordt de inhoud getoond.

#test kan vervangen worden door [  ]
if [ -f "/etc/passwd" ]
then
  cat /etc/passwd
fi

#While-structuur
teller=0
while [ $teller -lt 10 ] #zolang de teller kleiner is dan (-lt) 10
do
  echo -n "$teller "
  let teller += 1 # eentje bijtellen
done
echo -e "\nEinde" #-e zodat we \n kunnen gebruiken

#Bash operators uit "man test"
#                 string    numeriek
# gelijk          x = y     x -eq y
# niet gelijk     x!=y      x -ne y
# groter          x>y       x -gt y
# kleiner         x<y       x -lt y
# groter/gelijk   x>=y      x -ge y
# niet leeg       -n x
# leeg(zero)      -z x

#Voorbeeld: zien of alle 3 de argumenten ingevuld zijn
if [ -z "$3" ]; then echo $error_usage ; exit 1;

#nc pf netcat => programma om te zien of lokale ssh-service reageert
nc -w 1 127.0.0.1 22 2>/dev/null >/dev/null

#Bestanden nakijken (man test)
# -d is directory (Best practices => controleren of input wel een map is)
# -f is file
# -e bestand bestaat (exists)
# -r leesrechten op bestand
# -s bestaat en niet leeg (leesbaar)
# -w schrijfrechten op bestand
# -x exe rechten op bestand aka is uitvoerbaar
# -z kijken of een string null is
# locatie commandos = /bin/commando

#for-structuur
directory="/usr/share/backgrounds"
for bestand in `ls $directory` #ls laat de inhoud van de map zien
do
  echo "Bestand: $bestand" #Oproepen met $
done


#Week 2: Bash best practices
# > gaat een bestand aanmaken of overschrijven en de output daarin stoppen
# >> gaat de output toevoegen aan een bestaand bestand of
#    bestand aanmaken als het nog niet bestaat

# $# geeft het aantal parameters terug
# -o zelfde als || -a zelfde als &&

#--help
if [ $# -lt 1 -o "$1" = "--help" ] #-o = or
then #als er minder dan 1 parameter is of $1 gelijk is aan --help
  echo "Usage: `basename $0` arg1 " #basename $0 geeft de naam van het script terug
  exit 1 #script beeindigen
fi
echo "Eerste argument is $1"

#Voorbeeld --help
if [ "$1" = "--help" ]
then
	echo "This script searches for files of a given size in a given directory"
	echo ""
	echo "arguments: "
	echo "1: dir: the directory in which you want to search for files (default /)"
	echo "2: number: the size (in MB) of the file you want to search for (default 10)"
	exit 1
  #Voorbeeld --version
else if [ "$1" = "--version" ]
	then
		echo "`basename $0` version 0.1"
		exit 1
	fi
fi

#============================================================
#
# FILE: myscript.sh
#
# USAGE: ./myscript.sh
#
# DESCRIPTION:
# OPTIONS: ---
# REQUIREMENTS: ---
# BUGS: ---
# NOTES: ---
# AUTHOR: Styn Vercauteren (styn.vercauteren@student.kdg.be)
# COMPANY: KdG
# VERSION: 1.0
# CREATED: 27/05/2019 14:00:00 CET
# REVISION: ---
#============================================================

#testen of input integer is
echo "Geef een getal: "
read getal #read om input te vragen (-s = silent mode, geen echo in terminal) (-p = geen newline)
#numeriek controleren of de getallen gelijk zijn
if [ "$getal" -eq "$getal" ] 2>/dev/null;
then
  echo $getal is een getal
else
  echo $getal is geen getal
fi

#/dev/null kan ook gewoon zo gebruikt worden als output weg moet zonder error

#testen of een bestand leeg is
echo "Geef de bestandsnaam: "
read bestandsnaam
if [ -s "$bestandsnaam" ] #-s = bestaat het en zit er iets in (size > 0)
then
 cat $bestandsnaam
else
 echo $bestandsnaam werd niet gevonden
fi

#afspraken Variabelen
#Omgevingsvariabelen (env) met HOOFDLETTER (Bv: $HOME, $USER, ...)
#Eigen variabelen lowercase

#Begin script
#!/bin/bash
# Functie: Zoekt naar grote bestanden
#          In een bepaalde directory
# Arguments: Arg1 is een directory
# Auteur: styn.vercauteren@student.kdg.be
# Copyright: 2019 GNU v3 styn.vercauteren@student.kdg.be
# Versie: 0.1
# Requires: Standaard shell find (ander commando als geen find gebruikt wordt) commando

#sudo indien nodig
#!/bin/bash
#id -u = id van de user, 0 bij root
if [ "$(id -u)" != "0" ] #"" want controleren op strings
then
  echo "Dit script moet je als root uitvoeren" 1>&2
  exit 1
fi
sudo cat /etc/shadow

#Foutcodes
# 0 = STDIN = success
# 1 = STDOUT = script eindigen met klein fouten
# 2 = STDERR = error, bv >&2, heeft exit voor grotere fouten

#Functie
#!/bin/bash
# Functie: Geeft een foutbericht bij volle schijf
err_df="Fout in $0:Je schijf is vol"
function func_df()
{
#diskusage van root pipen naar tr (translate),
#gaat alle spaties naar 1 spatie doen, pipen naar cut wat spaties als delimiter gaat gebruiken,
#gaat de 5de field nemen en pipen naar tail wat de laatste lijn gaat nemen van de 2
  df_percent=`df /|tr -s ' ' |cut -d' ' -f5|tail -n1`
  if [ "$df_percent" = "100%" ]
  then
    echo "$err_df" >&2 #exception throwen naar standaarderror
  fi
}


#Dependencies
#Nakijken of een commando bestaat voor het gebruikt wordt
error_geen_ab="Het programma ab is niet geïnstalleerd"
#command -v gaat checken of het commmand bestaat
#door > /dev/null ziet de user de foutmelding niet
command -v ab >/dev/null || (echo $error_geen_ab >&2 && exit 1);
#foutmelding gooien en programma eindigen

#kan ook met which (laat zien waar het commando staat)
which ab >/dev/null || (echo $error_geen_ab >&2 && exit 1);
#kan je ook gebruiken of een programma / commando bestaat

#Nakijken of een programma fouten gaf of niet
error_url="de url is niet bereikbaar"
#curl wordt gebruikt om url-transfer te doen
#-o gaat output schrijven naar file ipv STDOUT
curl -o /dev/null --silent --head --connect-timeout 1 ${url}
#via $? kan je de errorcode van laatste commando zien
if [ $? -ne 0 ]
then
  echo ${error_url} && exit 1
fi

#Pakket commando? => dpkg -S commando (bij ab apache2 bv.)


#Week 3: Bash functies en tellen
#Functies:  moet gedefinieerd worden voor gebruik
#           mag niet leeg zijn
#           $1, $2, ... zijn in een functie parameters van de functie

#Functie met argument
#!/bin/bash
# Functie: Argument tonen in output in het rood
reset='[0m' # reset zodat na output niet alles in kleur is
rood='[0;31m'
function tooninkleur() {
  echo -e "\e$rood $1 \e$reset" #-e zorgt ervoor dat \e (escape) kan gebruikt worden
}

tooninkleur "Hallo" #Geen gebruik van haakjes!

#Functie kan alleen gelukt of niet gelukt teruggeven
function checkexist(){
  if [ -f "$1" ] #kijken of het bestaat en is regular
  then
    return 0 #succes
  else
    return 1 #stoppen
fi
}

if [ checkexist "/etc/passwd" ]
then
  echo passwd ok
fi

#return doen
#!/bin/bash
# Functie: "Return" waarde van een functie is een string
function tooninkleur() {
  local reset='[0m' #local voor var in functie
  local rood='[0;31m'
  echo -e "\e$rood $1 \e$reset" #return string via echo
}
resultaat=$(tooninkleur "ok") # of resultaat =`tooninkleur "ok"`
echo $resultaat

#Tellen
#+ - / * % (mod) ** (exponentioneel)

#in var stoppen
a=1
b=2
som=`expr $a + $b`
#of met let
let "som=$a+$b" #gebruiken om na initialisatie waarde aan te passen
#of in bash
som=$(($a+$b))

#Bij kommagetallen => bc
echo 'scale=3; 6.5 / 2.7' | bc: #3 cijfers na de komma

#pwd = naam afprinten van directory
echo "$counter $(pwd $1)"

#Week 4: Bash Paremeter Substitutie

#Interne variabelen
# $$ = eigen proces-id
# $_ = hele string van bovenstaande commando
# & = wordt na een commando gezet waardoor het in achtergond afloopt (./child.sh &)
# $! = proces-id laatste achtergondproces

#Gebruik IFS (Inter Field Separator)
#!/bin/bash
# Args: Arg $1 is een bestand OF via stdin
IFS=$'\n'
for lijn in $(cat "$@") #$@ = Alle meegegeven argumenten
do
  echo $lijn
done
unset IFS #Niet vergeten!

#Variabele ${var}
#Kan gebruikt worden om in commando te zoeken naar grote files
#(size plakken achter grootte (5MB))
#!/bin/bash
# Functie: Zoeken naar grote bestanden, default >MB
# Args: Arg $1 MAG meegegeven worden
# Als $1 leeg is, krijgt het een default waarde
default_waarde="10"
# :- kijkt of het argument ($1) leeg is. dan krijg het $default_waarde
size=${1:-$default_waarde} # of =${1:-10}
# met if
if [ $# -lt 1 ] ; #(Best practices)

find . -iname "*" -size "+${size}M"
#-iname gaat case insensitive kijken of de grootte van de file groter is dan size

size=${1?"Usage: `basename $0` ARGUMENT"}
# ? gaat als parameter leeg is de tekst geven als foutmelding en exit 1 doen
#code eronder komt hij pas als var gevuld is

#Replace (& replace)

#!/bin/bash
# Functie: Replace in een string
url="http://www.kdg.be/index.html"
echo String ${url}

echo Vervang kdg 1x door student
${url/kdg/student}

echo Vervang ht altijd door f
${url//ht/f}

echo Vervang begin met http door ftp
${url/#http/ftp} # # = vanaf links beginnen

echo Vervang einde met html met aspx
${url/%html/aspx}# % = vanaf rechts beginnen

#Substring
#!/bin/bash
url="http://www.kdg.be/index.html"
echo String ${url}

echo Eerste 7 karakters knippen ${url:7} #Zonder start positie
# Haakjes of spatie is escape van positie

echo Laatste 4 karakters knippen ${url: -4} #negatief getal dus omgekeerd van rechts
# of echo Laatste 4 karakters ${url:(-4)}

echo Eerste 4 karakters weergeven ${url:0:4}

echo Karakter 8 tot 18 weergeven ${url:7:10} #8ste karakter beginnen, 10 nemen inclusief

#Trim
# Functie: Verwijder gedeelte string voor/achteraan
# greedy en ungreedy
url="http://www.kdg.be/index.html"

# Verwijder korste substring http:// vooraan:
${url#http://}

# Verwijder langste substring http*. vooraan:
${url##http*.}

# Verwijder korste substring non-greedy .\* achteraan:
${url%.*}

# Verwijder langste substring greedy .\* achteraan:
${url%%.*}

#Lengte string
${#url}

#Uppercase (makkelijk punt op examen!)
${url^^}

#lowercase
${url,,}

#Week 5: Bash regex

#Opstelling regex (waar, wat, hoeveel)
#1) anchors = geven weer waar je kijkt in de tekst (^ (begin), $ (einde)) (^The end$)
#2) charactersets = wat ga je zoeken, ofwel letterlijke betekenis (woordje)
#                   of computerbetekenis (new line)
#3) modifier = je past aan wat je zoekt naar hoeveel keer je het zoekt

#Voorbeelden
# .       1 karakter
# [a-z]   karakter a tot en met z in kleine letters
# [0-9]   getal 0 tot en met 9
# [a|b]   karakter a of karakter b
# a{4}    vier keer a
# a{1,4}  van één tot 4 keer a
# +       1 tot n keer
# *       0 tot n keer

#Soorten karakters (best declareren als var in begin script)
# [[:digit:]]   een cijfer
# [[:space:]]   spatie,tab, newl, return
# [[:alnum:]]   letters en cijfers
# [[:alpha:]]   letters
# [[:blank:]]   spatie en tab
# [[:lower:]]   lowercase letters
# [[:print:]]   afdrukbare karakters

# =~ wordt gebruikt voor regex in if
#!/bin/bash
content="Karel de Grote-Hogeschool, Nationalestraat 5,B-2000 Antwerpen"
regex="B-[0-9]{4}" #postcode (start met B-, dan 4x een getal)

if [[ $content =~ $regex ]] #dubbele haken moet bij regex!
then
echo "postnummer gevonden" ; exit 0
else
echo "postnummer niet gevonden" >&2 ; exit 1
fi

#OPGELET: $regex is NOOIT met dubbele quotes!

#${BASH_REMATCH[0]} = array met het resultaat van de match. Element 0 is de hele match
#!/bin/bash
# Functie: Regex voor een postnummer
content="Karel de Grote-Hogeschool, Nationalestraat 5,B-2000 Antwerpen"
regex="B-[0-9]{4}"
[[ $content =~ $regex ]]
echo "${BASH_REMATCH[0]}"
#Geeft heel de string terug waarin de regex gevonden is (B-2000)

#Voorbeeld mailadres
# jan           . celis         @ kdg           . be
# [[:alnum:]]+  . [[:alnum:]]+  @ [[:alnum:]]+  . [[:alpha:]]+

# Het eerste stuk kan ook zonder punt zijn, dus dat plaatsen we optioneel:
# jancelis                          @ kdg           . be
# ([[:alnum:]]+.){0,2} [[:alnum:]]+ @ [[:alnum:]]+  . [[:alpha:]]+

# Het tweede deel kan ook uit subdomeinen bestaan:
# jan .                 celis        @  student . kdg . be
# ([[:alnum:]]+.){0,2}  [[:alnum:]]+ @  ([[:alnum:]]+.){1,3} [[:alpha:]]+

# Het laatste domein deel is van 2 tot 3 karakters (zonder cijfers):
# jan .                 celis       @ student . kdg . be
# ([[:alnum:]]+.){0,2} [[:alnum:]]+ @ ([[:alnum:]]+.){1,3} [[:alpha:]]{2,3}

#regex groups (selecteert met haakjes een onderdeel van de regex)
content="Karel de Grote-Hogeschool, Nationalestraat 5,B-2000 Antwerpen"
regex="([- a-zA-Z]+), ([[:alpha:]]+) ([[:digit:]]+),(.*) (.*)"
#alles opdelen met ()

[[ $content =~ $regex ]]
echo "Naam: ${BASH_REMATCH[1]}" #Eerste deel van regex
echo "Straat: ${BASH_REMATCH[2]} Nr: ${BASH_REMATCH[3]}"
echo "Postcode: ${BASH_REMATCH[4]} Stad: ${BASH_REMATCH[5]}"
#Output:
#Naam: Karel de Grote-Hogeschool
#Straat: Nationalestraat Nr: 5
#Postcode: 2000 Stad: Antwerpen

#regex met parameter Substitutie
#!/bin/bash
content=" Karel de Grote-Hogeschool, Nationalestraat 5,B-2000 Antwerpen"
shopt -q -s extglob #shopt wordt gebruik om bash shell opties aan en af te zetten
#-s = opstarten
content2=${content#*+([[:digit:]])} # # = korste substring, ungreedy
content=${content##*+([[:digit:]])} # ## = langste substring, greedy
shopt -q -u extglob
#Extended globbing => zelfde als regex, maar anders
#quantifiers hebben zelfde betekenis, maar moeten voor patroon staan ipv erachter
#zie slides
#-u = afzetten (Best practices)
echo "ungreedy: $content2"
echo "greedy: $content"
Output:
ungreedy: ,B-2000 Antwerpen
greedy: Antwerpen

#content = string functie om te knippen
content=${content##*+([[:digit:]])}
# String functie om te knippen
# # een zo klein mogelijk string vinden
# ## een zo groot mogelijk string vinden
# * = pattern = any string (including NULL)
# 1 of meer cijfers (equivalent met [[:digit:]]+ in regex)
#Besluit:
#Zoeken de grootst mogelijke string die start met eender wat en eindigt op
#1 of meer getallen en knippen die weg.
