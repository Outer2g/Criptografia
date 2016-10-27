from Crypto.Cipher import AES
key = open('2016_10_10_17_00_32_alex.oses.key','rb').read()
C = open('2016_10_10_17_00_32_alex.oses.enc','rb').read()

modos = [AES.MODE_ECB,AES.MODE_CBC,AES.MODE_CFB,AES.MODE_OFB]
for modo in modos:
    iv = C[:AES.block_size]
    aes = AES.new(key,modo,iv)
    m = aes.decrypt(C[AES.block_size:])
    open('resultados/result'+str(modo),'wb').write(m)
