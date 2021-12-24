#实现HTTP客户端的程序
# coding: utf-8

import socket
import hashlib
import RSAUtil as rsa
import AESUtil as aes

aes_password = "abcdefghijklmnop"
aes_iv = "1111111111111111"
AESUtil = aes.AESUtil(aes_password, aes_iv)

RSAUtil = rsa.RSAUtil()
RSAUtil.load_public_key()

data = '林聪是世界上最好的老师'
md5_data = hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()

encrypted_rsa_md5_data = RSAUtil.rsa_encrypt(md5_data)

send_data = "%s||%s" % (data, encrypted_rsa_md5_data)

encrypted_send_data = AESUtil.aes_encrypt(send_data)

s = socket.socket()
host = 'localhost'
port = 8891
s.connect((host, port))#连接服务端
ip, port = s.getsockname()
print("本机 ip 和 port {} {}".format(ip, port))

http_request = "GET %s HTTP/1.1\r\nhost:%s\r\n\r\n" % (encrypted_send_data, host)
request = http_request.encode('utf-8')
print('请求', request)
s.send(request)

response = s.recv(1023)
print('响应', response)
print('响应的 str 格式', response.decode('utf-8'))

s.close()