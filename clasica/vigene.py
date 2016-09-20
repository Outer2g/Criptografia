# -*- coding: utf-8 -*-
import re

f = open('2016_09_12_19_01_07_alex.oses.Vigenere','r')
especial = [' ','`','0','1','2','3','4','5','6','7','8','9','.',',']
separadores = [' ','`','.']
hash = {}
listText = []
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