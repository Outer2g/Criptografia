import Crypto.PublicKey.RSA as rsa
from Crypto.PublicKey.RSA import importKey
from fractions import gcd
from glob import glob

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
    4a:c1:e7:23:7a:ad:22:e8:4c:a1:89:31:dd:8a:f0:
    cb:6c:ff:51:64:ac:34:89:7c:1d:60:83:22:11:d0:
    c1:67:b5:59:d5:24:fe:71:7e:2e:0f:fd:9f:62:07:
    dd:22:22:96:7a:ac:a2:8a:09:88:17:b0:3e:a3:87:
    ed:a8:91:96:0b:60:a0:cb:df:ed:7b:2e:06:2c:e4:
    34:a1:ca:10:51:c7:2a:49:f8:a5:96:85:0b:96:fa:
    50:74:7a:e5:43:68:d0:77:60:2c:bc:8a:1e:4c:6d:
    1e:12:f6:0a:3c:9c:ad:c5:c1:e7:ff:3d:5d:26:e1:
    bb:69:68:85:d5:40:26:f8:c9:6d:71:6b:b5:b7:3c:
    2f:52:df:d0:a3:ab:c8:9a:b0:fb:0e:7c:b0:13:96:
    30:c3:e9:87:35:4d:12:f6:f3:b0:85:e4:b7:c6:73:
    95:00:10:ca:74:db:e4:8a:af:ba:77:4a:bd:31:f6:
    9e:06:e3:36:44:2f:14:da:21:42:59:39:bd:5f:e9:
    50:56:7a:0a:e1:c2:a3:22:85:a6:5a:f0:f1:c8:d9:
    64:bc:d6:ef:18:84:a3:04:e3:9b:2b:2f:93:89:74:
    6d:75:bb:a0:81:dd:24:23:cd:d4:14:1c:45:5e:e9:
    3d:ab:5e:04:4e:62:85:b0:15:64:ba:07:94:41:7f:
    3d
Exponent: 65537 (0x10001)
'''
n = '4a:c1:e7:23:7a:ad:22:e8:4c:a1:89:31:dd:8a:f0:' \
      'cb:6c:ff:51:64:ac:34:89:7c:1d:60:83:22:11:d0:' \
      'c1:67:b5:59:d5:24:fe:71:7e:2e:0f:fd:9f:62:07:' \
      'dd:22:22:96:7a:ac:a2:8a:09:88:17:b0:3e:a3:87:' \
      'ed:a8:91:96:0b:60:a0:cb:df:ed:7b:2e:06:2c:e4:' \
      '34:a1:ca:10:51:c7:2a:49:f8:a5:96:85:0b:96:fa:' \
      '50:74:7a:e5:43:68:d0:77:60:2c:bc:8a:1e:4c:6d:' \
      '1e:12:f6:0a:3c:9c:ad:c5:c1:e7:ff:3d:5d:26:e1:' \
      'bb:69:68:85:d5:40:26:f8:c9:6d:71:6b:b5:b7:3c:' \
      '2f:52:df:d0:a3:ab:c8:9a:b0:fb:0e:7c:b0:13:96:' \
      '30:c3:e9:87:35:4d:12:f6:f3:b0:85:e4:b7:c6:73:' \
      '95:00:10:ca:74:db:e4:8a:af:ba:77:4a:bd:31:f6:' \
      '9e:06:e3:36:44:2f:14:da:21:42:59:39:bd:5f:e9:' \
      '50:56:7a:0a:e1:c2:a3:22:85:a6:5a:f0:f1:c8:d9:' \
      '64:bc:d6:ef:18:84:a3:04:e3:9b:2b:2f:93:89:74:' \
      '6d:75:bb:a0:81:dd:24:23:cd:d4:14:1c:45:5e:e9:' \
      '3d:ab:5e:04:4e:62:85:b0:15:64:ba:07:94:41:7f:' \
      '3d'
e = long(65537)

'''https://news.ycombinator.com/item?id=3591429
Posting what I said in the other thread: As far as I can tell, this is what they're doing: if two different
keys have a factor in common (i.e. A=PQ, B=PR), then you can use Euclid's algorithm (which just requires
repeated subtraction, and is thus really easy) to find P (=gcd(A,B)), and then just use division to find
Q (=A/P) and R (=B/P) easily. So what the researchers did, apparently, was to gather all the RSA public
keys they could find (6 million or so) and then calculate the gcds of all pairs of keys.
Whenever they found a gcd that wasn't equal to 1, they'd cracked (at least) 2 keys.'''
n = eval('0x' + n.replace(':',''))
for filename in glob('./archivos/*pubkeyRSA_RW.pem'):
    with open(filename,'r') as f:
        key = importKey(f.read())
        if gcd(n,key.n) != 1:
            print filename
            print 'n found'
            p = gcd(n,key.n)
            break
q = n/p
phiP = p-1
phiQ = q-1
phiN = phiP*phiQ


d = inverseModulus(e,phiN)

dp = d%(p-1)
dq = d%(q-1)
u =  inverseModulus(p,q)

n = p*q;

key = rsa.construct((n,e,d,p,q,u));

f = open('test.pem', 'w')

f.write(key.exportKey('PEM'))

fileToDecrypt = open('alex.oses_RSA_RW.enc','rb').read()

'''n = eval('0x' + key.replace(':',''))
#after using sage: p = 10718556386827371703^16 q = 271282445560003256537783828664200566313^8
p = 10718556386827371703
q = 271282445560003256537783828664200566313
#fi de n:
fin = p**15 * (p-1) * q**7*(q-1)
d = inverseModulus(e,fin)
print(d)

rssa = rsa.construct((n,e,d,p**16,q**8))
f = open('private.pem','w')
f.write(rssa.exportKey('PEM'))
f.close()'''