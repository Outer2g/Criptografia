# -*- coding: utf-8 -*-
import time
#por byte 2
def Multiplicar_Por_X(numero):
    aux = numero << 1
    if (aux & 0x100) == 0x100:
        aux ^= 0x1b
    return (aux & 0xFF)

def GF_product_p(a,b):
    auxA = a
    auxB = b
    result = 0
    for i in range(8):
        if (auxB & 0x01) == 0x01:
            result ^= auxA
        auxA = Multiplicar_Por_X(auxA)
        auxB >>= 1
    return  result & 0xFF

def GF_Tables():
    global tabla_exp
    global tabla_log
    tabla_exp = [0x01]
    tabla_log = [0] * 256
    for i in range(2**8 -2):
        ant = tabla_exp[i]
        prod = GF_product_p(ant,0x03)
        tabla_exp += [prod]
        tabla_log[prod] = i+1

def GF_product_T(a,b):
    global tabla_exp
    global tabla_log
    ret = tabla_exp[(tabla_log[a] + tabla_log[b]) % 255]
    return ret & 0xFF

def GF_product_p_02(a):
    ret = Multiplicar_Por_X(a)
    return ret & 0xFF

def GF_product_t_02(a):
    global tabla_exp
    global tabla_log
    ret = tabla_exp[(tabla_log[a] + tabla_log[0x02]) % 255]
    return ret & 0xFF

def GF_product_p_03(a):
    ret = Multiplicar_Por_X(a) ^ a
    return ret & 0xFF

def GF_product_t_03(a):
    global tabla_exp
    global tabla_log
    ret = tabla_exp[(tabla_log[a] + tabla_log[0x03]) % 255]
    return ret & 0xFF

def GF_product_p_09(a):
    #0x09 = 0000 1001
    despl = a
    for _ in range(3):
        despl = Multiplicar_Por_X(despl)
    ret = despl
    ret ^= a
    return ret & 0xFF

def GF_product_t_09(a):
    global tabla_exp
    global tabla_log
    ret = tabla_exp[(tabla_log[a] + tabla_log[0x09]) % 255]
    return ret & 0xFF

def GF_product_p_0B(a):
    #0x0B = 0000 1011
    despl = a
    for _ in range(3):
        despl = Multiplicar_Por_X(despl)
    ret = despl
    ret ^= Multiplicar_Por_X(a)
    ret ^= a
    return ret & 0xFF

def GF_product_t_0B(a):
    global tabla_exp
    global tabla_log
    ret = tabla_exp[(tabla_log[a] + tabla_log[0x0B]) % 255]
    return ret & 0xFF

def GF_product_p_0D(a):
    # 0x00D = 0000 1101
    despl = a
    for _ in range(3):
        despl = Multiplicar_Por_X(despl)
    ret = despl
    despl = a
    for _ in range(2):
        despl = Multiplicar_Por_X(despl)
    ret ^= despl
    ret ^= a
    return ret & 0xFF

def GF_product_t_0D(a):
    global tabla_exp
    global tabla_log
    ret = tabla_exp[(tabla_log[a] + tabla_log[0x0D]) % 255]
    return ret & 0xFF

def GF_product_p_0E(a):
    #0x0E = 0000 1110
    despl = a
    for _ in range(3):
        despl = Multiplicar_Por_X(despl)
    ret = despl
    despl = a
    for _ in range(2):
        despl = Multiplicar_Por_X(despl)
    ret ^= despl
    ret ^= Multiplicar_Por_X(a)
    return ret & 0xFF

def GF_product_t_0E(a):
    global tabla_exp
    global tabla_log
    ret = tabla_exp[(tabla_log[a] + tabla_log[0x0E]) % 255]
    return ret & 0xFF
def GF_generador():
    list = []
    for i in range(200):
        prod = i+1
        j = 0
        while(prod != 1):
            prod = GF_product_p(prod,i+1)
            j += 1
        if j == 254:
            list += [i+1]
    return list
