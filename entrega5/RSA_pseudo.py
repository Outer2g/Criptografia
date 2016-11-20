import Crypto.PublicKey.RSA as rsa

#openssl rsa -in alex.oses_pubkeyRSA_pseudo.pem -pubin -text

def inverseModulus(a,n):
    t = 0
    newt = 1
    r = n
    newr = a
    while newr != 0:
        quotient = r // newr
        (t, newt) = (newt, t - quotient * newt)
        (r, newr) = (newr, r - quotient * newr)
    if t < 0:
        t += n
    return t

'''Modulus:
    01:ce:36:c6:66:8e:7c:60:cb:97:65:02:52:92:8e:
    34:7a:60:b3:42:81:69:e0:4f:1a:c9:db:bb:47:ff:
    6f:ed:69:1d:d0:21:fc:8e:13:4e:72:8e:27:4f:c8:
    c1:6d:86:ef:b0:4b:6a:31:e3:eb:0d:04:64:18:07:
    3e:70:d3:23:ec:dc:6a:bc:63:91:24:94:cf:49:ae:
    0f:d7:83:9f:c2:7f:cb:2c:e9:6b:f9:f6:f0:87:a2:
    02:d6:a2:d6:da:79:ab:32:dd:85:58:03:3b:80:4c:
    a8:71:1d:11:69:fc:65:ee:19:e2:80:46:fa:a0:97:
    4b:4a:59:50:80:c4:db:5a:15:6d:ba:54:b9:39:fa:
    0d:dc:0d:98:c0:bd:52:4f:dc:59:4d:59:7c:74:78:
    39:6b:8a:4e:90:17:ec:31:26:4f:19:d7:f7:b9:d4:
    79:26:45:31:b8:f8:74:8b:f7:eb:02:30:4c:2c:b5:
    51:b8:6e:a8:35:a2:4c:e6:eb:02:66:69:13:4b:58:
    c0:32:10:7f:51:2f:e2:78:6f:25:a5:0c:fe:08:bd:
    c8:0d:70:ee:41:ad:b9:19:3a:bf:16:22:ee:b2:d1:
    6d:62:e3:01:f1:06:4e:78:24:32:db:54:2f:1b:f3:
    06:4e:66:f5:a7:07:c2:7d:fd:1c:c0:f0:da:62:c1
Exponent: 65537 (0x10001)'''
key = '01:ce:36:c6:66:8e:7c:60:cb:97:65:02:52:92:8e:' \
      '34:7a:60:b3:42:81:69:e0:4f:1a:c9:db:bb:47:ff:' \
      '6f:ed:69:1d:d0:21:fc:8e:13:4e:72:8e:27:4f:c8:' \
      'c1:6d:86:ef:b0:4b:6a:31:e3:eb:0d:04:64:18:07:' \
      '3e:70:d3:23:ec:dc:6a:bc:63:91:24:94:cf:49:ae:' \
      '0f:d7:83:9f:c2:7f:cb:2c:e9:6b:f9:f6:f0:87:a2:' \
      '02:d6:a2:d6:da:79:ab:32:dd:85:58:03:3b:80:4c:' \
      'a8:71:1d:11:69:fc:65:ee:19:e2:80:46:fa:a0:97:' \
      '4b:4a:59:50:80:c4:db:5a:15:6d:ba:54:b9:39:fa:' \
      '0d:dc:0d:98:c0:bd:52:4f:dc:59:4d:59:7c:74:78:' \
      '39:6b:8a:4e:90:17:ec:31:26:4f:19:d7:f7:b9:d4:' \
      '79:26:45:31:b8:f8:74:8b:f7:eb:02:30:4c:2c:b5:' \
      '51:b8:6e:a8:35:a2:4c:e6:eb:02:66:69:13:4b:58:' \
      'c0:32:10:7f:51:2f:e2:78:6f:25:a5:0c:fe:08:bd:' \
      'c8:0d:70:ee:41:ad:b9:19:3a:bf:16:22:ee:b2:d1:' \
      '6d:62:e3:01:f1:06:4e:78:24:32:db:54:2f:1b:f3:' \
      '06:4e:66:f5:a7:07:c2:7d:fd:1c:c0:f0:da:62:c1'
e = long(65537)

n = eval('0x' + key.replace(':',''))
#after using sage: p = 10718556386827371703^16 q = 271282445560003256537783828664200566313^8 factoring
p = 10718556386827371703
q = 271282445560003256537783828664200566313
#fi de n:
fin = p**15 * (p-1) * q**7*(q-1)
d = inverseModulus(e,fin)
print(d)

rssa = rsa.construct((n,e,d,p**16,q**8))
f = open('private.pem','w')
f.write(rssa.exportKey('PEM'))
f.close()