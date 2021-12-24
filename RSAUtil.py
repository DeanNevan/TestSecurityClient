import rsa, base64

class RSAUtil:
    def __init__(self):
        pass
    
    # 生成公钥、私钥
    def create_keys(self, size = 512):
        (pubkey, privkey) = rsa.newkeys(size)
        pub = pubkey.save_pkcs1()
        with open("public.pem", "wb+")as f:
            f.write(pub)

        pri = privkey.save_pkcs1()
        with open("private.pem", "wb+")as f:
            f.write(pri)

    def load_public_key(self):
        with open('public.pem') as publickfile:
            p = publickfile.read()
            self.public_key = rsa.PublicKey.load_pkcs1(p)
    def load_private_key(self):
        with open('private.pem') as privatefile:
            p = privatefile.read()
            self.private_key = rsa.PrivateKey.load_pkcs1(p)

    # rsa加密
    def rsa_encrypt(self, str):
        # 明文编码格式
        content = str.encode("utf-8")
        # 公钥加密
        crypto = rsa.encrypt(content, self.public_key)
        crypto = base64.b64encode(crypto)
        return crypto
    
    
    # rsa解密
    def rsa_decrypt(self, str):
        str = base64.b64decode(str)
        # 私钥解密
        content = rsa.decrypt(str, self.private_key)
        con = content.decode("utf-8")
        return con