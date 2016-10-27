from Crypto.Cipher import AES
from Crypto.Util import Counter

iv = open('2016_10_10_17_00_32_alex.oses.puerta_trasera.enc', 'rb').read()[:16]


def toHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0' + hv
        lst.append(hv)

    return reduce(lambda x, y: x + y, lst)
def toInt(s):
    hexa = toHex(s)
    print hexa
    sum = int(hexa[0])*16 + int(hexa[1])
    return sum

for i in range(230,255):
    k = [chr(ord(x) ^ i) for x in iv]
    k = ''.join(k)
    aes = AES.new(k, AES.MODE_CBC, iv)
    decr = aes.decrypt(open('2016_10_10_17_00_32_alex.oses.puerta_trasera.enc', 'rb').read()[16:])
    ultimo_byte = decr[-1]
    if (i == 238) :
        print ord(ultimo_byte)

        for i in range(len(decr)-1,len(decr)-ord(ultimo_byte)):
            print i
    open('resultados2/' + str(i), 'wb').write(decr)