def GF_invers(a):
    global tabla_exp
    global tabla_log
    ret = tabla_exp[255-tabla_log[a]]
    return ret & 0xFF
GF_Tables()
number = 0x57
number2 =0x83
print(hex(GF_invers(0xf6)))
'''
GF_Tables()
print(tabla_exp)
print(tabla_log)
print(GF_product_t_0E(0x03))
print(GF_product_p(0x03,0x0E))
print(GF_generador())
def computeComparativas():
    list = []
    time1 = time.time()
    GF_product_p(0xA6,0x02)
    time2 = time.time()
    list += [time2-time1]

    time1 = time.time()
    GF_product_p_02(0xA6)
    time2 = time.time()
    list += [time2-time1]

    time1 = time.time()
    GF_product_p(0xA6,0x03)
    time2 = time.time()
    list += [time2 - time1]

    time1 = time.time()
    GF_product_p_03(0xA6)
    time2 = time.time()
    list += [time2 - time1]

    time1 = time.time()
    GF_product_p(0xA6,0x09)
    time2 = time.time()
    list += [time2 - time1]

    time1 = time.time()
    GF_product_p_09(0xA6)
    time2 = time.time()
    list += [time2 - time1]

    time1 = time.time()
    GF_product_p(0xA6, 0x0B)
    time2 = time.time()
    list += [time2 - time1]

    time1 = time.time()
    GF_product_p_0B(0xA6)
    time2 = time.time()
    list += [time2 - time1]

    time1 = time.time()
    GF_product_p(0xA6, 0x0D)
    time2 = time.time()
    list += [time2 - time1]

    time1 = time.time()
    GF_product_p_0D(0xA6)
    time2 = time.time()
    list += [time2 - time1]


    time1 = time.time()
    GF_product_p(0xA6, 0x0E)
    time2 = time.time()
    list += [time2 - time1]

    time1 = time.time()
    GF_product_p_0E(0xA6)
    time2 = time.time()
    list += [time2 - time1]


    #con t
    time1 = time.time()
    GF_product_T(0xA6, 0x02)
    time2 = time.time()
    list += [time2 - time1]

    time1 = time.time()
    GF_product_p_02(0xA6)
    time2 = time.time()
    list += [time2 - time1]

    time1 = time.time()
    GF_product_T(0xA6, 0x03)
    time2 = time.time()
    list += [time2 - time1]

    time1 = time.time()
    GF_product_p_03(0xA6)
    time2 = time.time()
    list += [time2 - time1]

    time1 = time.time()
    GF_product_T(0xA6, 0x09)
    time2 = time.time()
    list += [time2 - time1]

    time1 = time.time()
    GF_product_p_09(0xA6)
    time2 = time.time()
    list += [time2 - time1]

    time1 = time.time()
    GF_product_T(0xA6, 0x0B)
    time2 = time.time()
    list += [time2 - time1]

    time1 = time.time()
    GF_product_p_0B(0xA6)
    time2 = time.time()
    list += [time2 - time1]

    time1 = time.time()
    GF_product_T(0xA6, 0x0D)
    time2 = time.time()
    list += [time2 - time1]

    time1 = time.time()
    GF_product_p_0D(0xA6)
    time2 = time.time()
    list += [time2 - time1]

    time1 = time.time()
    GF_product_T(0xA6, 0x0E)
    time2 = time.time()
    list += [time2 - time1]

    time1 = time.time()
    GF_product_p_0E(0xA6)
    time2 = time.time()
    list += [time2 - time1]

    return list
def initHtmlDocument():
    file = open('res.dat', 'w+')
    file.write('<!DOCTYPE html> <html> <head> <style> table, th, td { border: 1px solid black;'+
               'border-collapse: collapse;} th, td { padding: 15px;} </style> </head><body></body>')
    file.write('<table style ="width:70%">')
    file.write('<tr><th>Metodo</th><th>Tiempo</th></tr>')
    list = computeComparativas()
    file.write('<tr> <td>GF_product_p(0xA6,0x02)</td> <td>'+str(list[0])+'</td></tr>')
    file.write('<tr> <td>GF_product_p_02(0xA6)</td> <td>'+str(list[1])+'</td></tr>')
    file.write('<tr> <td>GF_product_p(0xA6,0x03)</td> <td>'+str(list[2])+'</td></tr>')
    file.write('<tr> <td>GF_product_p_03(0xA6)</td> <td>'+str(list[3])+'</td></tr>')
    file.write('<tr> <td>GF_product_p(0xA6,0x09)</td> <td>'+str(list[4])+'</td></tr>')
    file.write('<tr> <td>GF_product_p_09(0xA6)</td> <td>'+str(list[5])+'</td></tr>')
    file.write('<tr> <td>GF_product_p(0xA6,0x0B)</td> <td>'+str(list[6])+'</td></tr>')
    file.write('<tr> <td>GF_product_p_0B(0xA6)</td> <td>'+str(list[7])+'</td></tr>')
    file.write('<tr> <td>GF_product_p(0xA6,0x0D)</td> <td>'+str(list[8])+'</td></tr>')
    file.write('<tr> <td>GF_product_p_0D(0xA6)</td> <td>'+str(list[9])+'</td></tr>')
    file.write('<tr> <td>GF_product_p(0xA6,0x0E)</td> <td>'+str(list[10])+'</td></tr>')
    file.write('<tr> <td>GF_product_p_0E(0xA6)</td> <td>'+str(list[11])+'</td></tr>')

    file.write('<table style ="width:70%"><br>')
    file.write('<tr><th>Metodo</th><th>Tiempo</th></tr>')
    file.write('<tr> <td>GF_product_t(0xA6,0x02)</td> <td>'+str(list[12])+'</td></tr>')
    file.write('<tr> <td>GF_product_t_02(0xA6)</td> <td>'+str(list[13])+'</td></tr>')
    file.write('<tr> <td>GF_product_t(0xA6,0x03)</td> <td>'+str(list[14])+'</td></tr>')
    file.write('<tr> <td>GF_product_t_03(0xA6)</td> <td>'+str(list[15])+'</td></tr>')
    file.write('<tr> <td>GF_product_t(0xA6,0x09)</td> <td>'+str(list[16])+'</td></tr>')
    file.write('<tr> <td>GF_product_t_09(0xA6)</td> <td>'+str(list[17])+'</td></tr>')
    file.write('<tr> <td>GF_product_t(0xA6,0x0B)</td> <td>'+str(list[18])+'</td></tr>')
    file.write('<tr> <td>GF_product_t_0B(0xA6)</td> <td>'+str(list[19])+'</td></tr>')
    file.write('<tr> <td>GF_product_t(0xA6,0x0D)</td> <td>'+str(list[20])+'</td></tr>')
    file.write('<tr> <td>GF_product_t_0D(0xA6)</td> <td>'+str(list[21])+'</td></tr>')
    file.write('<tr> <td>GF_product_t(0xA6,0x0E)</td> <td>'+str(list[22])+'</td></tr>')
    file.write('<tr> <td>GF_product_t_0E(0xA6)</td> <td>'+str(list[23])+'</td></tr>')
    return file
initHtmlDocument()
def initTable(file):

    file.write('<!DOCTYPE html> <html> <head> <style> table, th, td { border: 1px solid black;'+
               'border-collapse: collapse;} th, td { padding: 15px;} </style>'+
               '</head><body> <H3>Resultado de la busqueda:'+
               sys.argv[1]+' '+sys.argv[2]+'</H3><br></body></html>')
    #taula
    file.write('<table style ="width:70%">')
    file.write('<tr><th>Acte</th><th>adreca</th><th>data</th><th>transport</th></tr>')'''