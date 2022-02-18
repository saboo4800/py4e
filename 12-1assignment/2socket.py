import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('jisho.org', 443))
cmd = 'GET https://jisho.org/search/house HTTPS/1.0\r\n\r\n'.encode()
print(cmd)
mysock.send(cmd)
print('initiating')
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
    print('hello world')

mysock.close()
print('close')
