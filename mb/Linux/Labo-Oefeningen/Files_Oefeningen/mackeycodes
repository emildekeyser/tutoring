#!/bin/bash
# xev is eeneventviewer die keycodes toont
echo "volledige ingestelde lijst keycodes"
xmodmap -pke
echo "Special codes"
xmodmap -pm
#OUDE keycode  49 = twosuperior threesuperior twosuperior threesuperior notsign notsign
xmodmap -e "keycode  49 = at numbersign twosuperior threesuperior numbersign numbersign"

# HAAKJES
#keycode  14 = parenleft 5 parenleft 5 onehalf threeeighths onehalf threeeighths
xmodmap -e "keycode  14 = parenleft 5 parenleft 5 braceleft bracketleft braceleft bracketleft"
#keycode  20 = parenright degree parenright degree backslash questiondown backsla

xmodmap -e "keycode  20 = parenright degree parenright degree braceright bracketright braceright bracketright"


#PIPE
#keycode  46 = l L l L lstroke Lstroke lstroke Lstroke
xmodmap -e "keycode  46 = l L l L lstroke bar lstroke bar"

#backslash
#keycode  60 = colon slash colon slash periodcentered division periodcentered division
xmodmap -e "keycode  60 = colon slash colon slash backslash backslash periodcentered backslash"


#keycode  21 = minus underscore minus underscore dead_cedilla dead_ogonek dead_cedilla dead_ogonek minus underscore dead_cedilla dead_ogonek
xmodmap -e "keycode  21 = minus underscore minus underscore Insert Insert Insert Insert"

#keycode 123 = XF86AudioRaiseVolume NoSymbol XF86AudioRaiseVolume NoSymbol XF86AudioRaiseVolume
#werktnietxmodmap -e "keycode 123 = XF86AudioRaiseVolume NoSymbol XF86AudioRaiseVolume Print Print"
xmodmap -e "keycode  51 = dead_grave sterling dead_grave sterling dead_grave dead_breve dead_grave dead_breve mu sterling dead_grave dead_breve"
# mu aan m toegevoegd
xmodmap -e "keycode  47 = m M m M dead_acute dead_doubleacute dead_acute mu m M dead_acute dead_doubleacute"

