import socket
import random
import ast

# create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))  # ip: 127.0.0.01 port: 9999
# start listen
server.listen()
client, addr = server.accept()
start = True
trivia_QnA = [
    ["What is the capital of France?", "Paris"],
    ["Which planet is known as the Red Planet?", "Mars"],
    ["What is the largest mammal in the world?", "Blue whale"],
    ["What is the tallest mountain in the world?", "Mount Everest"]
]
while start:
    msg = client.recv(1024).decode('utf-8')
    if msg == 'q':
        start = False
        client.send(str(['q']).encode('utf-8'))
    elif msg == 'new_trivia':
        client.send(str(random.choice(trivia_QnA)).encode('utf-8'))
    else:
        client.send(f'help bot: welcome {msg}!'.encode('utf-8'))
# close socket
client.close()
server.close()
