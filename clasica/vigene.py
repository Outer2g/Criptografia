# -*- coding: utf-8 -*-
import re
import operator
import itertools

f = open('2016_09_12_19_01_07_alex.oses.Vigenere','r')
especial = [' ','`','0','1','2','3','4','5','6','7','8','9','.',',']
separadores = [' ','`','.']
hash = {}
listText = []
def k(f):
    for codedText in f:
        listText = re.findall(r"[\w']+", codedText)
    for elem in listText:
        try:
            apariciones = hash[elem][0]
            hash[elem] = [apariciones+1,0]
        except:
            hash[elem] = [1,0]
    for key, value in hash.items():
        if value[0]>20:
            print(key)

output = open('resultsvige.xd','w')
for codedText in f:
    for length in range(1):
        length += 1
        current = 0
        row =[]
        Mat = []
        apariciones = {}
        for letra in codedText:
            if not letra in especial:
                if len(row) < length:
                    row += letra.lower()
                else:
                    Mat += [row]
                    row = [letra.lower()]
        Mat += [row]
        for j in range(length):
            for i in range(len(Mat)):
                try:
                    letra = Mat[i][j]
                    if letra in apariciones:
                        if j in apariciones[letra]:
                            apariciones[letra][j] += 1
                        else:
                            apariciones[letra][j] = 1
                    else:
                        p = {}
                        p[j] = 1
                        apariciones[letra] = p
                except:
                    pass
        print(apariciones)
        finalPosibleKeys = []
        for posicion in range(length):
            ordenapariciones =''
            aux = {}
            for letra in apariciones:
                if posicion in apariciones[letra]:
                    aux[letra] = apariciones[letra][posicion]
            for letra in sorted(aux.items(), key=operator.itemgetter(1),reverse=True):
                ordenapariciones += letra[0]
            englishprobOrder = 'etaoinshrdlcumwfgypbvkjxqz'
            posibleKeys =[]
            i = 0
            ordenapariciones = ordenapariciones[:6][1:]
            for letra in ordenapariciones:
                number = (ord((letra))-97) - (ord(englishprobOrder[i])-97)
                if number < 0:
                    number += 26
                    posibleKeys += chr(number + 97)
                else:
                    posibleKeys += chr(number + 97)
                i += 1
            finalPosibleKeys += [posibleKeys]
        print(finalPosibleKeys)
        posibleKeys = []
        for r in list(itertools.product(*finalPosibleKeys)):
            posibleKeys += [''.join(r)]
        print(posibleKeys)
        todecode = codedText[:200]
        key = 'herbert'
        length = 6
        l = -1
        mensaje = ""
        for letra in todecode:
            if not letra in especial:
                if l < length-1:
                    l += 1
                else: l = -1
                number = (ord(letra) - 97) - (ord(key[l]) - 97)
                if number < 0:
                    number += 26
                    mensaje += chr(number + 97)
                else:
                    mensaje += chr(number + 97)
                l += 1
            else:
                mensaje += letra
        output.write(key + ' : ' + mensaje + '\n')
