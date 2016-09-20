# -*- coding: utf-8 -*-

f = open('2016_09_12_19_01_07_alex.oses.Escitalo','r')
especial = [' ','`','0','1','2','3','4','5','6','7','8','9','.',',']


def transpose(X):
    size = len(X)
    for i in range(int(size)):
       # iterate through columns
       j = i
       while j < int(size):
           aux = X[i][j]
           X[i][j] = X[j][i]
           X[j][i] = aux
           j += 1
    return X

p = open('result.xd','w')
for codedText in f:
    for currentSize in range(100):
        currentSize *= 7
        if not currentSize <= 0:
            codedAux = codedText
            mensaje = ""
            while codedAux != "":
                Mat = []
                for i in range(currentSize):
                    row = []
                    for j in range(currentSize):
                        if len(codedAux) > 0:
                            row += [codedAux[0]]
                            codedAux = codedAux[1:]
                        else:
                            row += [chr(0)]
                    Mat.append(row)
                Mat = transpose(Mat)
                for row in Mat:
                    for letra in row:
                        mensaje += letra
            p.write('clave: '+ str(currentSize) + ' : ' + mensaje)
            p.write(' ')