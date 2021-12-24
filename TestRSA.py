import RSAUtil as rsa

RSAUtil = rsa.RSAUtil()
RSAUtil.load_public_key()
data = "林聪是世界上最好的老师"
encrypted_data = RSAUtil.rsa_encrypt(data)

print("使用公钥:%s" % RSAUtil.public_key)
print("加密后:%s" % encrypted_data)

