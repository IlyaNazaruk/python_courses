def inch_to_cm(n):
    inch = n * 2.54
    return inch

def cm_to_inch(n):
    cm = n / 2.54
    return cm

def miles_to_km(n):
    ml = n * 1.609
    return ml

def km_to_miles(n):
    km = n / 1.609
    return km

def pound_to_kilo(n):
    kg = n / 2.204
    return kg

def kilo_to_pound(n):
    pound = n * 2.204
    return pound

def unc_to_gram(n):
    g = n * 28.35
    return g

def gram_to_unc(n):
    unc = n / 28.35
    return(unc)

def gal_to_l(n):
    l = n * 4.54
    return l
def l_to_gal(n):
    gal = n / 4.54
    return gal

def pint_to_l(n):
    l = n * 0.568
    return l

def l_to_pint(n):
    pint = n / 0.568
    return pint


while True:
    print(' 1. Дюймы в сантиметры\n 2. Сантиметры в дюймы\n 3. Мили в километры\n '
          '4. Километры в мили\n 5. Фунты в килограммы\n 6. Килограммы в фунты\n '
          '7. Унции в граммы\n 8. Граммы в унции\n ' '9. Галлон в литры\n '
          '10. Литры в галлоны\n 11. Пинты в литры\n 12. Литры в пинты')
    choose_convertation = int(input('Input number of convertation\n'))
    n = int(input('Input value to convertation\n'))

    if choose_convertation == 0:
        break

    if choose_convertation == 1:
        print(inch_to_cm(n))
    elif choose_convertation == 2:
        print(cm_to_inch(n))
    elif choose_convertation == 3:
        print(miles_to_km(n))
    elif choose_convertation == 4:
        print(km_to_miles(n))
    elif choose_convertation == 5:
        print(pound_to_kilo(n))
    elif choose_convertation == 6:
        print(kilo_to_pound(n))
    elif choose_convertation == 7:
        print(unc_to_gram(n))
    elif choose_convertation == 8:
        print(gram_to_unc(n))
    elif choose_convertation == 9:
        print(gal_to_l(n))
    elif choose_convertation == 10:
        print(l_to_gal(n))
    elif choose_convertation == 11:
        print(pint_to_l(n))
    elif choose_convertation == 12:
        print(l_to_pint(n))