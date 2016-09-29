# -*- coding: utf-8 -*-

f = open('2016_09_12_19_01_07_alex.oses.Escitalo','r')
especial = [' ','`','0','1','2','3','4','5','6','7','8','9','.',',']


def printToFile(data,key,extension):
    f = open("resultadosvig2.xd",'w+')
    f.write(data)

def escitalo():
    import math
    global data
    global clave
    solucion = ""
    clave = 0
    while True:
        clave += 7
        lenght = len(data)
        count = len(data)
        for c in range(0, math.ceil(lenght / clave)):
            for i in range(0, clave):
                print(data[c + i * int(lenght / clave)], end="")
                count -= 1
                if count < 0:
                    break
            if count < 0:
                break

        print("---")
        count = 100
        for c in range(0, clave):
            for i in range(0, math.ceil(lenght / clave)):
                print(data[i * clave + c], end="")
                count -= 1
                if count < 0:
                    break
            if count < 0:
                break

        if input("--- Solucion? [y/n] (clave " + str(clave) + ") ") == "y":
            print("--------- La clave es: " + str(clave))
            claveStr = str(clave)
            for c in range(0, clave):
                for i in range(0, math.ceil(lenght / clave)):
                    if i * clave + clave <= lenght:
                        solucion += data[clave * i + c]
                        print(data[clave * i + c], end="")
            printToFile(solucion, claveStr, "Escitalo")
            break


def main():
	global data
	data = open('2016_09_12_19_01_07_alex.oses.Escitalo','r').read()
	escitalo()

if __name__ == '__main__':
    main()