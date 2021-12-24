import AESUtil as aes
import base64
password = "abcdefghijklmnop"
iv = "1111111111111111"
data = "HelloWorld"
AESUtil = aes.AESUtil(password, iv)

encrypted_data = AESUtil.aes_encrypt(data)
print("内容%s经过AES-128-CBC加密后（密码%s，iv%s）结果为%s" % (
    data,
    password,
    AESUtil.iv,
    encrypted_data
))

decrypted_data = AESUtil.aes_decrypt(encrypted_data)
print("内容%s经过AES-128-CBC解密后（密码%s，iv%s）结果为%s" % (
    encrypted_data,
    password,
    AESUtil.iv,
    decrypted_data
))

