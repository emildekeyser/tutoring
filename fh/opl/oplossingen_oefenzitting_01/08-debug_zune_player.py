from calendar import isleap

ORIGIN_YEAR = 1980
days = int(input('Days since 1st January ' + str(ORIGIN_YEAR)))

year = ORIGIN_YEAR
while days > 365:
    if isleap(year):
        if days > 366:
            days -= 366
            year += 1
        else:
            break
    else:
        days -= 365
        year += 1

print('The current year ', year)
