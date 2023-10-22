import socket

# create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9999))
start = True
# response syntax: [response_reason, response]
# name
client.send(str(['name', input('what is your name?\nyou: ')]).encode('utf-8'))
while start:
    msg = client.recv(1024).decode('utf-8')
    if msg == 'q':
        start = False
    else:
        print(msg)
        client.send(str(['conv', input('you: ')]).encode('utf-8'))
# close socket
client.close()


