#################################################################################
# Voorbeeld-programma voor berekening van GGD, incl. PRE/POST/LUS-INVARIANT     #
# Een bewijs eindigheid moet je nog zelf aanvullen!                             #
#################################################################################

a = int(input("Geef a: "))
b = int(input("Geef b: "))


#PRECONDITIE: a en b strikt positieve gehele getallen

d = min(a,b)

# INVARIANT: voor alle e > d: e is geen gemene deler

#    -> is geldig na initialisatie (een getal groter dan min(a,b) kan nooit een gehelde deler zijn)

while (not ((a%d==0) and (b%d==0))):

    # INVARIANT:    voor alle e > d: e is geen gemene deler
    # EN:           d is ook geen gemene deler (gezien we in de while-lus zijn geraakt)
    # DUS WETEN WE: voor alle e >= d: e is geen gemene deler

    d = d - 1
    # DUS:          voor alle e > d: e is geen gemene deler
    # DUS:          INVARIANT is geldig


# INVARIANT:    voor alle e > d: d is geen gemene deler
# EN:           d is een gemene deler van a en b (anders was de while-lus niet gestopt)
# DUS:          d is een gemene deler, en er zijn geen grotere gemene delers van a en b
# DUS:          d is de grootste gemene deler van a en b

print(d)
