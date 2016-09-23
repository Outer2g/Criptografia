# -*- coding: utf-8 -*-
f = open('2016_09_12_19_01_07_alex.oses.Cesar','r')
k = 1
especial = [' ','`','0','1','2','3','4','5','6','7','8','9','.',',']
for CodedText in f:
    while k <= 26:
        p = open ('results','w')
        out = "k =" + str(k)+ ": "
        for letra in CodedText:
            if not letra in especial:
                number = ord(letra.lower()) - 97
                fletra = chr(((number+k)%26)+65)
                out += fletra
            else:
                out += letra
        k += 1
## winner is 21 aka 5
    out = ""
    k = 21
    for letra in CodedText:
        if not letra in especial:
            number = ord(letra.lower()) - 97
            fletra = chr(((number + k) % 26) + 65)
            out += fletra
        else:
            out += letra
    p.close()
    p = open('alexoses_21.cesar','w')
    p.write(out)
    p.close()
    ree = open('alexoses_21.cesar','r')
    for text in ree:
        print('wewae')
        k = 5
        out = ""
        for letra in text:
            if not letra in especial:
                number = ord(letra.lower()) - 97
                fletra = chr(((number+k)%26)+65)
                out += fletra
            else:
                out += letra
        print(out)