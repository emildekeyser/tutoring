#!/bin/bash
   
   for naam in $(ls /proc/*/cmdline); do
   
     if [ -f $naam ]
       then
         if cat $naam | grep -a sbin > /dev/null; then
             echo $naam: $(tr -d '\0' <$naam)
         fi
    fi
  done
