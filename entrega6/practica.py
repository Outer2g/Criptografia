string = 'eccaea470e54d43d4ba2c6f32d4049cb7528739ae2d90c561666dc2f366c27a9a514d481d8ff88423129883c3ea6cf138530c5fa0242bc45070eb39b98e32b6b'
size = int(len(string)/2)

py = string[size:]
px = string[:size]

print(px,py)

'''^^^Tiene f1 f2 r s
30 indica que es una lista de cosas
45 indica longitud de la lista (siguientes bytes)
02 indica un entero
20 indica longitud del entero en bytes
los siguientes tantos bytes es el elemento

Este firma firma el Random.
Exportar Random en un fichero.

Server Hello, Certificate, Server KeyExchange ->> sacar segundo Random

Firman curve type, named curve, pubkey length, pubkey
Extraer todos esos.

Terminar en 6 ficheros: 1.dat, 2.dat, ... 6.dat
Hacer cat 1.dat 2.dat .... 6.dat -> a_firmar.dat
Hacer h = SHA256(a_firmar.dat)

si tamaño de h es mas de 256 bytes: truncar hasta 256 bytes.

aux=mod(f2** (-1), orden)
w1=mod(h*aux, orden)
w2=mod(f1*aux, orden)
Q=E([publicKey_GoogleX,publicKey_GoogleY])
result=Integer(w1)*G+Integer(w2)*Q'''
'''firma : 30:44:02:20:19:e2:06:73:fd:2a:b9:54:2a:03:1d:90:92:11:61:c5:5e:82:f3:d5:78:c8:01:d7:4d:e4:b7:39:e1:55:44:00:02:20:53:d6:6a:33:72:85:cc:69:0e:dd:f9:99:ae:0e:5c:48:36:b7:a0:98:c5:a9:c6:a1:a9:86:c6:d7:4b:d3:2b:09'''
'''44:02:20:19:e2:06:73:fd:2a:b9:54:2a:03:1d:90:92:11:61:c5:5e:82:f3:d5:78:c8:01:d7:4d:e4:b7:39:e1:55:44:00:02:20:53:d6:6a:33:72:85:cc:69:0e:dd:f9:99:ae:0e:5c:48:36:b7:a0:98:c5:a9:c6:a1:a9:86:c6:d7:4b:d3:2b:09'''

import hashlib
with open('dadess/datos','rb') as datos:
    test = hashlib.sha256(datos.read()).hexdigest()
    print('sha512: ',test)
    size = int(len(test)/2)
    print('truncado_256: ',test[:size])

firma = '44:02:20:19:e2:06:73:fd:2a:b9:54:2a:03:1d:90:92:11:61:c5:5e:82:f3:d5:78:c8:01:d7:4d:e4:b7:39:e1:55:44:00:' \
        '02:20:53:d6:6a:33:72:85:cc:69:0e:dd:f9:99:ae:0e:5c:48:36:b7:a0:98:c5:a9:c6:a1:a9:86:c6:d7:4b:d3:2b:09'
firma = firma.split(':')
print(len(firma))
f1 = 0x19e20673fd2ab9542a031d90921161c55e82f3d578c801d74de4b739e1554400
f2 = 0x53d66a337285cc690eddf999ae0e5c4836b7a098c5a9c6a1a986c6d74bd32b09

'''pubKeyGoogle: 04:66:4f:ca:46:ef:4c:68:1b:74:76:0b:d8:95:34:58:87:94:d1:77:25:27:88:43:2e:63:f8:a7:d8:1d:28:7d:9e:47:4e:54:02:be:b9:0a:75:ae:4b:27:59:ff:35:79:92:23:e1:ff:14:aa:00:c7:48:9b:b6:8c:21:14:2e:dc:cd'''
'''pubKeyGoogle: 04664fca46ef4c681b74760bd89534588794d177252788432e63f8a7d81d287d9e474e5402beb90a75ae4b2759ff35799223e1ff14aa00c7489bb68c21142edccd'''
pubKeyGoogle = '664fca46ef4c681b74760bd89534588794d177252788432e63f8a7d81d287d9e474e5402beb90a75ae4b2759ff35799223e1ff14aa00c7489bb68c21142edccd'
size = int(len(pubKeyGoogle)/2)

py = pubKeyGoogle[size:]
px = pubKeyGoogle[:size]

print(px,py)
'''pubkey fb: 04 a0 f1 8c af a7 39 88 68 5b 13 56 0e 15 15 b4
a7 45 ef 1b c7 e5 85 3c 2b 04 d4 65 8a 31 31 22
ea a3 92 ed 64 9d ba 65 81 e3 b6 12 76 d8 b3 0b
45 f1 ff 0a 28 14 9c 4f dc 73 a9 b3 49 2d a0 76
d3 '''

pubKeyFb = 'a0f18cafa73988685b13560e1515b4a745ef1bc7e5853c2b04d4658a313122eaa392ed649dba6581e3b61276d8b30b45f1ff0a28149c4fdc73a9b3492da076d3'
size = int(len(pubKeyFb)/2)

py = pubKeyFb[size:]
px = pubKeyFb[:size]

print(px,py)