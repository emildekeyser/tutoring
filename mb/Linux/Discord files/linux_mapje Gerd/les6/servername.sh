#!/bin/bash
regex="ServerName.*"
IFS=$'\n'
testje="false"
for lijn in `cat /etc/apache2/apache2.conf`
        do
                if [[ $lijn =~ $regex ]]
                then
                        testje="true"
                fi
        done
        if [ $testje == "true" ]
        then
                echo $testje
                echo gevonden
                exit 0;
        else
                echo $testje
                echo ni gevonden, toevoegen
                sudo chmod +777 /etc/apache2/apache2.conf
                echo ServerName mijnlaptop >>/etc/apache2/apache2.conf
                exit 0;
        fi
